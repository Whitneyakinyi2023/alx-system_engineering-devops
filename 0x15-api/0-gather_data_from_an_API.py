#!/usr/bin/python3
"""Writing  a python script using REST API"""


from requests import get
from sys import argv



def to_do_list_info(employee_id):
    """base url fr accessing API"""
    
    base_url = 'https://jsonplaceholder.typicode.com/'
    
    user_response = get(f'{base_url}/users{employee_id}')
    if user_response.status_code != 200:
        print(f'Error: Employee with ID {employee_id} not found.')
        user = user_response.json()
        employee_name = user.get('name')
        todos_response = get(f'{base_url}/todos?userId={employee_id}')
        """Fetching the to-do list"""
        todos = todos_response.json()
        
        total_tasks = len(todos)
        """Calculation of total number  of tasks"""
        done_tasks = [todo for todo in todos if todo.get('completed')]
        number_of_done_tasks = len(done_tasks)
        
        print(f'Employee {employee_name} is done with tasks'
              f'({number_of_done_tasks}/{total_tasks}): ')
        """Printing out the output:"""
        
        for task in done_tasks:
            print(f'\t {task.get("title")}')
            
        if __name__ == "__main__":
            if len(sys.argv) != 2:
                print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        else:
             try:
                employee_id = int(sys.argv[1])
                to_do_list_info(employee_id)
             except ValueError:
                 print("Employee ID must be an integer.")
