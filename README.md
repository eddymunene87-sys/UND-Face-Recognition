# Face Recognition System

A professional desktop Face Recognition System built with **Python**, **CustomTkinter**, **OpenCV**, and **Face Recognition**. The application provides an intuitive graphical interface for registering people, generating facial encodings, and recognizing faces in real time.

---

## Features

### Face Registration
- Register new users through the GUI.
- Automatic face detection.
- Crops and saves only the detected face.
- Rejects blurry images.
- Rejects images with poor lighting.
- Rejects images containing multiple faces.
- Guides users through multiple face poses.
- Progress bar during registration.
- Automatic dataset organization.

### Face Encoding
- Automatically generates facial encodings after registration.
- Creates average encodings for improved accuracy.
- Filters out poor-quality images.
- Stores encodings in a serialized file.
- Fast loading during recognition.

### Face Recognition
- Real-time face recognition.
- Embedded camera preview in the GUI.
- Confidence percentage display.
- Unknown face detection.
- Face tracking for improved performance.
- FPS counter.
- Face counter.
- Configurable recognition threshold.

### Graphical User Interface
- Modern CustomTkinter interface.
- Dark theme.
- Sidebar navigation.
- Dashboard.
- Registration page.
- Recognition page.
- History page.
- Settings page.
- Responsive layout.
- Status bar.
- Header section.

### Quality Improvements
- Image quality validation.
- Blur detection.
- Lighting validation.
- Minimum face size validation.
- Average face encodings.
- Duplicate frame prevention.
- Multiple pose capture.

---

# Project Structure

```
FaceRecognition/
│
├── main.py
├── config.py
│
├── dataset/
│
├── encodings/
│   └── encodings.pkl
│
├── database/
│
├── gui/
│   ├── app.py
│   ├── header.py
│   ├── sidebar.py
│   ├── statusbar.py
│   │
│   └── pages/
│       ├── base_page.py
│       ├── dashboard.py
│       ├── register_page.py
│       ├── recognition_page.py
│       ├── history_page.py
│       └── settings_page.py
│
├── utils/
│   ├── camera.py
│   ├── config.py
│   ├── encoder.py
│   ├── face_detector.py
│   ├── face_tracker.py
│   ├── image_quality.py
│   ├── pose_detector.py
│   ├── recognizer.py
│   └── register.py
│
├── requirements.txt
│
└── README.md
```

---

# Technologies Used

- Python 3.11+
- OpenCV
- face_recognition
- dlib
- NumPy
- Pillow
- CustomTkinter
- Pickle

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/yourusername/FaceRecognition.git

cd FaceRecognition
```

---

## 2. Create a virtual environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the application

```bash
python main.py
```

---

# Requirements

Example `requirements.txt`

```
customtkinter
opencv-python
face_recognition
numpy
Pillow
```

---

# Registering a Person

1. Open the application.
2. Click **Register Person**.
3. Enter the person's name.
4. Click **Start Registration**.
5. Look at the camera.
6. Follow the pose instructions.
7. Wait until registration completes.
8. Facial encodings are generated automatically.

---

# Recognizing a Face

1. Open the **Recognition** page.
2. Click **Start Recognition**.
3. Stand in front of the camera.
4. The system will:
   - Detect your face
   - Track your movement
   - Recognize you
   - Display your name
   - Display confidence percentage

---

# Dataset Structure

```
dataset/

John/

    1.jpg

    2.jpg

    3.jpg

Mary/

    1.jpg

    2.jpg

    3.jpg
```

---

# Encoding Process

The encoder:

- Loads every registered image.
- Rejects poor-quality images.
- Generates facial encodings.
- Removes invalid images.
- Computes the average encoding for each person.
- Saves the result to:

```
encodings/encodings.pkl
```

---

# Recognition Pipeline

```
Camera

↓

Face Detection

↓

Face Tracking

↓

Face Encoding

↓

Encoding Comparison

↓

Confidence Calculation

↓

Display Result
```

---

# Dashboard

The dashboard displays:

- Registered users
- Camera status
- Recognition status
- Today's recognitions
- Unknown faces detected
- Recent activity

---

# Future Improvements

- SQLite database integration
- Recognition history
- Attendance system
- User authentication
- Face anti-spoofing
- Liveness detection
- MediaPipe Face Mesh
- Email notifications
- Face mask detection
- Multi-camera support
- REST API
- Cloud synchronization
- PDF report generation
- User management
- Audit logs

---

# Performance Optimizations

- Average face encodings
- Image quality filtering
- Face tracking
- Duplicate frame prevention
- Frame resizing
- Configurable recognition threshold
- Optimized face comparisons

---

# Security Features

- Automatic quality validation
- Unknown face detection
- Duplicate registration prevention
- Image filtering
- Confidence threshold control
- Local encoding storage

---

# Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature/new-feature
```

3. Commit your changes.

```bash
git commit -m "Added new feature"
```

4. Push to GitHub.

```bash
git push origin feature/new-feature
```

5. Open a Pull Request.

---

# License

This project is licensed under the MIT License.

---

# Author

**Eddy Munene**

Computer Science Graduate

Python Developer

Full Stack Developer

AI & Computer Vision Enthusiast

---

# Acknowledgements

- OpenCV
- face_recognition
- dlib
- CustomTkinter
- NumPy
- Python Community

---

## Version

**Version:** 1.0.0

---

## Screenshots

Add screenshots of:

- Dashboard
- Registration Page
- Recognition Page
- History Page
- Settings Page

after completing the GUI.

---

## Contact

For questions, suggestions, or contributions, feel free to open an issue or contact the project maintainer.
