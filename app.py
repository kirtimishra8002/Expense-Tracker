from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///expenses.db"
db = SQLAlchemy(app)

class Expense(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    date=db.Column(db.Date,nullable=False,default=date.today)
    amount=db.Column(db.Float,nullable=False)
    category=db.Column(db.String(50),nullable=False)
    description = db.Column(db.String(200), nullable=False)

@app.route("/")
def home():
    return "Expense Tracker Backend is Running!"

@app.route("/api/expenses")
def get_expenses():
    selected_date=request.args.get("date")
    if not selected_date:
        return {"error":"Please select a date"},400

    try:
        selected_date=date.fromisoformat(selected_date)
    except ValueError:
        return {"error":"Invalid date format. Please use YYYY-MM-DD."},400
    expenses=Expense.query.filter_by(date=selected_date).all()

    return [
        {
            "id":expense.id,
            "date":expense.date.isoformat(),
            "amount":expense.amount,
            "category":expense.category,
            "description":expense.description
        }
        for expense in expenses
    ]
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
