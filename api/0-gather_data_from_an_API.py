#!/usr/bin/python3
"""Display the TODO list progress of an employee using a REST API."""

import requests
import sys

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_user(user_id):
    response = requests.get("{}/users/{}".format(BASE_URL, user_id))
    if response.status_code == 200:
        return response.json()
    print("GET user failed:", response.status_code)
    return None


def get_todos(user_id):
    response = requests.get("{}/todos?userId={}".format(BASE_URL, user_id))
    if response.status_code == 200:
        return response.json()
    print("GET todos failed:", response.status_code)
    return None


if __name__ == "__main__":
    user_id = sys.argv[1]
    user = get_user(user_id)
    todos = get_todos(user_id)

    if user is not None and todos is not None:
        completed = [task for task in todos if task.get("completed")]
        lines = ["Employee {} is done with tasks({}/{}):".format(
            user["name"], len(completed), len(todos)
        )]
        lines.extend("\t {}".format(task["title"]) for task in completed)
        output = "\n".join(lines) + "\n"

        with open("student_output", "w") as output_file:
            output_file.write(output)
        print(output, end="")
