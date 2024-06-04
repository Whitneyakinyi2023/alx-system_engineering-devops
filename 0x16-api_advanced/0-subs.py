#!/usr/bin/python3
"""
API request for number of reddit subscribers
"""

import json
import requests
import sys


def number_of_subscribers(subreddit):
  """Queries the Reddit API to get the number of subscribers for a given subreddit.

  Args:
      subreddit: The name of the subreddit to query (string).

  Returns:
      The number of subscribers for the subreddit (integer), or 0 if the subreddit
      is invalid or an error occurs.
  """

  url = f"https://www.reddit.com/r/{subreddit}/about.json"
  headers = {'User-Agent': 'My Reddit API Script 0.1'}  # Custom User-Agent

  try:
    response = requests.get(url, allow_redirects=False, headers=headers)
    response.raise_for_status()  # Raise an exception for non-200 status codes

    data = response.json()
    if 'data' in data and 'subscribers' in data['data']:
      return data['data']['subscribers']
    else:
      return 0  # Invalid subreddit or unexpected response format

  except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    return 0

if __name__ == '__main__':
  import sys

  if len(sys.argv) < 2:
    print("Please pass an argument for the subreddit to search.")
  else:
    subreddit = sys.argv[1]
    subscribers = number_of_subscribers(subreddit)
    print(subscribers)
