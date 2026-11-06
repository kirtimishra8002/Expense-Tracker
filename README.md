# Expense Tracker Dashboard 📊💰

A modern, full-stack personal expense tracking web application featuring a Google Calendar-inspired monthly interactive dashboard, categorized expense management, and complete CRUD functionality in Indian Rupees (₹).

---

## ✨ Features

- **Today's Overview**: Displays the aggregated total of expenses incurred today and itemized log.
- **Interactive Monthly Calendar (Google Calendar Style)**:
  - Browse any month and year with `<` and `>` navigation controls and a `Today` quick jump button.
  - Active date highlighting and indicator dots on dates that have recorded expenses.
  - Click any day cell on the calendar to dynamically inspect that date's expenses and total without page reloads.
- **Complete CRUD Operations**:
  - **Add**: Record new expenses with Description, Amount (₹), Category, and Date.
  - **Modify (Edit)**: Update any logged expense via an interactive modal dialog.
  - **Delete**: Easily remove expenses with dynamic recalculation of totals and calendar dots.
- **Categorization**: Group expenses into *Food & Dining*, *Groceries*, *Transport*, *Utilities & Bills*, *Entertainment*, *Health*, or *General*.
- **Zero-Setup Static Preview**: Includes `preview.html` with persistent `localStorage` support for instant browser previewing without requiring Python.
- **Full-Stack REST Backend**: Powered by Python, Flask, SQLite, and SQLAlchemy.

---

## 📁 Project Structure

```text
Expense-Tracker-main/
│
├── static/
│   └── style.css            # Custom CSS styling and responsive layout
│
├── templates/
│   └── index.html           # Jinja2 Flask template with interactive calendar
│
├── app.py                   # Flask backend application and REST endpoints
├── preview.html             # Standalone instant browser preview (localStorage)
├── API_DOCUMENTATION.md     # Detailed REST API specification
├── .gitignore               # Ignored environments, databases, and cache
└── README.md                # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+ (or Python 3.14 / `uv`)
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/<YOUR_USERNAME>/<YOUR_REPO_NAME>.git
cd Expense-Tracker-main
```

### 2. Set Up Virtual Environment & Dependencies
```bash
# Using standard venv:
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\activate

# Install Flask and SQLAlchemy:
pip install flask flask-sqlalchemy
```

### 3. Run the Application
```bash
python app.py
```
Open your browser and navigate to:
👉 **`http://127.0.0.1:5000`**

---

## 🌐 Instant Browser Preview (No Python Required)
You can double-click **`preview.html`** in your file manager or open it with VS Code Live Server to test the UI, add expenses, edit amounts, and navigate the calendar immediately. Data persists in your browser's local storage.

---

## 📡 REST API Summary

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/expenses?date=YYYY-MM-DD` | Fetch expenses for a specific date |
| `POST` | `/api/expenses` | Create a new expense |
| `POST`/`PUT` | `/api/expenses/<id>` | Update an existing expense |
| `POST`/`DELETE` | `/api/expenses/<id>/delete` | Delete an expense |
| `GET` | `/api/month-summary?year=YYYY&month=MM` | Get dates in month that have expenses |

Refer to [API_DOCUMENTATION.md](API_DOCUMENTATION.md) for detailed JSON payloads and examples.

---

## 🛠️ Tech Stack
- **Frontend**: Semantic HTML5, Modern CSS3 (Grid & Flexbox), Vanilla JavaScript (ES6+)
- **Backend**: Python, Flask, Flask-SQLAlchemy, SQLite
- **Styling**: Google Calendar inspired UI, Custom Modals, Responsive Cards

