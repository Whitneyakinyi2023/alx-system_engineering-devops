#!/usr/bin/python3
"""importaation"""

import requests
import re
import json


def count_words(subreddit, word_list, word_counts={}, after=None):
    """
    Recursively queries Reddit API to count occurrences of keywords in hot articles.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of keywords to search for (case-insensitive).
        word_counts (dict, optional): A dictionary to store keyword counts. Defaults to {}.
        after (str, optional): The 'after' parameter for pagination. Defaults to None.

    Returns:
        None: The function doesn't return a value, it directly prints the results.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"

    headers = {'User-Agent': 'My Reddit API Script 0.1'}  # Custom User-Agent

    try:
        response = requests.get(url, allow_redirects=False, headers=headers)
        response.raise_for_status()

        data = response.json()

        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                title = post['data']['title'].lower()

                # Preprocess title to remove trailing punctuation and spaces
                title = re.sub(r"[^\w\s]", "", title).strip()

                # Split title into words and iterate through word list
                for word in title.split():
                    # Normalize keyword (lowercase and remove punctuation)
                    keyword = re.sub(r"[^\w]", "", word.lower())
                    if keyword in word_list:
                        word_counts[keyword] = word_counts.get(keyword, 0) + 1

            # Check for next page and recurse if necessary
            after = data['data'].get('after')
            if after:
                count_words(subreddit, word_list, word_counts.copy(), after)

        # Print results only if there are any matches
        if word_counts:
            sorted_counts = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))
            for keyword, count in sorted_counts:
                print(f"{keyword}: {count}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


