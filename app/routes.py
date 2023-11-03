from flask import Blueprint, request, jsonify, abort
from .models import Task

main = Blueprint('main', __name__)

@main.route('/api/v1/tasks', methods=['GET'])
def list_tasks():
    tasks = Task.get_all()
    return jsonify(tasks), 200

@main.route('/api/v1/tasks', methods=['POST'])
def create_task():
    try:
        data = request.get_json()
        new_task = Task(title=data['title'], description=data['description'], status=data['status'])
        task = new_task.create()
        return jsonify(task), 201
    except (KeyError, TypeError, ValueError):
        abort(400)

@main.route('/api/v1/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.get_by_id(task_id)
    if task:
        return jsonify(task), 200
    else:
        abort(404)

@main.route('/api/v1/tasks/<task_id>', methods=['PATCH'])
def update_task(task_id):
    update_data = request.get_json()
    task = Task.get_by_id(task_id)
    if task:
        updated_task = Task(title=task['title'], description=task['description'], status=task['status'], id=task_id)
        updated_task = updated_task.update(task_id, update_data)
        return jsonify(updated_task), 200
    else:
        abort(404)

@main.route('/api/v1/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.get_by_id(task_id)
    if task:
        Task.delete(task_id)
        return jsonify({"message": "Task deleted successfully."}), 200
    else:
        abort(404)

@main.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

@main.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@main.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal server error'}), 500
