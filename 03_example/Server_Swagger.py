from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='TodoMVC API',
          description='A simple TodoMVC API',
          )

# Define a namespace
ns = api.namespace('tasks', description='TODO operations')

# Define a model for a task (optional)
task_model = api.model('Task', {
    'id': fields.Integer(readOnly=True, description='The task unique identifier'),
    'title': fields.String(required=True, description='The task title'),
    'description': fields.String(required=True, description='The task description')
})

# Define the list of tasks (initially empty)
# tasks = []

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


# Endpoint for getting the list of tasks
@ns.route('/')
class TaskList(Resource):
    @ns.doc('list_tasks')
    @ns.marshal_list_with(task_model)
    def get(self):
        '''List all tasks'''
        return tasks

    @ns.doc('create_task')
    @ns.expect(task_model)
    @ns.marshal_with(task_model, code=201)
    def post(self):
        '''Create a new task'''
        task = api.payload
        task['id'] = max(task['id'] for task in tasks) + 1
        tasks.append(task)
        return task, 201


# Endpoint for getting a specific task
@ns.route('/<int:id>')
@ns.response(404, 'Task not found')
class Task(Resource):
    @ns.doc('get_task')
    @ns.marshal_with(task_model)
    def get(self, id):
        '''Fetch a task given its id'''
        for task in tasks:
            if task['id'] == id:
                return task
        ns.abort(404, message="Task {} doesn't exist".format(id))

    @ns.doc('update_task')
    @ns.expect(task_model)
    @ns.marshal_with(task_model)
    def put(self, id):
        '''Update a task given its id'''
        for task in tasks:
            if task['id'] == id:
                task.update(api.payload)
                return task
        ns.abort(404, message="Task {} doesn't exist".format(id))

    @ns.doc('delete_task')
    @ns.response(204, 'Task deleted')
    def delete(self, id):
        '''Delete a task given its id'''
        for task in tasks:
            if task['id'] == id:
                tasks.remove(task)
                return '', 204
        ns.abort(404, message="Task {} doesn't exist".format(id))


if __name__ == '__main__':
    app.run(debug=True)
