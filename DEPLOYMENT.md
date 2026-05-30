# 🚀 Panduan Deployment TopicFlow

Panduan lengkap untuk deploy aplikasi TopicFlow ke berbagai platform cloud.

## 📋 Persiapan Sebelum Deploy

### 1. Pastikan Aplikasi Berjalan Lokal
```bash
python app.py
# Test di http://localhost:5000
```

### 2. Commit ke Git
```bash
git init
git add .
git commit -m "Initial commit - TopicFlow v1.0"
```

### 3. Push ke GitHub
```bash
# Buat repository baru di GitHub
git remote add origin https://github.com/username/topicflow.git
git branch -M main
git push -u origin main
```

---

## 🎯 Option 1: Deploy ke Render (RECOMMENDED)

**Kelebihan:**
- ✅ Gratis untuk hobby projects
- ✅ Auto-deploy dari GitHub
- ✅ SSL certificate otomatis
- ✅ Easy setup

### Langkah-langkah:

#### 1. Buat Akun Render
- Kunjungi [render.com](https://render.com)
- Sign up dengan GitHub account

#### 2. Create New Web Service
- Klik **"New +"** → **"Web Service"**
- Connect repository GitHub Anda
- Pilih repository `topicflow`

#### 3. Konfigurasi Service
```
Name: topicflow
Region: Singapore (atau terdekat)
Branch: main
Runtime: Python 3
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
```

#### 4. Tambahkan Gunicorn ke requirements.txt
```bash
# Tambahkan di requirements.txt
gunicorn==21.2.0
```

#### 5. Set Environment Variables
Di Render dashboard, tambahkan:
```
GROQ_API_KEY = your_groq_api_key_here
PORT = 10000
SECRET_KEY = your-random-secret-key-here
```

#### 6. Deploy!
- Klik **"Create Web Service"**
- Tunggu build selesai (~2-3 menit)
- Aplikasi akan tersedia di: `https://topicflow.onrender.com`

### Update Aplikasi
Setiap push ke GitHub akan auto-deploy:
```bash
git add .
git commit -m "Update feature"
git push origin main
```

---

## 🌐 Option 2: Deploy ke Railway

**Kelebihan:**
- ✅ Setup sangat mudah
- ✅ Free tier generous
- ✅ Auto-deploy

### Langkah-langkah:

#### 1. Buat Akun Railway
- Kunjungi [railway.app](https://railway.app)
- Sign up dengan GitHub

#### 2. Deploy dari GitHub
- Klik **"New Project"**
- Pilih **"Deploy from GitHub repo"**
- Pilih repository `topicflow`

#### 3. Set Environment Variables
```
GROQ_API_KEY = your_groq_api_key_here
```

#### 4. Generate Domain
- Klik **"Settings"** → **"Generate Domain"**
- Aplikasi tersedia di: `https://topicflow.up.railway.app`

---

## ☁️ Option 3: Deploy ke Vercel

**Kelebihan:**
- ✅ Sangat cepat
- ✅ Global CDN
- ✅ Free SSL

### Langkah-langkah:

#### 1. Install Vercel CLI
```bash
npm install -g vercel
```

#### 2. Buat vercel.json
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ],
  "env": {
    "GROQ_API_KEY": "@groq_api_key"
  }
}
```

#### 3. Deploy
```bash
vercel
# Follow prompts
# Set GROQ_API_KEY saat diminta
```

---

## 🐳 Option 4: Deploy dengan Docker

### 1. Buat Dockerfile
```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

### 2. Buat .dockerignore
```
__pycache__
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.env
.git
.gitignore
```

### 3. Build & Run
```bash
# Build image
docker build -t topicflow .

# Run container
docker run -p 5000:5000 \
  -e GROQ_API_KEY=your_key_here \
  topicflow
```

### 4. Deploy ke Docker Hub
```bash
# Tag image
docker tag topicflow username/topicflow:latest

# Push to Docker Hub
docker push username/topicflow:latest
```

---

## 🔧 Konfigurasi Production

### 1. Update app.py untuk Production
```python
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV') != 'production'
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )
```

### 2. Tambahkan Gunicorn Config (gunicorn.conf.py)
```python
bind = "0.0.0.0:5000"
workers = 2
threads = 4
timeout = 120
```

### 3. Update requirements.txt
```txt
Flask==3.0.0
python-dotenv==1.0.0
openai==1.12.0
gunicorn==21.2.0
```

---

## 🔒 Security Checklist

- [ ] API key tidak di-commit ke Git
- [ ] `.env` ada di `.gitignore`
- [ ] SECRET_KEY di-generate random untuk production
- [ ] HTTPS enabled (otomatis di Render/Railway/Vercel)
- [ ] Rate limiting diaktifkan (opsional)
- [ ] CORS dikonfigurasi dengan benar

---

## 📊 Monitoring & Logs

### Render
- Dashboard → Logs tab
- Real-time logs
- Metrics (CPU, Memory)

### Railway
- Project → Deployments → View Logs
- Metrics dashboard

### Vercel
- Dashboard → Deployments → Function Logs
- Analytics

---

## 🐛 Troubleshooting Deployment

### Error: "Application failed to start"
```bash
# Check logs
# Pastikan requirements.txt lengkap
# Pastikan Python version match
```

### Error: "Module not found"
```bash
# Tambahkan missing module ke requirements.txt
pip freeze > requirements.txt
```

### Error: "Port already in use"
```bash
# Gunakan environment variable PORT
port = int(os.getenv('PORT', 5000))
```

### Error: "API key not found"
```bash
# Set environment variable di platform
# Jangan hardcode di code
```

---

## 🎯 Rekomendasi Platform

| Platform | Best For | Free Tier | Auto-Deploy |
|----------|----------|-----------|-------------|
| **Render** | Production apps | 750 hrs/month | ✅ |
| **Railway** | Quick prototypes | $5 credit | ✅ |
| **Vercel** | Serverless apps | Unlimited | ✅ |
| **Heroku** | Enterprise | Limited | ✅ |

**Rekomendasi untuk UTS:** **Render** - Paling mudah dan reliable!

---

## 📝 Post-Deployment Checklist

- [ ] Test semua fitur di production URL
- [ ] Test dark mode
- [ ] Test language toggle
- [ ] Test export features
- [ ] Test responsive di mobile
- [ ] Share URL dengan dosen/teman
- [ ] Backup database (jika ada)

---

## 🔄 Update Deployment

### Auto-Deploy (Render/Railway/Vercel)
```bash
git add .
git commit -m "Update: description"
git push origin main
# Auto-deploy dalam 2-3 menit
```

### Manual Deploy (Docker)
```bash
docker build -t topicflow .
docker push username/topicflow:latest
# Restart container di server
```

---

## 📞 Support

Jika ada masalah deployment:
1. Check platform documentation
2. Check logs untuk error messages
3. Verify environment variables
4. Test locally first

---

**Happy Deploying! 🚀**

Made with ❤️ by M Rizki Agil Prakoso & Imam Agus Faisal
