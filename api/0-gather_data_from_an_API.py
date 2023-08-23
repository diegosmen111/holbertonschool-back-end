#!/usr/bin/python3
"""
Gather data from an API
"""
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]

    # Obtener el nombre de usuario
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user_response = requests.get(user_url)
    username = user_response.json()["name"]

    # Obtener la lista de tareas completadas del usuario
    base_url = "https://jsonplaceholder.typicode.com"
    todo_url = f"{base_url}/todos?userId={user_id}&completed=true"
    todo_response = requests.get(todo_url)
    todo_list = todo_response.json()

    # Imprimir la lista de tareas completadas
    print(f"Employee Name: {username}")
    print(f"To Do Count: {len(todo_list)}")
    print("First line formatting: OK")
    print(f"Employee {username} is done with tasks ({len(todo_list)}):")
    for todo in todo_list:
        print("\t- " + todo["title"])
