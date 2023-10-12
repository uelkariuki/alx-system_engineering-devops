#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the title of
all hot articles, and prints a sorted count of given keywords
(case-insensitive, delimited by spaces. Javascript should count as
javascript, but java should not).
"""

import requests
import re


def count_words(subreddit, word_list, instances={}, after=None, count=0):
    """
    Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords (case-insensitive,
    delimited by spaces.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'User-agent': '100-count/2.0 (fipis92205@dixiser.com)'}
    params = {"after": after, "count": count, "limit": 100}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    try:
        results = response.json()
        if response.status_code == 404 or results is None:
            raise Exception
    except Exception:
        if not instances:
            print("")
        else:
            sort_instances = sorted(instances.items(),
                                    key=lambda x: (-x[1], x[0]))
            for word, count in sort_instances:
                print(f"{word}: {count}")
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")

    for children_result in results.get("children"):
        title = re.sub(r'[._!]', '', children_result.get("data").
                       get("title").lower()) .split()
        for word in word_list:
            if word.lower() in title:
                no_times = title.count(word.lower())
                instances[word] = instances.get(word, 0) + no_times

    if after is None:
        if not instances:
            print("")
        else:
            sort_instances = sorted(instances.items(),
                                    key=lambda x: (-x[1], x[0]))
            for word, count in sort_instances:
                print(f"{word}: {count}")
    else:
        count_words(subreddit, word_list, instances, after, count)
