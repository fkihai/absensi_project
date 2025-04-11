# 🕒 Django DRF Attendance API

A backend API for Employee Attendance System built with Django REST Framework (DRF) and JWT Authentication. This project supports employee check-in, check-out, and monthly attendance recap features.

## 🔧 Tech Stack

- **Python 3.10+**
- **Django 4.x**
- **Django REST Framework**
- **Simple JWT (`djangorestframework-simplejwt`)**
- **PostgreSQL / SQLite (configurable)**
- **Docker (optional)**
- **JWT Authentication**

---

## 🚀 Main Features

- ✅ User registration and login using JWT
- ✅ Attendance check-in and check-out
- ✅ Monthly attendance report per employee
- ✅ Token validation middleware
- ✅ Clean and scalable project structure

---

## 📦 Local Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/attendance-api.git
cd attendance-api
```

````

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # on Windows use `venv\Scripts\activate`
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run Development Server

```bash
python manage.py runserver
```

---

## 🔑 Authentication

This project uses **JWT (JSON Web Token)** for authentication.

- Obtain token:

  ```
  POST /api/token/
  ```

  Body:

  ```json
  {
    "email": "your_email",
    "password": "your_password"
  }
  ```

- Refresh token:
  ```
  POST /api/token/refresh/
  ```

Include the token in the `Authorization` header for protected endpoints:

```
Authorization: Bearer your_token
```

---

## 📁 API Endpoints Overview

| Method | Endpoint              | Description        |
| ------ | --------------------- | ------------------ |
| POST   | `/api/register/`      | Register new user  |
| POST   | `/api/token/`         | Get JWT token      |
| POST   | `/api/token/refresh/` | Refresh JWT token  |
| POST   | `/api/absen/in/`      | Check-in           |
| PATCH  | `/api/absen/out/`     | Check-out          |
| GET    | `/api/absen/rekap/`   | Get monthly report |

---

## 🧪 Testing (optional)

To run unit tests:

```bash
python manage.py test
```

---

## 📌 Project Structure

```
absensi_project/
├── account/              # Auth & user management
├── absensi/              # Attendance app
├── apps/                 # Settings & utilities
├── requirements.txt
├── manage.py
```

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed by [Fikri Haikal](https://github.com/fkihai)
````
