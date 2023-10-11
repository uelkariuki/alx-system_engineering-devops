#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the title of
all hot articles, and prints a sorted count of given keywords
(case-insensitive, delimited by spaces. Javascript should count as
javascript, but java should not).
"""

import requests


def count_words(subreddit, word_list, instances={}, after=None, count=0):
    """
    Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords (case-insensitive,
    delimited by spaces.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'User-agent': '100-count/1.0 (fipis92205@dixiser.com)'}
    params = {"after": after, "count": count, "limit": 100}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    try:
        all_data = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return
    Data = all_data.get("data")
    after = Data.get("after")
    count += Data.get("dist")
    children = Data.get("children")

    for children_result in children:
        title = children_result.get("data").get("title").lower().split()
        for word in word_list:
            word = word.lower()
            no_times = title.count(word)
            if no_times > 0:
                instances[word] = instances.get(word, 0) + no_times

    if after is None:
        if not instances:
            print("")
        else:
            sort_instances = sorted(
                                    instances.items(), key=lambda
                                    key_value: (key_value[1],
                                                key_value[0])
                                    )
            for key, value in sort_instances:
                print(f"{key}: {value}")
    else:
        count_words(subreddit, word_list, instances, after, count)
