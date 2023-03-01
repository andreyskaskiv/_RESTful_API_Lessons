from flask import Flask, request, jsonify

app = Flask(__name__)

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


# Endpoint for getting the list of tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    # Return the list of tasks as JSON
    return jsonify(tasks)


# Endpoint for creating a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    # Create a new task from the request data
    task = request.json
    # Assign a new ID to the task
    task['id'] = max(task['id'] for task in tasks) + 1
    # Add the new task to the list
    tasks.append(task)
    # Return the new task as JSON with HTTP status code 201 "Created"
    return jsonify(task), 201


# Endpoint for getting a specific task
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    # Find the task with the given ID
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        # Return an empty response with HTTP status code 404 "Not Found" if task not found
        return '', 404
    # Return the task as JSON
    return jsonify(task)


# Endpoint for updating a specific task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    # Find the task with the given ID
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        # Return an empty response with HTTP status code 404 "Not Found" if task not found
        return '', 404
    # Update the task with the request data
    task.update(request.json)
    # Return the updated task as JSON
    return jsonify(task)


# Endpoint for deleting a specific task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    # Find the task with the given ID
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        # Return an empty response with HTTP status code 404 "Not Found" if task not found
        return '', 404
    # Remove the task from the list
    tasks.remove(task)
    # Return an empty response with HTTP status code 204 "No Content"
    return '', 204


if __name__ == '__main__':
    # Start the Flask application
    app.run()
