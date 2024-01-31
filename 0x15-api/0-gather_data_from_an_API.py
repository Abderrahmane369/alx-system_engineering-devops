#!/usr/bin/python3
"""logar"""
import requests as rq
import json
from sys import argv

users = rq.get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
todos = rq.get(f'https://jsonplaceholder.typicode.com/todos/')
todos = json.loads(todos.content.decode())

employee = json.loads(users.content.decode())

emptodos = list(filter(lambda e: e['userId'] == employee['id'], todos))

tasksDone = list(filter(lambda e: e['completed'], emptodos))

print(f'Employee {employee["name"]} ' +
      f'is done with tasks({len(tasksDone)}/{len(emptodos)}):')

for i in tasksDone:
    print(f'\t {i["title"]}')
