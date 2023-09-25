#!/usr/bin/python3

"""
Python script that, using this REST API, exports data in the JSON format
"""

import json
import requests
""" Importing the required modules"""


def get_employee_info(api_endpoint):
    """ Method to get employee info"""
    user_response = requests.get(f"{api_endpoint}users")
    to_do_response = requests.get(f"{api_endpoint}todos")

    if user_response.status_code == 200 and to_do_response.status_code == 200:
        users_data = user_response.json()
        to_do_data = to_do_response.json()

        filename = 'todo_all_employees.json'
        all_tasks = {}
        for user in users_data:
            tasks = []
            for task in to_do_data:
                if task['userId'] == user['id']:
                    tasks.append({
                        "username": user['username'],
                        "task": task['title'],
                        "completed": task['completed']
                        })
            all_tasks[user['id']] = tasks
        with open(filename, "w") as file:
            json.dump(all_tasks, file)


def main():
    """ Main function"""
    api_endpoint = "https://jsonplaceholder.typicode.com/"
    get_employee_info(api_endpoint)


if __name__ == "__main__":
    main()
