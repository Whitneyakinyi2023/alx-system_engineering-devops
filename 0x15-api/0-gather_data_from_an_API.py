#!/usr/bin/python3

"""
Python script that, using a REST API
"""

from requests import get
from sys import argv


def main():
  if len(argv) != 2:
    print("Usage: python script.py <employee_id>")
    exit(1)

  try:
    employee_id = int(argv[1])
  except ValueError:
    print("Invalid employee ID: Please provide an integer.")
    exit(1)

  todos_url = 'https://jsonplaceholder.typicode.com/todos/'
  users_url = 'https://jsonplaceholder.typicode.com/users'

  todos_response = get(todos_url)
  if todos_response.status_code == 200:
      todos_data = todos_response.json()
  else:
      print(f"Error retrieving TODO data: {todos_response.status_code}")
      exit(1)

  user_response = get(users_url)
  if user_response.status_code == 200:
      user_data = user_response.json()
  else:
      print(f"Error retrieving user data: {user_response.status_code}")
      exit(1)

  completed_tasks = 0
  total_tasks = 0
  completed_task_titles = []

  for user in user_data:
    if user.get('id') == employee_id:
      employee_name = user.get('name')

  for todo in todos_data:
    if todo.get('userId') == employee_id:
      total_tasks += 1

      if todo.get('completed') is True:
        completed_tasks += 1
        completed_task_titles.append(todo.get('title'))

  print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, total_tasks))

  for task_title in completed_task_titles:
    print("\t {}".format(task_title))


if __name__ == "__main__":
  main()
