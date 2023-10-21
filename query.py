from app import db, models

entry = models.expense.query.get(1)
print(entry.name)


