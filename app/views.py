from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import IncomeInputForm, ExpenseInputForm, GoalInputForm, EditIncomeForm, EditExpenseForm, EditGoalForm
from app.models import income, expense, goal

@app.route('/')
def index():
    return render_template('index.html', title = 'index')

@app.route('/Expense')
def Expense():
    # check if any entries exist in the current table
    if (expense.query.first() == None):
        entries = []
    else:
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

@app.route('/DeleteExpense/<int:entry_id>')
def DeleteExpense(entry_id):
    entry = expense.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash('Deletion was a success','success')
    return redirect(url_for("Expense"))

@app.route('/EditExpense/<int:entry_id>', methods=["POST", "GET"])
def EditExpense(entry_id):
    entry = expense.query.get_or_404(int(entry_id))
    form = EditExpenseForm()
    # checking if form is empty, else save new values
    if form.validate_on_submit():
        if form.name.data != '' :
            entry.name = form.name.data
        if form.category.data != '':
            entry.category = form.category.data
        
        if form.amount.data is not None:
            entry.amount = form.amount.data
    # try:
    #     flash('Edit was a success','success')
    # except Exception as e:
    #     flash("ERROR", 'error')    
    db.session.commit()
    return render_template('EditExpense.html', title = 'edit expense', form = form)
    

@app.route('/Income')
def Income():
    # check if any entries exist in the current table
    if (income.query.first() == None):
        entries = []
    else:
        entries = income.query.all()
    return render_template('Income.html', title = 'Income', entries = entries)

@app.route("/AddIncome", methods=["POST", "GET"])
def add_income():
    form = IncomeInputForm()
    if form.validate_on_submit():
        entry = income(name=form.name.data, category=form.category.data, amount=form.amount.data)
        db.session.add(entry)
        db.session.commit()
        flash("Income entry saved", 'success')
        
    return render_template('AddIncome.html', title = 'add income', form = form)

@app.route('/DeleteIncome/<int:entry_id>')
def DeleteIncome(entry_id):
    entry = income.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash('Deletion was a success','success')
    return redirect(url_for("Income"))


@app.route('/EditIncome/<int:entry_id>', methods=["POST", "GET"])
def EditIncome(entry_id):
    entry = income.query.get_or_404(int(entry_id))
    form = EditIncomeForm()
    # checking if form is empty, else save new values
    if form.validate_on_submit():
        if form.name.data != '' :
            entry.name = form.name.data
        if form.category.data != '':
            entry.category = form.category.data
        
        if form.amount.data is not None:
            entry.amount = form.amount.data
    # try:
    #     flash('Edit was a success','success')
    # except Exception as e:
    #     flash("ERROR", 'error')    
    db.session.commit()
    return render_template('EditIncome.html', title = 'edit income', form = form)



@app.route("/goal", methods=["POST", "GET"])
def Goal():
    #checking if a goal exists
    if (goal.query.first() == None):

        input_form = GoalInputForm()
        if input_form.validate_on_submit():
            new_entry = goal(name=input_form.name.data, amount=input_form.amount.data)
            db.session.add(new_entry)
            db.session.commit()
            flash("Goal entry saved", 'success')
            
        return render_template('goal.html', title = 'Goal', form = input_form)
    else:
        output_form = EditGoalForm()
        entry = goal.query.first()
        if output_form.validate_on_submit():
            if output_form.name.data != '':
                entry.name = output_form.name.data
            if output_form.amount.data is not None:
                entry.amount = output_form.amount.data
        db.session.commit()
        flash("Goal entry edited","success")
        return render_template('EditGoal.html', title = 'Edit Goal', form = output_form)
            

                



