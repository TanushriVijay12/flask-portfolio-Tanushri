from datetime import datetime
from app import db, login
from flask_login import UserMixin

project_tags = db.Table('project_tags',
    db.Column('project_id', db.Integer, db.ForeignKey('project.id')),
    db.Column('tag_id',     db.Integer, db.ForeignKey('tag.id'))
)

class User(UserMixin, db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

class Project(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(140), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_path  = db.Column(db.String(200))
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)
    tags        = db.relationship('Tag', secondary=project_tags, backref='projects')

class Tag(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
