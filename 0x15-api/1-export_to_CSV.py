#!/usr/bin/python3

"""
This Python script retrieves TODO data (CSV)

"""

from requests import get
from sys import argv
import csv


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
  Exports TODO data for a specified employee ID to a CSV file.

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
    todos_url = 'https://jsonplaceholder.typicode.com/todos/'
    todos_response = get(todos_url)
    if todos_response.status_code != 200:
      print(f"Error retrieving TODO data: {todos_response.status_code}")
      return 1
    todos_data = todos_response.json()

    # Get user data
    users_url = 'https://jsonplaceholder.typicode.com/users'
    users_response = get(users_url)
    if users_response.status_code != 200:
      print(f"Error retrieving user data: {users_response.status_code}")
      return 1
    users_data = users_response.json()

    # Find employee username
    employee_username = get_employee_username(employee_id, users_data)
    if not employee_username:
      print(f"Employee with ID {employee_id} not found.")
      return 1

    # Build and write CSV data
    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
      writer = csv.writer(csvfile)
      for todo in todos_data:
        if todo['userId'] == employee_id:
          writer.writerow([
              todo['userId'],
              employee_username,
              todo['completed'],
              todo['title'],
          ])

    print(f"Employee data exported to {filename}")
    return 0

  except ValueError:
    print("Invalid employee ID: Please provide an integer.")
    return 1


if __name__ == "__main__":
  exit_code = export_todo_data(argv[1])
  exit(exit_code)

