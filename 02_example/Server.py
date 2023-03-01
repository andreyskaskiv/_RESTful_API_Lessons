from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

# The list of tasks
tasks = [
    {
        'id': 1,
        'title': 'Buy milk',
        'description': 'Buy milk from the store'
    },
    {
        'id': 2,
        'title': 'Do math homework',
        'description': 'Do math homework assignment'
    }
]


# A helper function to find a task by ID
def find_task(task_id):
    return next((task for task in tasks if task['id'] == task_id), None)


# A parser for parsing request data
parser = reqparse.RequestParser()
parser.add_argument('title')
parser.add_argument('description')


class Task(Resource):
    def get(self, task_id):
        task = find_task(task_id)
        if task is None:
            return {'message': 'Task not found'}, 404
        return task, 200

    def put(self, task_id):
        task = find_task(task_id)
        if task is None:
            return {'message': 'Task not found'}, 404
        args = parser.parse_args()
        task.update(args)
        return task, 200

    def delete(self, task_id):
        task = find_task(task_id)
        if task is None:
            return {'message': 'Task not found'}, 404
        tasks.remove(task)
        return {}, 204


class TaskList(Resource):
    def get(self):
        return tasks, 200

    def post(self):
        args = parser.parse_args()
        task = {
            'id': max(task['id'] for task in tasks) + 1,
            'title': args['title'],
            'description': args['description']
        }
        tasks.append(task)
        return task, 201


api.add_resource(TaskList, '/tasks')
api.add_resource(Task, '/tasks/<int:task_id>')

if __name__ == '__main__':
    app.run(debug=True)
