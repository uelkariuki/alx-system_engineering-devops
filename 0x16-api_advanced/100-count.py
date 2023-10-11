#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the title of
all hot articles, and prints a sorted count of given keywords
(case-insensitive, delimited by spaces. Javascript should count as
javascript, but java should not).
"""

import requests
import re
from collections import Counter


def count_words(subreddit, word_list, after=None, counter=None):
    """
    Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords (case-insensitive,
    delimited by spaces.
    """
    if counter is None:
        counter = Counter()
    headers = {'User-agent': '100-count/1.0 (fipis92205@dixiser.com)'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    data = response.json()
    if (response.status_code != 200 or "data" not in data
            or "children" not in data["data"]):
        return
    for post in data["data"]["children"]:
        title = post["data"]["title"].lower()
        for word in word_list:
            counter[word] += len(re.findall(rf"\b{word}\b", title))

    if "after" in data["data"] and data["data"]["after"]:
        count_words(subreddit, word_list,
                    after=data["data"]["after"], counter=counter)
    else:
        count_sorted = sorted([(key, value) for key, value in
                              counter.items() if value > 0],
                              key=lambda x: (-x[1], x[0]))
        result = sorted(count_sorted)
        for word, count in result:
            print(f"{word}: {count}")
