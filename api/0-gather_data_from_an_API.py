#!/usr/bin/python3
"""
Python script to export completed tasks data in JSON format
Usage: python3 0-gather_data_from_an_API.py <employee_id>
"""

import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]
url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)

response = requests.get(url)

if response.status_code == 404:
    print('Employee Name: {}'.format(employee_name))
    sys.exit(1)

todos = response.json()

completed_tasks = [todo for todo in todos if todo['completed']]
total_tasks = len(todos)

employee_name = todos[0]['username']

print('Employee {} has completed tasks({}/{}):'.format(employee_name, len(completed_tasks), total_tasks))

for task in completed_tasks:
    for task in completed_tasks:
    print('\t {} {}'.format(task['title'], '(completed)'))
