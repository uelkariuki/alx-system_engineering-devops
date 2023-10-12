#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the title of
all hot articles, and prints a sorted count of given keywords
(case-insensitive, delimited by spaces. Javascript should count as
javascript, but java should not).
"""

import requests


def count_words(subreddit, word_list, after=None, results=None):
    """
    Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords (case-insensitive,
    delimited by spaces.
    """
    if results is None:
        results = {}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-agent': '100-count/1.0'}
    params = {"after": after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if (response.status_code != 200):
        return

    data = response.json()['data']
    titles = [post['data']['title'] for post in data['children']]

    for children_result in titles:
        title = children_result.lower().split()

        for word in word_list:
            no_times = title.count(word)
            if (no_times > 0):
                results[word] = results.get(word, 0) + no_times

    if not data['after']:
        sort_instances = sorted(
                results.items(),
                key=lambda x: (-x[1], x[0].lower()))
        for word, count in sort_instances:
            if (count > 0):
                print(f"{word.lower()}: {count}")
    else:
        return count_words(subreddit, word_list,
                           after=data['after'], results=results)
