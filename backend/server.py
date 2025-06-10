import asyncio
import os
import uvicorn
from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError

from .types import GenerationRequest, GenerationResponse, AIAgentError

app = FastAPI(
    title="Project Linguist - AI Content Generator",
    description="Generate content concurrently across 119+ languages with a simple English prompt using Qwen3-32B powered by Groq",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001", 
        "http://127.0.0.1:3000",
        "http://127.0.0.1:3001"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Project Linguist Backend is running"}


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "message": "Backend is running. Users provide API keys through the web interface."
    }


@app.post("/api/generate", response_model=GenerationResponse)
async def generate_content(request: GenerationRequest, x_api_key: str = Header(..., alias="X-API-Key")):
    """Generate multilingual content"""
    try:
        # validate API key
        if not x_api_key or not x_api_key.strip():
            raise HTTPException(status_code=401, detail="Groq API key is required")
        
        # keeping this here just so api can validate input - if ever converted to mobile app or cli.
        if not request.prompt or not request.prompt.strip():
            raise HTTPException(status_code=400, detail="Prompt is required")
        
        if not request.targetLanguages or len(request.targetLanguages) == 0:
            raise HTTPException(status_code=400, detail="At least one target language is required")
        
        # create agent with user's API key
        from .ai_agent import AIAgent
        from . import create_groq_config
        
        config = create_groq_config(x_api_key.strip())
        
        agent = AIAgent(config)
        response = await agent.generate_multilingual_content(request)
        
        return response
        
    except AIAgentError as error:
        # handle specific error types
        if error.type == "VALIDATION_ERROR":
            raise HTTPException(status_code=400, detail=error.message)
        elif error.type == "RATE_LIMIT":
            raise HTTPException(status_code=429, detail="Rate limit exceeded. Please try again later.")
        elif error.type == "API_ERROR" and "unauthorized" in error.message.lower():
            raise HTTPException(status_code=401, detail="Invalid API key. Please check your Groq API key.")
        else:
            raise HTTPException(status_code=500, detail=error.message)
    
    except ValidationError as error:
        raise HTTPException(status_code=400, detail=f"Validation error: {str(error)}")
    
    except Exception as error:
        error_str = str(error)
        print(f"API Error: {error}")
        
        # check for unauthorized/authentication errors
        if "unauthorized" in error_str.lower() or "401" in error_str or "invalid" in error_str.lower():
            raise HTTPException(status_code=401, detail="Invalid API key. Please check your Groq API key.")
        
        raise HTTPException(status_code=500, detail=str(error))


@app.get("/api/languages")
async def get_languages():
    """Get all available languages"""
    from .types import AVAILABLE_LANGUAGES, LANGUAGES_BY_FAMILY
    
    return {
        "languages": [lang.dict() for lang in AVAILABLE_LANGUAGES],
        "languagesByFamily": {
            family: [lang.dict() for lang in langs] 
            for family, langs in LANGUAGES_BY_FAMILY.items()
        },
        "total": len(AVAILABLE_LANGUAGES)
    }


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(
        "backend.server:app",
        host="0.0.0.0",
        port=port,
        reload=True,
        log_level="info"
    ) 