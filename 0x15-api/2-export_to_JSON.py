#!/usr/bin/python3

"""
This Python script retrieves TODO data (JSON)
"""

from requests import get
from sys import argv
import json


def get_employee_username(user_id, user_data):
    """
    Finds the username for a given user ID from the provided user data.

    Args:
        user_id (int): The ID of the user to find the username for.
        user_data (list): A list of dictionaries representing user data.

    Returns:
        str: The username of the user with the provided ID, or None if not found.
    """
    for user in user_data:
        if user['id'] == user_id:
            return user['username']
    return None


def export_todo_data(employee_id):
    """
    Exports TODO data for a specified employee ID to a JSON file.

    Args:
        employee_id (int): The ID of the employee whose data to export.

    Returns:
        int: 0 on success, 1 on error.
    """
    try:
        # Validate user input
        if len(argv) != 2:
            print("Usage: python script.py <employee_id>")
            return 1

        employee_id = int(employee_id)

        # Get TODO data
        todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        todos_response = get(todos_url)
        if todos_response.status_code != 200:
            print(f"Error retrieving TODO data: {todos_response.status_code}")
            return 1
        todos_data = todos_response.json()

        # Get user data
        users_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        users_response = get(users_url)
        if users_response.status_code != 200:
            print(f"Error retrieving user data: {users_response.status_code}")
            return 1
        user_data = users_response.json()

        # Find employee username
        employee_username = user_data['username']
        if not employee_username:
            print(f"Employee with ID {employee_id} not found.")
            return 1

        # Build and write JSON data
        tasks = [{
            'task': todo['title'],
            'completed': todo['completed'],
            'username': employee_username
        } for todo in todos_data]

        json_data = {str(employee_id): tasks}

        filename = f"{employee_id}.json"
        with open(filename, 'w') as jsonfile:
            json.dump(json_data, jsonfile, indent= None)

        print(f"Employee data exported to {filename}")
        return 0

    except ValueError:
        print("Invalid employee ID: Please provide an integer.")
        return 1


if __name__ == "__main__":
    exit_code = export_todo_data(argv[1])
    exit(exit_code)
