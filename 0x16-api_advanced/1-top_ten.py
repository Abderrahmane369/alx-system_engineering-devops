#!/usr/bin/python3
"""requestsREDDIT"""
import requests
import json


def top_ten(subreddit):
    """READIT"""
    headers = {'User-agent': 'redddit'}

    response = requests.get(
        f'https://www.reddit.com/r/{subreddit}/hot.json',
        headers=headers
    )

    data = response.json()

    if not data.get('data'):
        return print('None')

    for post in data['data']['children'][:10]:
        print(post['data']['title'])
