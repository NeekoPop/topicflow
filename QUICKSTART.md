# 🚀 TopicFlow - Quick Start Guide

Panduan cepat untuk menjalankan TopicFlow dalam 5 menit!

## ⚡ Langkah Cepat

### 1. Setup API Key (2 menit)

1. Buka [console.groq.com](https://console.groq.com)
2. Login atau daftar (gratis!)
3. Buat API key baru
4. Copy API key tersebut
5. Buka file `Backend/.env`
6. Ganti `your_groq_api_key_here` dengan API key Anda

**File `Backend/.env` seharusnya terlihat seperti ini:**
```env
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 2. Install Dependencies (1 menit)

```bash
cd Backend
pip install -r requirements.txt
```

### 3. Jalankan Aplikasi (1 menit)

**Windows:**
```bash
# Dari root directory
run.bat
```

**Linux/Mac:**
```bash
cd Backend
python app.py
```

Anda akan melihat output seperti ini:
```
Starting TopicFlow API on port 5000
Environment: Development
Static files: ../Frontend/static
Templates: ../Frontend/templates
✓ API Key loaded successfully (length: 56)
 * Running on http://0.0.0.0:5000
```

### 4. Buka Browser (1 menit)

Buka browser dan kunjungi:
```
http://localhost:5000
```

## 🎉 Selesai!

Sekarang Anda bisa:
1. Masukkan materi belajar di tab "Material Input"
2. Klik "Generate Summary" untuk ringkasan
3. Klik "Generate Quiz" untuk kuis interaktif
4. Klik "Generate Flashcards" untuk flashcard

## 📁 Struktur Project

```
topicflow/
├── Backend/              ← Jalankan server dari sini
│   ├── app.py           ← Main application
│   ├── .env             ← API key Anda di sini
│   └── requirements.txt
└── Frontend/            ← UI files (auto-served)
    ├── static/
    └── templates/
```

## 🔍 Verifikasi Instalasi

Cek apakah API key sudah benar:
```bash
curl http://localhost:5000/health
```

Seharusnya mengembalikan:
```json
{
  "status": "healthy",
  "service": "TopicFlow API",
  "api_key": "valid",
  "static_files": "serving from ../Frontend/static/",
  "templates": "serving from ../Frontend/templates/"
}
```

## ❓ Masalah?

### API Key tidak terdeteksi
- Pastikan file `Backend/.env` ada
- Pastikan tidak ada spasi sebelum atau sesudah API key
- Restart aplikasi setelah mengubah `.env`

### Port 5000 sudah digunakan
```bash
cd Backend
PORT=8000 python app.py
```
Lalu buka `http://localhost:8000`

### Module tidak ditemukan
```bash
cd Backend
pip install -r requirements.txt --upgrade
```

### Frontend tidak loading
- Pastikan folder `Frontend/` ada di root directory
- Pastikan Anda menjalankan `app.py` dari folder `Backend/`
- Cek path di `app.py`: `static_folder='../Frontend/static'`

## 📚 Contoh Penggunaan

### Contoh Materi Input:
```
Photosynthesis is the process by which plants convert light energy 
into chemical energy. It occurs in the chloroplasts and involves 
two main stages: light-dependent reactions and the Calvin cycle. 
The overall equation is: 6CO2 + 6H2O + light → C6H12O6 + 6O2.
Light-dependent reactions occur in the thylakoid membranes and 
produce ATP and NADPH. The Calvin cycle occurs in the stroma and 
uses these products to fix carbon dioxide into glucose.
```

### Hasil yang Diharapkan:
- **Summary**: 5-10 poin penting tentang fotosintesis
- **Quiz**: 5 pertanyaan pilihan ganda dengan penjelasan
- **Flashcards**: Istilah seperti "Chloroplast", "Calvin Cycle", "Thylakoid", dll

## 🎯 Tips

1. **Materi yang lebih panjang = hasil yang lebih baik**
   - Minimal 100 kata untuk hasil optimal
   - Maksimal ~2000 kata (batasan API)

2. **Gunakan materi yang terstruktur**
   - Paragraf yang jelas
   - Poin-poin yang terorganisir
   - Definisi yang eksplisit

3. **Coba berbagai fitur**
   - Summary untuk review cepat
   - Quiz untuk self-assessment
   - Flashcards untuk memorisasi

4. **Upload PDF**
   - Klik "Choose File" di Material Input
   - Pilih PDF (max 16MB)
   - Klik Generate

## 🎨 Fitur Tambahan

- **🌓 Dark Mode**: Toggle di header (bulan/matahari icon)
- **🌐 Multi-Language**: Switch ID/EN di header
- **📚 History**: Lihat 10 hasil terakhir
- **💾 Export**: Copy, Text, PDF, Print

## 📞 Support

Jika ada masalah, cek:
1. [README.md](README.md) untuk dokumentasi lengkap
2. [TROUBLESHOOTING.md](TROUBLESHOOTING.md) untuk solusi masalah
3. [Backend/README.md](Backend/README.md) untuk dokumentasi backend
4. [Frontend/README.md](Frontend/README.md) untuk dokumentasi frontend
5. [ARCHITECTURE.md](ARCHITECTURE.md) untuk memahami struktur sistem

## 📖 Next Steps

- Baca [USAGE_GUIDE.md](USAGE_GUIDE.md) untuk panduan lengkap
- Cek [DEPLOYMENT.md](DEPLOYMENT.md) untuk deploy ke production
- Review [ARCHITECTURE.md](ARCHITECTURE.md) untuk memahami arsitektur

---

**Developers**: M Rizki Agil Prakoso & Imam Agus Faisal  
**Project**: AI Midterm Exam 2026

**Selamat belajar dengan TopicFlow! 📚✨**
