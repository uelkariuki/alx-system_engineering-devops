#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit

"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for
    a given subreddit
    """
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json')
    print(response.status_code)
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0
