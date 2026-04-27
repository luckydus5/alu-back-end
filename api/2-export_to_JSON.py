#!/usr/bin/python3
"""
Export to JSON from an API
"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    employee_id = sys.argv[1]
    
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(employee_id)).json()
    username = user.get("username")
    
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    dictionary = {
        employee_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            } for task in todos
        ]
    }
    
    with open("{}.json".format(employee_id), "w") as jsonfile:
        json.dump(dictionary, jsonfile)
