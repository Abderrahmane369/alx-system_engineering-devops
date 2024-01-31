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

    with open(f'{argv[1]}.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f, quotechar="'")

        for t in emptodos:
            writer.writerow(('"{}"'.format(t["userId"]),
                             '"{}"'.format(employee["username"]),
                             '"{}"'.format(t["completed"]),
                             '"{}"'.format(t["title"])))
