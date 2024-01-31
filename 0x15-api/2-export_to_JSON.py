#!/usr/bin/python3
"""logar"""
import csv
import json
import requests as rq
from sys import argv

if __name__ == '__main__':
    users = rq.get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
    todos = rq.get(f'https://jsonplaceholder.typicode.com/todos/')
    todos = json.loads(todos.content.decode())

    employee = json.loads(users.content.decode())

    emptodos = list(filter(lambda e: e.get('userId')
                    == employee.get('id'), todos))

    with open(f'{argv[1]}.json', 'w', encoding='utf-8') as f:
        userTasks = {
            f'{employee.get("id")}': []
        }
        for t in emptodos:
            task = {
                'task': t['title'],
                'completed': t['completed'],
                'username': employee['username']
            }
            userTasks.get(f'{employee.get("id")}').append(task)

        f.write(json.dumps(userTasks))
