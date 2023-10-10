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
    headers = {'User-agent': '0-subs/1.0 (fipis92205@dixiser.com)'}
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json',
                            headers=headers)
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0
