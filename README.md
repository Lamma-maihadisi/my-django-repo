# 🍋 Little Lemon Restaurant API

Welcome to the **Little Lemon Restaurant API**, a Django REST Framework (DRF)-powered backend system for managing restaurant menu items and bookings. This project supports listing, creating, updating, and deleting menu items, as well as secure booking management for authenticated users.

---

## 🚀 Features

- 🧾 **Menu Management**  
  - View all menu items  
  - Add, update, or delete individual menu entries

- 📅 **Booking System**  
  - Authenticated users can manage restaurant bookings  
  - Create, retrieve, update, and delete bookings

- 🔐 **Authentication**  
  - Bookings are only accessible to authenticated users

- 🖥️ **Frontend Index Page**  
  - Simple landing page at `/` rendered via Django template

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **Django**
- **Django REST Framework**
- **SQLite3** (default, replaceable with PostgreSQL/MySQL)
- **JWT / Session Authentication** (based on configuration)

---

## 📂 Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page |
| `/api/menu/` | GET, POST | List or create menu items |
| `/api/menu/<id>/` | GET, PUT, PATCH, DELETE | Retrieve, update, or delete a specific menu item |
| `/api/bookings/` | GET, POST | List or create bookings (Auth required) |
| `/api/bookings/<id>/` | GET, PUT, DELETE | Manage individual bookings (Auth required) |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Lamma-maihadisi/littlelemon-restaurant.git
cd littlelemon-restaurant


### 2. Create Virtual Environment

python -m venv env
source env/bin/activate   # On Windows use: env\Scripts\activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Run Migrations

python manage.py migrate

### 5. Start Development Server

python manage.py runserver

