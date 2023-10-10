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
    all_data = response.json()
    if (response.status_code == 200 and "data" in all_data
            and "children" in all_data["data"]):
        for post in all_data["data"]["children"]:
            title = post["data"]["title"]
            for word in word_list:
                counter[word] += len(re.findall(rf"\b{word}\b", title))
    else:
        return

    if "after" in all_data["data"] and all_data["data"]["after"]:
        count_words(subreddit, word_list,
                    after=all_data["data"]["after"], counter=counter)
    else:
        count_sorted = sorted([(key, value) for key, value in
                              counter.items() if value > 0],
                              key=lambda x: (-x[1], x[0]))
        for word, count in count_sorted:
            print(f"{word}: {count}")
