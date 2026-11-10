
from datetime import datetime
from flask import request, jsonify


# Input Validation
def validate_expense_input(data, is_update=False):
    errors = []

    if not is_update:
        for field in ['amount', 'category', 'date']:
            if field not in data or data[field] is None or str(data[field]).strip() == "":
                errors.append(f"Field '{field}' is required.")

    if 'amount' in data and data['amount'] is not None:
        try:
            val = float(data['amount'])
            if val <= 0:
                errors.append("Amount must be a positive number greater than 0.")
        except (ValueError, TypeError):
            errors.append("Amount must be a valid number.")

    if 'date' in data and data['date'] is not None:
        try:
            datetime.strptime(data['date'], "%Y-%m-%d")
        except (ValueError, TypeError):
            errors.append("Date must be in YYYY-MM-DD format.")

    return errors


# Add Expense
def add_expense(db, Expense):
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON payload required"}), 400

    errors = validate_expense_input(data)
    if errors:
        return jsonify({"errors": errors}), 400

    try:
        new_expense = Expense(
            amount=float(data['amount']),
            category=data['category'].strip(),
            date=datetime.strptime(data['date'], "%Y-%m-%d").date(),
            description=data.get('description', '').strip()
        )

        db.session.add(new_expense)
        db.session.commit()

        return jsonify({
            "message": "Expense created successfully!",
            "expense": new_expense.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Database error", "details": str(e)}), 500


# Update Expense
def update_expense(db, Expense, expense_id):
    expense = Expense.query.get(expense_id)

    if not expense:
        return jsonify({"error": f"Expense with ID {expense_id} not found."}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON payload required"}), 400

    errors = validate_expense_input(data, is_update=True)
    if errors:
        return jsonify({"errors": errors}), 400

    try:
        if 'amount' in data:
            expense.amount = float(data['amount'])
        if 'category' in data:
            expense.category = data['category'].strip()
        if 'date' in data:
            expense.date = datetime.strptime(data['date'], "%Y-%m-%d").date()
        if "title" in data or 'description' in data:
            expense.description = (data.get('title') or data.get('description')).strip()

        db.session.commit()

        return jsonify({
            "message": "Expense updated successfully!",
            "expense": expense.to_dict()
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Database update failed", "details": str(e)}), 500


# Delete Expense
def delete_expense(db, Expense, expense_id):
    expense = Expense.query.get(expense_id)

    if not expense:
        return jsonify({"error": f"Expense with ID {expense_id} not found."}), 404

    try:
        db.session.delete(expense)
        db.session.commit()

        return jsonify({"message": f"Expense ID {expense_id} deleted successfully."}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Database deletion failed", "details": str(e)}), 500
