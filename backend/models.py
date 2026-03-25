from database import db
from datetime import datetime
from constants import TITLE_MAX_LENGTH, DESCRIPTION_MAX_LENGTH, PRIORITY_MIN, PRIORITY_MAX

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(TITLE_MAX_LENGTH), nullable=False)
    description = db.Column(db.String(DESCRIPTION_MAX_LENGTH), nullable=True)
    deadline = db.Column(db.String(50), nullable=True)
    priority = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)