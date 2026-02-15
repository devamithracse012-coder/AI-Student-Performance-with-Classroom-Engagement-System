🎓 AI-Based Student Performance & Classroom Engagement System
An AI-powered web application that predicts academic performance and analyzes classroom engagement using Machine Learning and Computer Vision.

🚀 Project Overview
This system consists of two intelligent modules:
📊 Academic Score Prediction
📷 Classroom Engagement Detection
It helps educators monitor student performance and engagement using AI-driven insights.

🧠 Features
📊 1. Academic Performance Prediction
Input study hours
Input attendance percentage
Predict academic score (0–100%)
Dynamic performance indicator:
🟢 Green – Good Performance
🟡 Yellow – Needs Improvement
🔴 Red – Poor Performance
Animated circular progress UI

📷 2. Classroom Engagement Detection
Upload classroom/student image
Integrated with Azure Custom Vision
Detects:
Attentive
Distracted
Displays confidence percentage

Real-time API response handling
🎨 Frontend Highlights
✨ Glassmorphism UI
🎥 Transparent background video
🌙 Light / Dark theme toggle
📱 Responsive layout
🔄 Smooth animations
🛠️ Tech Stack
1.Frontend
HTML5
CSS3
JavaScript

2.Backend
Python
Flask
Flask-CORS

3.AI & Cloud
Azure Custom Vision
REST API Integration
📂 Project Structure
Copy code

Student-perf/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── backend/
│   ├── app.py
│   └── requirements.txt

⚙️ How to Run Locally
🔹 1. Clone the Repository
Bash
Copy code
git clone https://github.com/devamithraseo12-coder/AI-Student-Performance-with-Classroom-Engagement-System.git
cd AI-Student-Performance-with-Classroom-Engagement-System
🔹 2. Setup Backend
Bash
Copy code
cd backend
pip install -r requirements.txt
python app.py
Server runs at:
Copy code

http://127.0.0.1:5000
🔹 3. Open Frontend
Open:
Copy code

frontend/index.html
in your browser.

📈 Output Preview
Dynamic colored performance circle
Engagement result with confidence %
Smooth UI transitions

🌟 Future Improvements
Advanced ML model for score prediction
Teacher/Admin dashboard
Student analytics visualization
Azure Web App deployment
Database integration
📜 License
This project is developed for academic and learning purposes.
