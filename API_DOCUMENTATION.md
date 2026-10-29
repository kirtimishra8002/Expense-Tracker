
# Expense Tracker API Documentation

## 1. Get Expenses by Date

**Method:** GET

**Endpoint:** `/api/expenses`

### Query Parameter

| Parameter | Required | Format | Description |
|---|---|---|---|
| date | Yes | YYYY-MM-DD | Date selected on the calendar |

### Example Request

`GET /api/expenses?date=2026-10-29`

### Successful Response — HTTP 200

Returns a list of expenses for the selected date.

```json
[
  {
    "id": 1,
    "date": "2026-10-29",
    "amount": 250.0,
    "category": "Food",
    "description": "Lunch"
  }
]
```

### If No Expenses Exist

Status: HTTP 200

Response:

```json
[]
```

### Error Responses

**HTTP 400 — Missing date**

```json
{
  "error": "Please select a date"
}
```

**HTTP 400 — Invalid date format**

```json
{
  "error": "Invalid date format. Please use YYYY-MM-DD."
}
```

### Expense Fields

| Field | Type | Description |
|---|---|---|
| id | Integer | Unique expense ID |
| date | String | Expense date in YYYY-MM-DD format |
| amount | Number | Expense amount |
| category | String | Expense category |
| description | String | Expense description |
