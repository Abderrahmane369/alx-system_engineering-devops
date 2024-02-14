#!/usr/bin/python3
"""requestsREDDIT"""
import requests
import json


def recurse(subreddit, hot_list=[]):
    """READIT"""
    headers = {'User-agent': 'redddit'}

    response = requests.get(
        f'https://www.reddit.com/r/{subreddit}/hot.json',
        headers=headers
    )

    data = response.json()

    if not data.get('data').get('children'):
        return None

    posts = data['data']['children']

    if len(posts) != len(hot_list):
        hot_list.append(posts[len(hot_list)]['data']['title'])
        return recurse(subreddit, hot_list)

    return hot_list


print(recurse('Islam'))
