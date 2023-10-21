from app import models, db
#calculating total of income
def Income_Total():
    total = 0.0
    for entries in models.income.query.all():
        total += entries.amount
    return total

def Income_Max():

    Highest_Entry = models.income.query.first()   
    for entry in models.income.query.all():
        if entry.amount > Highest_Entry.amount:
            Highest_Entry = entry
    return Highest_Entry

            


def Expense_Total():
    total = 0.0
    for entries in models.expense.query.all():
        total += entries.amount
    return total

def Expense_Max():

    Highest_Entry = models.expense.query.first()   
    for entry in models.expense.query.all():
        if entry.amount > Highest_Entry.amount:
            Highest_Entry = entry
    return Highest_Entry

