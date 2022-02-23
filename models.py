from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)
class UserData(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    username = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(200),nullable=False)
    message = db.Column(db.Text(),nullable=False)