# 📖 TopicFlow - Panduan Penggunaan

## ✅ Aplikasi Sudah Berjalan!

Jika Anda melihat file ini, berarti aplikasi TopicFlow sudah berhasil dijalankan! 🎉

## 🌐 Akses Aplikasi

Buka browser dan ketik:
```
http://localhost:5000
```

## 🎯 Cara Menggunakan

### 1️⃣ Masukkan Materi Belajar

Di tab **"Material Input"**:
- Paste atau ketik materi belajar Anda
- Bisa berupa: catatan kuliah, bab buku, artikel, dll
- Minimal 50 kata untuk hasil optimal
- Maksimal ~2000 kata

**Contoh Materi:**
```
Photosynthesis is the process by which plants convert light energy 
into chemical energy. It occurs in the chloroplasts and involves 
two main stages: light-dependent reactions and the Calvin cycle. 
The overall equation is: 6CO2 + 6H2O + light → C6H12O6 + 6O2.

During the light-dependent reactions, chlorophyll absorbs light 
energy, which is used to split water molecules and produce ATP 
and NADPH. These energy carriers are then used in the Calvin cycle 
to fix carbon dioxide and produce glucose.
```

### 2️⃣ Generate Summary (Ringkasan)

1. Klik tombol **"Generate Summary"** 📋
2. Tunggu 3-5 detik
3. Lihat ringkasan dalam bentuk bullet points
4. Ringkasan akan muncul di tab "Summarizer"

**Hasil yang Diharapkan:**
- Poin-poin penting dari materi
- Format bullet points yang rapi
- Ringkasan yang concise dan jelas

### 3️⃣ Generate Quiz (Kuis)

1. Klik tombol **"Generate Quiz"** ❓
2. Tunggu 5-10 detik
3. Akan muncul 5 pertanyaan pilihan ganda
4. Klik jawaban yang menurut Anda benar
5. Lihat feedback (hijau = benar, merah = salah)
6. Baca penjelasan untuk setiap jawaban

**Fitur Quiz:**
- 5 pertanyaan per quiz
- 4 pilihan jawaban per pertanyaan
- Highlight jawaban benar/salah
- Penjelasan detail untuk setiap jawaban
- Score tracker

### 4️⃣ Generate Flashcards (Kartu Belajar)

1. Klik tombol **"Generate Flashcards"** 🎴
2. Tunggu 5-10 detik
3. Akan muncul beberapa flashcards (5-15 kartu)
4. **Klik kartu** untuk flip antara term dan definition
5. Gunakan untuk memorisasi

**Fitur Flashcards:**
- Animasi flip 3D yang smooth
- Gradient background yang menarik
- Grid layout responsif
- Cocok untuk memorisasi istilah

## 🔄 Tips Penggunaan

### ✨ Untuk Hasil Terbaik:

1. **Materi yang Jelas**
   - Gunakan materi yang terstruktur
   - Hindari materi yang terlalu pendek (<50 kata)
   - Pastikan ada definisi dan konsep yang jelas

2. **Panjang Materi Optimal**
   - Summary: 200-1000 kata
   - Quiz: 300-1500 kata
   - Flashcards: 200-1000 kata

3. **Jenis Materi yang Cocok**
   - ✅ Catatan kuliah
   - ✅ Bab dari buku teks
   - ✅ Artikel ilmiah
   - ✅ Study guide
   - ✅ Lecture transcript
   - ❌ Tabel data mentah
   - ❌ Kode program panjang
   - ❌ Daftar tanpa konteks

### 🎨 Navigasi Antar Tab

- Klik tab di bagian atas untuk berpindah
- Tab aktif akan berwarna biru
- Semua fitur bisa diakses dari tab manapun

### 🔄 Generate Ulang

- Anda bisa generate ulang kapan saja
- Hasil akan berbeda setiap kali (AI generative)
- Coba beberapa kali untuk hasil terbaik

## ⚠️ Troubleshooting

### Error: "Failed to generate summary"

**Penyebab:**
- Materi terlalu pendek
- Koneksi internet bermasalah
- API rate limit

**Solusi:**
1. Coba lagi setelah beberapa detik
2. Pastikan materi minimal 50 kata
3. Cek koneksi internet

### Error: "summaryText.split is not a function"

**Sudah diperbaiki!** Refresh halaman (F5) jika masih muncul.

### Quiz/Flashcard Tidak Muncul

**Solusi:**
1. Pastikan materi sudah diinput
2. Tunggu hingga loading selesai
3. Cek browser console (F12) untuk error
4. Refresh halaman dan coba lagi

### Aplikasi Lambat

**Tips:**
- Gunakan materi yang tidak terlalu panjang
- Tunggu hingga satu request selesai sebelum request lain
- Groq API gratis memiliki rate limit

## 🛑 Menghentikan Aplikasi

Jika ingin stop aplikasi:
1. Kembali ke terminal/command prompt
2. Tekan **Ctrl + C**
3. Ketik **Y** jika diminta konfirmasi

## 🔄 Menjalankan Ulang

Untuk menjalankan aplikasi lagi:
```cmd
python app.py
```

Atau gunakan:
```cmd
run.bat
```

## 📊 Contoh Use Case

### Use Case 1: Persiapan Ujian
1. Input: Catatan kuliah 1 bab
2. Generate Summary → Baca untuk review cepat
3. Generate Quiz → Test pemahaman
4. Generate Flashcards → Hafal istilah penting

### Use Case 2: Belajar Topik Baru
1. Input: Artikel atau bab buku
2. Generate Summary → Pahami konsep utama
3. Generate Flashcards → Hafal definisi
4. Generate Quiz → Validasi pemahaman

### Use Case 3: Review Sebelum Presentasi
1. Input: Materi presentasi
2. Generate Summary → Poin-poin penting
3. Generate Quiz → Antisipasi pertanyaan
4. Generate Flashcards → Hafal key terms

## 🎓 Fitur Tambahan

### Tab About
- Informasi tentang aplikasi
- Cara penggunaan
- Developer information
- Technology stack

### Responsive Design
- Bisa diakses dari HP, tablet, atau laptop
- Layout otomatis menyesuaikan ukuran layar
- Touch-friendly untuk mobile

### Dark Mode
- Saat ini belum tersedia
- Akan ditambahkan di versi mendatang

## 📞 Bantuan

Jika ada masalah:
1. Cek file `FIX_ERROR.md` untuk troubleshooting
2. Cek file `README.md` untuk dokumentasi lengkap
3. Lihat browser console (F12) untuk error details
4. Cek terminal untuk backend error logs

---

**Developers**: M Rizki Agil Prakoso & Imam Agus Faisal  
**Project**: AI Midterm Exam 2026  
**Technology**: Python Flask + Groq API + Tailwind CSS

## 🎨 Fitur Tambahan Terbaru

### ✨ Dark Mode 🌓
- Toggle di header (kanan atas)
- Klik 🌙 untuk dark mode
- Klik ☀️ untuk light mode
- Preferensi tersimpan otomatis

### 🌐 Multi-Language
- Toggle di header (kiri atas)
- Klik 🌐 EN/ID untuk ganti bahasa
- Dukungan Bahasa Inggris & Indonesia
- UI otomatis berubah

### 📚 History Panel
- Klik tombol 📚 History di header
- Lihat 10 hasil terakhir
- View detail atau delete item
- Clear all untuk hapus semua

### 💾 Export Options (Summary)
- **📋 Copy** - Copy ke clipboard
- **💾 Export Text** - Download .txt file
- **📄 Export PDF** - Download PDF profesional
- **🖨️ Print** - Print langsung

### 📱 Responsive Design
- Optimal di desktop, tablet, mobile
- Touch-friendly untuk HP
- Layout otomatis menyesuaikan

🎉 **Selamat Belajar dengan TopicFlow!** 🎉
