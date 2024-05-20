#!/usr/bin/python3

"""
This Python script retrieves TODO data from a sample API, processes it,
and exports all tasks in a single JSON file with the specified format,
including error handling.
"""

from requests import get
from sys import argv
import json


def get_usernames(user_data):
  """
  Extracts usernames from the provided user data.

  Args:
      user_data (list): A list of dictionaries representing user data.

  Returns:
      dict: A dictionary mapping user IDs to usernames.
  """
  usernames = {}
  for user in user_data:
    usernames[user['id']] = user['username']
  return usernames


def export_all_todo_data():
  """
  Exports all TODO data from the API to a JSON file with error handling.
  """
  todos_url = 'https://jsonplaceholder.typicode.com/todos/'
  users_url = 'https://jsonplaceholder.typicode.com/users'

  try:
    todos_response = get(todos_url)
    todos_response.raise_for_status()  # Raise exception for non-200 status codes
    todos_data = todos_response.json()

    users_response = get(users_url)
    users_response.raise_for_status()
    users_data = users_response.json()

  except requests.exceptions.RequestException as e:
    print(f"Error retrieving data: {e}")
    return

  usernames = get_usernames(users_data)
  all_tasks = {}

  for todo in todos_data:
    user_id = todo['userId']
    if user_id not in all_tasks:
      all_tasks[user_id] = []

    task_data = {
        "username": usernames[user_id],
        "task": todo['title'],
        "completed": todo['completed'],
    }
    all_tasks[user_id].append(task_data)

  with open('todo_all_employees.json', 'w') as outfile:
    try:
      json.dump(all_tasks, outfile, indent=None)
      print("All employee TODO data exported to todo_all_employees.json")
    except json.JSONDecodeError as e:
      print(f"Error encoding data to JSON: {e}")


if __name__ == "__main__":
  export_all_todo_data()
  