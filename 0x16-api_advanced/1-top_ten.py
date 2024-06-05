#!/usr/bin/python3
"""Importation"""
import requests


def top_ten(subreddit):
    """
    Queries Reddit API and prints titles of the first 10 hot posts for a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
    """

    headers = {'User-Agent': 'My Reddit API Script 0.1'}  # Custom User-Agent

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    try:
        response = requests.get(url, allow_redirects=False, headers=headers)
        response.raise_for_status()

        data = response.json()

        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                title = post['data']['title']
                print(title)
                if len(data['data']['children']) == 10:  # Check if 10 posts found
                    return

    except requests.exceptions.RequestException as e:
        print(f"Error fetching hot articles: {e}")
        return None  # Return None on errors
    else:
        print("None")  # No results found (less than 10 posts)


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
