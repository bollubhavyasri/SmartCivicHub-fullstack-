# 🌍 SmartCivic Hub

SmartCivic Hub is a Django-based Smart Complaint & Issue Management System developed to improve communication between users and organizations. The platform allows users to register, log in, submit complaints with image proof, and track complaint status, while administrators can efficiently manage and resolve issues through a dedicated dashboard.

---

# 🚀 Features

## 👤 User Features
- User Registration & Login
- Secure Authentication
- Submit Complaints
- Upload Image Proof
- Track Complaint Status
- Organization-based Complaint Submission

---

## 🛠️ Admin Features
- Admin Dashboard
- View Organization Complaints
- Update Complaint Status
- Manage Complaint Data
- Role-Based Access Control

---

# 🏢 Supported Organizations

The system supports multiple organizations such as:

- Municipality
- College
- School
- Company
- Apartment Association
- Sanitation Department
- Road & Transport Department

---

# 🧠 Technologies Used

## Frontend
- HTML
- CSS
- JavaScript

## Backend
- Python
- Django Framework

## Database
- SQLite

---

# 📂 Project Structure

```bash
smartmanagement/
│
├── complaint/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── smartmanagement/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── media/
├── manage.py
└── README.md
```

---

# ⚙️ Installation Steps

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/SmartCivicHub.git
```

---

## 2️⃣ Move into Project Folder

```bash
cd SmartCivicHub
```

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv test
```

---

## 4️⃣ Activate Virtual Environment

### Windows
```bash
test\Scripts\activate
```

---

## 5️⃣ Install Dependencies

```bash
pip install django pillow
```

---

## 6️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 7️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

---

## 8️⃣ Run Server

```bash
python manage.py runserver
```

---

# 🌐 Open in Browser

```bash
http://127.0.0.1:8000/
```

---

# 🔐 Role-Based Access

## Admin
- Access dashboard
- View organization complaints
- Manage complaint status

## User
- Submit complaints
- Upload proofs
- Track complaint progress

---

# 💾 Database Handling

The project uses SQLite database for storing:

- User Details
- Organizations
- Complaints
- Complaint Status
- Uploaded Image Paths

---

# 🔄 Frontend & Backend Communication

The frontend communicates with the Django backend using HTTP requests and forms.

- HTML forms send user data
- Django views process requests
- Models store data in database
- Templates display dynamic content

---

# 🎯 Project Objective

The main goal of SmartCivic Hub is to provide a centralized, transparent, and secure platform for complaint management across multiple organizations.

---

# 🚀 Future Scope

- Email/SMS Notifications
- AI-based Complaint Categorization
- Complaint Analytics Dashboard
- Mobile Application
- GPS-based Complaint Tracking
- Multi-language Support

---

# 👨‍💻 Developed By

Bhavya Sri

---

# 📜 License

This project is developed for educational and academic purposes.
