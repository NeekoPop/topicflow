# 🚀 TopicFlow - Quick Start Guide

Panduan cepat untuk menjalankan TopicFlow dalam 5 menit!

## ⚡ Langkah Cepat

### 1. Install Dependencies (1 menit)

```bash
pip install -r requirements.txt
```

### 2. Setup API Key (2 menit)

1. Buka [console.groq.com](https://console.groq.com)
2. Login atau daftar (gratis!)
3. Buat API key baru
4. Copy API key tersebut
5. Buka file `.env` di folder topicflow
6. Ganti `your_groq_api_key_here` dengan API key Anda

**File `.env` seharusnya terlihat seperti ini:**
```env
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 3. Jalankan Aplikasi (1 menit)

```bash
python app.py
```

Anda akan melihat output seperti ini:
```
Starting TopicFlow API on port 5000
Static files: static
Templates: templates
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
  "api_key": "valid"
}
```

## ❓ Masalah?

### API Key tidak terdeteksi
- Pastikan file `.env` ada di folder yang sama dengan `app.py`
- Pastikan tidak ada spasi sebelum atau sesudah API key
- Restart aplikasi setelah mengubah `.env`

### Port 5000 sudah digunakan
```bash
PORT=8000 python app.py
```
Lalu buka `http://localhost:8000`

### Module tidak ditemukan
```bash
pip install -r requirements.txt --upgrade
```

## 📚 Contoh Penggunaan

### Contoh Materi Input:
```
Photosynthesis is the process by which plants convert light energy 
into chemical energy. It occurs in the chloroplasts and involves 
two main stages: light-dependent reactions and the Calvin cycle. 
The overall equation is: 6CO2 + 6H2O + light → C6H12O6 + 6O2
```

### Hasil yang Diharapkan:
- **Summary**: Poin-poin penting tentang fotosintesis
- **Quiz**: 5 pertanyaan pilihan ganda tentang fotosintesis
- **Flashcards**: Istilah seperti "Chloroplast", "Calvin Cycle", dll

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

## 📞 Support

Jika ada masalah, cek:
1. README.md untuk dokumentasi lengkap
2. File log di terminal untuk error messages
3. Browser console (F12) untuk error frontend

---

**Developer**: M Rizki Agil Prakoso (NIM: 25.01.53.0015)  
**Project**: AI Midterm Exam 2026
