# 🔧 Fix: "unexpected keyword argument 'proxies'" Error

## Masalah
Error: `Client.__init__() got an unexpected keyword argument 'proxies'`

Ini terjadi karena ada konflik dengan proxy settings atau versi library OpenAI yang tidak kompatibel.

## Solusi Cepat (3 Langkah)

### 1. Hentikan Flask Server yang Sedang Berjalan

**Windows:**
```cmd
# Tekan Ctrl+C di terminal yang menjalankan Flask
# Atau tutup terminal tersebut
```

Atau gunakan Task Manager:
1. Buka Task Manager (Ctrl+Shift+Esc)
2. Cari proses "python.exe" atau "Python"
3. Klik kanan → End Task

### 2. Uninstall dan Install Ulang OpenAI Library

```cmd
pip uninstall openai -y
pip install "openai>=1.0.0"
```

### 3. Jalankan Ulang Aplikasi

```cmd
python app.py
```

## Solusi Alternatif: Gunakan Script Otomatis

Jalankan file `run.bat` yang sudah disediakan:

```cmd
run.bat
```

Script ini akan:
1. Upgrade library OpenAI
2. Install dependencies lainnya
3. Menjalankan aplikasi

## Verifikasi Instalasi

Setelah install ulang, test koneksi dengan:

```cmd
python test_groq_connection.py
```

Output yang diharapkan:
```
============================================================
TopicFlow - Groq API Connection Test
============================================================

✓ OpenAI library version: 1.x.x
✓ API Key loaded (length: 56)

Testing Groq API connection...
------------------------------------------------------------
Creating OpenAI client with Groq base URL...
✓ Client created successfully

Testing API call with simple prompt...
✓ API call successful!

Response:
{"message": "Hello!"}

============================================================
✓ All tests passed! Groq API is working correctly.
============================================================
```

## Troubleshooting Tambahan

### Jika Masih Error Setelah Reinstall

1. **Cek versi Python:**
   ```cmd
   python --version
   ```
   Pastikan Python 3.8 atau lebih tinggi.

2. **Bersihkan cache pip:**
   ```cmd
   pip cache purge
   pip uninstall openai -y
   pip install --no-cache-dir "openai>=1.0.0"
   ```

3. **Gunakan virtual environment (recommended):**
   ```cmd
   # Buat virtual environment
   python -m venv venv
   
   # Aktifkan (Windows)
   venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Jalankan aplikasi
   python app.py
   ```

### Jika Ada Proxy di Jaringan Anda

Aplikasi sudah dikonfigurasi untuk menonaktifkan proxy settings. Tapi jika masih bermasalah, tambahkan ini di file `.env`:

```env
NO_PROXY=*
```

### Cek Port yang Digunakan

Jika port 5000 sudah digunakan:

```cmd
# Gunakan port lain
set PORT=8000
python app.py
```

Lalu buka `http://localhost:8000`

## Versi Library yang Direkomendasikan

```
Flask==3.0.0
python-dotenv==1.0.0
openai>=1.0.0
```

## Masih Bermasalah?

1. Pastikan file `.env` sudah berisi API key yang valid
2. Cek koneksi internet
3. Pastikan tidak ada firewall yang memblokir koneksi ke api.groq.com
4. Coba restart komputer (untuk clear semua environment variables)

## Kontak

Jika masih ada masalah, cek:
- Terminal output untuk error message lengkap
- Browser console (F12) untuk error frontend
- File `test_groq_connection.py` untuk diagnostic

---

**Developer**: M Rizki Agil Prakoso (NIM: 25.01.53.0015)
