#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot
    posts listed for a given subreddit.
    """
    headers = {'User-agent': '1-top_ten/1.0 (fipis92205@dixiser.com)'}
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/\
hot.json?limit=10', headers=headers)
    if response.status_code == 200:
        total_posts = response.json()['data']['children']
        titles = [post['data']['title'] for post in total_posts]
        for title in titles:
            print(title)
    else:
        return None
