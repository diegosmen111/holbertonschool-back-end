#!/usr/bin/python3
"""
Gather data from an API
"""
import requests
from sys import argv


def main():
    user_id = argv[1]

    # Obtener el nombre de usuario
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data["name"]

    # Obtener la lista de tareas completadas del usuario
    base_url = "https://jsonplaceholder.typicode.com"
    todo_url = f"{base_url}/todos?userId={user_id}&completed=true"
    todo_response = requests.get(todo_url)
    todo_list = todo_response.json()

    # Imprimir la información
    print(f"Employee {username} is done with tasks ({len(todo_list)}/{len(todo_list)}):")
    for todo in todo_list:
        print("\t- " + todo["title"])


if __name__ == "__main__":
    main()
