# TopicFlow Backend

Backend API untuk aplikasi TopicFlow - AI Educational Assistant.

## 📁 Struktur Backend

```
Backend/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (API key)
├── test_ai_service.py     # Unit tests untuk AI service
├── test_api_key.py        # Unit tests untuk API key
├── test_groq_connection.py # Connection tests
└── test_summarize_endpoint.py # Endpoint tests
```

## 🚀 Cara Menjalankan Backend

### 1. Install Dependencies

```bash
cd Backend
pip install -r requirements.txt
```

### 2. Setup Environment Variables

Edit file `.env` dan masukkan Groq API key Anda:

```env
GROQ_API_KEY=your_actual_groq_api_key_here
SECRET_KEY=your_secret_key_here
```

### 3. Jalankan Server

```bash
python app.py
```

Server akan berjalan di `http://localhost:5000`

## 📡 API Endpoints

### POST /api/summarize
Generate summary dari study material

**Request:**
```json
{
  "material": "Your study material text..."
}
```

**Response:**
```json
{
  "summary": "• Point 1\n• Point 2\n• Point 3"
}
```

### POST /api/quiz
Generate quiz questions

**Request:**
```json
{
  "material": "Your study material text..."
}
```

**Response:**
```json
{
  "questions": [
    {
      "question": "Question text?",
      "choices": ["A", "B", "C", "D"],
      "correct_answer": "A",
      "explanation": "Explanation text"
    }
  ]
}
```

### POST /api/flashcard
Generate flashcards

**Request:**
```json
{
  "material": "Your study material text..."
}
```

**Response:**
```json
{
  "flashcards": [
    {
      "term": "Key term",
      "definition": "Definition text"
    }
  ]
}
```

### GET /health
Health check endpoint

### GET /api/config
Configuration check endpoint (for debugging)

## 🧪 Testing

```bash
# Install pytest
pip install pytest

# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest test_api_key.py
```

## 🛠️ Teknologi

- **Python 3.12+**
- **Flask 3.0.0** - Web framework
- **OpenAI SDK** - Untuk Groq API integration
- **python-dotenv** - Environment variable management
- **PyPDF2** - PDF file processing
- **gunicorn** - Production server

## 🔒 Security

- API key stored in `.env` file
- Input validation on all endpoints
- Error handling and logging
- CORS support for cross-origin requests
- File upload size limits (16MB max)

## 📝 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GROQ_API_KEY` | Groq API key untuk AI service | Yes |
| `SECRET_KEY` | Flask secret key untuk sessions | No (default provided) |
| `PORT` | Port untuk menjalankan server | No (default: 5000) |

## 🐛 Troubleshooting

### API Key Error
Pastikan `.env` file ada dan `GROQ_API_KEY` sudah diisi dengan benar.

### Port Already in Use
Ubah port dengan environment variable:
```bash
PORT=8000 python app.py
```

### Module Import Error
Pastikan semua dependencies sudah terinstall:
```bash
pip install -r requirements.txt
```
