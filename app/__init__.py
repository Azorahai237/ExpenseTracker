from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.app_context().push()

app.config.from_object('config')
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app import views, models
