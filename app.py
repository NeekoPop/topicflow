#!/usr/bin/env python3
"""
TopicFlow - AI Educational Assistant Backend API
Main application file for the Flask backend.
"""

import os
import json
from flask import Flask, render_template, jsonify, request, send_from_directory
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Disable proxy settings that might interfere with OpenAI client
os.environ.pop('HTTP_PROXY', None)
os.environ.pop('HTTPS_PROXY', None)
os.environ.pop('http_proxy', None)
os.environ.pop('https_proxy', None)

# Import OpenAI after clearing proxy settings
from openai import OpenAI

# Initialize Flask application
app = Flask(__name__, 
            static_folder='static',
            template_folder='templates')

# Configuration
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
app.config['JSON_SORT_KEYS'] = False  # Keep JSON response order as defined

# API Key Management
def load_api_key() -> str:
    """
    Load GROQ_API_KEY from .env file.
    
    Returns:
        str: The API key
        
    Raises:
        ValueError: If API key is missing or empty
    """
    api_key = os.getenv('GROQ_API_KEY')
    if not api_key or api_key.strip() == '':
        raise ValueError("GROQ_API_KEY not found in environment. Please check your .env file.")
    return api_key.strip()

# AI Service Client Integration
def create_groq_client() -> OpenAI:
    """
    Initialize OpenAI client configured for Groq API.
    
    Returns:
        OpenAI: Configured OpenAI client instance with Groq base URL
        
    Raises:
        ValueError: If API key is missing or invalid
        Exception: If client initialization fails
    """
    try:
        api_key = load_api_key()
        
        # Clear any proxy settings that might interfere
        for proxy_var in ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'NO_PROXY', 'no_proxy']:
            os.environ.pop(proxy_var, None)
        
        # Try to initialize OpenAI client with Groq base URL
        # Method 1: Standard initialization
        try:
            client = OpenAI(
                api_key=api_key,
                base_url="https://api.groq.com/openai/v1"
            )
            return client
        except TypeError as te:
            # If there's a TypeError about unexpected arguments, try alternative method
            if "unexpected keyword argument" in str(te):
                # Method 2: Try with explicit parameters only
                import openai as openai_module
                print(f"Warning: OpenAI library version {openai_module.__version__} may have compatibility issues")
                print("Attempting alternative initialization method...")
                
                # Create client with minimal parameters
                client = OpenAI(api_key=api_key)
                # Manually set base_url if possible
                if hasattr(client, '_base_url'):
                    client._base_url = "https://api.groq.com/openai/v1"
                elif hasattr(client, 'base_url'):
                    client.base_url = "https://api.groq.com/openai/v1"
                
                return client
            else:
                raise
        
    except ValueError as e:
        # Re-raise API key errors
        raise
    except Exception as e:
        # Wrap other initialization errors with more details
        error_msg = str(e)
        if "unexpected keyword argument" in error_msg:
            raise Exception(
                f"OpenAI client version incompatibility detected.\n"
                f"Please run these commands:\n"
                f"  pip uninstall openai -y\n"
                f"  pip install 'openai>=1.0.0'\n"
                f"Original error: {error_msg}"
            )
        raise Exception(f"Failed to initialize Groq client: {error_msg}")

def call_ai_service(client: OpenAI, system_prompt: str, user_prompt: str) -> dict:
    """
    Make API call to Groq AI service with JSON response format.
    
    Args:
        client: Configured OpenAI client instance
        system_prompt: System message defining AI behavior
        user_prompt: User message with the actual content/request
        
    Returns:
        dict: Parsed JSON response from AI service
        
    Raises:
        ValueError: If prompts are empty or invalid
        Exception: If AI service call fails or response is invalid
    """
    # Validate inputs
    if not system_prompt or not system_prompt.strip():
        raise ValueError("System prompt cannot be empty")
    if not user_prompt or not user_prompt.strip():
        raise ValueError("User prompt cannot be empty")
    
    try:
        # Make API call with configured parameters
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format={"type": "json_object"}
        )
        
        # Extract content from response
        content = response.choices[0].message.content
        
        # Parse JSON response
        try:
            result = json.loads(content)
            return result
        except json.JSONDecodeError as e:
            raise Exception(f"Failed to parse AI response as JSON: {str(e)}")
            
    except ValueError as e:
        # Re-raise validation errors
        raise
    except json.JSONDecodeError as e:
        # Re-raise JSON parsing errors
        raise Exception(f"Invalid JSON response from AI service: {str(e)}")
    except Exception as e:
        # Handle AI service errors
        error_msg = str(e)
        if "rate_limit" in error_msg.lower():
            raise Exception("AI service rate limit exceeded. Please try again later.")
        elif "authentication" in error_msg.lower() or "api_key" in error_msg.lower():
            raise Exception("AI service authentication failed. Please check your API key.")
        elif "timeout" in error_msg.lower():
            raise Exception("AI service request timed out. Please try again.")
        else:
            raise Exception(f"AI service unavailable: {error_msg}")

# Routes
@app.route('/')
def index():
    """Serve the main application page."""
    return render_template('index.html')

@app.route('/static/<path:path>')
def serve_static(path):
    """Serve static files from the static directory."""
    return send_from_directory('static', path)

@app.route('/api/summarize', methods=['POST'])
def summarize():
    """
    Summarize study material using AI.
    
    Request JSON:
        {
            "material": "string (study material text)"
        }
    
    Response JSON:
        {
            "summary": "string (bulleted summary text)"
        }
    
    Error Responses:
        400: Missing or empty material
        500: AI service error or API key issues
    """
    try:
        # Get material from request
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Request body must be JSON'}), 400
        
        material = data.get('material', '').strip()
        if not material:
            return jsonify({'error': 'Material input is required and cannot be empty'}), 400
        
        # Create Groq client
        try:
            client = create_groq_client()
        except ValueError as e:
            return jsonify({'error': 'API key configuration error. Please check your .env file.'}), 500
        except Exception as e:
            return jsonify({'error': f'Failed to initialize AI service: {str(e)}'}), 500
        
        # Construct prompts with proper JSON format
        system_prompt = """You are an educational assistant that creates concise summaries.

CRITICAL: You MUST return ONLY valid JSON. Do NOT include newlines inside the JSON string value.

Return format (example):
{"summary": "Point 1. Point 2. Point 3."}

Rules:
- Combine all points into ONE string
- Separate points with periods or semicolons
- Do NOT use newline characters inside the string
- Do NOT use bullet symbols inside the JSON
- Keep it concise (5-10 key points)
- Focus on main concepts"""
        
        user_prompt = f"""Summarize this study material into 5-10 key points. Return as valid JSON with a "summary" field containing all points in one string, separated by periods.

Material:
{material}

Example response format:
{{"summary": "First point about the topic. Second important concept. Third key fact. Fourth detail. Fifth conclusion."}}"""
        
        # Call AI service
        try:
            result = call_ai_service(client, system_prompt, user_prompt)
        except Exception as e:
            return jsonify({'error': f'AI service error: {str(e)}'}), 500
        
        # Validate and extract summary
        if not result or not isinstance(result, dict):
            return jsonify({'error': 'Invalid response format from AI service'}), 500
        
        summary = result.get('summary', '')
        
        # If summary is None or empty, try to extract from other fields
        if not summary:
            summary = result.get('text', '') or result.get('content', '') or result.get('response', '')
        
        # If still no summary, return error
        if not summary:
            return jsonify({'error': 'AI service returned empty response. Please try again.'}), 500
        
        # Convert summary to bullet points format
        # Split by periods or semicolons and create bullet points
        if '.' in summary:
            points = [p.strip() for p in summary.split('.') if p.strip()]
        elif ';' in summary:
            points = [p.strip() for p in summary.split(';') if p.strip()]
        else:
            # If no clear separators, treat as single point
            points = [summary.strip()]
        
        # Format as bullet points
        formatted_summary = '\n'.join([f'• {point}' for point in points if point])
        
        return jsonify({'summary': formatted_summary}), 200
        
    except Exception as e:
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

@app.route('/api/quiz', methods=['POST'])
def quiz():
    """
    Generate quiz questions from study material using AI.
    
    Request JSON:
        {
            "material": "string (study material text)"
        }
    
    Response JSON:
        {
            "questions": [
                {
                    "question": "string",
                    "choices": ["string", "string", "string", "string"],
                    "correct_answer": "string",
                    "explanation": "string"
                }
            ]
        }
    
    Error Responses:
        400: Missing or empty material
        500: AI service error or API key issues
    """
    try:
        # Get material from request
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Request body must be JSON'}), 400
        
        material = data.get('material', '').strip()
        if not material:
            return jsonify({'error': 'Material input is required and cannot be empty'}), 400
        
        # Create Groq client
        try:
            client = create_groq_client()
        except ValueError as e:
            return jsonify({'error': 'API key configuration error. Please check your .env file.'}), 500
        except Exception as e:
            return jsonify({'error': f'Failed to initialize AI service: {str(e)}'}), 500
        
        # Construct prompts
        system_prompt = """You are an educational assistant that creates quiz questions. 
Generate exactly 5 multiple-choice questions from the provided material. 
Each question must have exactly 4 answer choices, one correct answer, and an explanation. 
Return the response as JSON with a 'questions' array.

JSON format:
{
    "questions": [
        {
            "question": "Question text here?",
            "choices": ["Choice A", "Choice B", "Choice C", "Choice D"],
            "correct_answer": "Choice A",
            "explanation": "Explanation of why this is correct"
        }
    ]
}"""
        
        user_prompt = f"""Please create exactly 5 multiple-choice questions based on the following study material:

{material}

Requirements:
- Each question should test understanding of key concepts
- Provide exactly 4 answer choices for each question
- Indicate the correct answer (must match one of the choices exactly)
- Provide a clear explanation for each correct answer
- Make the questions challenging but fair"""
        
        # Call AI service
        try:
            result = call_ai_service(client, system_prompt, user_prompt)
        except Exception as e:
            return jsonify({'error': f'AI service error: {str(e)}'}), 500
        
        # Validate response structure
        if 'questions' not in result:
            return jsonify({'error': 'Invalid response from AI service: missing questions field'}), 500
        
        questions = result['questions']
        if not isinstance(questions, list):
            return jsonify({'error': 'Invalid response from AI service: questions must be an array'}), 500
        
        # Validate each question
        for i, q in enumerate(questions):
            if not isinstance(q, dict):
                return jsonify({'error': f'Invalid question {i+1}: must be an object'}), 500
            
            required_fields = ['question', 'choices', 'correct_answer', 'explanation']
            for field in required_fields:
                if field not in q:
                    return jsonify({'error': f'Invalid question {i+1}: missing {field} field'}), 500
            
            if not isinstance(q['choices'], list) or len(q['choices']) != 4:
                return jsonify({'error': f'Invalid question {i+1}: must have exactly 4 choices'}), 500
        
        return jsonify({'questions': questions}), 200
        
    except Exception as e:
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

@app.route('/api/flashcard', methods=['POST'])
def flashcard():
    """
    Generate flashcards from study material using AI.
    
    Request JSON:
        {
            "material": "string (study material text)"
        }
    
    Response JSON:
        {
            "flashcards": [
                {
                    "term": "string",
                    "definition": "string"
                }
            ]
        }
    
    Error Responses:
        400: Missing or empty material
        500: AI service error or API key issues
    """
    try:
        # Get material from request
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Request body must be JSON'}), 400
        
        material = data.get('material', '').strip()
        if not material:
            return jsonify({'error': 'Material input is required and cannot be empty'}), 400
        
        # Create Groq client
        try:
            client = create_groq_client()
        except ValueError as e:
            return jsonify({'error': 'API key configuration error. Please check your .env file.'}), 500
        except Exception as e:
            return jsonify({'error': f'Failed to initialize AI service: {str(e)}'}), 500
        
        # Construct prompts
        system_prompt = """You are an educational assistant that creates flashcards. 
Extract key terms and their definitions from the provided material. 
Return the response as JSON with a 'flashcards' array containing term-definition pairs.

JSON format:
{
    "flashcards": [
        {
            "term": "Key term or concept",
            "definition": "Clear, concise definition or explanation"
        }
    ]
}"""
        
        user_prompt = f"""Please create flashcards from the following study material:

{material}

Requirements:
- Extract the most important terms, concepts, and vocabulary
- Provide clear, concise definitions for each term
- Create at least 5 flashcards, but no more than 15
- Focus on terms that are essential for understanding the material"""
        
        # Call AI service
        try:
            result = call_ai_service(client, system_prompt, user_prompt)
        except Exception as e:
            return jsonify({'error': f'AI service error: {str(e)}'}), 500
        
        # Validate response structure
        if 'flashcards' not in result:
            return jsonify({'error': 'Invalid response from AI service: missing flashcards field'}), 500
        
        flashcards = result['flashcards']
        if not isinstance(flashcards, list):
            return jsonify({'error': 'Invalid response from AI service: flashcards must be an array'}), 500
        
        # Validate each flashcard
        for i, card in enumerate(flashcards):
            if not isinstance(card, dict):
                return jsonify({'error': f'Invalid flashcard {i+1}: must be an object'}), 500
            
            if 'term' not in card or 'definition' not in card:
                return jsonify({'error': f'Invalid flashcard {i+1}: must have term and definition fields'}), 500
            
            if not card['term'].strip() or not card['definition'].strip():
                return jsonify({'error': f'Invalid flashcard {i+1}: term and definition cannot be empty'}), 500
        
        return jsonify({'flashcards': flashcards}), 200
        
    except Exception as e:
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

@app.route('/health')
def health():
    """Health check endpoint."""
    try:
        # Test API key loading as part of health check
        api_key = load_api_key()
        api_key_status = 'valid' if api_key and api_key != 'your_groq_api_key_here' else 'placeholder'
        
        return jsonify({
            'status': 'healthy',
            'service': 'TopicFlow API',
            'version': '1.0.0',
            'api_key': api_key_status,
            'static_files': 'serving from /static/',
            'templates': 'serving from /templates/'
        })
    except ValueError as e:
        # API key error - still return health but with warning
        return jsonify({
            'status': 'degraded',
            'service': 'TopicFlow API',
            'version': '1.0.0',
            'warning': 'API key configuration issue',
            'error': str(e),
            'static_files': 'serving from /static/',
            'templates': 'serving from /templates/'
        }), 200

@app.route('/api/config')
def config():
    """Configuration endpoint to verify API key loading (for debugging)."""
    try:
        api_key = load_api_key()
        # Don't expose the actual API key, just confirm it's loaded
        key_preview = f"{api_key[:8]}...{api_key[-4:]}" if len(api_key) > 12 else "***"
        
        return jsonify({
            'api_key_loaded': True,
            'api_key_preview': key_preview,
            'api_key_length': len(api_key),
            'is_placeholder': api_key == 'your_groq_api_key_here',
            'static_folder': app.static_folder,
            'template_folder': app.template_folder
        })
    except ValueError as e:
        return jsonify({
            'api_key_loaded': False,
            'error': str(e),
            'static_folder': app.static_folder,
            'template_folder': app.template_folder
        }), 500

# Error handlers
@app.errorhandler(400)
def bad_request(error):
    """Handle 400 errors."""
    return jsonify({'error': 'Bad request'}), 400

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    # Check if it's an API key error
    if isinstance(error, ValueError) and 'GROQ_API_KEY' in str(error):
        return jsonify({'error': 'API key configuration error'}), 500
    
    # Generic internal error
    return jsonify({'error': 'Internal server error'}), 500

@app.errorhandler(ValueError)
def handle_value_error(error):
    """Handle ValueError exceptions (e.g., missing API key)."""
    if 'GROQ_API_KEY' in str(error):
        return jsonify({'error': 'API key configuration error'}), 500
    return jsonify({'error': str(error)}), 400

if __name__ == '__main__':
    # Get port from environment or use default
    port = int(os.getenv('PORT', 5000))
    
    # Run the application
    print(f"Starting TopicFlow API on port {port}")
    print(f"Static files: {app.static_folder}")
    print(f"Templates: {app.template_folder}")
    
    try:
        api_key = load_api_key()
        if api_key == 'your_groq_api_key_here':
            print("⚠️  WARNING: Using placeholder API key. Update .env file with your actual GROQ_API_KEY.")
        else:
            print(f"✓ API Key loaded successfully (length: {len(api_key)})")
    except ValueError as e:
        print(f"❌ ERROR: {e}")
        print("The application will start but AI features will not work.")
    
    app.run(host='0.0.0.0', port=port, debug=True)