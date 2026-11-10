import routes
from datetime import date
from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import extract

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///expenses.db"
db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, default=date.today)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), default="General")
    description = db.Column(db.String(200), nullable=False)

    @property
    def title(self):
        return self.description

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.description,
            "description": self.description,
            "amount": self.amount,
            "category": self.category,
            "date": self.date.isoformat()
        }

@app.route("/", methods=["GET", "POST"])
def home():
    today = date.today()
    if request.method == "POST":
        try:
            exp = Expense(
                description=request.form["title"].strip(),
                amount=float(request.form["amount"]),
                category=request.form.get("category", "General"),
                date=date.fromisoformat(request.form.get("date") or today.isoformat())
            )
            db.session.add(exp)
            db.session.commit()
        except (KeyError, ValueError):
            pass
        return redirect(url_for("home"))

    sel_str = request.args.get("date", today.isoformat())
    try:
        sel_date = date.fromisoformat(sel_str)
    except ValueError:
        sel_date, sel_str = today, today.isoformat()

    todays = Expense.query.filter_by(date=today).all()
    selected = Expense.query.filter_by(date=sel_date).all()
    return render_template(
        "index.html",
        todays_expenses=todays,
        todays_total=sum(e.amount for e in todays),
        today_str=today.isoformat(),
        selected_expenses=selected,
        selected_total=sum(e.amount for e in selected),
        selected_date=sel_str
    )

@app.route("/api/expenses", methods=["GET", "POST"])
def api_expenses():
    if request.method == "POST":
        return routes.add_expense(db, Expense)

    d_str = request.args.get("date")
    if not d_str:
        return {"error": "Date required"}, 400

    try:
        items = Expense.query.filter_by(date=date.fromisoformat(d_str)).all()
        return jsonify([e.to_dict() for e in items])
    except ValueError:
        return {"error": "Invalid date format"}, 400
    
@app.route("/api/expenses/<int:id>", methods=["POST", "PUT"])
def update_expense(id):
    return routes.update_expense(db, Expense, id)


@app.route("/api/expenses/<int:id>/delete", methods=["POST", "DELETE"])
def delete_expense(id):
    return routes.delete_expense(db, Expense, id)

@app.route("/api/month-summary")
def month_summary():
    y, m = request.args.get("year", type=int), request.args.get("month", type=int)
    if not y or not m:
        return {"error": "Invalid year/month"}, 400
    items = Expense.query.filter(extract("year", Expense.date) == y, extract("month", Expense.date) == m).all()
    return {"dates_with_expenses": sorted({e.date.isoformat() for e in items})}

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
