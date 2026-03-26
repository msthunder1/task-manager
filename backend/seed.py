from app import app
from database import db
from models import Task

tasks = [
    Task(title="Buy groceries", description="Milk, eggs, bread, butter", deadline="2026-04-01", priority=2),
    Task(title="Fix login bug", description="Users are getting 401 on refresh token", deadline="2026-03-28", priority=9),
    Task(title="Write unit tests", description="Cover the auth and payment modules", deadline="2026-04-10", priority=7),
    Task(title="Team meeting", description="Discuss Q2 roadmap with the team", deadline="2026-03-27", priority=5),
    Task(title="Update README", description="Add setup instructions and API docs", deadline="2026-04-05", priority=3),
]

with app.app_context():
    db.session.add_all(tasks)
    db.session.commit()
    print("Database seeded!")