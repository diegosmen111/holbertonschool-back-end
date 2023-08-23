#!/usr/bin/python3
"""
Gather data from an API
"""
import requests
import sys


def main():
    # URL de la REST API
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    # ID de empleado
    employee_id = int(sys.argv[1])

    # Hacemos la solicitud GET al punto final '/todos' para obtener la lista
    # de tareas para el empleado dado
    response = requests.get(
    f'{BASE_URL}/todos?userId={employee_id}')
    
    # Analizamos la respuesta JSON y contamos la cantidad de tareas completadas
    todos = response.json()
    tasks_completed = [todo for todo in todos if todo['completed']]
    num_tasks_completed = len(tasks_completed)
    num_tasks = len(todos)

    # Obtenemos el nombre del empleado del punto final '/users'
    user_response = requests.get(f'{BASE_URL}/users/{employee_id}')
    user_data = user_response.json()
    employee_name = user_data['name']

    # Imprimimos la información de la lista
    print(f"Employee {employee_name} has completed tasks ({num_tasks_completed}/{num_tasks}):")

    for todo in tasks_completed:
        print(f'\t {todo["title"]}')


if __name__ == '__main__':
    main()
