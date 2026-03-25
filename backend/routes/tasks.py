from flask import Blueprint, request, jsonify
from database import db
from models import Task
from schemas import TaskSchema

tasks_bp = Blueprint('tasks', __name__)
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

# Get all tasks
@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify(tasks_schema.dump(tasks)), 200

# Get single task
@tasks_bp.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get_or_404(id)
    return jsonify(task_schema.dump(task)), 200

# Create task
@tasks_bp.route('/tasks', methods=['POST'])
def create_task():
    errors = task_schema.validate(request.json)
    if errors:
        return jsonify(errors), 400
    task = Task(**task_schema.load(request.json))
    db.session.add(task)
    db.session.commit()
    return jsonify(task_schema.dump(task)), 201

# Update task
@tasks_bp.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get_or_404(id)
    errors = task_schema.validate(request.json)
    if errors:
        return jsonify(errors), 400
    for key, value in task_schema.load(request.json).items():
        setattr(task, key, value)
    db.session.commit()
    return jsonify(task_schema.dump(task)), 200

# Delete task
@tasks_bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted'}), 200