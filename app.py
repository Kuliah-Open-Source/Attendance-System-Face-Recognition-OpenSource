from flask import Flask, render_template, request, jsonify, Response
from flask_socketio import SocketIO, emit
import cv2
import numpy as np
import pandas as pd
from datetime import datetime
import os
import base64
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'attendance_system_secret'
socketio = SocketIO(app, cors_allowed_origins="*")

class WebAttendanceSystem:
    def __init__(self):
        self.known_faces = {}
        self.attendance_file = "attendance.csv"
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.load_known_faces()
        
    def extract_face_features(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
        face = cv2.resize(gray, (100, 100))
        hist = cv2.calcHist([face], [0], None, [256], [0, 256])
        hist = cv2.normalize(hist, hist).flatten()
        return hist
        
    def load_known_faces(self):
        faces_dir = "faces"
        if not os.path.exists(faces_dir):
            os.makedirs(faces_dir)
            return
            
        for filename in os.listdir(faces_dir):
            if filename.endswith(('.jpg', '.jpeg', '.png')):
                name = os.path.splitext(filename)[0]
                image_path = os.path.join(faces_dir, filename)
                
                image = cv2.imread(image_path)
                if image is not None:
                    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
                    
                    if len(faces) > 0:
                        x, y, w, h = max(faces, key=lambda f: f[2] * f[3])
                        face_crop = image[y:y+h, x:x+w]
                        features = self.extract_face_features(face_crop)
                        
                        if name not in self.known_faces:
                            self.known_faces[name] = []
                        self.known_faces[name].append(features)
    
    def compare_faces(self, features1, features2):
        correlation = np.corrcoef(features1, features2)[0, 1]
        return correlation if not np.isnan(correlation) else 0
    
    def recognize_face(self, face_image):
        features = self.extract_face_features(face_image)
        
        best_match = None
        best_score = 0.7
        
        for name, known_features_list in self.known_faces.items():
            scores = []
            for known_features in known_features_list:
                score = self.compare_faces(features, known_features)
                scores.append(score)
            
            avg_score = np.mean(scores) if scores else 0
            
            if avg_score > best_score:
                best_score = avg_score
                best_match = name
        
        return best_match, best_score
    
    def mark_attendance(self, name):
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M:%S")
        
        if os.path.exists(self.attendance_file):
            df = pd.read_csv(self.attendance_file)
        else:
            df = pd.DataFrame(columns=['Name', 'Date', 'Time'])
        
        today_attendance = df[(df['Name'] == name) & (df['Date'] == date_str)]
        
        if today_attendance.empty:
            new_record = pd.DataFrame({
                'Name': [name],
                'Date': [date_str], 
                'Time': [time_str]
            })
            df = pd.concat([df, new_record], ignore_index=True)
            df.to_csv(self.attendance_file, index=False)
            return True, f"Kehadiran {name} tercatat"
        else:
            return False, f"{name} sudah absen hari ini"

# Initialize system
attendance_system = WebAttendanceSystem()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/attendance')
def attendance():
    return render_template('attendance.html')

@app.route('/camera-test')
def camera_test():
    return render_template('camera_test.html')

@app.route('/api/register_face', methods=['POST'])
def register_face():
    try:
        data = request.get_json()
        name = data['name']
        image_data = data['image']
        
        # Decode base64 image
        image_data = image_data.split(',')[1]
        image_bytes = base64.b64decode(image_data)
        nparr = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # Save image
        filename = f"faces/{name}.jpg"
        cv2.imwrite(filename, image)
        
        # Reload known faces
        attendance_system.load_known_faces()
        
        return jsonify({'success': True, 'message': f'Wajah {name} berhasil didaftarkan'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/api/recognize_face', methods=['POST'])
def recognize_face():
    try:
        data = request.get_json()
        image_data = data['image']
        
        # Decode base64 image
        image_data = image_data.split(',')[1]
        image_bytes = base64.b64decode(image_data)
        nparr = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # Detect face
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = attendance_system.face_cascade.detectMultiScale(gray, 1.1, 4)
        
        if len(faces) > 0:
            x, y, w, h = faces[0]
            face_crop = image[y:y+h, x:x+w]
            
            name, confidence = attendance_system.recognize_face(face_crop)
            
            if name:
                success, message = attendance_system.mark_attendance(name)
                return jsonify({
                    'success': True,
                    'name': name,
                    'confidence': f"{confidence:.2f}",
                    'attendance_marked': success,
                    'message': message
                })
            else:
                return jsonify({'success': False, 'message': 'Wajah tidak dikenali'})
        else:
            return jsonify({'success': False, 'message': 'Tidak ada wajah terdeteksi'})
            
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/api/attendance_data')
def get_attendance_data():
    try:
        if os.path.exists(attendance_system.attendance_file):
            df = pd.read_csv(attendance_system.attendance_file)
            
            # Get today's attendance
            today = datetime.now().strftime("%Y-%m-%d")
            today_df = df[df['Date'] == today]
            
            return jsonify({
                'success': True,
                'all_attendance': df.to_dict('records'),
                'today_attendance': today_df.to_dict('records'),
                'total_today': len(today_df)
            })
        else:
            return jsonify({
                'success': True,
                'all_attendance': [],
                'today_attendance': [],
                'total_today': 0
            })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)