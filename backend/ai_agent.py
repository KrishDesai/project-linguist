import time
from typing import List, Optional
from .groq_service import GroqService
from .types import (
    GenerationRequest, 
    GenerationResponse, 
    GroqConfig,
    AIAgentError,
    validate_language_codes
)
from .prompts import generate_prompt
from .utils import create_generated_content, clean_content


class AIAgent:
    """AI Agent that orchestrates content generation and translation"""
    
    def __init__(self, config: GroqConfig):
        self.groq_service = GroqService(config)
    
    async def generate_multilingual_content(self, request: GenerationRequest) -> GenerationResponse:
        """Generate multilingual content based on the request"""
        start_time = time.time()
        total_tokens = 0
        
        try:
            self._validate_request(request)
            
            validation_result = validate_language_codes(request.targetLanguages)
            valid_languages = validation_result["valid"]
            invalid_languages = validation_result["invalid"]
            
            if invalid_languages:
                raise AIAgentError(
                    "VALIDATION_ERROR",
                    f"Invalid language codes: {', '.join(invalid_languages)}",
                    {"invalidLanguages": invalid_languages}
                )
            
            print(f"Generating {request.contentType.value} content...")
            original_content, original_tokens = await self._generate_original_content(request)
            if original_tokens:
                total_tokens += original_tokens
            
            source_language = request.sourceLanguage or "en"
            languages_to_translate = [lang for lang in valid_languages if lang != source_language]
            
            translations = []
            if languages_to_translate:
                print(f"Translating to {len(languages_to_translate)} languages...")
                translation_results, translation_tokens = await self.groq_service.translate_to_multiple_languages(
                    original_content,
                    languages_to_translate,
                    source_language
                )
                if translation_tokens:
                    total_tokens += translation_tokens
                
                translations = [
                    create_generated_content(result["language"], result["content"])
                    for result in translation_results
                ]
            
            response = GenerationResponse(
                originalContent=create_generated_content(source_language, original_content),
                translations=translations,
                totalTokensUsed=total_tokens if total_tokens > 0 else None,
                processingTime=int((time.time() - start_time) * 1000)
            )
            
            print(f"Generation completed in {response.processingTime}ms (tokens: {total_tokens})")
            return response
            
        except Exception as error:
            print(f"Generation failed: {error}")
            raise error
    
    async def _generate_original_content(self, request: GenerationRequest) -> tuple[str, Optional[int]]:
        """Generate the original content based on the request"""
        system_prompt, user_prompt = generate_prompt(
            request.contentType,
            request.prompt,
            request.tone or "professional",
            request.length or "medium"
        )
        
        return await self.groq_service.generate_content(user_prompt, system_prompt)
    
    def _validate_request(self, request: GenerationRequest) -> None:
        """Validate the generation request"""
        
        if len(request.prompt) > 5000:
            raise AIAgentError(
                "VALIDATION_ERROR",
                "Prompt is too long (maximum 5000 characters)",
                {"field": "prompt", "maxLength": 5000}
            )
    
    async def test_connection(self) -> bool:
        """Test the AI agent connection"""
        try:
            print("Testing AI agent connection...")
            is_connected = await self.groq_service.test_connection()
            
            if is_connected:
                print("AI agent is ready")
            else:
                print("AI agent connection failed")
            
            return is_connected
        except Exception as error:
            print(f"Connection test error: {error}")
            return False
    
    async def generate_single_language_content(
        self,
        prompt: str,
        content_type: str,
        tone: str = "professional",
        length: str = "medium",
        language: str = "en"
    ) -> str:
        """Generate content for a single language"""
        from .types import ContentType, Tone, Length
        
        system_prompt, user_prompt = generate_prompt(
            ContentType(content_type),
            prompt,
            Tone(tone),
            Length(length)
        )
        
        content, _ = await self.groq_service.generate_content(user_prompt, system_prompt)
        return content
    
    async def translate_content(
        self,
        content: str,
        target_languages: List[str],
        source_language: str = "en"
    ) -> List[dict]:
        """Translate content to multiple target languages"""
        validation_result = validate_language_codes(target_languages)
        valid_languages = validation_result["valid"]
        invalid_languages = validation_result["invalid"]
        
        if invalid_languages:
            raise AIAgentError(
                "VALIDATION_ERROR",
                f"Invalid language codes: {', '.join(invalid_languages)}",
                {"invalidLanguages": invalid_languages}
            )
        
        results, _ = await self.groq_service.translate_to_multiple_languages(
            content,
            valid_languages,
            source_language
        )
        
        return results 