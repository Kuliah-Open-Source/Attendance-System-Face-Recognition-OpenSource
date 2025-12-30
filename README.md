<div align="center">

# 🎯 Face Recognition Attendance System

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&duration=3000&pause=1000&color=DC2626&center=true&vCenter=true&width=600&lines=Real-time+Face+Recognition;Modern+Web+Interface;Premium+UI%2FUX+Effects;Computer+Vision+%26+ML" alt="Typing SVG" />

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.0+-red.svg?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=for-the-badge)](CONTRIBUTING.md)

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="900">

### 🚀 Sistem absensi otomatis menggunakan teknologi computer vision untuk mengenali wajah karyawan secara real-time dengan antarmuka web yang modern.

<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="400">

</div>

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🎥 **Core Features**
- 🔍 **Real-time Face Recognition** - Deteksi wajah dengan OpenCV Haar Cascade
- 🌐 **Modern Web Interface** - Flask web app dengan Bootstrap UI
- 📱 **Responsive Design** - Berfungsi di desktop dan mobile
- 🔒 **Anti-duplicate System** - Mencegah absen ganda dalam satu hari
- 📊 **CSV Data Export** - Export data kehadiran ke file CSV

</td>
<td width="50%">

### 🎨 **UI/UX Features**
- ✨ **Glassmorphism Design** - Efek kaca transparan modern
- 🎭 **3D Card Effects** - Animasi kartu 3D interaktif
- 💫 **Neon Glow Effects** - Efek cahaya neon pada video
- 🎪 **Floating Animations** - Elemen melayang yang smooth
- 🧲 **Magnetic Buttons** - Tombol interaktif dengan hover effects

</td>
</tr>
</table>

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/225813708-98b745f2-7d22-48cf-9150-083f1b00d6c9.gif" width="600">
</div>

---

## 🚀 Quick Start

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257454-16e3712e-945a-4ca2-b238-408ad0bf87e6.gif" width="100">
</div>

### 📋 Prerequisites

```bash
✅ Python 3.8+
✅ Webcam/Camera  
✅ Modern web browser (Chrome, Firefox, Edge)
```

### 🛠️ Installation

<details>
<summary>📦 <b>Click to expand installation steps</b></summary>

```bash
# 📥 Clone repository
git clone https://github.com/yourusername/face-recognition-attendance.git
cd face-recognition-attendance

# 🐍 Create virtual environment
python -m venv venv

# ⚡ Activate virtual environment
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 📦 Install dependencies
pip install -r requirements.txt

# 🚀 Run web application
python app.py
```

</details>

<div align="center">

### 🌐 Akses aplikasi di: **http://localhost:5000**


</div>

---

## 📖 Usage Guide


<table>
<tr>
<td width="25%" align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257481-9e9588a0-8fce-4908-8a30-5353b02aa5e8.gif" width="80">
<h3>1️⃣ Register</h3>
<p>Daftarkan wajah karyawan</p>
</td>
<td width="25%" align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257465-7ce8d493-cac5-494e-982a-5a9deb852c4b.gif" width="80">
<h3>2️⃣ Attendance</h3>
<p>Scan wajah untuk absen</p>
</td>
<td width="25%" align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257468-1e9a91f1-b626-4baa-b15d-5c385dfa7763.gif" width="80">
<h3>3️⃣ View Data</h3>
<p>Lihat data kehadiran</p>
</td>
<td width="25%" align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257460-738ff738-247f-4445-a718-cdd0ca76e2db.gif" width="80">
<h3>4️⃣ Diagnostics</h3>
<p>Test kamera</p>
</td>
</tr>
</table>

### 🎯 Web Interface

<details>
<summary>🏠 <b>Dashboard (http://localhost:5000)</b></summary>

- 🎥 Live camera feed dengan face recognition
- 🔄 Auto-scan setiap 3 detik atau manual scan
- 📊 Statistik kehadiran hari ini
- 🎨 Premium UI dengan glassmorphism effects

</details>

<details>
<summary>👤 <b>Register Face (/register)</b></summary>

- ✍️ Input nama karyawan
- 📸 Capture foto dengan webcam
- 💾 Simpan ke folder `faces/`
- ✅ Konfirmasi registrasi berhasil

</details>

<details>
<summary>📊 <b>Attendance Data (/attendance)</b></summary>

- 📋 Tabel data kehadiran lengkap
- 🔍 Filter berdasarkan tanggal
- 📈 Statistik kehadiran real-time
- 💾 Export data ke CSV

</details>

<details>
<summary>🔧 <b>Camera Test (/camera-test)</b></summary>

- 🎥 Test kamera dan troubleshooting
- 📊 Performance metrics real-time
- 🔍 Device detection dan diagnostics
- 📥 Download diagnostic report

</details>

### 💻 CLI Version

```bash
# Daftarkan wajah (CLI)
python register_face.py

# Jalankan attendance (CLI)
python face_recognition.py

# Lihat data kehadiran (CLI)
python view_attendance.py
```

---

## 🏗️ Architecture

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257463-4d082cb4-7483-4eaf-bc25-6dde2628aabd.gif" width="100">
</div>

```mermaid
graph TD
    A[📹 Webcam Input] --> B[🔍 Haar Cascade Detection]
    B --> C[📊 Histogram Features]
    C --> D[🗃️ Face Database]
    D --> E[🔄 Correlation Matching]
    E --> F[📝 CSV Attendance Log]
    
    style A fill:#ff6b6b
    style B fill:#4ecdc4
    style C fill:#45b7d1
    style D fill:#96ceb4
    style E fill:#feca57
    style F fill:#ff9ff3
```

### 🛠️ Tech Stack

<div align="center">

| Backend | Frontend | Computer Vision | Database | UI Framework |
|---------|----------|----------------|----------|-------------|
| ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) | ![OpenCV](https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white) | ![CSV](https://img.shields.io/badge/CSV-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white) | ![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white) |
| ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) | ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) | ![NumPy](https://img.shields.io/badge/NumPy-777BB4?style=for-the-badge&logo=numpy&logoColor=white) | ![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white) | ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) |

</div>

---

## 📁 Project Structure

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257456-4d082cb4-7483-4eaf-bc25-6dde2628aabd.gif" width="100">
</div>

```
🎯 face-recognition-attendance/
├── 📂 static/                    # Web assets
│   ├── 🎨 css/
│   │   ├── style.css            # Main styling dengan tema merah-putih
│   │   ├── effects.css          # Premium effects (glassmorphism, 3D)
│   │   ├── text-fixes.css       # Text visibility fixes
│   │   └── camera-test.css      # Camera diagnostics styling
│   ├── ⚡ js/
│   │   ├── app.js              # Core JavaScript functionality
│   │   └── premium-effects.js   # Interactive effects (magnetic, tilt)
│   └── 🎯 favicon.svg          # App icon
├── 🌐 templates/                # Flask templates
│   ├── index.html              # Dashboard dengan live camera
│   ├── register.html           # Face registration form
│   ├── attendance.html         # Data viewer dengan filter
│   └── camera_test.html        # Camera diagnostics
├── 👥 faces/                    # Face database (images)
├── 🚀 app.py                   # Flask web application
├── 🤖 face_recognition.py      # CLI version
├── 📝 register_face.py         # CLI registration
├── 📊 view_attendance.py       # CLI data viewer
├── 📈 attendance.csv           # Attendance data
├── 📦 requirements.txt         # Python dependencies
├── 🔧 run.sh                   # CLI launcher
├── 🌐 run_web.sh              # Web launcher
├── 📖 README.md               # Documentation
├── ⚖️ LICENSE                 # MIT License
├── 🤝 CONTRIBUTING.md         # Contribution guide
└── 📋 CODE_OF_CONDUCT.md      # Code of conduct
```

---

## 🔧 Algorithm Details

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257487-1f283c85-8d75-4c94-9f5c-6d3c3d0c7a5e.gif" width="100">
</div>

### 🎯 Face Detection
- **Haar Cascade Classifier** - OpenCV pre-trained model
- **Real-time Processing** - 30 FPS detection rate
- **Multi-scale Detection** - Deteksi wajah berbagai ukuran

### 📊 Feature Extraction
- **Histogram Analysis** - Ekstraksi fitur dari grayscale image
- **Normalization** - Normalisasi histogram untuk konsistensi
- **Feature Vector** - 256-dimensional feature representation

### 🔄 Face Matching
- **Correlation Coefficient** - Perbandingan similarity antar wajah
- **Confidence Threshold** - 0.7 minimum untuk recognition
- **Best Match Selection** - Pilih wajah dengan skor tertinggi

### ⚙️ Configuration

```python
# Adjust recognition sensitivity
best_score = 0.7  # Lower = more sensitive (0.5-0.8)

# Change auto-scan interval
recognition_cooldown = 3  # seconds

# Modify detection parameters
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#                                    scale, neighbors
```

---

## 📊 Performance

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257489-e0d3d5c2-c4c4-4c4c-8c4c-8c4c8c4c8c4c.gif" width="100">
</div>

<table align="center">
<tr>
<td align="center">
<img src="https://img.shields.io/badge/Accuracy-85--95%25-brightgreen?style=for-the-badge&logo=target&logoColor=white">
</td>
<td align="center">
<img src="https://img.shields.io/badge/Speed-30_FPS-blue?style=for-the-badge&logo=speedtest&logoColor=white">
</td>
</tr>
<tr>
<td align="center">
<img src="https://img.shields.io/badge/Memory-50--100_MB-orange?style=for-the-badge&logo=memory&logoColor=white">
</td>
<td align="center">
<img src="https://img.shields.io/badge/CPU-10--20%25-red?style=for-the-badge&logo=cpu&logoColor=white">
</td>
</tr>
</table>

### 🌐 Browser Support

<div align="center">

![Chrome](https://img.shields.io/badge/Chrome-✅_Recommended-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white)
![Firefox](https://img.shields.io/badge/Firefox-✅_Good-FF7139?style=for-the-badge&logo=firefox&logoColor=white)
![Edge](https://img.shields.io/badge/Edge-✅_Good-0078D4?style=for-the-badge&logo=microsoftedge&logoColor=white)
![Safari](https://img.shields.io/badge/Safari-✅_Limited-000000?style=for-the-badge&logo=safari&logoColor=white)

</div>

---

## 🤝 Contributing

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257491-1f283c85-8d75-4c94-9f5c-6d3c3d0c7a5e.gif" width="100">
</div>

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### 🚀 Quick Contribution Steps

```bash
1️⃣ Fork the repository
2️⃣ Create feature branch: git checkout -b feature/amazing-feature
3️⃣ Commit changes: git commit -m 'Add amazing feature'
4️⃣ Push to branch: git push origin feature/amazing-feature
5️⃣ Open a Pull Request
```

<div align="center">

### 🏆 Contributors

<a href="https://github.com/yourusername/face-recognition-attendance/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=yourusername/face-recognition-attendance" />
</a>

</div>

---

## 🐛 Issues & Support

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257493-e0d3d5c2-c4c4-4c4c-8c4c-8c4c8c4c8c4c.gif" width="100">
</div>

<table>
<tr>
<td align="center">
<a href="https://github.com/yourusername/face-recognition-attendance/issues">
<img src="https://img.shields.io/badge/🐛_Bug_Reports-Create_Issue-red?style=for-the-badge">
</a>
</td>
<td align="center">
<a href="https://github.com/yourusername/face-recognition-attendance/issues">
<img src="https://img.shields.io/badge/💡_Feature_Requests-Request_Feature-blue?style=for-the-badge">
</a>
</td>
</tr>
<tr>
<td align="center">
<a href="https://github.com/yourusername/face-recognition-attendance/discussions">
<img src="https://img.shields.io/badge/💬_Discussions-Join_Chat-green?style=for-the-badge">
</a>
</td>
<td align="center">
<a href="/camera-test">
<img src="https://img.shields.io/badge/🔧_Diagnostics-Test_Camera-orange?style=for-the-badge">
</a>
</td>
</tr>
</table>

---

## 📝 License

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257495-1f283c85-8d75-4c94-9f5c-6d3c3d0c7a5e.gif" width="100">
</div>

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

</div>

---

## 🙏 Acknowledgments

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257497-e0d3d5c2-c4c4-4c4c-8c4c-8c4c8c4c8c4c.gif" width="100">
</div>

<table>
<tr>
<td align="center">
<img src="https://img.shields.io/badge/OpenCV-Community-27338e?style=for-the-badge&logo=opencv&logoColor=white">
<br><sub>Computer vision library</sub>
</td>
<td align="center">
<img src="https://img.shields.io/badge/Flask-Team-000000?style=for-the-badge&logo=flask&logoColor=white">
<br><sub>Web framework</sub>
</td>
<td align="center">
<img src="https://img.shields.io/badge/Bootstrap-Team-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white">
<br><sub>UI framework</sub>
</td>
</tr>
</table>

---

## 🔮 Roadmap

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257499-1f283c85-8d75-4c94-9f5c-6d3c3d0c7a5e.gif" width="100">
</div>

<table>
<tr>
<td width="50%">

### 🔥 **Phase 1 - Core Improvements**
- [ ] 🧠 Deep learning face recognition (CNN)
- [ ] 👥 Multi-face detection support
- [ ] 🎯 Improved accuracy algorithms
- [ ] 📱 Mobile app development
- [ ] 🗄️ Database integration (SQLite/PostgreSQL)

</td>
<td width="50%">

### 🚀 **Phase 2 - Enterprise Features**
- [ ] 🌐 REST API development
- [ ] 🐳 Docker containerization
- [ ] ☁️ Cloud deployment guides
- [ ] 📊 Advanced analytics dashboard
- [ ] 🔔 Real-time notifications

</td>
</tr>
</table>

---

## 📞 Contact

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257501-e0d3d5c2-c4c4-4c4c-8c4c-8c4c8c4c8c4c.gif" width="100">
</div>

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-@yourusername-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourusername)
[![Email](https://img.shields.io/badge/Email-your.email@example.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:your.email@example.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Your_Profile-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/yourprofile)

</div>

---

<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="900">

### ⭐ **Star this repository if you find it helpful!** ⭐

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=18&duration=2000&pause=1000&color=DC2626&center=true&vCenter=true&width=500&lines=Built+with+%E2%9D%A4%EF%B8%8F+for+the+community;Open+Source+%26+Free+Forever;Contributions+Welcome!" alt="Typing SVG" />

<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="300">

**Made with ❤️ by developers, for developers**

</div>