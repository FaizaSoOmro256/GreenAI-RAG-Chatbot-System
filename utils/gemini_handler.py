"""
Gemini Flash 2.0 Integration Handler for GreenAI-RAG Chatbot
This module manages the integration of Google's Gemini Flash 2.0 for enhanced natural language processing,
climate data analysis, and multilingual support.
"""

import os
from typing import Dict, List, Any, Optional
from datetime import datetime
import logging
import google.generativeai as genai
from dotenv import load_dotenv
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GeminiHandler:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.model_version = "gemini-flash-2.0"
        self.initialize_model()
        
        # Supported languages for our climate chatbot
        self.supported_languages = {
            "en": "English",
            "ur": "Urdu",
            "sd": "Sindhi",
            "pa": "Punjabi",
            "ps": "Pashto"
        }
        
        # Specialized contexts for climate data
        self.contexts = {
            "climate_analysis": "Analyze climate patterns and trends",
            "agricultural_impact": "Assess agricultural implications",
            "water_resources": "Evaluate water resource management",
            "disaster_preparedness": "Analyze disaster risks and preparedness",
            "sdg_progress": "Track SDG implementation progress"
        }

    def initialize_model(self):
        """Initialize Gemini Flash 2.0 model with our specific configuration"""
        try:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(
                model_name=self.model_version,
                generation_config={
                    "temperature": 0.7,
                    "top_p": 0.9,
                    "top_k": 40,
                    "max_output_tokens": 2048
                }
            )
            logger.info("Gemini Flash 2.0 model initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing Gemini model: {str(e)}")
            raise

    def process_climate_query(self, 
                            query: str, 
                            district: str, 
                            language: str = "en",
                            context: str = "climate_analysis") -> Dict[str, Any]:
        """
        Process climate-related queries using Gemini's advanced capabilities
        
        Args:
            query: User's question about climate data
            district: Specific district for data analysis
            language: Preferred language for response
            context: Type of analysis needed
        """
        try:
            # Prepare prompt with context
            prompt = self._prepare_climate_prompt(query, district, context)
            
            # Generate response
            response = self.model.generate_content(prompt)
            
            # Process and structure the response
            processed_response = self._structure_climate_response(response)
            
            # Translate if needed
            if language != "en":
                processed_response = self._translate_response(processed_response, language)
            
            return {
                "status": "success",
                "response": processed_response,
                "metadata": {
                    "district": district,
                    "language": language,
                    "context": context,
                    "timestamp": datetime.now().isoformat()
                }
            }
            
        except Exception as e:
            logger.error(f"Error processing climate query: {str(e)}")
            return {
                "status": "error",
                "error": str(e),
                "fallback_response": "Unable to process query at the moment"
            }

    def analyze_climate_trends(self, 
                             district_data: Dict[str, Any], 
                             timeframe: str = "historical") -> Dict[str, Any]:
        """
        Use Gemini's analytical capabilities to analyze climate trends
        
        Args:
            district_data: Historical and current climate data
            timeframe: Period for analysis (historical/current/future)
        """
        try:
            # Prepare data for analysis
            analysis_prompt = self._prepare_analysis_prompt(district_data, timeframe)
            
            # Generate analytical insights
            analysis = self.model.generate_content(analysis_prompt)
            
            return {
                "status": "success",
                "analysis": self._structure_analysis_response(analysis),
                "confidence_score": self._calculate_confidence(analysis)
            }
            
        except Exception as e:
            logger.error(f"Error in climate trend analysis: {str(e)}")
            return {"status": "error", "error": str(e)}

    def generate_climate_recommendations(self, 
                                      district: str, 
                                      current_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate climate action recommendations using Gemini's predictive capabilities
        
        Args:
            district: Target district
            current_data: Current climate and environmental data
        """
        try:
            # Prepare recommendation prompt
            prompt = self._prepare_recommendation_prompt(district, current_data)
            
            # Generate recommendations
            recommendations = self.model.generate_content(prompt)
            
            return {
                "status": "success",
                "recommendations": self._structure_recommendations(recommendations),
                "priority_actions": self._extract_priority_actions(recommendations)
            }
            
        except Exception as e:
            logger.error(f"Error generating recommendations: {str(e)}")
            return {"status": "error", "error": str(e)}

    def _prepare_climate_prompt(self, query: str, district: str, context: str) -> str:
        """Prepare context-aware prompt for climate queries"""
        return f"""
        Context: {self.contexts[context]}
        District: {district}
        Query: {query}
        
        Analyze the query considering:
        1. Historical climate patterns
        2. Current environmental conditions
        3. Future projections and risks
        4. Local geographical features
        5. Socio-economic factors
        
        Provide a detailed response with:
        - Data-driven insights
        - Practical implications
        - Relevant recommendations
        """

    def _structure_climate_response(self, response: Any) -> Dict[str, Any]:
        """Structure the raw response into organized sections"""
        try:
            # Parse the response content
            content = response.text
            
            # Split into sections based on common patterns
            sections = content.split("\n\n")
            
            # Organize into structured format
            structured_response = {
                "summary": sections[0] if sections else "",
                "analysis": {
                    "historical": self._extract_section(content, "Historical Analysis"),
                    "current": self._extract_section(content, "Current Conditions"),
                    "future": self._extract_section(content, "Future Projections")
                },
                "implications": self._extract_section(content, "Implications"),
                "recommendations": self._extract_section(content, "Recommendations")
            }
            
            return structured_response
            
        except Exception as e:
            logger.error(f"Error structuring response: {str(e)}")
            return {"error": "Could not structure response"}

    def _translate_response(self, response: Dict[str, Any], target_language: str) -> Dict[str, Any]:
        """Translate response to target language while maintaining structure"""
        try:
            # Prepare translation prompt
            translation_prompt = f"""
            Translate the following climate analysis to {self.supported_languages[target_language]}
            while maintaining technical accuracy and cultural context:
            
            {response}
            """
            
            # Get translation
            translation = self.model.generate_content(translation_prompt)
            
            # Structure translated content
            translated_response = self._structure_climate_response(translation)
            
            return translated_response
            
        except Exception as e:
            logger.error(f"Error in translation: {str(e)}")
            return response  # Return original response if translation fails

    def _prepare_analysis_prompt(self, data: Dict[str, Any], timeframe: str) -> str:
        """Prepare prompt for climate trend analysis"""
        return f"""
        Analyze the following climate data for {timeframe} timeframe:
        
        Data:
        {json.dumps(data, indent=2)}
        
        Please provide:
        1. Key trends and patterns
        2. Statistical significance of changes
        3. Correlation with other environmental factors
        4. Potential impacts on:
           - Agriculture
           - Water resources
           - Local communities
        5. Confidence level in the analysis
        """

    def _structure_analysis_response(self, analysis: Any) -> Dict[str, Any]:
        """Structure the analysis results"""
        try:
            content = analysis.text
            
            return {
                "trends": self._extract_section(content, "Key Trends"),
                "significance": self._extract_section(content, "Statistical Significance"),
                "correlations": self._extract_section(content, "Correlations"),
                "impacts": {
                    "agriculture": self._extract_section(content, "Agricultural Impacts"),
                    "water": self._extract_section(content, "Water Resources"),
                    "community": self._extract_section(content, "Community Impacts")
                },
                "confidence_level": self._calculate_confidence(analysis)
            }
            
        except Exception as e:
            logger.error(f"Error structuring analysis: {str(e)}")
            return {"error": "Could not structure analysis"}

    def _calculate_confidence(self, analysis: Any) -> float:
        """Calculate confidence score for analysis"""
        try:
            content = analysis.text.lower()
            
            # Define confidence indicators
            high_confidence = ["certain", "clear evidence", "strong correlation", "significant"]
            medium_confidence = ["likely", "moderate", "possible", "suggests"]
            low_confidence = ["uncertain", "unclear", "might", "could"]
            
            # Count indicators
            high_count = sum(content.count(term) for term in high_confidence)
            medium_count = sum(content.count(term) for term in medium_confidence)
            low_count = sum(content.count(term) for term in low_confidence)
            
            # Calculate weighted score
            total_count = high_count + medium_count + low_count
            if total_count == 0:
                return 0.5  # Default medium confidence
                
            confidence_score = (high_count * 1.0 + medium_count * 0.6 + low_count * 0.2) / total_count
            
            return round(confidence_score, 2)
            
        except Exception as e:
            logger.error(f"Error calculating confidence: {str(e)}")
            return 0.5  # Default to medium confidence on error

    def _prepare_recommendation_prompt(self, district: str, data: Dict[str, Any]) -> str:
        """Prepare prompt for generating recommendations"""
        return f"""
        Based on the following climate and environmental data for {district}:
        
        {json.dumps(data, indent=2)}
        
        Please provide:
        1. Immediate actions needed (next 7 days)
        2. Short-term recommendations (1-3 months)
        3. Long-term strategic actions (1-5 years)
        4. Priority ranking for each recommendation
        5. Implementation considerations
        
        Focus on practical, actionable recommendations for:
        - Local authorities
        - Farmers and agricultural workers
        - Community members
        - Environmental organizations
        """

    def _structure_recommendations(self, recommendations: Any) -> List[Dict[str, Any]]:
        """Structure the recommendations"""
        try:
            content = recommendations.text
            
            # Extract different timeframe recommendations
            immediate = self._extract_section(content, "Immediate Actions")
            short_term = self._extract_section(content, "Short-term")
            long_term = self._extract_section(content, "Long-term")
            
            # Convert to list of structured recommendations
            structured_recommendations = []
            
            # Process immediate actions
            if immediate:
                structured_recommendations.extend([
                    {
                        "timeframe": "immediate",
                        "action": action.strip(),
                        "priority": "high"
                    }
                    for action in immediate.split("\n") if action.strip()
                ])
            
            # Process short-term recommendations
            if short_term:
                structured_recommendations.extend([
                    {
                        "timeframe": "short_term",
                        "action": action.strip(),
                        "priority": "medium"
                    }
                    for action in short_term.split("\n") if action.strip()
                ])
            
            # Process long-term recommendations
            if long_term:
                structured_recommendations.extend([
                    {
                        "timeframe": "long_term",
                        "action": action.strip(),
                        "priority": "low"
                    }
                    for action in long_term.split("\n") if action.strip()
                ])
            
            return structured_recommendations
            
        except Exception as e:
            logger.error(f"Error structuring recommendations: {str(e)}")
            return []

    def _extract_priority_actions(self, recommendations: Any) -> List[str]:
        """Extract priority actions from recommendations"""
        try:
            structured_recs = self._structure_recommendations(recommendations)
            
            # Filter high priority and immediate actions
            priority_actions = [
                rec["action"]
                for rec in structured_recs
                if rec["priority"] == "high" or rec["timeframe"] == "immediate"
            ]
            
            return priority_actions[:5]  # Return top 5 priority actions
            
        except Exception as e:
            logger.error(f"Error extracting priority actions: {str(e)}")
            return []

    def _extract_section(self, content: str, section_name: str) -> str:
        """Helper method to extract sections from response content"""
        try:
            start = content.lower().find(section_name.lower())
            if start == -1:
                return ""
                
            # Find the start of the next section
            next_section = float('inf')
            for section in ["Historical Analysis", "Current Conditions", "Future Projections",
                          "Implications", "Recommendations", "Key Trends", "Statistical Significance",
                          "Correlations", "Agricultural Impacts", "Water Resources", "Community Impacts",
                          "Immediate Actions", "Short-term", "Long-term"]:
                pos = content.lower().find(section.lower(), start + len(section_name))
                if pos != -1:
                    next_section = min(next_section, pos)
            
            # Extract the section content
            section_content = content[start + len(section_name):next_section].strip()
            return section_content if section_content else ""
            
        except Exception as e:
            logger.error(f"Error extracting section: {str(e)}")
            return "" 