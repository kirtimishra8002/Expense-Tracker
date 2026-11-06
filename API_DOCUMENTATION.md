# Expense Tracker API Documentation

## 1. Get Expenses by Date

**Method:** GET  
**Endpoint:** `/api/expenses`

### Query Parameter

| Parameter | Required | Format | Description |
|---|---|---|---|
| `date` | Yes | YYYY-MM-DD | Date selected on the calendar |

### Example Request
`GET /api/expenses?date=2026-11-06`

### Successful Response — HTTP 200
```json
[
  {
    "id": 1,
    "date": "2026-11-06",
    "amount": 250.0,
    "category": "Food",
    "description": "Lunch",
    "title": "Lunch"
  }
]
```

---

## 2. Add New Expense

**Method:** POST  
**Endpoint:** `/api/expenses`

### Request Body (JSON)
```json
{
  "title": "Groceries",
  "amount": 45.50,
  "category": "Groceries",
  "date": "2026-11-06"
}
```

### Successful Response — HTTP 201
```json
{
  "id": 2,
  "title": "Groceries",
  "description": "Groceries",
  "amount": 45.50,
  "category": "Groceries",
  "date": "2026-11-06"
}
```

---

## 3. Modify (Update) Expense

**Method:** POST or PUT  
**Endpoint:** `/api/expenses/<expense_id>`

### Request Body (JSON)
```json
{
  "title": "Supermarket Groceries",
  "amount": 52.00,
  "category": "Groceries",
  "date": "2026-11-06"
}
```

### Successful Response — HTTP 200
```json
{
  "id": 2,
  "title": "Supermarket Groceries",
  "description": "Supermarket Groceries",
  "amount": 52.00,
  "category": "Groceries",
  "date": "2026-11-06"
}
```

---

## 4. Delete Expense

**Method:** POST or DELETE  
**Endpoint:** `/api/expenses/<expense_id>/delete`

### Successful Response — HTTP 200
```json
{
  "id": 2,
  "message": "Expense deleted successfully"
}
```

---

## 5. Get Monthly Summary (Calendar Indicators)

**Method:** GET  
**Endpoint:** `/api/month-summary`

### Query Parameters

| Parameter | Required | Format | Description |
|---|---|---|---|
| `year` | Yes | Integer (e.g. 2026) | Year to inspect |
| `month` | Yes | Integer (1-12) | Month number |

### Successful Response — HTTP 200
```json
{
  "year": 2026,
  "month": 11,
  "dates_with_expenses": ["2026-11-02", "2026-11-06"]
}
```
