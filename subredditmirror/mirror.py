"""This module aims to mirror the last n posts of a subreddit, specifically
for testing subreddit-specific bots.
"""
from argparse import ArgumentParser
import praw
import sys


def bot_setup():
    return praw.Reddit('bot')


def parse_args(args):
    parser = ArgumentParser(description='Mirror posts from another subreddit.')
    parser.add_argument('subreddit', help='subreddit to copy posts from')
    parser.add_argument('destination', help='destination subreddit to post to')
    parser.add_argument('--count', help='how many posts to try to copy',
                        default=15, type=int)
    parser.add_argument('--sort', help='how to sort posts', default='new',
                        choices=['hot', 'new', 'controversial', 'top'])
    parser.add_argument('--time', help='time frame to grab from', default='day',
                        choices=['day', 'week', 'month', 'year', 'all'])

    return parser.parse_args(args)


def get_posts(reddit, subreddit, count, sort, time):
    return {
        'hot': reddit.subreddit(subreddit).hot(limit=count),
        'new': reddit.subreddit(subreddit).new(limit=count),
        'controversial': reddit.subreddit(subreddit).controversial(time, limit=count),
        'top': reddit.subreddit(subreddit).top(time, limit=count),
    }[sort]


if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    print(vars(args))
