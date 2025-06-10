import asyncio
import random
import time
from typing import List, Dict, Optional
from groq import Groq
from .types import GroqConfig, AIAgentError
from .utils import remove_thinking_blocks


class GroqService:
    """This class handles all interactions with the Groq API"""
    
    def __init__(self, config: GroqConfig):
        self.config = config
        self.client = Groq(api_key=config.apiKey)
    
    async def generate_content(self, prompt: str, system_prompt: Optional[str] = None) -> tuple[str, Optional[int]]:
        """Generate content using Groq API with retry logic"""
        max_retries = 3
        last_error = None
        
        for attempt in range(1, max_retries + 1):
            try:
                messages = []
                if system_prompt:
                    messages.append({"role": "system", "content": system_prompt})
                messages.append({"role": "user", "content": prompt})
                
                completion = self.client.chat.completions.create(
                    messages=messages,
                    model=self.config.model,
                    max_tokens=self.config.maxTokens,
                    temperature=self.config.temperature,
                )
                
                content = completion.choices[0].message.content
                if not content:
                    raise Exception("No content generated from Groq API")
                
                tokens_used = None
                if hasattr(completion, 'usage') and completion.usage:
                    tokens_used = completion.usage.total_tokens
                
                # remove thinking blocks and return content with token count
                return remove_thinking_blocks(content), tokens_used
                
            except Exception as error:
                last_error = error
                print(f"Groq API Error (attempt {attempt}/{max_retries}): {error}")
                
                # check if this is a retryable error
                is_retryable = (
                    hasattr(error, 'status_code') and error.status_code in [503, 502, 504, 429]
                ) or "503" in str(error) or "502" in str(error) or "504" in str(error) or "429" in str(error)
                
                if not is_retryable or attempt == max_retries:
                    raise self._handle_groq_error(error)
                
                # calculate exponential backoff delay
                base_delay = 1000  # 1 second base
                exponential_delay = base_delay * (2 ** (attempt - 1))
                jitter_delay = exponential_delay + random.randint(0, 1000)
                delay_seconds = jitter_delay / 1000
                
                print(f"Retrying in {delay_seconds:.1f}s... ({attempt}/{max_retries})")
                await asyncio.sleep(delay_seconds)
        
        raise self._handle_groq_error(last_error)
    
    async def translate_content(
        self,
        content: str,
        target_language: str,
        source_language: str = "en"
    ) -> str:
        """Translate content to a target language"""
        translation_prompt = f"""Translate the following content from {source_language} to {target_language}. 
        Maintain the original tone, style, and formatting. 

        IMPORTANT: Output ONLY the translated content. Do NOT include any reasoning, thinking process, commentary, explanations, or phrases like "Here's the translation" or "The translated content is...". Do NOT explain what you're doing. Start directly with the translated content.
        Make SURE TO TRANSLATE THE ENTIRE CONTENT. Do not skip any part of the content.
        Content to translate:
        {content}

        Remember: Output ONLY the translation. No explanations or commentary."""

        try:
            translated_content, _ = await self.generate_content(translation_prompt)
            return translated_content
        except Exception as error:
            print(f"Translation Error ({source_language} -> {target_language}): {error}")
            raise error
    
    async def translate_to_multiple_languages(
        self,
        content: str,
        target_languages: List[str],
        source_language: str = "en"
    ) -> tuple[List[Dict[str, str]], Optional[int]]:
        """Generate multiple translations in parallel"""
        total_tokens = 0
        
        async def translate_single(lang: str) -> Dict[str, str]:
            nonlocal total_tokens
            
            system_prompt = "You are a professional translation tool. Your job is to translate ALL content completely from start to finish. Use all available tokens to ensure the translation is complete. Output only the translated text with no explanations or commentary."
            
            user_prompt = f"""TRANSLATE THIS COMPLETE CONTENT FROM {source_language.upper()} TO {lang.upper()}:

            {content}

            CRITICAL REQUIREMENTS:
            1. TRANSLATE THE ENTIRE CONTENT - Do not stop midway
            2. Output ONLY the translated text with no explanations
            3. NO reasoning, thinking, or commentary
            4. NO "Here is the translation" or similar phrases
            5. Maintain the original structure and formatting exactly
            6. Ensure the translation is COMPLETE from start to finish
            7. Use all necessary tokens to finish the translation

            TRANSLATE EVERYTHING - START NOW:"""

            translated_content, tokens = await self.generate_content(user_prompt, system_prompt)
            if tokens:
                total_tokens += tokens
            return {"language": lang, "content": translated_content}
        
        try:
            # create tasks for parallel translation
            tasks = [translate_single(lang) for lang in target_languages]
            results = await asyncio.gather(*tasks)
            return results, total_tokens if total_tokens > 0 else None
        except Exception as error:
            print(f"Batch translation error: {error}")
            raise error
    
    def _handle_groq_error(self, error: Exception) -> AIAgentError:
        """Handle and categorize Groq API errors"""
        error_str = str(error)
        
        if "429" in error_str or "rate limit" in error_str.lower():
            return AIAgentError(
                "RATE_LIMIT",
                "Rate limit exceeded. Please try again later.",
                {"original_error": error_str}
            )
        
        if "503" in error_str:
            return AIAgentError(
                "API_ERROR",
                "Groq service is temporarily unavailable. This is usually resolved within a few minutes. Please try again later.",
                {"original_error": error_str}
            )
        
        if "502" in error_str or "504" in error_str:
            return AIAgentError(
                "API_ERROR",
                "Groq service is experiencing temporary issues. Please try again in a moment.",
                {"original_error": error_str}
            )
        
        if hasattr(error, 'status_code') and 400 <= error.status_code < 500:
            return AIAgentError(
                "API_ERROR",
                str(error),
                {"original_error": error_str}
            )
        
        return AIAgentError(
            "UNKNOWN",
            f"An unknown error occurred: {error_str}",
            {"original_error": error_str}
        )
    
    async def test_connection(self) -> bool:
        """Test the API connection"""
        try:
            _, _ = await self.generate_content('Say "Hello" in one word.')
            return True
        except Exception as error:
            print(f"Connection test failed: {error}")
            return False 