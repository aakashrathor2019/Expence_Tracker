from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# List to store expenses
expenses = []

# Home route to display expenses and summary
@app.route('/')
def home():
    total_expenses = sum(expense['amount'] for expense in expenses)
    return render_template('index.html', expenses=enumerate(expenses), total_expenses=total_expenses)

# Route to add new expense
@app.route('/add', methods=['POST'])
def add_expense():
    description = request.form['description']
    category = request.form['category']
    amount = float(request.form['amount'])
    date = datetime.today()
    expenses.append({'description': description, 'category': category, 'amount': amount, 'date': date})
    return redirect(url_for('home'))

# Route to delete expense
@app.route('/delete/<int:index>', methods=['POST'])
def delete_expense(index):
    if request.method == 'POST':
        del expenses[index]
        return redirect(url_for('home'))
    else:
        return "Method Not Allowed", 405


if __name__ == '__main__':
    app.run(debug=True, port=5003)
