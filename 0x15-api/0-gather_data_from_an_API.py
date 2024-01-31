#!/usr/bin/python3
"""logar"""
import requests as rq
import json
from sys import argv

users = rq.get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
todos = rq.get(f'https://jsonplaceholder.typicode.com/todos/')
todos = json.loads(todos.content.decode())

employee = json.loads(users.content.decode())

emptodos = list(filter(lambda e: e.get('userId') == employee.get('id'), todos))

tasksDone = list(filter(lambda e: e.get('completed'), emptodos))

print(f'Employee {employee.get("name")} ' +
      f'is done with tasks({len(tasksDone)}/{len(emptodos)}):')

for i in tasksDone:
    print(f'\t {i.get("title")}')
