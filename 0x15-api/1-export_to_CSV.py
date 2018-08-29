#!/usr/bin/python3
'''
gathers information about an employee by ID and returns their TODO progress
'''
import csv
import os
import requests
import sys


def main(argv):

    raw_users = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                       .format(sys.argv[1]))
    names = raw_users.json().get('username')
    raw_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    raw_todos = raw_todos.json()
    complete = 0
    fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    titles = []
    total = 0
    filename = sys.argv[1] + ".csv"
    with open(filename, 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL, quotechar='"')
        for todo in raw_todos:
            if todo['userId'] == int(sys.argv[1]):
                todo['name'] = names
                writer.writerow([todo['userId'], todo['name'],
                                 todo['completed'], todo['title']])


if __name__ == "__main__":
    import sys
    main(sys.argv)
