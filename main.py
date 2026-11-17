#!/usr/bin/python3
"""Print a user's completed tasks from the JSONPlaceholder API."""

import sys

import requests


USERS_URL = "https://jsonplaceholder.typicode.com/users"
TODOS_URL = "https://jsonplaceholder.typicode.com/todos"


def main(user_id):
    users = requests.get(USERS_URL).json()
    todos = requests.get(TODOS_URL).json()

    user = next(user for user in users if user["id"] == user_id)
    user_tasks = [todo for todo in todos if todo["userId"] == user_id]
    completed = [todo for todo in user_tasks if todo["completed"]]

    with open("student_output", "w") as output:
        output.write("Employee {} is done with tasks({}/{}):\n".format(
            user["name"], len(completed), len(user_tasks)
        ))
        for task in completed:
            output.write("\t {}\n".format(task["title"]))


if __name__ == "__main__":
    main(int(sys.argv[1]))
