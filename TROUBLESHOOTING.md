# 🔧 Troubleshooting Guide - TopicFlow

Panduan mengatasi masalah umum yang mungkin terjadi saat menggunakan TopicFlow.

## 📋 Daftar Isi
- [Masalah Instalasi](#masalah-instalasi)
- [Masalah API Key](#masalah-api-key)
- [Masalah Backend](#masalah-backend)
- [Masalah Frontend](#masalah-frontend)
- [Masalah Deployment](#masalah-deployment)

---

## 🔨 Masalah Instalasi

### Error: "pip: command not found"
**Penyebab:** Python atau pip belum terinstall

**Solusi:**
```bash
# Windows
python -m ensurepip --upgrade

# Mac/Linux
sudo apt-get install python3-pip  # Ubuntu/Debian
brew install python3              # macOS
```

### Error: "No module named 'flask'"
**Penyebab:** Dependencies belum terinstall

**Solusi:**
```bash
pip install -r requirements.txt

# Atau install manual
pip install Flask python-dotenv openai
```

### Error: "Permission denied"
**Penyebab:** Tidak punya permission untuk install

**Solusi:**
```bash
# Gunakan virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

---

## 🔑 Masalah API Key

### Error: "GROQ_API_KEY not found in environment"
**Penyebab:** File `.env` tidak ada atau API key tidak diset

**Solusi:**
1. Pastikan file `.env` ada di root folder
2. Buka `.env` dan isi:
```env
GROQ_API_KEY=your_actual_api_key_here
```
3. Restart aplikasi

### Error: "API key configuration error"
**Penyebab:** API key masih placeholder atau kosong

**Solusi:**
1. Dapatkan API key dari [console.groq.com](https://console.groq.com)
2. Copy API key yang valid
3. Paste ke `.env` (ganti placeholder)
4. Jangan gunakan `your_groq_api_key_here`

### Error: "AI service authentication failed"
**Penyebab:** API key tidak valid atau expired

**Solusi:**
1. Login ke [console.groq.com](https://console.groq.com)
2. Verify API key masih aktif
3. Generate API key baru jika perlu
4. Update di `.env`

---

## 🖥️ Masalah Backend

### Error: "Address already in use" / Port 5000 sudah dipakai
**Penyebab:** Port 5000 sudah digunakan aplikasi lain

**Solusi 1 - Ganti Port:**
```bash
# Set environment variable
PORT=8000 python app.py
```

**Solusi 2 - Kill Process:**
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Mac/Linux
lsof -ti:5000 | xargs kill -9
```

### Error: "Failed to initialize Groq client"
**Penyebab:** Masalah dengan OpenAI library version

**Solusi:**
```bash
# Uninstall dan reinstall
pip uninstall openai -y
pip install openai==1.12.0

# Atau upgrade ke latest
pip install --upgrade openai
```

### Error: "AI service rate limit exceeded"
**Penyebab:** Terlalu banyak request dalam waktu singkat

**Solusi:**
1. Tunggu beberapa menit
2. Coba lagi
3. Jika sering terjadi, upgrade Groq plan

### Error: "AI service unavailable"
**Penyebab:** Koneksi internet atau Groq API down

**Solusi:**
1. Check koneksi internet
2. Test dengan curl:
```bash
curl https://api.groq.com/openai/v1/models \
  -H "Authorization: Bearer YOUR_API_KEY"
```
3. Check [status.groq.com](https://status.groq.com)

---

## 🎨 Masalah Frontend

### Masalah: "Menu tidak bisa diklik"
**Penyebab:** JavaScript error atau duplikasi ID

**Solusi:**
1. Buka Developer Tools (F12)
2. Check Console untuk error
3. Refresh browser (Ctrl+F5)
4. Clear cache browser

### Masalah: "Dark mode tidak berfungsi"
**Penyebab:** localStorage issue atau CSS tidak load

**Solusi:**
```javascript
// Clear localStorage
localStorage.clear()

// Refresh browser
location.reload()
```

### Masalah: "Export PDF tidak berfungsi"
**Penyebab:** jsPDF library tidak load

**Solusi:**
1. Check internet connection
2. Verify CDN link di index.html:
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
```
3. Refresh browser

### Masalah: "History tidak tersimpan"
**Penyebab:** localStorage disabled atau penuh

**Solusi:**
```javascript
// Test localStorage
try {
    localStorage.setItem('test', 'test');
    localStorage.removeItem('test');
    console.log('localStorage works!');
} catch(e) {
    console.error('localStorage disabled:', e);
}

// Clear old data
localStorage.clear()
```

### Masalah: "Responsive tidak bekerja di mobile"
**Penyebab:** Viewport meta tag atau CSS issue

**Solusi:**
1. Verify meta tag di HTML:
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
2. Clear browser cache
3. Test di browser lain

---

## 🚀 Masalah Deployment

### Error: "Build failed" di Render/Railway
**Penyebab:** requirements.txt tidak lengkap atau Python version mismatch

**Solusi:**
1. Update requirements.txt:
```bash
pip freeze > requirements.txt
```
2. Specify Python version di `runtime.txt`:
```
python-3.12.0
```
3. Commit dan push lagi

### Error: "Application timeout"
**Penyebab:** Aplikasi terlalu lama start atau crash

**Solusi:**
1. Check logs di platform dashboard
2. Verify environment variables
3. Test locally first:
```bash
gunicorn app:app
```

### Error: "502 Bad Gateway"
**Penyebab:** Aplikasi crash atau port configuration salah

**Solusi:**
1. Verify PORT environment variable
2. Check logs untuk error
3. Restart service

### Error: "Environment variable not found" di production
**Penyebab:** Environment variables tidak diset di platform

**Solusi:**
1. Login ke platform dashboard
2. Go to Settings → Environment Variables
3. Add:
```
GROQ_API_KEY = your_key
PORT = 10000
SECRET_KEY = random_string
```
4. Redeploy

---

## 🧪 Debugging Tips

### 1. Enable Debug Mode
```python
# app.py
if __name__ == '__main__':
    app.run(debug=True)
```

### 2. Check Logs
```bash
# Local
python app.py

# Production (Render)
# Dashboard → Logs tab

# Production (Railway)
# Project → Deployments → View Logs
```

### 3. Test API Endpoints
```bash
# Test health
curl http://localhost:5000/health

# Test summarize
curl -X POST http://localhost:5000/api/summarize \
  -H "Content-Type: application/json" \
  -d '{"material":"test material"}'
```

### 4. Browser Developer Tools
```
F12 → Console tab
Check for JavaScript errors
Check Network tab for failed requests
```

---

## 📞 Masih Ada Masalah?

### Langkah-langkah Debugging:

1. **Check Error Message**
   - Baca error message dengan teliti
   - Google error message spesifik

2. **Check Logs**
   - Backend: Terminal output
   - Frontend: Browser Console (F12)

3. **Verify Configuration**
   - `.env` file exists dan terisi
   - `requirements.txt` lengkap
   - Python version compatible

4. **Test Locally First**
   - Pastikan berjalan di local
   - Baru deploy ke production

5. **Check Documentation**
   - README.md
   - DEPLOYMENT.md
   - Platform documentation

---

## 🔍 Common Error Messages

| Error | Penyebab | Solusi |
|-------|----------|--------|
| `ModuleNotFoundError` | Package tidak terinstall | `pip install <package>` |
| `FileNotFoundError: .env` | File .env tidak ada | Buat file .env |
| `KeyError: 'GROQ_API_KEY'` | API key tidak diset | Set di .env |
| `ConnectionError` | Tidak ada internet | Check koneksi |
| `JSONDecodeError` | Response bukan JSON | Check API response |
| `PermissionError` | Tidak ada permission | Gunakan sudo/admin |

---

## ✅ Prevention Checklist

Untuk menghindari masalah:

- [ ] Gunakan virtual environment
- [ ] Install semua dependencies dari requirements.txt
- [ ] Set API key dengan benar di .env
- [ ] Test locally sebelum deploy
- [ ] Commit .gitignore dengan benar
- [ ] Backup code secara regular
- [ ] Monitor logs di production
- [ ] Keep dependencies up to date

---

**Jika masalah masih berlanjut, hubungi developer atau buat issue di GitHub repository.**

Made with ❤️ by M Rizki Agil Prakoso & Imam Agus Faisal
