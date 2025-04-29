from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as orm
from app import db, login
from flask_login import UserMixin
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin

class User(UserMixin, db.Model):
    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    email: orm.Mapped[str] = orm.mapped_column(sa.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.id}, email {self.email}>'

class oAuth(OAuthConsumerMixin, db.Model):
    provider_user_id: orm.Mapped[str] = orm.mapped_column(sa.String(255), nullable=False, index=True)
    user_id: orm.Mapped[int] = orm.mapped_column(db.ForeignKey('user.id'), nullable=False)
    user: orm.Mapped[User] = orm.relationship('User', backref=db.backref('oauth', lazy=True))
    
    def __repr__(self):
        return f'<oAuth {self.provider_user_id}, user {self.user_id}>'

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))
    
class Unit(db.Model):
    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    name: orm.Mapped[str] = orm.mapped_column(sa.String(255), nullable=False, unique=True)

    def __repr__(self):
        return f'<Unit {self.name}>'
    
class Topic(db.Model):
    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    name: orm.Mapped[str] = orm.mapped_column(sa.String(255), nullable=False, unique=True)
    
    unit_id: orm.Mapped[int] = orm.mapped_column(db.ForeignKey('unit.id'), nullable=False)
    unit: orm.Mapped[Unit] = orm.relationship('Unit', backref=db.backref('topics', lazy=True))

    def __repr__(self):
        return f'<Topic {self.name}>'
    
class Question(db.Model):
    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    mi: orm.Mapped[str] = orm.mapped_column(sa.String(255), nullable=True)
    question_number: orm.Mapped[str] = orm.mapped_column(sa.String(255), nullable=False)
    sub_question: orm.Mapped[str] = orm.mapped_column(sa.String(255), nullable=True)
    subsub_question: orm.Mapped[str] = orm.mapped_column(sa.String(255), nullable=True)
    year: orm.Mapped[int] = orm.mapped_column(nullable=False)
    max_marks: orm.Mapped[int] = orm.mapped_column(nullable=False)
    section: orm.Mapped[str] = orm.mapped_column(sa.String(255), nullable=False)
    
    topic_id: orm.Mapped[int] = orm.mapped_column(db.ForeignKey('topic.id'), nullable=False)
    topic: orm.Mapped[Topic] = orm.relationship('Topic', backref=db.backref('questions', lazy=True))

    def __repr__(self):
        return f'<Question {self.question_number}, {self.year} Section {self.section}>'
    
class Attempt(db.Model):
    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    user_id: orm.Mapped[int] = orm.mapped_column(db.ForeignKey('user.id'), nullable=False)
    question_id: orm.Mapped[int] = orm.mapped_column(db.ForeignKey('question.id'), nullable=False)
    score: orm.Mapped[Optional[int]] = orm.mapped_column(sa.Integer, nullable=True)

    user: orm.Mapped[User] = orm.relationship('User', backref=db.backref('attempts', lazy=True))
    question: orm.Mapped[Question] = orm.relationship('Question', backref=db.backref('attempts', lazy=True))

    def __repr__(self):
        return f'<Attempt by User {self.user_id}, Question {self.question_id}>'