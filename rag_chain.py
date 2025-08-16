from typing import List, Dict, Any
import google.generativeai as genai
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
import config
from pinecone_loader import get_vector_store
from translations import TRANSLATIONS
import re

# Import district data
try:
    from data.district_data import sindh_district_climate_info, sindh_regions, regional_challenges, sindh_districts
    HAS_DISTRICT_DATA = True
except ImportError:
    HAS_DISTRICT_DATA = False
    sindh_districts = []

# Configure the Google Generative AI API
genai.configure(api_key=config.GEMINI_API_KEY)

def setup_model():
    """
    Set up and configure the Gemini model.
    """
    generation_config = {
        "temperature": config.TEMPERATURE,
        "top_p": config.TOP_P,
        "top_k": config.TOP_K,
        "max_output_tokens": config.MAX_OUTPUT_TOKENS,
    }
    
    model = genai.GenerativeModel(
        model_name=config.GEMINI_MODEL_NAME,
        generation_config=generation_config
    )
    
    return model

def format_docs(docs: List[Dict[str, Any]]) -> str:
    """
    Format the retrieved documents into a string with enhanced structure.
    """
    formatted_docs = []
    for i, doc in enumerate(docs):
        # Extract metadata if available
        metadata = doc.metadata if hasattr(doc, 'metadata') else {}
        
        # Get the content and clean it
        content = doc.page_content if hasattr(doc, 'page_content') else str(doc)
        
        # Split content into sections
        sections = content.split('\n\n')
        
        # Only keep relevant sections (those with climate data)
        relevant_sections = []
        for section in sections:
            if any(keyword in section.lower() for keyword in 
                ['temperature', 'rainfall', 'humidity', 'wind', 'climate']):
                # Clean up the section
                clean_section = section.strip()
                if clean_section:
                    relevant_sections.append(clean_section)
        
        # Join relevant sections
        if relevant_sections:
            formatted_docs.append('\n'.join(relevant_sections))
    
    # Join all documents with clear separation
    return '\n\n'.join(formatted_docs)

def get_district_info(district: str, query: str = "") -> str:
    """Get comprehensive information about a district."""
    try:
        if not district or district not in sindh_district_climate_info:
            return "District not found."
        
        district_data = sindh_district_climate_info[district]
        climate_data = district_data.get('climate_data', {})
        
        # For direct measurement questions, return only the specific value
        query = query.lower().strip()
        if 'how much' in query or 'what is' in query:
            if 'rainfall' in query:
                rainfall = climate_data.get('climate_profile', {}).get('rainfall', {})
                if rainfall and 'annual_average' in rainfall:
                    return rainfall['annual_average']
            elif 'temperature' in query:
                temp = climate_data.get('climate_profile', {}).get('temperature', {})
                if temp and 'annual_average' in temp:
                    return temp['annual_average']
            elif 'humidity' in query:
                humidity = climate_data.get('climate_profile', {}).get('humidity', {})
                if humidity and 'annual_average' in humidity:
                    return humidity['annual_average']
            elif 'wind' in query and 'speed' in query:
                wind = climate_data.get('climate_profile', {}).get('wind', {})
                if wind and 'average_speed' in wind:
                    return wind['average_speed']
        
        # For trend questions, return only the trend
        if 'trend' in query:
            if 'temperature' in query:
                temp = climate_data.get('climate_profile', {}).get('temperature', {})
                if temp and 'trend' in temp:
                    return temp['trend']
            elif 'rainfall' in query:
                rainfall = climate_data.get('climate_profile', {}).get('rainfall', {})
                if rainfall and 'trend' in rainfall:
                    return rainfall['trend']
        
        # If no specific query matches or it's a general query, return the full profile
        response = [f"Climate Information for {district.title()}:"]
        
        climate = climate_data.get('climate_profile', {})
        if climate:
            # Temperature
            temp = climate.get('temperature', {})
            if temp:
                response.append("\nTemperature:")
                response.append(f"•Current Annual Average: {temp.get('annual_average', 'N/A')}")
                response.append(f"•Summer Maximum: {temp.get('summer_max', 'N/A')}")
                response.append(f"•Winter Minimum: {temp.get('winter_min', 'N/A')}")
                if 'trend' in temp:
                    response.append(f"•Historical Trend: {temp.get('trend', 'N/A')}")
            
            # Rainfall
            rainfall = climate.get('rainfall', {})
            if rainfall:
                response.append("\nRainfall:")
                response.append(f"•Annual Average: {rainfall.get('annual_average', 'N/A')}")
                response.append(f"•Monsoon Contribution: {rainfall.get('monsoon_contribution', 'N/A')}")
                response.append(f"•Rainy Days: {rainfall.get('rainy_days', 'N/A')}")
                if 'trend' in rainfall:
                    response.append(f"•Trend: {rainfall.get('trend', 'N/A')}")
            
            # Rest of the function remains unchanged for general queries
            # ... existing code ...
        
        return '\n'.join(response)
        
    except Exception as e:
        logger.error(f"Error getting district info: {str(e)}")
        return "Error retrieving district information."

def get_language_specific_prompt(language: str) -> PromptTemplate:
    """
    Return a language-specific prompt template with enhanced context handling.
    """
    if language == "urdu":
        template = """
        آپ سندھ میں پائیدار آب و ہوا کے اقدامات کے بارے میں ایک معلوماتی چیٹ بوٹ ہیں۔ ذیل میں کچھ معلومات ہیں:

        {context}

        {district_info}

        صرف دی گئی معلومات کا استعمال کرتے ہوئے، اس سوال کا جواب دیں: {question}

        جواب دیتے وقت، درج ذیل نکات کو مدنظر رکھیں:
        1. جواب میں مخصوص اعدادوشمار اور حقائق شامل کریں
        2. جہاں ممکن ہو، مقامی سیاق و سباق کو شامل کریں
        3. اگر سوال کسی خاص ضلع یا علاقے سے متعلق ہے تو اس کی مخصوص خصوصیات کو نمایاں کریں
        4. جواب کو واضح اور معلوماتی بنائیں
        5. اگر سوال موسمیاتی تبدیلی کے اثرات سے متعلق ہے تو اس کے طویل مدتی اثرات کو بھی شامل کریں

        اگر آپ کو معلومات میں سے جواب نہیں ملتا ہے، تو آپ میں تخلیقی صلاحیت نہیں ہے اور "معذرت، مجھے اس سوال کا جواب معلوم نہیں ہے۔" کہیں۔
        یاد رکھیں کہ آپ کو صرف اردو میں جواب دینا ہے۔
        """
    elif language == "sindhi":
        template = """
        توهان سنڌ ۾ پائيدار آب و هوا جي قدمن بابت هڪ معلوماتي چيٽ بوٽ آهيو. هيٺ ڪجھه معلومات آهن:

        {context}

        {district_info}

        فقط ڏنل معلومات استعمال ڪندي، هن سوال جو جواب ڏيو: {question}

        جواب ڏيندي، هيٺيان نکات ذهن ۾ رکو:
        1. جواب ۾ مخصوص انگ اکر ۽ حقائق شامل ڪريو
        2. جتي ممڪن هجي، مقامي سياق ۽ سباق کي شامل ڪريو
        3. جيڪڏهن سوال ڪنهن خاص ضلعي يا علائقي سان لاڳاپيل آهي ته ان جي خاصيتن کي اجاگر ڪريو
        4. جواب کي واضح ۽ معلوماتي بڻايئو
        5. جيڪڏهن سوال موسمياتي تبديلي جي اثرن سان لاڳاپيل آهي ته ان جي طويل مدتي اثرن کي به شامل ڪريو

        جيڪڏهن توهان کي معلومات مان جواب نه ملي ٿو، ته توهان وٽ تخليقي صلاحيت ناهي ۽ "معاف ڪجو، مون کي هن سوال جو جواب معلوم ناهي." چئو.
        ياد رکو ته توهان کي فقط سنڌي ۾ جواب ڏيڻو آهي.
        """
    else:  # Default to English
        template = """
        You are a direct-response climate data assistant. Extract and provide ONLY the specific data point asked for.

        Context Information:
        {context}

        District-Specific Data:
        {district_info}

        Question: {question}

        Instructions:
        1. Return ONLY the specific value or data point asked for
        2. Do not add any additional information, context, or explanation
        3. Format for different types of answers:
           - For measurements: just the number with unit (e.g., "180mm" or "27°C")
           - For trends: only the trend statement (e.g., "Increasing by 0.4°C per decade")
           - For yes/no questions: just "Yes" or "No"
        4. If the exact data point is not available, respond only with "No data"
        5. Do not include any other text, bullets, or formatting

        Example correct responses:
        Q: "What is the annual rainfall in District X?" 
        A: "180mm"

        Q: "What is the temperature trend in District Y?"
        A: "Increasing by 0.3°C per decade"
        """
    
    return PromptTemplate.from_template(template)

def extract_specific_data(query: str, context: str) -> str:
    """
    Extract only the specific data point requested in the query.
    """
    query = query.lower().strip()
    context = context.lower().strip()
    
    # Handle direct rainfall questions
    if 'rainfall' in query and ('how much' in query or 'what is' in query):
        rainfall_patterns = [
            r'annual average:\s*([\d.]+\s*mm)',
            r'annual rainfall:\s*([\d.]+\s*mm)',
            r'rainfall:.*?(\d+\s*mm)',
            r'(\d+\s*mm).*?per year'
        ]
        for pattern in rainfall_patterns:
            match = re.search(pattern, context)
            if match:
                return match.group(1).strip()
    
    # Handle temperature trend questions
    if 'temperature' in query and 'trend' in query:
        trend_patterns = [
            r'trend:\s*(increasing[^.]*(?:per|\/)\s*(?:decade|year|month))',
            r'trend:\s*(decreasing[^.]*(?:per|\/)\s*(?:decade|year|month))',
            r'(increasing by [^.]*(?:per|\/)\s*(?:decade|year|month))',
            r'(decreasing by [^.]*(?:per|\/)\s*(?:decade|year|month))'
        ]
        for pattern in trend_patterns:
            match = re.search(pattern, context)
            if match:
                return match.group(1).strip()
    
    # Handle current temperature questions
    if 'temperature' in query and ('current' in query or 'average' in query):
        temp_patterns = [
            r'current annual average:\s*([\d.]+\s*°c)',
            r'average temperature:\s*([\d.]+\s*°c)',
            r'temperature:.*?(\d+\s*°c)'
        ]
        for pattern in temp_patterns:
            match = re.search(pattern, context)
            if match:
                return match.group(1).strip()
    
    # Handle humidity questions
    if 'humidity' in query:
        humidity_patterns = [
            r'annual average:\s*([\d.]+\s*%)',
            r'average humidity:\s*([\d.]+\s*%)',
            r'humidity:.*?(\d+\s*%)'
        ]
        for pattern in humidity_patterns:
            match = re.search(pattern, context)
            if match:
                return match.group(1).strip()
    
    # Handle wind speed questions
    if 'wind' in query and 'speed' in query:
        wind_patterns = [
            r'average speed:\s*([\d.]+\s*km/h)',
            r'average wind:\s*([\d.]+\s*km/h)',
            r'wind speed:.*?(\d+\s*km/h)'
        ]
        for pattern in wind_patterns:
            match = re.search(pattern, context)
            if match:
                return match.group(1).strip()
    
    return "No data"

def process_response(response_text: str, question_context: dict) -> str:
    """
    Process response to ensure only the exact data point is returned.
    """
    try:
        # Extract the specific data point based on the query type
        query = question_context.get('query', '').lower()
        response_text = response_text.lower()
        
        # Handle direct measurement questions
        if 'how much' in query or 'what is' in query:
            # Rainfall patterns
            if 'rainfall' in query:
                patterns = [
                    r'annual\s+average:\s*(\d+(?:\.\d+)?\s*mm)',
                    r'annual\s+rainfall:\s*(\d+(?:\.\d+)?\s*mm)',
                    r'rainfall:\s*(\d+(?:\.\d+)?\s*mm)'
                ]
                for pattern in patterns:
                    match = re.search(pattern, response_text)
                    if match:
                        return match.group(1)
            
            # Temperature patterns
            if 'temperature' in query:
                patterns = [
                    r'current\s+annual\s+average:\s*(\d+(?:\.\d+)?\s*°c)',
                    r'temperature:\s*(\d+(?:\.\d+)?\s*°c)',
                    r'average\s+temperature:\s*(\d+(?:\.\d+)?\s*°c)'
                ]
                for pattern in patterns:
                    match = re.search(pattern, response_text)
                    if match:
                        return match.group(1)
        
        # Handle trend questions
        if 'trend' in query:
            patterns = [
                r'trend:\s*(increasing|decreasing)\s+by\s+[\d.]+\s*°c\s+per\s+decade',
                r'trend:\s*(increasing|decreasing)\s+by\s+[\d.]+\s*mm\s+per\s+year'
            ]
            for pattern in patterns:
                match = re.search(pattern, response_text)
                if match:
                    return match.group(0).replace('trend:', '').strip()
        
        # If no specific pattern matches, return the first relevant line
        lines = response_text.split('\n')
                for line in lines:
            if any(key in line.lower() for key in ['rainfall:', 'temperature:', 'humidity:', 'wind speed:']):
                return line.strip()
        
        return response_text
        
    except Exception as e:
        logger.error(f"Error processing response: {str(e)}")
        return response_text

def create_rag_chain(language: str = "english"):
    """
    Create and return a RAG chain using Gemini and Pinecone.
    """
    # Set up the vector store and retriever
    vector_store = get_vector_store()
    
    # Set up the retriever with more focused parameters
    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": 1,  # Reduce to single most relevant result
            "score_threshold": 0.8,  # Increase similarity threshold
            "fetch_k": 3,  # Fetch more candidates but return only top match
            "lambda_mult": 0.5,  # Increase diversity penalty
        }
    )
    
    # Set up the LLM model
    model = setup_model()
    
    # Enhanced wrapper for Gemini model with better error handling and context preservation
    def gemini_llm(text):
        """Enhanced wrapper for Gemini model with better error handling"""
        try:
            # Extract question and context
            question_start = text.find("Question: ") + len("Question: ")
            question_end = text.find("\n", question_start) if text.find("\n", question_start) != -1 else len(text)
            current_question = text[question_start:question_end].strip()
            
            # Clean up the input text to focus on relevant sections
            text_parts = text.split('\n\n')
            focused_text = []
            for part in text_parts:
                if 'Question:' in part or any(keyword in part.lower() for keyword in 
                    ['temperature', 'rainfall', 'humidity', 'wind', 'climate']):
                    focused_text.append(part.strip())
            
            # Generate response with enhanced settings
            response = model.generate_content(
                '\n\n'.join(focused_text),
                generation_config={
                    "temperature": 0.01,  # Extremely low temperature for maximum precision
                    "top_p": 0.01,  # Very focused sampling
                    "top_k": 1,  # Single most likely response
                    "max_output_tokens": 30,  # Very short responses
                    "stop_sequences": ["\n", ".", ","],  # Stop at any sentence or clause boundary
                    "candidate_count": 1  # Generate only one response
                }
            )
            
            # Process the response to extract only the specific data point
            if response and response.text:
                extracted_data = extract_specific_data(current_question, response.text)
                if extracted_data != "No data":
                    return extracted_data
                
                # If no specific data point was extracted, try to find a direct answer
                response_text = response.text.lower().strip()
                if any(term in current_question.lower() for term in ['how much', 'what is']):
                    # Look for direct measurements
                    patterns = {
                        'rainfall': r'(\d+(?:\.\d+)?\s*mm)',
                        'temperature': r'(\d+(?:\.\d+)?\s*°c)',
                        'humidity': r'(\d+(?:\.\d+)?\s*%)',
                        'wind speed': r'(\d+(?:\.\d+)?\s*km/h)'
                    }
                    for key, pattern in patterns.items():
                        if key in current_question.lower():
                            match = re.search(pattern, response_text)
                            if match:
                                return match.group(1)
                
                # For trend questions, look for trend statements
                if 'trend' in current_question.lower():
                    trend_pattern = r'(increasing|decreasing)\s+by\s+[\d.]+\s*(?:°c|mm)\s+per\s+(?:decade|year)'
                    match = re.search(trend_pattern, response_text)
                    if match:
                        return match.group(0)
                
                # If still no match, return the first line only
                return response_text.split('\n')[0]
            
            return "No data"
            
        except Exception as e:
            logger.error(f"Error in Gemini response generation: {str(e)}")
            return "No data"
    
    # Create the RAG chain
    rag_chain = (
        {
            "context": RunnableLambda(retrieve_docs), 
            "question": RunnablePassthrough(),
            "district_info": RunnableLambda(get_district_info)
        }
        | get_language_specific_prompt(language)
        | RunnableLambda(gemini_llm)
        | StrOutputParser()
    )
    
    return rag_chain

def generate_fallback_response(district_info: str, language: str) -> str:
    """
    Generate a fallback response based on available district information.
    """
    if language == "urdu":
        return f"""معذرت، مجھے آپ کے سوال کا مکمل جواب دینے میں دشواری پیش آ رہی ہے۔ تاہم، میں آپ کو دستیاب معلومات فراہم کر سکتا ہوں:

{district_info}

مزید تفصیلی معلومات کے لیے، براہ کرم موسم کا ڈیش بورڈ چیک کریں یا اپنا سوال دوبارہ پوچھیں۔"""

    elif language == "sindhi":
        return f"""معاف ڪجو، مون کي توهان جي سوال جو مڪمل جواب ڏيڻ ۾ ڏکيائي پيش اچي رهي آهي. تنهن هوندي به، مان توهان کي دستياب معلومات فراهم ڪري سگهان ٿو:

{district_info}

وڌيڪ تفصيلي معلومات لاءِ، مهرباني ڪري موسم جو ڊيش بورڈ چيڪ ڪريو يا پنهنجو سوال ٻيهر پڇو."""

    else:  # Default to English
        return f"""I apologize, but I'm having trouble providing a complete answer to your question. However, I can share the available information:

{district_info}

For more detailed information, please check the Weather Dashboard or rephrase your question."""

def generate_context_based_response(context: str, language: str) -> str:
    """
    Generate a response based on available context when district information is not available.
    """
    if language == "urdu":
        return f"""معذرت، مجھے آپ کے سوال کا مکمل جواب دینے میں دشواری پیش آ رہی ہے۔ تاہم، یہ متعلقہ معلومات مفید ہو سکتی ہیں:

{context}

مزید معلومات کے لیے، براہ کرم اپنا سوال دوبارہ پوچھیں یا مخصوص ضلع کے بارے میں پوچھیں۔"""

    elif language == "sindhi":
        return f"""معاف ڪجو، مون کي توهان جي سوال جو مڪمل جواب ڏيڻ ۾ ڏکيائي پيش اچي رهي آهي. تنهن هوندي به، هي لاڳاپيل معلومات مددگار ٿي سگهن ٿيون:

{context}

وڌيڪ معلومات لاءِ، مهرباني ڪري پنهنجو سوال ٻيهر پڇو يا ڪنهن خاص ضلعي بابت پڇو."""

    else:  # Default to English
        return f"""I apologize, but I'm having trouble providing a complete answer to your question. However, this related information might be helpful:

{context}

For more information, please rephrase your question or ask about a specific district."""

def generate_generic_fallback(language: str) -> str:
    """
    Generate a generic fallback response when no specific information is available.
    """
    if language == "urdu":
        return """معذرت، مجھے آپ کے سوال کا جواب دینے میں دشواری پیش آ رہی ہے۔ سندھ میں مختلف موسمیاتی علاقے ہیں، ساحلی علاقوں میں معتدل درجہ حرارت سے لے کر اندرونی علاقوں میں انتہائی گرمی تک۔ کئی اضلاع پانی کی کمی، شدید گرمی، اور سیلاب جیسے مسائل کا سامنا کر رہے ہیں۔

براہ کرم اپنا سوال دوبارہ پوچھیں یا کسی مخصوص ضلع کے بارے میں پوچھیں۔"""

    elif language == "sindhi":
        return """معاف ڪجو، مون کي توهان جي سوال جو جواب ڏيڻ ۾ ڏکيائي پيش اچي رهي آهي. سنڌ ۾ مختلف موسمياتي علائقا آهن، ساحلي علائقن ۾ معتدل درجه حرارت کان وٺي اندروني علائقن ۾ انتهائي گرمي تائين. ڪيترائي ضلعا پاڻي جي کوٽ، شديد گرمي، ۽ ٻوڏ جهڙن مسئلن جو شڪار آهن.

مهرباني ڪري پنهنجو سوال ٻيهر پڇو يا ڪنهن خاص ضلعي بابت پڇو."""

    else:  # Default to English
        return """I apologize, but I'm having trouble processing your request. Here's what I know about Sindh's climate: Sindh has diverse climate zones ranging from coastal areas with moderate temperatures to extremely hot interior regions. Many districts face challenges including water scarcity, extreme heat, and flooding.

Please try rephrasing your question or ask about a specific district.""" 