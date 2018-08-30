#!/usr/bin/python3
"""documentation"""
from requests import get
from sys import argv


def recurse(subreddit, hotlist=[], after=None):
    """recursive"""
    header = {'User-Agent': 'Isaiah Becker-Mayer'}
    try:
        if after:
            count = get('https://www.reddit.com/r/{}/hot.json?after={}'.format(
                subreddit, after), headers=header).json().get('data')
        else:
            count = get('https://www.reddit.com/r/{}/hot.json'.format(
                subreddit), headers=header).json().get('data')
        hotlist += [dic.get('data').get('title')
                    for dic in count.get('children')]
        if count.get('after'):
            return recurse(subreddit, hotlist, after=count.get('after'))
        return hotlist
    except:
        return None


if __name__ == "__main__":
    recurse(argv[1])
