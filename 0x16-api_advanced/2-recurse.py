#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively fetches titles of hot articles for a subreddit using pagination.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list, optional): A list to store collected titles. Defaults to [].
        after (str, optional): The 'after' parameter for pagination. Defaults to None.

    Returns:
        list: A list containing all hot article titles, or None if an error occurs.
    """

    headers = {'User-Agent': 'My Reddit API Script 0.1'}  # Custom User-Agent

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"

    try:
        response = requests.get(url, allow_redirects=False, headers=headers)
        response.raise_for_status()

        data = response.json()

        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                hot_list.append(post['data']['title'])

            # Check for next page and recurse if necessary
            after = data['data'].get('after')
            if after:
                recurse(subreddit, hot_list.copy(), after)

        return hot_list

    except requests.exceptions.RequestException as e:
        print(f"Error fetching hot articles: {e}")
        return None  # Return None on errors


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = recurse(subreddit)
        if result is not None:
            print(len(result))  # Print the number of articles
        else:
            print("None")  # No results found
