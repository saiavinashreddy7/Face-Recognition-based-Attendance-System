# 👨‍🏫 Face Recognition Based Attendance System

An **automated attendance management system** that uses **face recognition** to mark attendance in real-time.  
Built using **Python**, **OpenCV**, and **Tkinter**, this project detects and recognizes student faces from live camera input and stores attendance data in a CSV file.

---

## ✨ Features
- 🧠 Face detection and recognition using **OpenCV Haarcascade**  
- 📸 Real-time camera feed integration  
- 💾 Attendance stored automatically in `attendance.csv`  
- 👨‍💻 GUI interface for admin and students  
- 🧰 Training module to register new faces  
- 📊 Easy to view and manage attendance records  

---

## 🧰 Tech Stack
- **Python 3.x**  
- **OpenCV**  
- **NumPy**  
- **Pandas**  
- **Tkinter (GUI)**  
- **Haarcascade Classifier**

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/saiavinashreddy7/Face-Recognition-based-Attendance-System.git
   Install dependencies:
pip install opencv-python numpy pandas

Run the main program:
python main.py

🧩 Working Modules
Module	Description
train.py	Train the face recognition model on student images
face_recognizer.py	Recognizes faces and marks attendance
attendance.py	Handles attendance logging
student.py	Student registration and management
login.py	Simple login interface
main.py	Main application launcher
🧠 How It Works

The system captures a live video stream from the webcam.

It detects faces using Haar Cascade Classifier.

Each detected face is compared against the trained dataset.

If a match is found, attendance is recorded in attendance.csv with date and time.
