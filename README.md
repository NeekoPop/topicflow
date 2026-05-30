# TopicFlow - AI Educational Assistant

TopicFlow adalah aplikasi web berbasis AI yang membantu mahasiswa mengubah materi belajar mereka menjadi sumber pembelajaran terstruktur. Aplikasi ini dibangun untuk AI Midterm Exam 2026.

## 🎯 Fitur Utama

- **📋 AI Summarizer**: Menghasilkan ringkasan berbentuk poin-poin dari materi belajar
- **❓ Quiz Generator**: Membuat kuis pilihan ganda interaktif dengan penjelasan
- **🎴 Flashcard Maker**: Mengekstrak istilah kunci dan definisi untuk memorisasi

## 🛠️ Teknologi

- **Backend**: Python 3.12, Flask
- **AI Service**: Groq API (llama-3.1-8b-instant)
- **Frontend**: HTML5, Vanilla JavaScript, Tailwind CSS
- **Environment Management**: python-dotenv

## 📋 Persyaratan

- Python 3.12 atau lebih tinggi
- Groq API Key (gratis di [console.groq.com](https://console.groq.com))
- Browser modern (Chrome, Firefox, Safari, Edge)

## 🚀 Instalasi

### 1. Clone atau Download Repository

```bash
cd topicflow
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Konfigurasi API Key

Buka file `.env` dan ganti placeholder dengan API key Groq Anda:

```env
GROQ_API_KEY=your_actual_groq_api_key_here
```

**Cara mendapatkan Groq API Key:**
1. Kunjungi [console.groq.com](https://console.groq.com)
2. Daftar atau login
3. Buat API key baru
4. Copy dan paste ke file `.env`

### 4. Jalankan Aplikasi

```bash
python app.py
```

Aplikasi akan berjalan di `http://localhost:5000`

## 📖 Cara Menggunakan

1. **Masukkan Materi Belajar**
   - Buka tab "Material Input"
   - Paste atau ketik materi belajar Anda (catatan kuliah, buku teks, dll)

2. **Pilih Fitur**
   - Klik tombol "Generate Summary" untuk ringkasan
   - Klik tombol "Generate Quiz" untuk kuis
   - Klik tombol "Generate Flashcards" untuk flashcard

3. **Interaksi dengan Hasil**
   - **Summary**: Lihat poin-poin penting dari materi
   - **Quiz**: Jawab pertanyaan dan lihat penjelasan
   - **Flashcards**: Klik kartu untuk membalik antara istilah dan definisi

## 📁 Struktur Proyek

```
topicflow/
├── app.py                  # Backend Flask application
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (API key)
├── .gitignore             # Git ignore rules
├── README.md              # Dokumentasi ini
├── templates/
│   └── index.html         # Frontend HTML
├── static/
│   ├── css/
│   │   └── style.css      # Custom CSS styles
│   └── js/
│       └── main.js        # Frontend JavaScript logic
└── tests/
    ├── test_api_key.py    # Unit tests untuk API key
    └── test_ai_service.py # Unit tests untuk AI service
```

## 🧪 Testing

Jalankan unit tests:

```bash
# Install pytest jika belum
pip install pytest

# Jalankan semua tests
pytest

# Jalankan tests dengan verbose output
pytest -v

# Jalankan test spesifik
pytest test_api_key.py
pytest test_ai_service.py
```

## 🔒 Keamanan

- ✅ API key disimpan di file `.env` (tidak di-commit ke git)
- ✅ File `.env` sudah ada di `.gitignore`
- ✅ Tidak ada hardcoded API key di source code
- ✅ Input validation untuk semua endpoint
- ✅ Error handling yang komprehensif

## 🐛 Troubleshooting

### Error: "API key configuration error"
- Pastikan file `.env` ada di root directory
- Pastikan `GROQ_API_KEY` sudah diisi dengan API key yang valid
- Jangan gunakan placeholder `your_groq_api_key_here`

### Error: "AI service unavailable"
- Cek koneksi internet Anda
- Pastikan API key masih valid
- Coba lagi setelah beberapa saat (mungkin rate limit)

### Port 5000 sudah digunakan
Ubah port dengan environment variable:
```bash
PORT=8000 python app.py
```

## 📝 API Endpoints

### POST /api/summarize
Menghasilkan ringkasan dari materi belajar.

**Request:**
```json
{
  "material": "Your study material here..."
}
```

**Response:**
```json
{
  "summary": "• Point 1\n• Point 2\n• Point 3"
}
```

### POST /api/quiz
Menghasilkan kuis pilihan ganda.

**Request:**
```json
{
  "material": "Your study material here..."
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
Menghasilkan flashcards.

**Request:**
```json
{
  "material": "Your study material here..."
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
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "service": "TopicFlow API",
  "version": "1.0.0"
}
```

## 👨‍💻 Developer

**Developers:**
- M Rizki Agil Prakoso
- Imam Agus Faisal

**Project**: AI Midterm Exam 2026

## ✨ Fitur Tambahan

### 🎨 UI/UX Features
- **🌓 Dark Mode** - Mode gelap untuk kenyamanan mata
- **🌐 Multi-Language** - Dukungan Bahasa Inggris & Indonesia  
- **📱 Responsive Design** - Tampilan optimal di desktop, tablet, dan mobile

### 💾 Export & Storage
- **📚 History Panel** - Simpan 10 hasil terakhir di localStorage
- **📋 Copy to Clipboard** - Copy hasil dengan satu klik
- **💾 Export Text** - Download hasil sebagai file .txt
- **📄 Export PDF** - Download hasil sebagai PDF dengan format profesional
- **🖨️ Print** - Print hasil langsung dari browser

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Setup API key di .env
GROQ_API_KEY=your_actual_groq_api_key_here

# 3. Run aplikasi
python app.py

# 4. Buka browser
http://localhost:5000
```

## 📄 License

This project is created for educational purposes as part of AI Midterm Exam 2026.

## 🙏 Acknowledgments

- Groq API untuk layanan AI yang cepat dan powerful
- Tailwind CSS untuk framework CSS yang modern
- Flask untuk web framework Python yang simple dan elegant
