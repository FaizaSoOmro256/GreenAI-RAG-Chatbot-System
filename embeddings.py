from langchain_community.embeddings import HuggingFaceEmbeddings
import pinecone
from langchain_pinecone import PineconeVectorStore
import config
import os
import pickle
import hashlib
from typing import List, Dict, Any
import time

# Try to import monitoring utilities - use conditionally to prevent import errors
try:
    from utils.monitoring import metrics_store
    HAS_MONITORING = True
except ImportError:
    HAS_MONITORING = False
    print("Monitoring module not found. Cache statistics will not be recorded.")

# Create a cache directory if it doesn't exist
CACHE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")
os.makedirs(CACHE_DIR, exist_ok=True)

def get_embedding_model():
    """
    Load and return the embedding model specified in the config.
    """
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': True}
    
    embedding_model = HuggingFaceEmbeddings(
        model_name=config.EMBEDDING_MODEL_NAME,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    
    # Enhance the embedding model with caching capabilities
    return CachedEmbeddings(embedding_model)

class CachedEmbeddings:
    """
    Wrapper class that adds caching functionality to any embedding model.
    This reduces computation time for repeated queries.
    """
    def __init__(self, embedding_model, cache_dir=CACHE_DIR, ttl=86400):
        """
        Initialize the cached embeddings wrapper.
        
        Args:
            embedding_model: The base embedding model to wrap
            cache_dir: Directory to store cache files
            ttl: Time-to-live for cache entries in seconds (default: 24 hours)
        """
        self.embedding_model = embedding_model
        self.cache_dir = cache_dir
        self.ttl = ttl
        self.cache_hits = 0
        self.cache_misses = 0
        self.last_recording_time = time.time()
        self.recording_interval = 60  # Record cache stats once per minute
    
    def _get_cache_path(self, text):
        """Create a cache file path based on the text content hash"""
        text_hash = hashlib.md5(text.encode()).hexdigest()
        return os.path.join(self.cache_dir, f"{text_hash}.pkl")
    
    def _record_cache_stats(self):
        """Record cache statistics to monitoring module if time interval has passed"""
        if not HAS_MONITORING:
            return
            
        current_time = time.time()
        if current_time - self.last_recording_time >= self.recording_interval:
            # Record cache stats
            metrics_store.record_cache_stats(self.cache_hits, self.cache_misses)
            self.last_recording_time = current_time
            
            # Log stats to console if debug mode is on
            if config.DEBUG_MODE:
                total = self.cache_hits + self.cache_misses
                hit_rate = (self.cache_hits / total) * 100 if total > 0 else 0
                print(f"Embedding cache stats: {self.cache_hits} hits, {self.cache_misses} misses, {hit_rate:.2f}% hit rate")
    
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Embed documents with caching"""
        results = []
        uncached_texts = []
        uncached_indices = []
        
        # Check cache for each text
        for i, text in enumerate(texts):
            cache_path = self._get_cache_path(text)
            if os.path.exists(cache_path):
                # Check if cache entry is still valid (not expired)
                cache_time = os.path.getmtime(cache_path)
                if time.time() - cache_time <= self.ttl:
                    try:
                        with open(cache_path, 'rb') as f:
                            embedding = pickle.load(f)
                            results.append(embedding)
                            self.cache_hits += 1
                            continue
                    except (pickle.PickleError, EOFError):
                        # If cache file is corrupted, recompute
                        pass
            
            # Cache miss or expired
            uncached_texts.append(text)
            uncached_indices.append(i)
            self.cache_misses += 1
        
        # Get embeddings for texts not in cache
        if uncached_texts:
            new_embeddings = self.embedding_model.embed_documents(uncached_texts)
            
            # Save new embeddings to cache and insert at correct positions
            for i, embedding in zip(uncached_indices, new_embeddings):
                cache_path = self._get_cache_path(texts[i])
                with open(cache_path, 'wb') as f:
                    pickle.dump(embedding, f)
                
                # Results list might not have all positions filled yet
                while len(results) <= i:
                    results.append(None)
                results[i] = embedding
        
        # Record cache stats periodically
        self._record_cache_stats()
        
        return results
    
    def embed_query(self, text: str) -> List[float]:
        """Embed query with caching"""
        cache_path = self._get_cache_path(text)
        
        # Check if we have a valid cache entry
        if os.path.exists(cache_path):
            cache_time = os.path.getmtime(cache_path)
            if time.time() - cache_time <= self.ttl:
                try:
                    with open(cache_path, 'rb') as f:
                        embedding = pickle.load(f)
                        self.cache_hits += 1
                        self._record_cache_stats()
                        return embedding
                except (pickle.PickleError, EOFError):
                    # If cache file is corrupted, recompute
                    pass
        
        # Cache miss or expired
        self.cache_misses += 1
        embedding = self.embedding_model.embed_query(text)
        
        # Save to cache
        with open(cache_path, 'wb') as f:
            pickle.dump(embedding, f)
        
        # Record cache stats periodically
        self._record_cache_stats()
        
        return embedding
    
    def get_cache_stats(self):
        """Return cache hit/miss statistics"""
        total = self.cache_hits + self.cache_misses
        hit_rate = (self.cache_hits / total) * 100 if total > 0 else 0
        return {
            "hits": self.cache_hits,
            "misses": self.cache_misses,
            "total": total,
            "hit_rate": f"{hit_rate:.2f}%"
        }

def initialize_pinecone():
    """
    Initialize and return the Pinecone client.
    """
    if not config.PINECONE_API_KEY or not config.PINECONE_ENVIRONMENT:
        raise ValueError("Pinecone API key and environment must be set in .env file")
    
    # Initialize pinecone with API key and environment
    pinecone.init(
        api_key=config.PINECONE_API_KEY,
        environment=config.PINECONE_ENVIRONMENT
    )
    
    # Check if index exists, if not create it
    if config.PINECONE_INDEX not in pinecone.list_indexes():
        pinecone.create_index(
            name=config.PINECONE_INDEX,
            dimension=384,  # dimension for multilingual-MiniLM-L12-v2
            metric="cosine"
        )
        print(f"Created new Pinecone index: {config.PINECONE_INDEX}")
    
    return pinecone

def get_vector_store(embedding_model=None):
    """
    Initialize and return the Pinecone vector store.
    """
    if embedding_model is None:
        embedding_model = get_embedding_model()
        
    try:
        # Initialize Pinecone
        initialize_pinecone()
        
        # Connect to the index
        index = pinecone.Index(config.PINECONE_INDEX)
        
        # Create and return the vector store
        vector_store = PineconeVectorStore(
            pinecone_index=index,
            embedding=embedding_model,
            text_key="text"
        )
        
        return vector_store
        
    except Exception as e:
        print(f"Error initializing vector store: {e}")
        raise 