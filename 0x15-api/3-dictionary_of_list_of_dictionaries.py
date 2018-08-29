#!/usr/bin/python3p
'''
gathers information about an employee by ID and returns their TODO progress
'''
import json
from collections import OrderedDict
import requests
import sys


def get_users_todo():

    raw_users = requests.get('https://jsonplaceholder.typicode.com/users')
    users = {}
    final_id = OrderedDict()
    filename = "todo_all_employees.json"

    for item in raw_users.json():
        users[item['id']] = item['username']

    with open(filename, 'w+') as f:
        for user in users:
            todos = requests.get(
                'https://jsonplaceholder.typicode.com/todos?userId={}'
                .format(user))
            todos = todos.json()
            res = []
            for todo in todos:
                final = OrderedDict()
                final['username'] = users[user]
                final['task'] = todo['title']
                final['completed'] = todo['completed']
                res.append(final)
            final_id[user] = res
        json.dump(final_id, f)


if __name__ == "__main__":
    get_users_todo()
