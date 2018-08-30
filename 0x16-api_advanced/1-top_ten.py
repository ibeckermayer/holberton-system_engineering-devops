#!/usr/bin/python3
"""documentation"""
from requests import get
from sys import argv


def top_ten(subreddit):
    """top ten"""
    header = {'User-Agent': 'Isaiah Becker-Mayer'}
    try:
        count = get('https://www.reddit.com/r/{}/hot.json?count=10'.format(
            subreddit), headers=header).json().get('data').get('children')
        print('\n'.join([dic.get('data').get('title')
                         for dic in count][:10]))
    except:
        print('None')


if __name__ == "__main__":
    top_ten(argv[1])
