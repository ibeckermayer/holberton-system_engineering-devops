#!/usr/bin/python3
'''
gathers information about an employee by ID and returns their TODO progress
'''
import requests
import sys


def info():
    raw_users = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(sys.argv[1]))
    names = raw_users.json().get('name')
    raw_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()
    comp = 0
    titles = []
    tot = 0
    for todo in raw_todos:
        if todo['userId'] == int(sys.argv[1]):
            if todo['completed'] is True:
                comp += 1
                titles.append(todo['title'])
            tot += 1
    print("Employee {} is done with raw_todos({}/{}):"
          .format(names, comp, tot))
    for title in titles:
        print('\t ', end="")
        print(title)


if __name__ == "__main__":
    info()
