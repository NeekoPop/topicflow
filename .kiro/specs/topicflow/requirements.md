# Requirements Document

## Introduction

TopicFlow is an AI-powered educational assistant web application designed for the AI Midterm Exam 2026. The system enables students to transform study materials into structured learning resources through AI-generated summaries, quizzes, and flashcards. The application uses a responsive web interface with a Python backend (Flask/FastAPI) and vanilla JavaScript frontend with Tailwind CSS.

## Glossary

- **TopicFlow_System**: The complete web application including backend API and frontend interface
- **Backend_API**: The Python-based REST API server (Flask or FastAPI) that processes requests
- **Frontend_UI**: The HTML/JavaScript/Tailwind CSS user interface
- **Material_Input**: Text content provided by students (study text or lecture notes)
- **AI_Service**: The Groq API integration using OpenAI-compatible client library
- **Summarizer**: The component that generates bulleted summaries from Material_Input
- **Quiz_Generator**: The component that creates multiple-choice questions from Material_Input
- **Flashcard_Maker**: The component that extracts key terms and definitions from Material_Input
- **API_Key**: The GROQ_API_KEY credential stored in the .env file
- **JSON_Response**: Structured data returned by the AI_Service in JSON format
- **Tab_Navigation**: The UI component allowing users to switch between features
- **Student**: The end user of the TopicFlow_System

## Requirements

### Requirement 1: Project Structure and File Organization

**User Story:** As a developer, I want a well-organized project structure, so that the codebase is maintainable and follows best practices.

#### Acceptance Criteria

1. THE TopicFlow_System SHALL contain an app.py file with Backend_API routes
2. THE TopicFlow_System SHALL contain a templates/index.html file with Frontend_UI markup
3. THE TopicFlow_System SHALL contain a static/css/style.css file for Tailwind CSS configurations
4. THE TopicFlow_System SHALL contain a static/js/main.js file for frontend JavaScript logic
5. THE TopicFlow_System SHALL contain a .env file for API_Key storage
6. THE TopicFlow_System SHALL contain a .gitignore file that excludes the .env file
7. THE TopicFlow_System SHALL contain a requirements.txt file listing Python dependencies

### Requirement 2: Backend Technology Stack

**User Story:** As a developer, I want to use Python 3.12 with Flask or FastAPI, so that the backend is modern and performant.

#### Acceptance Criteria

1. THE Backend_API SHALL be implemented using Python version 3.12
2. THE Backend_API SHALL use either Flask or FastAPI framework
3. THE Backend_API SHALL serve the Frontend_UI from the templates directory
4. THE Backend_API SHALL serve static assets from the static directory

### Requirement 3: Frontend Technology Stack

**User Story:** As a developer, I want to use vanilla HTML, JavaScript, and Tailwind CSS, so that the frontend is lightweight and responsive.

#### Acceptance Criteria

1. THE Frontend_UI SHALL be implemented using vanilla HTML without frameworks
2. THE Frontend_UI SHALL use vanilla JavaScript with Fetch API for HTTP requests
3. THE Frontend_UI SHALL use Tailwind CSS for styling and responsive design
4. THE Frontend_UI SHALL NOT use jQuery, React, Vue, or other JavaScript frameworks

### Requirement 4: Material Input Interface

**User Story:** As a student, I want to input my study materials, so that I can generate learning resources from them.

#### Acceptance Criteria

1. THE Frontend_UI SHALL provide a textarea element for Material_Input
2. THE Material_Input textarea SHALL accept multi-line text content
3. THE Material_Input textarea SHALL be accessible across all Tab_Navigation views
4. WHEN Material_Input is empty, THE Frontend_UI SHALL disable submission buttons

### Requirement 5: Tab Navigation System

**User Story:** As a student, I want to navigate between different AI features, so that I can choose the learning resource I need.

#### Acceptance Criteria

1. THE Frontend_UI SHALL provide Tab_Navigation with five tabs: Material Input Area, AI Summarizer, AI Quiz Generator, AI Flashcard Maker, and About
2. WHEN a Student clicks a tab, THE Frontend_UI SHALL display the corresponding content panel
3. WHEN a Student clicks a tab, THE Frontend_UI SHALL hide all other content panels
4. THE Frontend_UI SHALL indicate the currently active tab visually
5. THE Tab_Navigation SHALL be responsive on mobile and desktop devices

### Requirement 6: AI Summarizer Feature

**User Story:** As a student, I want to generate a summary of my study materials, so that I can quickly review key points.

#### Acceptance Criteria

1. THE Frontend_UI SHALL provide a submit button in the AI Summarizer tab
2. WHEN the submit button is clicked, THE Frontend_UI SHALL send a POST request to /api/summarize with Material_Input
3. THE Backend_API SHALL expose a POST /api/summarize endpoint
4. WHEN /api/summarize receives Material_Input, THE Summarizer SHALL generate a bulleted summary using AI_Service
5. THE Summarizer SHALL return JSON_Response containing the summary text
6. THE Frontend_UI SHALL display the summary in bulleted format
7. WHEN the AI_Service request fails, THE Backend_API SHALL return an error message with HTTP status code 500

### Requirement 7: AI Quiz Generator Feature

**User Story:** As a student, I want to generate quiz questions from my study materials, so that I can test my knowledge.

#### Acceptance Criteria

1. THE Frontend_UI SHALL provide a submit button in the AI Quiz Generator tab
2. WHEN the submit button is clicked, THE Frontend_UI SHALL send a POST request to /api/quiz with Material_Input
3. THE Backend_API SHALL expose a POST /api/quiz endpoint
4. WHEN /api/quiz receives Material_Input, THE Quiz_Generator SHALL generate exactly 5 multiple-choice questions using AI_Service
5. THE Quiz_Generator SHALL return JSON_Response containing an array of questions, where each question includes question text, answer choices, correct answer, and explanation
6. THE Frontend_UI SHALL display each question with selectable answer choices
7. THE Frontend_UI SHALL reveal the correct answer and explanation after a Student selects an answer
8. WHEN the AI_Service request fails, THE Backend_API SHALL return an error message with HTTP status code 500

### Requirement 8: AI Flashcard Maker Feature

**User Story:** As a student, I want to generate flashcards from my study materials, so that I can memorize key concepts.

#### Acceptance Criteria

1. THE Frontend_UI SHALL provide a submit button in the AI Flashcard Maker tab
2. WHEN the submit button is clicked, THE Frontend_UI SHALL send a POST request to /api/flashcard with Material_Input
3. THE Backend_API SHALL expose a POST /api/flashcard endpoint
4. WHEN /api/flashcard receives Material_Input, THE Flashcard_Maker SHALL extract core terms and definitions using AI_Service
5. THE Flashcard_Maker SHALL return JSON_Response containing an array of flashcards, where each flashcard includes a term and definition
6. THE Frontend_UI SHALL display flashcards in an interactive format allowing Students to flip between term and definition
7. WHEN the AI_Service request fails, THE Backend_API SHALL return an error message with HTTP status code 500

### Requirement 9: About Section

**User Story:** As a student, I want to learn about TopicFlow and its developers, so that I understand the application's purpose and creators.

#### Acceptance Criteria

1. THE Frontend_UI SHALL provide an About tab
2. THE About tab SHALL display a description of TopicFlow as an AI-powered educational assistant built for AI Midterm Exam 2026
3. THE About tab SHALL display the names of both developers
4. THE About tab SHALL display the Student IDs (NIM) of both developers
5. THE Frontend_UI footer SHALL display both group members' names

### Requirement 10: Groq API Integration

**User Story:** As a developer, I want to integrate the Groq API, so that the application can generate AI-powered content.

#### Acceptance Criteria

1. THE Backend_API SHALL use the OpenAI-compatible client library to connect to AI_Service
2. THE Backend_API SHALL configure the client with base_url set to "https://api.groq.com/openai/v1"
3. THE Backend_API SHALL use the model "llama-3.1-8b-instant" for all AI_Service requests
4. THE Backend_API SHALL include response_format parameter set to {"type": "json_object"} for all AI_Service requests
5. THE Backend_API SHALL send appropriate system and user prompts to AI_Service for each feature

### Requirement 11: API Key Security

**User Story:** As a developer, I want to securely manage API credentials, so that sensitive information is not exposed.

#### Acceptance Criteria

1. THE Backend_API SHALL load API_Key from the .env file using python-dotenv library
2. THE Backend_API SHALL NOT contain hardcoded API_Key values in source code
3. THE .gitignore file SHALL include .env to prevent API_Key from being committed to version control
4. WHEN API_Key is missing or invalid, THE Backend_API SHALL return an error message with HTTP status code 500

### Requirement 12: JSON Response Format

**User Story:** As a frontend developer, I want all API responses in JSON format, so that I can easily parse and display the data.

#### Acceptance Criteria

1. THE Backend_API SHALL return all successful responses with Content-Type header set to "application/json"
2. THE Backend_API SHALL structure all AI_Service responses as valid JSON objects
3. THE Frontend_UI SHALL parse JSON_Response using JavaScript JSON.parse() method
4. WHEN JSON_Response is malformed, THE Frontend_UI SHALL display an error message to the Student

### Requirement 13: Responsive Design

**User Story:** As a student, I want to use TopicFlow on any device, so that I can study on mobile, tablet, or desktop.

#### Acceptance Criteria

1. THE Frontend_UI SHALL be responsive on screen widths from 320px to 1920px
2. THE Frontend_UI SHALL use Tailwind CSS responsive utility classes for layout adaptation
3. WHEN viewed on mobile devices, THE Tab_Navigation SHALL remain usable and accessible
4. WHEN viewed on mobile devices, THE Material_Input textarea SHALL be appropriately sized

### Requirement 14: Error Handling and User Feedback

**User Story:** As a student, I want clear feedback when errors occur, so that I understand what went wrong.

#### Acceptance Criteria

1. WHEN a Backend_API request fails, THE Frontend_UI SHALL display an error message to the Student
2. WHEN Material_Input is empty, THE Frontend_UI SHALL display a validation message
3. WHEN AI_Service is unavailable, THE Backend_API SHALL return a descriptive error message
4. THE Frontend_UI SHALL provide loading indicators during API requests
5. WHEN an API request completes, THE Frontend_UI SHALL hide loading indicators

### Requirement 15: Python Dependencies Management

**User Story:** As a developer, I want to manage Python dependencies, so that the application can be easily installed and deployed.

#### Acceptance Criteria

1. THE requirements.txt file SHALL list Flask or FastAPI as the web framework
2. THE requirements.txt file SHALL list python-dotenv for environment variable management
3. THE requirements.txt file SHALL list openai library for AI_Service integration
4. THE requirements.txt file SHALL specify compatible version constraints for all dependencies
