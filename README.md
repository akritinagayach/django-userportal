# Django User Signup/Login System

A Django web application that supports user registration, login, logout, and personalized dashboards for Patients and Doctors with profile pictures and styled UI.

## ✨ Features

- User signup with custom fields (name, email, user type, address, profile picture)
- Secure login/logout functionality
- Custom user model with extended fields
- Separate dashboards for Doctor and Patient roles
- Profile picture upload and display
- Responsive and styled UI with centered forms and buttons

## 📂 Folder Structure

```
userportal/
├── accounts/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── templates/accounts/
│       ├── login.html
│       ├── signup.html
│       ├── doctor_dashboard.html
│       └── patient_dashboard.html
├── userportal/
│   ├── settings.py
│   ├── urls.py
├── db.sqlite3
└── manage.py
```

## ⚙️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/akritinagayach/django-userportal.git
   cd django-userportal
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install django
   ```

4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Visit `http://127.0.0.1:8000/` to access the app.

## 🔐 Admin Panel

Access at: `http://127.0.0.1:8000/admin`  
Use superuser credentials to log in.

## 📸 Media Files

Uploaded profile pictures are stored in the `media/profile_pics/` directory. Make sure to include this in `.gitignore` and configure media settings in `settings.py`.

## 📄 License

This project is licensed under the MIT License.
