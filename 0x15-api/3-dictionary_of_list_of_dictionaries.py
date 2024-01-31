#!/usr/bin/python3
"""logar"""
import csv
import json
import requests as rq
from sys import argv

if __name__ == '__main__':
    users = rq.get(f'https://jsonplaceholder.typicode.com/users/')
    todos = rq.get(f'https://jsonplaceholder.typicode.com/todos/')
    todos = json.loads(todos.content.decode())

    employees = json.loads(users.content.decode())

    with open('todo_all_employees.json', 'w', encoding='utf-8') as f:
        employeesTasks = {}

        for employee in employees:
            emptodos = list(filter(lambda e: e.get('userId')
                                   == employee.get('id'), todos))
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
            employeesTasks = {**employeesTasks, **userTasks}

        f.write(json.dumps(employeesTasks))
