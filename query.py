from app import db, models

print(db.session.query(models.income).all())


