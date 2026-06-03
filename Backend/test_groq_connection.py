#!/usr/bin/env python3
"""
Test script to verify Groq API connection and OpenAI library compatibility.
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("=" * 60)
print("TopicFlow - Groq API Connection Test")
print("=" * 60)
print()

# Check OpenAI library version
try:
    import openai
    print(f"✓ OpenAI library version: {openai.__version__}")
except ImportError:
    print("✗ OpenAI library not installed")
    print("  Run: pip install openai")
    sys.exit(1)

# Check API key
api_key = os.getenv('GROQ_API_KEY')
if not api_key or api_key == 'your_groq_api_key_here':
    print("✗ GROQ_API_KEY not configured")
    print("  Please update .env file with your actual API key")
    sys.exit(1)
else:
    print(f"✓ API Key loaded (length: {len(api_key)})")

# Clear proxy settings
for proxy_var in ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy']:
    if proxy_var in os.environ:
        print(f"  Clearing {proxy_var}: {os.environ[proxy_var]}")
        os.environ.pop(proxy_var, None)

print()
print("Testing Groq API connection...")
print("-" * 60)

try:
    from openai import OpenAI
    
    # Try to create client
    print("Creating OpenAI client with Groq base URL...")
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )
    print("✓ Client created successfully")
    
    # Try a simple API call
    print()
    print("Testing API call with simple prompt...")
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Respond in JSON format."},
            {"role": "user", "content": "Say hello in JSON format with a 'message' field."}
        ],
        response_format={"type": "json_object"},
        max_tokens=50
    )
    
    print("✓ API call successful!")
    print()
    print("Response:")
    print(response.choices[0].message.content)
    print()
    print("=" * 60)
    print("✓ All tests passed! Groq API is working correctly.")
    print("=" * 60)
    
except TypeError as e:
    print(f"✗ TypeError: {e}")
    print()
    print("This usually means the OpenAI library version is incompatible.")
    print("Try running:")
    print("  pip uninstall openai")
    print("  pip install openai>=1.0.0")
    sys.exit(1)
    
except Exception as e:
    print(f"✗ Error: {e}")
    print()
    print("Possible causes:")
    print("  1. Invalid API key")
    print("  2. Network connection issues")
    print("  3. Groq API service unavailable")
    sys.exit(1)
