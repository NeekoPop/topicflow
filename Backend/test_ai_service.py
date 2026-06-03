#!/usr/bin/env python3
"""
Unit tests for TopicFlow AI service client.
Tests for Requirements 10.1, 10.2, 10.3, 10.4.

This test file focuses on testing the create_groq_client() and call_ai_service()
functions as implemented in app.py.
"""

import os
import json
import pytest
from unittest import mock
from unittest.mock import Mock, MagicMock, patch
import sys

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import app to access AI service functions
import app
from openai import OpenAI


# ============================================================================
# Unit Tests for create_groq_client() Function (Task 3.2)
# ============================================================================

def test_create_groq_client_success():
    """Test successful Groq client initialization with valid API key.
    
    Validates: Requirement 10.1 - THE Backend_API SHALL use the OpenAI-compatible 
    client library to connect to AI_Service
    
    Validates: Requirement 10.2 - THE Backend_API SHALL configure the client with 
    base_url set to "https://api.groq.com/openai/v1"
    
    This test verifies that create_groq_client() successfully initializes an 
    OpenAI client with the correct base URL when a valid API key is present.
    """
    test_key = 'test_groq_api_key_12345'
    
    with mock.patch.dict(os.environ, {'GROQ_API_KEY': test_key}):
        with mock.patch('app.OpenAI') as mock_openai:
            # Create a mock client instance
            mock_client = Mock()
            mock_openai.return_value = mock_client
            
            # Call the function
            result = app.create_groq_client()
            
            # Verify OpenAI was called with correct parameters
            mock_openai.assert_called_once_with(
                api_key=test_key,
                base_url="https://api.groq.com/openai/v1"
            )
            
            # Verify the result is the mock client
            assert result == mock_client, "Should return the OpenAI client instance"


def test_create_groq_client_correct_base_url():
    """Test that create_groq_client() uses the correct Groq base URL.
    
    Validates: Requirement 10.2 - THE Backend_API SHALL configure the client with 
    base_url set to "https://api.groq.com/openai/v1"
    
    This test specifically verifies the base_url parameter is set correctly.
    """
    test_key = 'test_api_key'
    expected_base_url = "https://api.groq.com/openai/v1"
    
    with mock.patch.dict(os.environ, {'GROQ_API_KEY': test_key}):
        with mock.patch('app.OpenAI') as mock_openai:
            mock_client = Mock()
            mock_openai.return_value = mock_client
            
            app.create_groq_client()
            
            # Extract the call arguments
            call_args = mock_openai.call_args
            assert call_args is not None, "OpenAI should have been called"
            
            # Check base_url parameter
            assert 'base_url' in call_args.kwargs, "base_url should be in kwargs"
            assert call_args.kwargs['base_url'] == expected_base_url, \
                f"base_url should be '{expected_base_url}'"


def test_create_groq_client_missing_api_key():
    """Test error handling when API key is missing.
    
    Validates: Requirement 10.1 - THE Backend_API SHALL use the OpenAI-compatible 
    client library to connect to AI_Service
    
    This test verifies that create_groq_client() raises ValueError when the API key
    is missing from the environment.
    """
    with mock.patch.dict(os.environ, {}, clear=True):
        with pytest.raises(ValueError) as exc_info:
            app.create_groq_client()
        
        # Verify the error message mentions API key
        error_message = str(exc_info.value)
        assert 'GROQ_API_KEY' in error_message, \
            "Error message should mention GROQ_API_KEY"


def test_create_groq_client_empty_api_key():
    """Test error handling when API key is empty.
    
    Validates: Requirement 10.1 - THE Backend_API SHALL use the OpenAI-compatible 
    client library to connect to AI_Service
    
    This test verifies that create_groq_client() raises ValueError when the API key
    is an empty string.
    """
    with mock.patch.dict(os.environ, {'GROQ_API_KEY': ''}):
        with pytest.raises(ValueError) as exc_info:
            app.create_groq_client()
        
        error_message = str(exc_info.value)
        assert 'GROQ_API_KEY' in error_message


def test_create_groq_client_initialization_failure():
    """Test error handling when OpenAI client initialization fails.
    
    Validates: Requirement 10.1 - THE Backend_API SHALL use the OpenAI-compatible 
    client library to connect to AI_Service
    
    This test verifies that create_groq_client() handles initialization failures
    gracefully by wrapping them in an Exception.
    """
    test_key = 'test_api_key'
    
    with mock.patch.dict(os.environ, {'GROQ_API_KEY': test_key}):
        with mock.patch('app.OpenAI') as mock_openai:
            # Simulate initialization failure
            mock_openai.side_effect = Exception("Network error")
            
            with pytest.raises(Exception) as exc_info:
                app.create_groq_client()
            
            error_message = str(exc_info.value)
            assert 'Failed to initialize Groq client' in error_message, \
                "Error message should indicate initialization failure"


def test_create_groq_client_returns_openai_instance():
    """Test that create_groq_client() returns an OpenAI client instance.
    
    Validates: Requirement 10.1 - THE Backend_API SHALL use the OpenAI-compatible 
    client library to connect to AI_Service
    
    This test verifies the return type is correct.
    """
    test_key = 'test_api_key'
    
    with mock.patch.dict(os.environ, {'GROQ_API_KEY': test_key}):
        with mock.patch('app.OpenAI') as mock_openai:
            mock_client = Mock(spec=OpenAI)
            mock_openai.return_value = mock_client
            
            result = app.create_groq_client()
            
            # Verify result is the mock client (which has OpenAI spec)
            assert result == mock_client
            assert isinstance(result, Mock), "Should return a client instance"


# ============================================================================
# Unit Tests for call_ai_service() Function (Task 3.2)
# ============================================================================

def test_call_ai_service_success():
    """Test successful AI service call with valid inputs.
    
    Validates: Requirement 10.3 - THE Backend_API SHALL use the model 
    "llama-3.1-8b-instant" for all AI_Service requests
    
    Validates: Requirement 10.4 - THE Backend_API SHALL include response_format 
    parameter set to {"type": "json_object"} for all AI_Service requests
    
    This test verifies that call_ai_service() successfully makes an API call
    with the correct model and response format parameters.
    """
    # Create mock client
    mock_client = Mock()
    
    # Create mock response
    mock_response = Mock()
    mock_response.choices = [Mock()]
    mock_response.choices[0].message.content = '{"result": "success", "data": "test"}'
    
    # Configure mock to return the response
    mock_client.chat.completions.create.return_value = mock_response
    
    # Call the function
    system_prompt = "You are a helpful assistant."
    user_prompt = "Generate a summary."
    
    result = app.call_ai_service(mock_client, system_prompt, user_prompt)
    
    # Verify the API was called with correct parameters
    mock_client.chat.completions.create.assert_called_once()
    call_args = mock_client.chat.completions.create.call_args
    
    # Check model parameter
    assert call_args.kwargs['model'] == "llama-3.1-8b-instant", \
        "Should use llama-3.1-8b-instant model"
    
    # Check response_format parameter
    assert call_args.kwargs['response_format'] == {"type": "json_object"}, \
        "Should use json_object response format"
    
    # Check messages structure
    messages = call_args.kwargs['messages']
    assert len(messages) == 2, "Should have system and user messages"
    assert messages[0]['role'] == 'system', "First message should be system"
    assert messages[0]['content'] == system_prompt, "System message content should match"
    assert messages[1]['role'] == 'user', "Second message should be user"
    assert messages[1]['content'] == user_prompt, "User message content should match"
    
    # Verify result is parsed JSON
    assert result == {"result": "success", "data": "test"}, \
        "Should return parsed JSON response"


def test_call_ai_service_correct_model():
    """Test that call_ai_service() uses the correct model.
    
    Validates: Requirement 10.3 - THE Backend_API SHALL use the model 
    "llama-3.1-8b-instant" for all AI_Service requests
    
    This test specifically verifies the model parameter.
    """
    mock_client = Mock()
    mock_response = Mock()
    mock_response.choices = [Mock()]
    mock_response.choices[0].message.content = '{"test": "data"}'
    mock_client.chat.completions.create.return_value = mock_response
    
    app.call_ai_service(mock_client, "System prompt", "User prompt")
    
    call_args = mock_client.chat.completions.create.call_args
    assert call_args.kwargs['model'] == "llama-3.1-8b-instant", \
        "Model should be llama-3.1-8b-instant"


def test_call_ai_service_correct_response_format():
    """Test that call_ai_service() uses the correct response format.
    
    Validates: Requirement 10.4 - THE Backend_API SHALL include response_format 
    parameter set to {"type": "json_object"} for all AI_Service requests
    
    This test specifically verifies the response_format parameter.
    """
    mock_client = Mock()
    mock_response = Mock()
    mock_response.choices = [Mock()]
    mock_response.choices[0].message.content = '{"test": "data"}'
    mock_client.chat.completions.create.return_value = mock_response
    
    app.call_ai_service(mock_client, "System prompt", "User prompt")
    
    call_args = mock_client.chat.completions.create.call_args
    assert 'response_format' in call_args.kwargs, \
        "response_format should be in parameters"
    assert call_args.kwargs['response_format'] == {"type": "json_object"}, \
        "response_format should be {'type': 'json_object'}"


def test_call_ai_service_empty_system_prompt():
    """Test error handling when system prompt is empty.
    
    Validates: Requirement 10.1 - THE Backend_API SHALL use the OpenAI-compatible 
    client library to connect to AI_Service
    
    This test verifies input validation for system prompt.
    """
    mock_client = Mock()
    
    with pytest.raises(ValueError) as exc_info:
        app.call_ai_service(mock_client, "", "User prompt")
    
    error_message = str(exc_info.value)
    assert 'System prompt' in error_message, \
        "Error message should mention system prompt"


def test_call_ai_service_empty_user_prompt():
    """Test error handling when user prompt is empty.
    
    Validates: Requirement 10.1 - THE Backend_API SHALL use the OpenAI-compatible 
    client library to connect to AI_Service
    
    This test verifies input validation for user prompt.
    """
    mock_client = Mock()
    
    with pytest.raises(ValueError) as exc_info:
        app.call_ai_service(mock_client, "System prompt", "")
    
    error_message = str(exc_info.value)
    assert 'User prompt' in error_message, \
        "Error message should mention user prompt"


def test_call_ai_service_whitespace_only_prompts():
    """Test error handling when prompts contain only whitespace.
    
    Validates: Requirement 10.1 - THE Backend_API SHALL use the OpenAI-compatible 
    client library to connect to AI_Service
    
    This test verifies that whitespace-only prompts are rejected.
    """
    mock_client = Mock()
    
    # Test whitespace-only system prompt
    with pytest.raises(ValueError):
        app.call_ai_service(mock_client, "   ", "User prompt")
    
    # Test whitespace-only user prompt
    with pytest.raises(ValueError):
        app.call_ai_service(mock_client, "System prompt", "   ")


def test_call_ai_service_json_parsing():
    """Test JSON response parsing.
    
    Validates: Requirement 10.4 - THE Backend_API SHALL include response_format 
    parameter set to {"type": "json_object"} for all AI_Service requests
    
    This test verifies that the function correctly parses JSON responses.
    """
    mock_client = Mock()
    mock_response = Mock()
    mock_response.choices = [Mock()]
    
    # Test with complex JSON structure
    test_json = {
        "summary": "Test summary",
        "items": ["item1", "item2"],
        "count": 2,
        "nested": {"key": "value"}
    }
    mock_response.choices[0].message.content = json.dumps(test_json)
    mock_client.chat.completions.create.return_value = mock_response
    
    result = app.call_ai_service(mock_client, "System", "User")
    
    assert result == test_json, "Should correctly parse complex JSON"
    assert isinstance(result, dict), "Result should be a dictionary"
    assert result['summary'] == "Test summary"
    assert result['count'] == 2
    assert result['nested']['key'] == "value"


def test_call_ai_service_malformed_json():
    """Test error handling for malformed JSON response.
    
    Validates: Requirement 10.4 - THE Backend_API SHALL include response_format 
    parameter set to {"type": "json_object"} for all AI_Service requests
    
    This test verifies that malformed JSON responses are handled gracefully.
    """
    mock_client = Mock()
    mock_response = Mock()
    mock_response.choices = [Mock()]
    mock_response.choices[0].message.content = 'This is not valid JSON'
    mock_client.chat.completions.create.return_value = mock_response
    
    with pytest.raises(Exception) as exc_info:
        app.call_ai_service(mock_client, "System", "User")
    
    error_message = str(exc_info.value)
    assert 'JSON' in error_message, "Error message should mention JSON parsing"


def test_call_ai_service_api_failure():
    """Test error handling when AI service API call fails.
    
    Validates: Requirement 10.1 - THE Backend_API SHALL use the OpenAI-compatible 
    client library to connect to AI_Service
    
    This test verifies that API failures are handled gracefully.
    """
    mock_client = Mock()
    mock_client.chat.completions.create.side_effect = Exception("API connection failed")
    
    with pytest.raises(Exception) as exc_info:
        app.call_ai_service(mock_client, "System", "User")
    
    error_message = str(exc_info.value)
    assert 'AI service unavailable' in error_message or 'API connection failed' in error_message, \
        "Error message should indicate service unavailability"


def test_call_ai_service_rate_limit_error():
    """Test error handling for rate limit errors.
    
    Validates: Requirement 10.1 - THE Backend_API SHALL use the OpenAI-compatible 
    client library to connect to AI_Service
    
    This test verifies that rate limit errors are handled with appropriate messaging.
    """
    mock_client = Mock()
    mock_client.chat.completions.create.side_effect = Exception("rate_limit exceeded")
    
    with pytest.raises(Exception) as exc_info:
        app.call_ai_service(mock_client, "System", "User")
    
    error_message = str(exc_info.value)
    assert 'rate limit' in error_message.lower(), \
        "Error message should mention rate limit"


def test_call_ai_service_authentication_error():
    """Test error handling for authentication errors.
    
    Validates: Requirement 10.1 - THE Backend_API SHALL use the OpenAI-compatible 
    client library to connect to AI_Service
    
    This test verifies that authentication errors are handled appropriately.
    """
    mock_client = Mock()
    mock_client.chat.completions.create.side_effect = Exception("authentication failed")
    
    with pytest.raises(Exception) as exc_info:
        app.call_ai_service(mock_client, "System", "User")
    
    error_message = str(exc_info.value)
    assert 'authentication' in error_message.lower(), \
        "Error message should mention authentication"


def test_call_ai_service_timeout_error():
    """Test error handling for timeout errors.
    
    Validates: Requirement 10.1 - THE Backend_API SHALL use the OpenAI-compatible 
    client library to connect to AI_Service
    
    This test verifies that timeout errors are handled appropriately.
    """
    mock_client = Mock()
    mock_client.chat.completions.create.side_effect = Exception("Request timeout")
    
    with pytest.raises(Exception) as exc_info:
        app.call_ai_service(mock_client, "System", "User")
    
    error_message = str(exc_info.value).lower()
    assert 'time' in error_message, \
        "Error message should mention timeout or timed out"


def test_call_ai_service_message_structure():
    """Test that messages are structured correctly.
    
    Validates: Requirement 10.1 - THE Backend_API SHALL use the OpenAI-compatible 
    client library to connect to AI_Service
    
    This test verifies the message structure sent to the API.
    """
    mock_client = Mock()
    mock_response = Mock()
    mock_response.choices = [Mock()]
    mock_response.choices[0].message.content = '{"test": "data"}'
    mock_client.chat.completions.create.return_value = mock_response
    
    system_prompt = "You are a test assistant."
    user_prompt = "Generate test data."
    
    app.call_ai_service(mock_client, system_prompt, user_prompt)
    
    call_args = mock_client.chat.completions.create.call_args
    messages = call_args.kwargs['messages']
    
    # Verify message structure
    assert isinstance(messages, list), "Messages should be a list"
    assert len(messages) == 2, "Should have exactly 2 messages"
    
    # Verify system message
    assert messages[0]['role'] == 'system'
    assert messages[0]['content'] == system_prompt
    
    # Verify user message
    assert messages[1]['role'] == 'user'
    assert messages[1]['content'] == user_prompt


def test_call_ai_service_returns_dict():
    """Test that call_ai_service() returns a dictionary.
    
    Validates: Requirement 10.4 - THE Backend_API SHALL include response_format 
    parameter set to {"type": "json_object"} for all AI_Service requests
    
    This test verifies the return type is a dictionary (parsed JSON).
    """
    mock_client = Mock()
    mock_response = Mock()
    mock_response.choices = [Mock()]
    mock_response.choices[0].message.content = '{"key": "value"}'
    mock_client.chat.completions.create.return_value = mock_response
    
    result = app.call_ai_service(mock_client, "System", "User")
    
    assert isinstance(result, dict), "Result should be a dictionary"


def test_call_ai_service_empty_json_response():
    """Test handling of empty JSON object response.
    
    Validates: Requirement 10.4 - THE Backend_API SHALL include response_format 
    parameter set to {"type": "json_object"} for all AI_Service requests
    
    This test verifies that empty JSON objects are handled correctly.
    """
    mock_client = Mock()
    mock_response = Mock()
    mock_response.choices = [Mock()]
    mock_response.choices[0].message.content = '{}'
    mock_client.chat.completions.create.return_value = mock_response
    
    result = app.call_ai_service(mock_client, "System", "User")
    
    assert result == {}, "Should handle empty JSON object"
    assert isinstance(result, dict), "Result should be a dictionary"


# ============================================================================
# Integration Tests for AI Service Client
# ============================================================================

def test_create_client_and_call_service_integration():
    """Integration test for creating client and calling service.
    
    Validates: Requirements 10.1, 10.2, 10.3, 10.4
    
    This test verifies the complete flow of creating a client and making a call.
    """
    test_key = 'test_api_key_integration'
    
    with mock.patch.dict(os.environ, {'GROQ_API_KEY': test_key}):
        with mock.patch('app.OpenAI') as mock_openai:
            # Create mock client
            mock_client = Mock()
            mock_response = Mock()
            mock_response.choices = [Mock()]
            mock_response.choices[0].message.content = '{"status": "success"}'
            mock_client.chat.completions.create.return_value = mock_response
            mock_openai.return_value = mock_client
            
            # Create client
            client = app.create_groq_client()
            
            # Verify client was created with correct parameters
            mock_openai.assert_called_once_with(
                api_key=test_key,
                base_url="https://api.groq.com/openai/v1"
            )
            
            # Call service
            result = app.call_ai_service(client, "System prompt", "User prompt")
            
            # Verify call was made with correct parameters
            call_args = mock_client.chat.completions.create.call_args
            assert call_args.kwargs['model'] == "llama-3.1-8b-instant"
            assert call_args.kwargs['response_format'] == {"type": "json_object"}
            
            # Verify result
            assert result == {"status": "success"}


def test_client_reuse():
    """Test that a single client can be reused for multiple calls.
    
    Validates: Requirement 10.1 - THE Backend_API SHALL use the OpenAI-compatible 
    client library to connect to AI_Service
    
    This test verifies that a client instance can be reused efficiently.
    """
    test_key = 'test_api_key'
    
    with mock.patch.dict(os.environ, {'GROQ_API_KEY': test_key}):
        with mock.patch('app.OpenAI') as mock_openai:
            mock_client = Mock()
            mock_response = Mock()
            mock_response.choices = [Mock()]
            mock_response.choices[0].message.content = '{"result": "test"}'
            mock_client.chat.completions.create.return_value = mock_response
            mock_openai.return_value = mock_client
            
            # Create client once
            client = app.create_groq_client()
            
            # Make multiple calls with the same client
            result1 = app.call_ai_service(client, "System 1", "User 1")
            result2 = app.call_ai_service(client, "System 2", "User 2")
            result3 = app.call_ai_service(client, "System 3", "User 3")
            
            # Verify client was created only once
            assert mock_openai.call_count == 1, "Client should be created only once"
            
            # Verify service was called three times
            assert mock_client.chat.completions.create.call_count == 3, \
                "Service should be called three times"
            
            # Verify all results are correct
            assert result1 == {"result": "test"}
            assert result2 == {"result": "test"}
            assert result3 == {"result": "test"}


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
