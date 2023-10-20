from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import IncomeInputForm, ExpenseInputForm, GoalInputForm
from app.models import income, expense, goal

@app.route('/')
def index():
    return render_template('index.html', title = 'index')

@app.route('/Expense')
def Income():
    entries = expense.query.all()
    return render_template('Expense.html', title = 'Expenses', entries = entries)

@app.route("/AddExpense", methods=["POST", "GET"])
def add_expense():
    form = ExpenseInputForm()
    if form.validate_on_submit():
        entry = expense(name=form.name.data, category=form.category.data, amount=form.amount.data)
        db.session.add(entry)
        db.session.commit()
        flash("Expense entry saved", 'success')
        
    return render_template('AddExpense.html', title = 'add expense', form = form)

@app.route("/AddIncome", methods=["POST", "GET"])
def add_income():
    form = IncomeInputForm()
    if form.validate_on_submit():
        entry = income(name=form.name.data, category=form.category.data, amount=form.amount.data)
        db.session.add(entry)
        db.session.commit()
        flash("Income entry saved", 'success')
        
    return render_template('AddIncome.html', title = 'add income', form = form)


@app.route("/goal", methods=["POST", "GET"])
def add_goal():
    form = GoalInputForm()
    if form.validate_on_submit():
        entry = goal(name=form.name.data, amount=form.amount.data)
        db.session.add(entry)
        db.session.commit()
        flash("Goal entry saved", 'success')
        
    return render_template('goal.html', title = 'Goal', form = form)


@app.route("/DeleteExpense/<int:entry_id>")
def delete(entry_id):
    entry = expense.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash('Deletion was a success','success')