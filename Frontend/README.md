# TopicFlow Frontend

Frontend untuk aplikasi TopicFlow - AI Educational Assistant.

## 📁 Struktur Frontend

```
Frontend/
├── index.html            # Main HTML page
├── main.js              # JavaScript logic
├── style.css            # Custom styles
└── README.md            # Documentation (this file)
```

Semua file HTML, CSS, dan JavaScript langsung berada di folder Frontend tanpa subfolder untuk kemudahan akses dan maintenance.

## 🎨 Teknologi

- **HTML5** - Semantic markup
- **Tailwind CSS** - Utility-first CSS framework
- **Vanilla JavaScript** - No framework dependencies
- **Responsive Design** - Mobile-first approach

## ✨ Fitur UI/UX

### 🌓 Dark Mode
- Toggle dark/light mode dengan satu klik
- Preference disimpan di localStorage
- Smooth transition animations

### 🌐 Multi-Language Support
- Bahasa Indonesia & English
- Language preference disimpan di localStorage
- Real-time language switching

### 📱 Responsive Design
- Optimal di desktop, tablet, dan mobile
- Adaptive layouts
- Touch-friendly interface

### 💾 Export Features
- **Copy to Clipboard** - Copy hasil dengan satu klik
- **Export Text** - Download sebagai .txt file
- **Export PDF** - Professional PDF format
- **Print** - Direct browser printing

### 📚 History Panel
- Menyimpan 10 hasil terakhir
- Stored di localStorage
- Quick access ke hasil sebelumnya
- Clear history option

## 🎯 Komponen Utama

### 1. Material Input Tab
- Text area untuk input materi belajar
- PDF file upload support
- Character counter
- Clear button

### 2. Summary Tab
- Display summary results
- Bullet points format
- Export & copy options

### 3. Quiz Tab
- Interactive multiple choice questions
- Answer feedback
- Score tracking
- Explanation display

### 4. Flashcard Tab
- Interactive flip cards
- Term & definition
- Navigation controls
- Card counter

## 🔧 Konfigurasi API

Frontend berkomunikasi dengan backend melalui fetch API:

```javascript
// API endpoint configuration
const API_BASE = window.location.origin;

// Example API call
fetch(`${API_BASE}/api/summarize`, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ material: text })
});
```

## 🎨 Styling

### Tailwind CSS
Frontend menggunakan Tailwind CSS via CDN:
```html
<script src="https://cdn.tailwindcss.com"></script>
```

### Custom CSS
Additional styling di `static/css/style.css`:
- Flashcard flip animations
- Dark mode transitions
- Custom scrollbars
- Print styles

## 📱 Browser Support

- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+

## 🚀 Development

### Local Development

1. Pastikan backend sudah running di `http://localhost:5000`
2. Buka `http://localhost:5000` di browser
3. Frontend akan di-serve oleh Flask langsung dari folder Frontend/

### Modifikasi Frontend

**Edit HTML:**
```bash
# Edit file langsung di Frontend/
notepad Frontend\index.html
```

**Edit JavaScript:**
```bash
notepad Frontend\main.js
```

**Edit CSS:**
```bash
notepad Frontend\style.css
```

### Auto-reload
Flask development server akan auto-reload ketika ada perubahan file.

## 📦 Assets

### Icons
Menggunakan emojis untuk icons (no external dependencies)

### Fonts
System fonts stack untuk optimal performance:
```css
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, ...
```

## 🎯 User Flow

1. **Input Material**
   - User paste/type study material
   - Or upload PDF file
   - Click generate button

2. **Processing**
   - Show loading state
   - Send request to backend
   - Handle errors gracefully

3. **Display Results**
   - Show formatted results
   - Enable interactions (quiz answers, card flips)
   - Provide export options

4. **History**
   - Auto-save to history
   - Allow re-view previous results
   - Clear history option

## ♿ Accessibility

- Semantic HTML tags
- ARIA labels where needed
- Keyboard navigation support
- Screen reader friendly
- High contrast mode support

## 🔄 State Management

State dikelola dengan localStorage:

```javascript
// Save state
localStorage.setItem('theme', 'dark');
localStorage.setItem('language', 'id');
localStorage.setItem('history', JSON.stringify(historyArray));

// Load state
const theme = localStorage.getItem('theme');
const language = localStorage.getItem('language');
const history = JSON.parse(localStorage.getItem('history') || '[]');
```

## 🐛 Troubleshooting

### API Connection Error
- Pastikan backend running
- Check browser console untuk error messages
- Verify CORS settings

### Dark Mode Not Working
- Clear browser cache
- Check localStorage permissions
- Verify JavaScript enabled

### Export Not Working
- Check browser download permissions
- Verify popup blocker settings
- Try different browser
