# app.py
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from models import tasks

app = Flask(__name__)
api = Api(app)

class TaskList(Resource):
    def get(self):
        return jsonify(tasks)

    def post(self):
        new_task = {
            'id': len(tasks) + 1,
            'title': request.json['title'],
            'description': request.json.get('description', ""),
            'done': False
        }
        tasks.append(new_task)
        return jsonify(new_task), 201

class Task(Resource):
    def get(self, task_id):
        task = next((task for task in tasks if task['id'] == task_id), None)
        if task is None:
            return {'message': 'Task not found'}, 404
        return jsonify(task)

    def put(self, task_id):
        task = next((task for task in tasks if task['id'] == task_id), None)
        if task is None:
            return {'message': 'Task not found'}, 404
        task['title'] = request.json.get('title', task['title'])
        task['description'] = request.json.get('description', task['description'])
        task['done'] = request.json.get('done', task['done'])
        return jsonify(task)

    def delete(self, task_id):
        global tasks
        tasks = [task for task in tasks if task['id'] != task_id]
        return '', 204

api.add_resource(TaskList, '/tasks')
api.add_resource(Task, '/tasks/<int:task_id>')

if __name__ == '__main__':
    app.run(debug=True)