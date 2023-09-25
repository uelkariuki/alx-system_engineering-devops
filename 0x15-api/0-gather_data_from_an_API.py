#!/usr/bin/python3

"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

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

        total_tasks = len(to_do_data)
        completed_tasks = len([task for task in to_do_data
                              if task["completed"]])
        print(f"Employee {user_data['name']} is done with\
 tasks({completed_tasks}/{total_tasks}):")

        for task in to_do_data:
            if task["completed"]:
                print("\t ", task["title"])


def main():
    """ Main function"""
    api_endpoint = "https://jsonplaceholder.typicode.com/"
    employee_id = int(sys.argv[1])
    get_employee_info(api_endpoint, employee_id)


if __name__ == "__main__":
    main()
