#!/usr/bin/python3
"""doc"""
from requests import get
from sys import argv


def number_of_subscribers(subreddit):
    """get number of subscribers for a subreddit"""
    header = {'User-Agent': 'Isaiah Becker-Mayer'}
    count = get('https://www.reddit.com/r/{}/about.json'.format(
        subreddit), headers=header).json()
    try:
        return count.get('data').get('subscribers')
    except:
        return 0

if __name__ == "__main__":
    number_of_subscribers(argv[1])
