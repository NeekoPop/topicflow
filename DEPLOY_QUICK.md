# 🚀 Quick Deploy Guide - TopicFlow

Panduan cepat deploy TopicFlow dalam 10 menit!

## 🎯 Pilihan Terbaik: Render.com

**Kenapa Render?**
- ✅ Gratis 750 jam/bulan
- ✅ Auto-deploy dari GitHub
- ✅ SSL gratis
- ✅ Setup super mudah

---

## 📝 Langkah-langkah (10 Menit)

### 1. Persiapan (2 menit)

#### A. Tambahkan Gunicorn
```bash
# Tambahkan di requirements.txt
gunicorn==21.2.0
```

#### B. Commit ke Git
```bash
git add .
git commit -m "Ready for deployment"
```

#### C. Push ke GitHub
```bash
# Buat repo baru di github.com
git remote add origin https://github.com/username/topicflow.git
git branch -M main
git push -u origin main
```

---

### 2. Deploy ke Render (5 menit)

#### A. Buat Akun
1. Kunjungi [render.com](https://render.com)
2. Sign up dengan GitHub

#### B. Create Web Service
1. Klik **"New +"** → **"Web Service"**
2. Connect repository `topicflow`
3. Klik **"Connect"**

#### C. Konfigurasi
```
Name: topicflow
Region: Singapore
Branch: main
Runtime: Python 3
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
Instance Type: Free
```

#### D. Environment Variables
Klik **"Advanced"** → **"Add Environment Variable"**:
```
GROQ_API_KEY = your_groq_api_key_here
PORT = 10000
SECRET_KEY = random-secret-key-123
```

#### E. Deploy!
1. Klik **"Create Web Service"**
2. Tunggu build (~2-3 menit)
3. Done! ✅

---

### 3. Test Aplikasi (1 menit)

URL akan tersedia di:
```
https://topicflow.onrender.com
```

Test semua fitur:
- [ ] Summarizer
- [ ] Quiz Generator
- [ ] Flashcard Maker
- [ ] Dark Mode
- [ ] Language Toggle
- [ ] Export Features

---

## 🔄 Update Aplikasi

Setiap kali push ke GitHub, otomatis deploy:
```bash
git add .
git commit -m "Update feature"
git push origin main
# Auto-deploy dalam 2-3 menit
```

---

## ⚡ Alternative: Railway (Lebih Cepat)

### Deploy dalam 3 Menit:

1. **Buat Akun**
   - [railway.app](https://railway.app)
   - Sign up dengan GitHub

2. **Deploy**
   - Klik **"New Project"**
   - Pilih **"Deploy from GitHub repo"**
   - Pilih `topicflow`

3. **Set Environment**
   ```
   GROQ_API_KEY = your_key_here
   ```

4. **Generate Domain**
   - Settings → Generate Domain
   - Done! ✅

---

## 🐛 Troubleshooting

### Build Failed?
```bash
# Update requirements.txt
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update dependencies"
git push
```

### App Crash?
1. Check logs di Render dashboard
2. Verify environment variables
3. Test locally first: `gunicorn app:app`

### 502 Error?
1. Verify PORT environment variable
2. Check logs
3. Restart service

---

## ✅ Checklist Deployment

- [ ] Gunicorn di requirements.txt
- [ ] Code di GitHub
- [ ] Akun Render/Railway
- [ ] Environment variables set
- [ ] Build success
- [ ] App accessible
- [ ] All features working
- [ ] Share URL dengan dosen!

---

## 📞 Need Help?

- **Logs**: Render Dashboard → Logs tab
- **Docs**: [DEPLOYMENT.md](DEPLOYMENT.md) (lengkap)
- **Issues**: [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

---

**Deploy Time: ~10 minutes**  
**Cost: FREE** 🎉

Made with ❤️ by M Rizki Agil Prakoso & Imam Agus Faisal
