from datetime import datetime
from pytweet.database import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(200),nullable=False)
    password = db.Column(db.String(200),nullable=False)
    created_at = db.Column(db.DateTime,nullable=False,default=datetime.now)
    updated_at = db.Column(db.DateTime,nullable=False,default=datetime.now,onupdate=datetime.now)
    name = db.Column(db.String(200),nullable=False)
    address = db.Column(db.String(200),nullable=False)
    contact_number = db.Column(db.String(200),nullable=False)

class Posts(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    title = db.Column(db.String(250),nullable=False)
    content= db.Column(db.String(250),nullable=False)
    likes = db.Column(db.String(250),nullable=False)
    created_at = db.Column(db.DateTime,nullable=False,default=datetime.now)
    updated_at = db.Column(db.DateTime,nullable=False,default=datetime.now,onupdate=datetime.now)

