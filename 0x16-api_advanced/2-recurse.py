#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""

import requests


def helper_recurse(posts):
    """
    Helper recursive function to help with getting the list of titles
    """
    # if list is empty return an empty list
    if not posts:
        return []
    return [posts[0]['data']['title']] + helper_recurse(posts[1:])


def recurse(subreddit, hot_list=[]):
    """
    Queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit
    """
    headers = {'User-agent': '1-top_ten/1.0 (fipis92205@dixiser.com)'}
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/\
hot.json', headers=headers)
    if response.status_code == 200:
        total_posts = response.json()['data']['children']
        hot_list = helper_recurse(total_posts)
        return hot_list
    else:
        return None
