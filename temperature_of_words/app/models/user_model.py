from app import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.String(64), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


    def __repr__(self):
        return f"User {self.id}"
