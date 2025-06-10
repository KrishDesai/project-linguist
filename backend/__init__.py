import os
from groq import Groq
from .types import GroqConfig
from .ai_agent import AIAgent

def create_groq_config(api_key: str) -> GroqConfig:
    """Create a GroqConfig with the provided API key"""
    return GroqConfig(
        apiKey=api_key,
        model=os.getenv('GROQ_MODEL', 'qwen/qwen3-32b'),
        maxTokens=int(os.getenv('GROQ_MAX_TOKENS', '100000')),
        temperature=float(os.getenv('GROQ_TEMPERATURE', '0.7'))
    )

__all__ = [
    'create_groq_config',
    'AIAgent',
    'GroqConfig'
] 