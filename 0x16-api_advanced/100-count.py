#!/usr/bin/python3
"""Imports"""
import requests


def count_words(subreddit, word_list):
    """
    Counts occurrences of keywords in hot articles of a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of keywords to search for (case-insensitive).

    Prints:
        Keyword counts in descending order of count, then alphabetically by keyword.
    """

    word_counts = {}
    after = None

    while True:
        # Fetch hot articles for the current page
        data = fetch_hot_articles(subreddit, after)
        if not data:
            break  # No more pages or error

        # Process titles and update word counts
        for post in data.get('data', {}).get('children', []):
            title = post.get('data', {}).get('title', "").lower()
            for word in title.split():
                normalized_word = word.lower()  # Normalize keyword
                if normalized_word in word_list:
                    word_counts[normalized_word] = word_counts.get(normalized_word, 0) + 1

        # Check for next page and update 'after' parameter
        after = data.get('data', {}).get('after')
        if not after:
            break

    # Print sorted word counts (descending by count, then alphabetically)
    if word_counts:
        sorted_counts = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))
        for keyword, count in sorted_counts:
            print(f"{keyword}: {count}")
    else:
        print("No matches found for any keywords.")


def fetch_hot_articles(subreddit, after=None):
    """
    Fetches hot articles from a subreddit using pagination.

    Args:
        subreddit (str): The subreddit to query.
        after (str, optional): The 'after' parameter for pagination. Defaults to None.

    Returns:
        dict: The JSON response from the Reddit API, or None if an error occurs.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"

    headers = {'User-Agent': 'My Reddit API Script 0.1'}  # Custom User-Agent

    try:
        response = requests.get(url, allow_redirects=False, headers=headers)
        response.raise_for_status()  # Raise exception for non-200 status codes

        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching hot articles: {e}")
        return None


if __name__ == '__main__':
    subreddit = input("Enter subreddit name: ")
    word_list = input("Enter keywords separated by spaces: ").split()
    count_words(subreddit, word_list)
