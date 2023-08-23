#!/usr/bin/python3
"""
This script retrieves and processes employee tasks data from a REST API.
"""

import requests
import sys

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    sys.exit(1)

# Get the employee ID from the command-line argument
employee_id = sys.argv[1]
url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)

# Make a GET request to the API
response = requests.get(url)

# Check if the employee exists
if response.status_code == 404:
    print('Employee with ID {} does not exist'.format(employee_id))
    sys.exit(1)

# Extract task data from the response
todos = response.json()

# Filter completed tasks
completed_tasks = [todo for todo in todos if todo['completed']]
total_tasks = len(todos)

# Get the employee's name from the first task
employee_name = todos[0]['username']

# Print employee and task information
print('Employee Name: {}'.format(employee_name))
print('Employee is done with tasks ({}/{}):'.format(len(completed_tasks), total_tasks))

# Print completed tasks
for task in completed_tasks:
    print('\t {} {}'.format(task['title'], '(completed)'))
