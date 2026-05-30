# Implementation Plan: TopicFlow Educational Assistant

## Overview

This implementation plan breaks down the TopicFlow application into discrete coding tasks. The application will be built using Python (Flask/FastAPI) for the backend and vanilla JavaScript with Tailwind CSS for the frontend. Each task builds incrementally, with early validation through code and testing checkpoints.

## Tasks

- [x] 1. Set up project structure and environment configuration
  - Create directory structure (templates/, static/css/, static/js/)
  - Create .env file with GROQ_API_KEY placeholder
  - Create .gitignore file excluding .env
  - Create requirements.txt with Flask/FastAPI, python-dotenv, openai dependencies
  - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 2.1, 2.2, 11.3, 15.1, 15.2, 15.3, 15.4_

- [ ] 2. Implement backend API foundation
  - [ ] 2.1 Create app.py with Flask/FastAPI application initialization
    - Initialize web framework (Flask or FastAPI)
    - Configure static file serving from static/ directory
    - Configure template rendering from templates/ directory
    - Implement API key loading from .env using python-dotenv
    - Add error handling for missing API key
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 11.1, 11.2, 11.4_
  
  - [x] 2.2 Write unit tests for API key loading and validation
    - Test successful API key loading from .env
    - Test error handling when API key is missing
    - Test error handling when .env file doesn't exist
    - _Requirements: 11.1, 11.4_

- [ ] 3. Implement Groq API client integration
  - [ ] 3.1 Create AI service client wrapper
    - Initialize OpenAI client with Groq base URL (https://api.groq.com/openai/v1)
    - Implement generic AI service call function with model "llama-3.1-8b-instant"
    - Configure response_format parameter as {"type": "json_object"}
    - Add error handling for AI service failures
    - _Requirements: 10.1, 10.2, 10.3, 10.4, 10.5_
  
  - [ ] 3.2 Write unit tests for AI service client
    - Test client initialization with correct base URL
    - Test error handling for AI service failures (mocked)
    - Test JSON response parsing
    - _Requirements: 10.1, 10.2, 10.3, 10.4_

- [ ] 4. Checkpoint - Verify backend foundation
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 5. Implement AI Summarizer backend endpoint
  - [ ] 5.1 Create POST /api/summarize endpoint
    - Accept JSON payload with "material" field
    - Validate material input is non-empty
    - Construct system prompt for summarization
    - Call AI service with summarization prompt
    - Parse JSON response and extract summary field
    - Return JSON response with summary
    - Handle errors (empty input, AI service failure)
    - _Requirements: 6.2, 6.3, 6.4, 6.5, 6.7, 12.1, 12.2, 14.3_
  
  - [ ] 5.2 Write property test for API request structure
    - **Property 3: API Request Structure for Summarizer**
    - **Validates: Requirements 6.2**
    - Test that valid material inputs generate correct POST request structure
  
  - [ ] 5.3 Write property test for JSON response structure
    - **Property 4: Summarizer JSON Response Structure**
    - **Validates: Requirements 6.5**
    - Test that AI service responses (mocked) return valid JSON with "summary" field
  
  - [ ] 5.4 Write unit tests for summarizer endpoint
    - Test successful summarization with valid input
    - Test 400 error for empty material input
    - Test 500 error for AI service failure (mocked)
    - Test JSON response format
    - _Requirements: 6.3, 6.4, 6.5, 6.7, 12.1, 12.2_

- [ ] 6. Implement AI Quiz Generator backend endpoint
  - [ ] 6.1 Create POST /api/quiz endpoint
    - Accept JSON payload with "material" field
    - Validate material input is non-empty
    - Construct system prompt for quiz generation (exactly 5 questions, 4 choices each)
    - Call AI service with quiz generation prompt
    - Parse JSON response and extract questions array
    - Validate response structure (5 questions, each with question, choices, correct_answer, explanation)
    - Return JSON response with questions
    - Handle errors (empty input, AI service failure, invalid response structure)
    - _Requirements: 7.2, 7.3, 7.4, 7.5, 7.8, 12.1, 12.2, 14.3_
  
  - [ ] 6.2 Write property test for API request structure
    - **Property 6: API Request Structure for Quiz Generator**
    - **Validates: Requirements 7.2**
    - Test that valid material inputs generate correct POST request structure
  
  - [ ] 6.3 Write property test for JSON response structure
    - **Property 7: Quiz JSON Response Structure**
    - **Validates: Requirements 7.5**
    - Test that AI service responses (mocked) return valid JSON with "questions" array containing required fields
  
  - [ ] 6.4 Write unit tests for quiz endpoint
    - Test successful quiz generation with valid input
    - Test 400 error for empty material input
    - Test 500 error for AI service failure (mocked)
    - Test JSON response format with 5 questions
    - Test each question has 4 choices
    - _Requirements: 7.3, 7.4, 7.5, 7.8, 12.1, 12.2_

- [ ] 7. Implement AI Flashcard Maker backend endpoint
  - [ ] 7.1 Create POST /api/flashcard endpoint
    - Accept JSON payload with "material" field
    - Validate material input is non-empty
    - Construct system prompt for flashcard generation
    - Call AI service with flashcard generation prompt
    - Parse JSON response and extract flashcards array
    - Validate response structure (array of term-definition pairs)
    - Return JSON response with flashcards
    - Handle errors (empty input, AI service failure, invalid response structure)
    - _Requirements: 8.2, 8.3, 8.4, 8.5, 8.7, 12.1, 12.2, 14.3_
  
  - [ ] 7.2 Write property test for API request structure
    - **Property 9: API Request Structure for Flashcard Maker**
    - **Validates: Requirements 8.2**
    - Test that valid material inputs generate correct POST request structure
  
  - [ ] 7.3 Write property test for JSON response structure
    - **Property 10: Flashcard JSON Response Structure**
    - **Validates: Requirements 8.5**
    - Test that AI service responses (mocked) return valid JSON with "flashcards" array containing term and definition fields
  
  - [ ] 7.4 Write unit tests for flashcard endpoint
    - Test successful flashcard generation with valid input
    - Test 400 error for empty material input
    - Test 500 error for AI service failure (mocked)
    - Test JSON response format with flashcards array
    - _Requirements: 8.3, 8.4, 8.5, 8.7, 12.1, 12.2_

- [ ] 8. Checkpoint - Verify all backend endpoints
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 9. Create frontend HTML structure
  - [ ] 9.1 Create templates/index.html with base structure
    - Add HTML5 doctype and meta tags
    - Include Tailwind CSS CDN link
    - Create tab navigation structure (Material Input, Summarizer, Quiz, Flashcard, About)
    - Create content panels for each tab
    - Add material input textarea
    - Add submit buttons for each feature
    - Add result display containers for each feature
    - Add About section with developer information
    - Add footer with group members' names
    - Link to static/js/main.js
    - _Requirements: 3.1, 3.3, 4.1, 4.2, 4.3, 5.1, 5.2, 6.1, 7.1, 8.1, 9.1, 9.2, 9.3, 9.4, 9.5, 13.1, 13.2_

- [ ] 10. Implement frontend tab navigation
  - [ ] 10.1 Create tab switching logic in static/js/main.js
    - Implement switchTab() function to show/hide content panels
    - Add event listeners to tab buttons
    - Apply active tab styling
    - Ensure only one panel visible at a time
    - _Requirements: 5.2, 5.3, 5.4, 5.5_
  
  - [ ] 10.2 Write property test for tab navigation exclusivity
    - **Property 2: Tab Navigation Exclusivity and State**
    - **Validates: Requirements 5.2, 5.3, 5.4**
    - Test that selecting any tab shows only that panel and hides others

- [ ] 11. Implement input validation and button state management
  - [ ] 11.1 Create input validation logic
    - Implement updateButtonState() function to enable/disable submit buttons
    - Add event listener to material input textarea for input changes
    - Validate input is non-empty and not whitespace-only
    - Disable buttons when input is invalid
    - Enable buttons when input is valid
    - _Requirements: 4.4, 14.2_
  
  - [ ] 11.2 Write property test for input validation
    - **Property 1: Input Validation Controls Button State**
    - **Validates: Requirements 4.4**
    - Test that button state correctly reflects input validity for any input

- [ ] 12. Implement AI Summarizer frontend
  - [ ] 12.1 Create summarizer API call and result rendering
    - Implement submitSummarizer() function to call /api/summarize
    - Show loading indicator during API call
    - Parse JSON response and extract summary
    - Render summary in bulleted format
    - Display error messages on failure
    - Hide loading indicator on completion
    - _Requirements: 6.1, 6.2, 6.6, 12.3, 12.4, 14.1, 14.4, 14.5_
  
  - [ ] 12.2 Write property test for summary display formatting
    - **Property 5: Summary Display Formatting**
    - **Validates: Requirements 6.6**
    - Test that any summary text is rendered in bulleted format
  
  - [ ] 12.3 Write unit tests for summarizer frontend
    - Test API call with valid input
    - Test loading indicator display
    - Test error message display on network failure
    - Test summary rendering
    - _Requirements: 6.1, 6.2, 6.6, 14.1, 14.4, 14.5_

- [ ] 13. Implement AI Quiz Generator frontend
  - [ ] 13.1 Create quiz API call and result rendering
    - Implement submitQuiz() function to call /api/quiz
    - Show loading indicator during API call
    - Parse JSON response and extract questions array
    - Render all 5 questions with selectable answer choices
    - Implement answer selection logic
    - Reveal correct answer with highlighting on selection
    - Display explanation after answer selection
    - Display error messages on failure
    - Hide loading indicator on completion
    - _Requirements: 7.1, 7.2, 7.6, 7.7, 12.3, 12.4, 14.1, 14.4, 14.5_
  
  - [ ] 13.2 Write property test for quiz display and interaction
    - **Property 8: Quiz Display and Interaction**
    - **Validates: Requirements 7.6, 7.7**
    - Test that any quiz response data renders correctly with interactive answer selection
  
  - [ ] 13.3 Write unit tests for quiz frontend
    - Test API call with valid input
    - Test loading indicator display
    - Test error message display on network failure
    - Test quiz rendering with 5 questions
    - Test answer selection and highlighting
    - Test explanation display
    - _Requirements: 7.1, 7.2, 7.6, 7.7, 14.1, 14.4, 14.5_

- [ ] 14. Implement AI Flashcard Maker frontend
  - [ ] 14.1 Create flashcard API call and result rendering
    - Implement submitFlashcard() function to call /api/flashcard
    - Show loading indicator during API call
    - Parse JSON response and extract flashcards array
    - Render flashcards with flip interaction
    - Implement flip animation between term and definition
    - Display error messages on failure
    - Hide loading indicator on completion
    - _Requirements: 8.1, 8.2, 8.6, 12.3, 12.4, 14.1, 14.4, 14.5_
  
  - [ ] 14.2 Write property test for flashcard flip interaction
    - **Property 11: Flashcard Flip Interaction**
    - **Validates: Requirements 8.6**
    - Test that clicking any flashcard toggles between term and definition
  
  - [ ] 14.3 Write unit tests for flashcard frontend
    - Test API call with valid input
    - Test loading indicator display
    - Test error message display on network failure
    - Test flashcard rendering
    - Test flip interaction
    - _Requirements: 8.1, 8.2, 8.6, 14.1, 14.4, 14.5_

- [ ] 15. Implement responsive design with Tailwind CSS
  - [ ] 15.1 Add Tailwind CSS utility classes for responsive layout
    - Apply responsive classes to tab navigation
    - Apply responsive classes to material input textarea
    - Apply responsive classes to result containers
    - Test layout on mobile (320px), tablet (768px), and desktop (1920px) widths
    - Ensure all interactive elements remain accessible on mobile
    - _Requirements: 3.3, 13.1, 13.2, 13.3, 13.4_

- [ ] 16. Implement comprehensive error handling
  - [ ] 16.1 Add frontend error handling utilities
    - Create showError() function to display error messages
    - Create hideError() function to clear error messages
    - Add error handling for network failures
    - Add error handling for JSON parsing errors
    - Add error handling for empty API responses
    - _Requirements: 14.1, 14.2, 14.3, 12.4_
  
  - [ ] 16.2 Write property test for error display
    - **Property 15: Error Display on API Failure**
    - **Validates: Requirements 14.1**
    - Test that any API error response displays an error message
  
  - [ ] 16.3 Write property test for loading indicator lifecycle
    - **Property 16: Loading Indicator Lifecycle**
    - **Validates: Requirements 14.4, 14.5**
    - Test that loading indicator is shown on request start and hidden on completion

- [ ] 17. Integration testing and end-to-end validation
  - [ ] 17.1 Write integration tests for complete user flows
    - Test complete summarizer flow (input → submit → display)
    - Test complete quiz flow (input → submit → display → interaction)
    - Test complete flashcard flow (input → submit → display → flip)
    - Test error flows for each feature
    - _Requirements: 6.1, 6.2, 6.6, 7.1, 7.2, 7.6, 7.7, 8.1, 8.2, 8.6_
  
  - [ ] 17.2 Write property test for AI service configuration consistency
    - **Property 12: AI Service Configuration Consistency**
    - **Validates: Requirements 10.3, 10.4**
    - Test that all AI service calls use correct model and response format
  
  - [ ] 17.3 Write property test for JSON response headers
    - **Property 13: JSON Response Content-Type Header**
    - **Validates: Requirements 12.1**
    - Test that all successful API responses include correct Content-Type header
  
  - [ ] 17.4 Write property test for JSON serialization round-trip
    - **Property 14: JSON Serialization Round-Trip**
    - **Validates: Requirements 12.2**
    - Test that any response data structure preserves all fields through JSON serialization
  
  - [ ] 17.5 Write property test for AI service error handling
    - **Property 17: AI Service Error Handling**
    - **Validates: Requirements 6.7, 7.8, 8.7**
    - Test that all endpoints return 500 status with error message when AI service fails

- [ ] 18. Final checkpoint and documentation
  - Ensure all tests pass, ask the user if questions arise.
  - Verify .env file is excluded from git
  - Verify no hardcoded API keys in source code
  - Verify requirements.txt is complete and accurate

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Property tests validate universal correctness properties from the design document
- Unit tests validate specific examples and edge cases
- Integration tests validate complete user flows
- All AI service interactions should be mocked in tests to ensure deterministic results
- The backend can use either Flask or FastAPI - choose based on preference
- Checkpoints ensure incremental validation and provide opportunities for user feedback

## Task Dependency Graph

```json
{
  "waves": [
    { "id": 0, "tasks": ["1"] },
    { "id": 1, "tasks": ["2.1", "2.2"] },
    { "id": 2, "tasks": ["3.1", "3.2"] },
    { "id": 3, "tasks": ["5.1", "6.1", "7.1"] },
    { "id": 4, "tasks": ["5.2", "5.3", "5.4", "6.2", "6.3", "6.4", "7.2", "7.3", "7.4"] },
    { "id": 5, "tasks": ["9.1"] },
    { "id": 6, "tasks": ["10.1", "10.2"] },
    { "id": 7, "tasks": ["11.1", "11.2"] },
    { "id": 8, "tasks": ["12.1", "13.1", "14.1"] },
    { "id": 9, "tasks": ["12.2", "12.3", "13.2", "13.3", "14.2", "14.3"] },
    { "id": 10, "tasks": ["15.1"] },
    { "id": 11, "tasks": ["16.1", "16.2", "16.3"] },
    { "id": 12, "tasks": ["17.1", "17.2", "17.3", "17.4", "17.5"] }
  ]
}
```
