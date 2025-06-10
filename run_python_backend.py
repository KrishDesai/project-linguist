#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Startup script for The Linguist Python Backend
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    # check if we're in the correct directory
    if not Path("backend").exists():
        print("❌ Error: backend directory not found")
        print("Please run this script from the project root directory")
        sys.exit(1)
    
    # check if requirements are installed
    try:
        import fastapi
        import groq
        import uvicorn
        print("✅ Dependencies are installed")
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please install dependencies:")
        print("Check Readme.md for instructions")
        sys.exit(1)
    
    # start the server
    print("🚀 Starting The Linguist Python Backend...")
    print("📡 Server will be available at: http://localhost:8000")
    print("📚 API docs will be available at: http://localhost:8000/docs")
    print("🌍 Health check: http://localhost:8000/health")
    print("💡 Users will enter their Groq API keys through the web interface")
    print("\nPress Ctrl+C to stop the server\n")
    
    try:
        # run the server
        os.system("python3 -m backend.server")
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")

if __name__ == "__main__":
    main() 