#!/usr/bin/python3
"""
Gather data from an API
"""
import requests
import sys


def fetch_employee_todo_list(employee_id):
    """
    Fetches the employee's todo list from the JSONPlaceholder API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        dict: A dictionary containing the employee's data and todo list.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)
        user_data = user_response.json()
        todo_data = todo_response.json()
        return {"user_data": user_data, "todo_data": todo_data}
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        sys.exit(1)


def display_employee_todo_progress(employee_name, done_tasks, total_tasks, completed_task_titles):
    """
    Displays the progress of an employee's tasks.

    Args:
        employee_name (str): The name of the employee.
        done_tasks (int): The number of completed tasks.
        total_tasks (int): The total number of tasks.
        completed_task_titles (list): A list of titles of completed tasks.
    """
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for title in completed_task_titles:
        print(f"    {title}")


def main():
    """
    Main function that fetches the employee's todo list and displays their progress.
    """
    # ID de empleado
    employee_id = int(sys.argv[1])

    # Obtenemos la lista de tareas del empleado
    data = fetch_employee_todo_list(employee_id)
    user_data = data["user_data"]
    todo_data = data["todo_data"]

    employee_name = user_data["name"]
    completed_task_titles = [task["title"] for task in todo_data if task["completed"]]
    done_tasks = len(completed_task_titles)
    total_tasks = len(todo_data)

    display_employee_todo_progress(employee_name, done_tasks, total_tasks, completed_task_titles)


if __name__ == "__main__":
    main()
