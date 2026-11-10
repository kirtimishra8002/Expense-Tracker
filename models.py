from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy instance
db = SQLAlchemy()

# Model matching Person 1's exact column specifications
class Expense(db.Model):
    __tablename__ = 'expense'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        """Formats model fields to JSON response dictionary."""
        return {
            "id": self.id,
            "date": self.date.strftime("%Y-%m-%d") if self.date else None,
            "amount": self.amount,
            "category": self.category,
            "description": self.description
        }