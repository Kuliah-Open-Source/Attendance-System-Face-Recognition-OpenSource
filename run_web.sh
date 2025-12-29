#!/bin/bash

echo "🌐 Starting Face Recognition Attendance Web Application..."
echo "📋 Pastikan webcam sudah terhubung"
echo "🔗 Aplikasi akan berjalan di: http://localhost:5000"
echo

# Activate virtual environment
source venv/bin/activate

# Start Flask application
python app.py