🚀 Project Echo – Local Setup Guide

This guide explains how to clone the repository and run both frontend and backend servers locally.

1️⃣ Prerequisites
Make sure the following are installed on your system:

🔹 Git
🔹 Node.js (v16 or later)
🔹 Python (v3.8 or later)
🔹 npm (comes with Node)
🔹 PostgreSQL (optional for now; SQLite works by default)

Verify:

git --version
node --version
python --version

2️⃣ Clone the Repository
git clone https://github.com/Kavya-p78/Echo.git
cd Echo
By default, you will be on the develop branch.
If not:
git checkout develop

3️⃣ Backend Setup (Django)
Step 1: Create and Activate Virtual Environment
cd backend
python -m venv venv

Activate virtual environment:
🔹 Windows (PowerShell):
    venv\Scripts\Activate
🔹 macOS / Linux:
    source venv/bin/activate
You should see (venv) in your terminal.

Step 2: Install Backend Dependencies
pip install -r requirements.txt

Step 3: Run Database Migrations
python manage.py migrate

Step 4: Start Backend Server
python manage.py runserver

Backend will be available at:

http://127.0.0.1:8000/

4️⃣ Frontend Setup (React)
Open a new terminal window (keep backend running).

cd frontend
npm install
npm start

Frontend will be available at:

http://localhost:3000/

5️⃣ Running the Project
At this point:

🔹 Backend server → running on port 8000
🔹 Frontend server → running on port 3000

Both must be running simultaneously during development.

6️⃣ Common Issues & Fixes
🔹 Virtual environment activation blocked (Windows)

Run once:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

🔹 Port already in use

Stop other services or change port:

python manage.py runserver 8001

🔹 Node modules missing

Always run: npm install
