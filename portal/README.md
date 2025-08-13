# Student Portal LMS in Django

This is a Learning Management System (LMS) built with Django. It provides features for students, teachers, and administrators to manage courses, assignments, quizzes, and communication.

## Features
- User authentication and profiles
- Course management
- Assignment submission
- Quiz system
- Direct messaging
- Admin dashboard
- CKEditor integration for rich text editing

## Setup Instructions
1. **Clone the repository**
   ```
   git clone <repo-url>
   cd Student-Portal-LMS-in-Django-master
   ```
2. **Create and activate a virtual environment**
   ```
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```
4. **Apply migrations**
   ```
   python manage.py migrate
   ```
5. **Create a superuser**
   ```
   python manage.py createsuperuser
   ```
6. **Run the development server**
   ```
   python manage.py runserver
   ```

## Usage
- Access the admin panel at `/admin/`
- Register and log in as a user
- Enroll in courses, submit assignments, and take quizzes

## Folder Structure
- `assignment/` - Assignment management
- `authy/` - Authentication and user profiles
- `classroom/` - Classroom and course management
- `completion/` - Completion tracking
- `course/` - Course details and cart
- `direct/` - Direct messaging
- `lms/` - LMS core
- `module/` - Course modules
- `page/` - Static pages
- `question/` - Question bank
- `quiz/` - Quiz system
- `student_portal/` - Project settings and URLs

## Requirements
- Python 3.8+
- Django 3.2+
- Pillow
- django-ckeditor

