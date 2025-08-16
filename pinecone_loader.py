"""
Compatibility layer for Pinecone integration with LangChain.
This handles the version mismatches between langchain-pinecone and newer langchain versions.
"""

from pinecone import Pinecone, ServerlessSpec
from langchain_community.embeddings import HuggingFaceEmbeddings
import config

def initialize_pinecone():
    """
    Initialize Pinecone client.
    """
    if not config.PINECONE_API_KEY or not config.PINECONE_ENVIRONMENT:
        raise ValueError("Pinecone API key and environment must be set in .env file")
    
    # Initialize pinecone with API key
    pc = Pinecone(api_key=config.PINECONE_API_KEY)
    
    # Check if index exists, if not create it
    index_names = [index.name for index in pc.list_indexes()]
    if config.PINECONE_INDEX not in index_names:
        pc.create_index(
            name=config.PINECONE_INDEX,
            dimension=384,  # dimension for multilingual-MiniLM-L12-v2
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region=config.PINECONE_ENVIRONMENT.split('-')[0])
        )
        print(f"Created new Pinecone index: {config.PINECONE_INDEX}")
    
    # Get pinecone index
    index = pc.Index(config.PINECONE_INDEX)
    return index

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
    
    return embedding_model

class PineconeVectorStore:
    """
    Custom vector store implementation that works with both older and newer versions of LangChain.
    """
    def __init__(self, index, embedding):
        self.index = index
        self.embedding = embedding
        self.text_key = "text"
        
    def add_documents(self, documents):
        """
        Add documents to the vector store.
        """
        # Process document chunks into vectors
        for i, doc in enumerate(documents):
            # Get embedding for document
            embedding_vector = self.embedding.embed_query(doc.page_content)
            
            # Create metadata
            metadata = doc.metadata.copy() if hasattr(doc, 'metadata') else {}
            metadata[self.text_key] = doc.page_content
            
            # Add to Pinecone
            self.index.upsert(
                vectors=[(f"doc_{i}", embedding_vector, metadata)]
            )
        
        print(f"Added {len(documents)} documents to Pinecone index")
    
    def as_retriever(self, search_type="similarity", search_kwargs=None):
        """
        Create a retriever from the vector store.
        """
        return PineconeRetriever(
            vectorstore=self,
            search_type=search_type,
            search_kwargs=search_kwargs or {}
        )

class PineconeRetriever:
    """
    Custom retriever implementation for Pinecone.
    """
    def __init__(self, vectorstore, search_type="similarity", search_kwargs=None):
        self.vectorstore = vectorstore
        self.search_type = search_type
        self.search_kwargs = search_kwargs or {}
    
    def invoke(self, query):
        """
        Retrieve documents relevant to the query.
        """
        from langchain_core.documents import Document
        
        # Get embedding for query
        query_embedding = self.vectorstore.embedding.embed_query(query)
        
        # Search Pinecone
        results = self.vectorstore.index.query(
            vector=query_embedding,
            top_k=self.search_kwargs.get("k", config.NUM_RESULTS),
            include_metadata=True
        )
        
        # Convert to Documents
        documents = []
        for match in results.matches:
            if match.score < self.search_kwargs.get("score_threshold", config.SIMILARITY_SCORE_THRESHOLD):
                continue
                
            # Get text from metadata
            text = match.metadata.get(self.vectorstore.text_key, "")
            
            # Create document
            doc = Document(
                page_content=text,
                metadata={k: v for k, v in match.metadata.items() if k != self.vectorstore.text_key}
            )
            documents.append(doc)
        
        return documents
    
    def get_relevant_documents(self, query):
        """
        Legacy method for compatibility with older LangChain versions.
        """
        return self.invoke(query)

def get_vector_store():
    """
    Initialize and return a custom vector store.
    """
    try:
        # Initialize Pinecone
        index = initialize_pinecone()
        
        # Get embedding model
        embedding_model = get_embedding_model()
        
        # Create and return the vector store
        vector_store = PineconeVectorStore(
            index=index,
            embedding=embedding_model
        )
        
        return vector_store
        
    except Exception as e:
        print(f"Error initializing vector store: {e}")
        raise 