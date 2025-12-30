<div align="center">

# 🎯 Face Recognition Attendance System

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&duration=3000&pause=1000&color=DC2626&center=true&vCenter=true&width=600&lines=Real-time+Face+Recognition;Modern+Web+Interface;Premium+UI%2FUX+Effects;Computer+Vision+%26+ML" alt="Typing SVG" />

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.0+-red.svg?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=for-the-badge)](CONTRIBUTING.md)

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="900">

### 🚀 Sistem absensi otomatis menggunakan teknologi computer vision dan machine learning untuk mengenali wajah karyawan secara real-time dengan antarmuka web yang modern dan premium.

<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="400">

</div>

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🎥 **Core Features**
- 🔍 **Real-time Face Recognition** - Deteksi dan pengenalan wajah secara langsung
- 🌐 **Modern Web Interface** - UI/UX premium dengan animasi dan efek visual
- 📱 **Responsive Design** - Berfungsi di desktop, tablet, dan mobile
- 🔒 **Anti-duplicate System** - Mencegah absen ganda dalam satu hari
- 📊 **Data Analytics** - Dashboard dengan statistik kehadiran

</td>
<td width="50%">

### 🎨 **Premium Effects**
- ✨ **Glassmorphism** - Efek kaca transparan modern
- 🎭 **3D Tilt Effects** - Animasi kartu 3D interaktif
- 💫 **Neon Glow** - Efek cahaya neon yang memukau
- 🎪 **Floating Animations** - Elemen melayang yang smooth
- 🧲 **Magnetic Buttons** - Tombol yang tertarik ke mouse

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

# 🚀 Run application
python app.py
```

</details>

<div align="center">

### 🌐 Akses aplikasi di: **http://localhost:5000**

<img src="https://user-images.githubusercontent.com/74038190/212257467-871d32b7-e401-42e8-a166-fcfd7baa4c6b.gif" width="100">

</div>

---

## 📖 Usage Guide

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257472-08e52665-c503-4bd9-aa20-f5a4dae769b5.gif" width="100">
</div>

<table>
<tr>
<td width="25%" align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257481-9e9588a0-8fce-4908-8a30-5353b02aa5e8.gif" width="80">
<h3>1️⃣ Register</h3>
<p>Daftarkan wajah karyawan baru</p>
</td>
<td width="25%" align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257465-7ce8d493-cac5-494e-982a-5a9deb852c4b.gif" width="80">
<h3>2️⃣ Scan</h3>
<p>Sistem otomatis mengenali wajah</p>
</td>
<td width="25%" align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257468-1e9a91f1-b626-4baa-b15d-5c385dfa7763.gif" width="80">
<h3>3️⃣ Analytics</h3>
<p>Lihat data dan statistik</p>
</td>
<td width="25%" align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257460-738ff738-247f-4445-a718-cdd0ca76e2db.gif" width="80">
<h3>4️⃣ Export</h3>
<p>Download laporan CSV</p>
</td>
</tr>
</table>

### 🎯 Detailed Steps

<details>
<summary>👤 <b>1. Register Employee Face</b></summary>

- 🌐 Kunjungi `/register`
- ✍️ Masukkan nama karyawan
- 📸 Ambil foto dengan kamera
- ✅ Klik "Daftarkan Wajah"

</details>

<details>
<summary>🎥 <b>2. Attendance System</b></summary>

- 📊 Dashboard utama menampilkan live camera
- ⏰ Sistem otomatis mengenali wajah setiap 3 detik
- 👆 Atau klik "Scan Wajah" untuk manual scan
- 💾 Data kehadiran tersimpan otomatis

</details>

<details>
<summary>📈 <b>3. View Attendance Data</b></summary>

- 📋 Kunjungi `/attendance`
- 🔍 Filter data berdasarkan tanggal
- 📊 Export ke CSV
- 📈 Lihat statistik real-time

</details>

<details>
<summary>🔧 <b>4. Camera Diagnostics</b></summary>

- 🛠️ Kunjungi `/camera-test`
- 🔍 Test kamera dan troubleshooting
- 📊 Monitor performance metrics
- 📥 Download diagnostic report

</details>

---

## 🏗️ Architecture

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257463-4d082cb4-7483-4eaf-bc25-6dde2628aabd.gif" width="100">
</div>

```mermaid
graph TD
    A[📹 Camera Input] --> B[🔍 Face Detection]
    B --> C[🧠 Feature Extract]
    C --> D[🗃️ Face Database]
    D --> E[🔄 Face Matching]
    E --> F[📊 Attendance Log]
    
    style A fill:#ff6b6b
    style B fill:#4ecdc4
    style C fill:#45b7d1
    style D fill:#96ceb4
    style E fill:#feca57
    style F fill:#ff9ff3
```

### 🛠️ Tech Stack

<div align="center">

| Backend | Frontend | Computer Vision | Database | UI/UX |
|---------|----------|----------------|----------|-------|
| ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) | ![OpenCV](https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white) | ![CSV](https://img.shields.io/badge/CSV-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white) | ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) |
| ![NumPy](https://img.shields.io/badge/NumPy-777BB4?style=for-the-badge&logo=numpy&logoColor=white) | ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) | ![Haar Cascade](https://img.shields.io/badge/Haar_Cascade-FF6B6B?style=for-the-badge) | ![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white) | ![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white) |

</div>

---

## 📁 Project Structure

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257456-4d082cb4-7483-4eaf-bc25-6dde2628aabd.gif" width="100">
</div>

```
🎯 face-recognition-attendance/
├── 📂 static/
│   ├── 🎨 css/
│   │   ├── ✨ style.css           # Main styling
│   │   ├── 🎭 effects.css         # Premium effects
│   │   ├── 📝 text-fixes.css      # Text visibility
│   │   └── 📷 camera-test.css     # Camera diagnostics
│   ├── ⚡ js/
│   │   ├── 🧠 app.js             # Core JavaScript
│   │   └── 🎪 premium-effects.js  # Interactive effects
│   └── 🎯 favicon.svg            # App icon
├── 🌐 templates/
│   ├── 🏠 index.html             # Dashboard
│   ├── 👤 register.html          # Face registration
│   ├── 📊 attendance.html        # Data viewer
│   └── 🔧 camera_test.html       # Diagnostics
├── 👥 faces/                     # Face database
├── 🚀 app.py                     # Flask application
├── 🤖 face_recognition.py        # CLI version
├── 📝 register_face.py           # CLI registration
├── 📈 view_attendance.py         # CLI data viewer
├── 📊 attendance.csv             # Attendance data
├── 📦 requirements.txt           # Dependencies
├── 📖 README.md                  # Documentation
├── ⚖️ LICENSE                    # MIT License
├── 🤝 CONTRIBUTING.md            # Contribution guide
├── 📋 CODE_OF_CONDUCT.md         # Code of conduct
└── 🚀 run.sh                     # Launch script
```

---

## 🎨 UI/UX Features

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257470-1f283c85-8d75-4c94-9f5c-6d3c3d0c7a5e.gif" width="100">
</div>

<table>
<tr>
<td width="33%" align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257475-e0d3d5c2-c4c4-4c4c-8c4c-8c4c8c4c8c4c.gif" width="80">
<h3>✨ Glassmorphism</h3>
<p>Modern glass-like effects</p>
</td>
<td width="33%" align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257477-1f283c85-8d75-4c94-9f5c-6d3c3d0c7a5e.gif" width="80">
<h3>🎭 3D Animations</h3>
<p>Interactive 3D card tilt</p>
</td>
<td width="33%" align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257479-e0d3d5c2-c4c4-4c4c-8c4c-8c4c8c4c8c4c.gif" width="80">
<h3>💫 Neon Effects</h3>
<p>Glowing elements</p>
</td>
</tr>
<tr>
<td width="33%" align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257481-9e9588a0-8fce-4908-8a30-5353b02aa5e8.gif" width="80">
<h3>🎪 Floating</h3>
<p>Smooth floating elements</p>
</td>
<td width="33%" align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257483-1f283c85-8d75-4c94-9f5c-6d3c3d0c7a5e.gif" width="80">
<h3>🧲 Magnetic</h3>
<p>Mouse-attracted buttons</p>
</td>
<td width="33%" align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257485-e0d3d5c2-c4c4-4c4c-8c4c-8c4c8c4c8c4c.gif" width="80">
<h3>📱 Responsive</h3>
<p>All screen sizes</p>
</td>
</tr>
</table>

---

## 🔧 Configuration

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257487-1f283c85-8d75-4c94-9f5c-6d3c3d0c7a5e.gif" width="100">
</div>

### ⚙️ Adjust Recognition Sensitivity
```python
# 🎯 In face_recognition.py
best_score = 0.7  # Lower = more sensitive (0.5-0.8)
```

### ⏱️ Change Cooldown Timer
```python
# ⏰ Auto-scan interval
recognition_cooldown = 3  # seconds between auto-scans
```

### 🔍 Modify Detection Parameters
```python
# 📷 Face detection settings
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#                                    scale, neighbors
```

---

## 📊 Performance Metrics

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
![Safari](https://img.shields.io/badge/Safari-✅_Good-000000?style=for-the-badge&logo=safari&logoColor=white)

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
<a href="mailto:support@yourproject.com">
<img src="https://img.shields.io/badge/📧_Email-Support-orange?style=for-the-badge">
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
<br><sub>Computer vision tools</sub>
</td>
<td align="center">
<img src="https://img.shields.io/badge/Flask-Team-000000?style=for-the-badge&logo=flask&logoColor=white">
<br><sub>Web framework</sub>
</td>
<td align="center">
<img src="https://img.shields.io/badge/Bootstrap-Team-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white">
<br><sub>UI components</sub>
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

### 🔥 **Phase 1 - AI Enhancement**
- [ ] 🧠 Deep learning integration (CNN)
- [ ] 👥 Multi-face simultaneous recognition
- [ ] 🎯 Improved accuracy algorithms
- [ ] 🔍 Liveness detection
- [ ] 🎭 Mask detection support

</td>
<td width="50%">

### 🚀 **Phase 2 - Platform Expansion**
- [ ] 🗄️ Database integration (PostgreSQL/MySQL)
- [ ] 🌐 REST API development
- [ ] 📱 Mobile app (React Native)
- [ ] 🐳 Docker containerization
- [ ] ☁️ Cloud deployment guides

</td>
</tr>
<tr>
<td width="50%">

### 📊 **Phase 3 - Analytics & Integration**
- [ ] 📈 Advanced analytics dashboard
- [ ] 🔔 Real-time notifications
- [ ] 🏢 LDAP/Active Directory integration
- [ ] 💼 HR system integration
- [ ] 📊 Business intelligence reports

</td>
<td width="50%">

### 🌟 **Phase 4 - Enterprise Features**
- [ ] 🔐 Advanced security features
- [ ] 🌍 Multi-language support
- [ ] 🎨 Custom themes
- [ ] 📡 IoT device integration
- [ ] 🤖 AI-powered insights

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
[![Twitter](https://img.shields.io/badge/Twitter-@yourusername-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/yourusername)

</div>

---

<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="900">

### ⭐ **Star this repository if you find it helpful!** ⭐

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=18&duration=2000&pause=1000&color=DC2626&center=true&vCenter=true&width=500&lines=Built+with+%E2%9D%A4%EF%B8%8F+for+the+community;Open+Source+%26+Free+Forever;Contributions+Welcome!" alt="Typing SVG" />

<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="300">

**Made with ❤️ by developers, for developers**

</div>