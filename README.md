# 📝 To-Do List Application

A fully functional **To-Do List Web Application** built with Django.  
The app allows users to manage tasks with deadlines, tags, and completion status using a clean and maintainable Django architecture.

---

## 🚀 Features

- ✅ Create, update, delete tasks
- ✅ Mark tasks as completed / uncompleted
- ✅ Add deadlines to tasks
- ✅ Assign multiple tags to tasks
- ✅ Manage tags (create, update, delete)
- ✅ Clean and user-friendly UI with form validation and helpful hints
- ✅ Organized codebase using Django Class-Based Views (CBV)

---

## 🛠️ Tech Stack

- ⚙️ **Backend Framework:** Django 4.x (Python 3.10+)
- 🗄️ **Database:** SQLite (default), PostgreSQL-ready
- 🧮 **ORM:** Django ORM
- 🎨 **Frontend:** HTML (Django Templates), Bootstrap *(optional)*
- 📝 **Forms:** Django ModelForms
- 🔄 **Version Control:** Git, GitHub

---

## 🔧 Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Yurkiv313/todo-list-app.git
cd todo-list-app
```

### 2️⃣ Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply migrations

```bash
python manage.py migrate
```

### 5️⃣ Run development server

```bash
python manage.py runserver
```
