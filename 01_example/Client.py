from typing import List, Dict

import requests


def get_tasks(base_url: str) -> List[Dict[str, str]]:
    """
    Send a GET request to retrieve the list of tasks from the API.

    Args:
        base_url (str): The base URL for the API.

    Returns:
        List[Dict[str, str]]: A list of dictionaries representing the tasks.
    """
    response = requests.get(f"{base_url}/tasks")
    return response.json()


def create_task(base_url: str, title: str, description: str) -> Dict[str, str]:
    """
    Send a POST request to create a new task in the API.

    Args:
        base_url (str): The base URL for the API.
        title (str): The title of the new task.
        description (str): The description of the new task.

    Returns:
        Dict[str, str]: A dictionary representing the newly created task.
    """
    task = {'title': title, 'description': description}
    response = requests.post(f"{base_url}/tasks", json=task)
    return response.json()


def get_task(base_url: str, task_id: int | str) -> Dict[str, str]:
    """
    Send a GET request to retrieve a single task from the API.

    Args:
        base_url (str): The base URL for the API.
        task_id (int): The ID of the task to retrieve.

    Returns:
        Dict[str, str]: A dictionary representing the task.
    """
    response = requests.get(f"{base_url}/tasks/{task_id}")
    return response.json()


def update_task(base_url: str, task_id: int | str, description: str) -> Dict[str, str]:
    """
    Send a PUT request to update a task in the API.

    Args:
        base_url (str): The base URL for the API.
        task_id (int): The ID of the task to update.
        description (str): The new description of the task.

    Returns:
        Dict[str, str]: A dictionary representing the updated task.
    """
    task = {'description': description}
    response = requests.put(f"{base_url}/tasks/{task_id}", json=task)
    return response.json()


def delete_task(base_url: str, task_id: int | str) -> int:
    """
    Send a DELETE request to delete a task from the API.

    Args:
        base_url (str): The base URL for the API.
        task_id (int): The ID of the task to delete.

    Returns:
        int: The status code of the response.
    """
    response = requests.delete(f"{base_url}/tasks/{task_id}")
    return response.status_code


if __name__ == "__main__":
    base_url = "http://localhost:5000"

    tasks = get_tasks(base_url)
    print(f"GET get_tasks => {tasks}")
    # prints: [{'id': 1, 'title': 'Buy milk', 'description': 'Buy milk from the store'},
    # {'id': 2, 'title': 'Do math homework', 'description': 'Do math homework assignment'}]

    new_task = create_task(base_url, "Walk the dog", "Take the dog for a walk")
    print(f"POST create_task => {new_task}")
    # # prints: {'id': 3, 'title': 'Walk the dog', 'description': 'Take the dog for a walk'}

    task_id = new_task['id']
    task = get_task(base_url, task_id)
    print(f"GET get_task => {task}")
    # prints: {'id': 3, 'title': 'Walk the dog', 'description': 'Take the dog for a walk'}

    updated_task = update_task(base_url, task_id, "Take the dog for a long walk")
    print(f"PUT update_task => {updated_task}")
    # prints: {'id': 3, 'title': 'Walk the dog', 'description': 'Take the dog for a long walk'}

    status_code = delete_task(base_url, task_id)
    print(f"DELETE delete_task => {status_code}")
    # prints: 204
