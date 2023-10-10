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


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit
    """
    headers = {'User-agent': '2-recurse/1.0 (fipis92205@dixiser.com)'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    # to handle pagination that the Reddit API uses
    # add 'after' parameter to the url if it is not none
    if after:
        url += f'?after={after}'

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        total_data = response.json()['data']
        total_posts = total_data['children']
        hot_list += helper_recurse(total_posts)

        # if more data is present call the function recursively
        # with the 'after' parameter
        if total_data['after']:
            return recurse(subreddit, hot_list, total_data['after'])

        return hot_list
    else:
        return None
