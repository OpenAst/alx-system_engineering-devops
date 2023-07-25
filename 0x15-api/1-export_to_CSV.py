#!/usr/bin/python3
"""
Export API data to CSV
"""

import csv
import requests
import sys

def export_to_csv(user):
    """
    function to export to a csv file
    """

    url_user = 'https://jsonplaceholder.typicode.com/users/' + user
    res = requests.get(url_user)
    user_name = res.json().get('username')
    task = url_user + '/todos'
    res = requests.get(task)
    tasks = res.json()

    with open('{}.csv'.format(user), 'w') as csvfile:
        for task in tasks:
            completed = task.get('completed')
            title_task = task.get('title')
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user, user_name, completed, title_task))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <user_id>")
        sys.exit(1)

    user = sys.argv[1]
    export_to_csv(user)

