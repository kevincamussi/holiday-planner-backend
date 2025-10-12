
## 📁 3. **Backend Repository – `holiday-planner-backend`**

# 🌴 Holiday Planner – Backend (FastAPI + MongoDB)

A powerful REST API built with **FastAPI**, **Python**, and **MongoDB** to manage employee holiday schedules.

---

## 📚 API Documentation

Swagger UI:  
👉 [https://holiday-planner-backend-rht3.onrender.com/docs](https://holiday-planner-backend-rht3.onrender.com/docs)

---

## 🛠️ Tech Stack

- FastAPI (Python)
- Pydantic
- MongoDB (Motor driver)
- JWT Authentication
- Python Dotenv
- Docker

---

## 📦 Features

✅ CRUD endpoints for holidays  
✅ Autocomplete for employee name and department  
✅ JWT-based authentication system  
✅ MongoDB for persistent storage  
✅ Automatic schema validation with Pydantic

---

## ⚙️ Environment Setup

Create a `.env` file in the project root:

.env file:  

SECRET_KEY="5a3e4d2f7e8c9a1b6d0e3f2c4a8b7d9f1234567890abcdef1234567890abcdef"  
MONGO_URL=mongodb://localhost:27017/holiday_planner   
ALGORITHM=HS256   
ACCESS_TOKEN_EXPIRE_MINUTES=60  
DB_NAME=holiday_planner  
FRONTEND_URL=http://localhost:5173  


⚠️ Important: MongoDB must be installed and running locally on port 27017.
If it doesn’t exist, the holiday_planner database will be created automatically.

📥 Download MongoDB[https://www.mongodb.com/try/download/community]

🧪 Run Locally
git clone https://github.com/kevincamussi/holiday-planner-backend.git

It is strongly recommended to use a virtual environment when working with Python projects.
This keeps the project’s dependencies isolated from your global Python installation.

📦 1. Create the virtual environment

cd holiday-planner-backend

python -m venv venv

This will create a new folder called venv/ with the isolated Python environment.

▶️ 2. Activate the virtual environment

venv\Scripts\Activate

After activation, you’ll see (venv) before your terminal prompt, meaning the environment is active.

📥 3. Install dependencies

With the virtual environment active, install the project’s dependencies:

pip install -r requirements.txt

▶️ 4. Run the backend

uvicorn app.main:app --reload

Backend will run on:  
👉 http://localhost:8000  


📜 License  

This project is for educational and portfolio purposes.
