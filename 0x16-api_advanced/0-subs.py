#!/usr/bin/python3
"""requestsREDDIT"""
import requests
import json


def number_of_subscribers(subreddit):
    """READIT"""
    headers = {'User-agent': 'redddit'}

    response = requests.get(
        f'https://www.reddit.com/r/{subreddit}/about.json',
        headers=headers
    )

    data = response.json()

    if not data.get('data').get('subscribers'):
        return 0

    return data['data']['subscribers']
