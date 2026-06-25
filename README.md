# 🚀 Blog API

A production-ready RESTful Blog API built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **JWT Authentication**. This project provides secure user authentication and complete CRUD operations for blog posts. It is deployed on Render with a live PostgreSQL database.

---

## ✨ Features

* User Registration
* User Login with JWT Authentication
* Secure Password Hashing (bcrypt)
* Protected Routes
* User Profile Endpoint
* Create Blog Posts
* Get All Posts
* Get Single Post
* Update Own Posts
* Delete Own Posts
* Alembic Database Migrations
* Environment Variable Support
* Deployed on Render

---

## 🛠 Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* Pydantic
* JWT (python-jose)
* Passlib (bcrypt)
* Uvicorn
* Render
* Git & GitHub

---

## 📁 Project Structure

```
blog_api/
│
├── app/
│   ├── auth.py
│   ├── database.py
│   ├── main.py
│   ├── model.py
│   ├── routes/
│   ├── schemas.py
│   └── utils.py
│
├── alembic/
├── requirements.txt
├── alembic.ini
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/srirambalu-bot/blog_api.git

cd blog_api

python -m venv venv

source venv/bin/activate
# Windows
venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

## 🔐 Environment Variables

Create a `.env` file.

```
DATABASE_URL=your_database_url

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 📚 API Endpoints

### Authentication

* POST `/users`
* POST `/login`
* GET `/profile`

### Posts

* POST `/posts`
* GET `/posts`
* GET `/post/{id}`
* PUT `/post/{id}`
* DELETE `/post/{id}`

---

## 🌐 Live API

Render Deployment

https://blog-api-f7jy.onrender.com

Swagger Documentation

https://blog-api-f7jy.onrender.com/docs

---

## 🚀 Future Improvements

* React Frontend
* Docker Support
* Pagination
* Search & Filtering
* Unit Testing
* CI/CD Pipeline

---

## 👨‍💻 Author

Sriram
