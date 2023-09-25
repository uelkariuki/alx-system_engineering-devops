#!/usr/bin/python3

"""
Python script that, using this REST API, exports data in the JSON format
"""

import json
import requests
import sys
""" Importing the required modules"""


def get_employee_info(api_endpoint, employee_id):
    """ Method to get employee info"""
    user_response = requests.get(f"{api_endpoint}users/{employee_id}")
    to_do_response = requests.get(f"{api_endpoint}todos",
                                  params={"userId": employee_id})

    if user_response.status_code == 200 and to_do_response.status_code == 200:
        user_data = user_response.json()
        to_do_data = to_do_response.json()

        filename = f'{user_data["id"]}.json'
        tasks = []
        for task in to_do_data:
            tasks.append({
                "task": task['title'],
                "completed": task['completed'],
                "username": user_data['username']
                })
        with open(filename, "w") as file:
            json.dump({employee_id: tasks}, file)


def main():
    """ Main function"""
    api_endpoint = "https://jsonplaceholder.typicode.com/"
    employee_id = int(sys.argv[1])
    get_employee_info(api_endpoint, employee_id)


if __name__ == "__main__":
    main()
