# A bot to copy posts from one subreddit to another.
# Copyright (C) 2018  Jacob Patterson

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""This module aims to mirror the last n posts of a subreddit, specifically
for testing subreddit-specific bots.
"""
from argparse import ArgumentParser
import praw
import sys
from progress.bar import Bar
from .exceptions import NotModeratorError


def main():
    """Main running function of entire script."""

    reddit = bot_setup()
    args = parse_args(sys.argv[1:])
    print('Gathering posts...')
    posts = get_posts(reddit, args.subreddit, args.count, args.sort, args.time)

    mirror_posts(reddit, args.destination, posts)
    print()


def bot_setup():
    """Start a new Reddit instance.

    This creates a REddit instance based on the [bot] entry in praw.ini
    in the project root directory, or based on the current system user's
    directory. See the `PRAW Documentation on the topic
    <https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html>`_.

    Returns:
        A new praw.Reddit instance
    """
    return praw.Reddit('bot')


def parse_args(args):
    """Parse arguments, represented as a string.

    This function generates an argument parser, and will use this to
    parse a string of command line arguments, which are stored and used
    throughout the program to control different input.

    Arguments:
        args: A string representing command line arguments

    Returns:
        A collection of arguments and their values
    """
    parser = ArgumentParser(prog='subreddit-mirror', description='Mirror posts from another subreddit.')
    parser.add_argument('subreddit', help='subreddit to copy posts from')
    parser.add_argument('destination', help='destination subreddit to post to')
    parser.add_argument('--count', help='how many posts to try to copy',
                        default=15, type=int)
    parser.add_argument('--sort', help='how to sort posts', default='new',
                        choices=['hot', 'new', 'controversial', 'top'])
    parser.add_argument('--time', help='time frame to grab from', default='day',
                        choices=['day', 'week', 'month', 'year', 'all'])

    parsed_args = parser.parse_args(args)

    if parsed_args.count < 1:
        parser.error("Minimum post count is 1")

    return parser.parse_args(args)


def get_posts(reddit, subreddit, count, sort, time):
    """Gets a certain amount of posts from a subreddit, based on a sort
    method and timeframe.

    Arguments:
        reddit: A praw.Reddit instance
        subreddit: A string containing the name of the subreddit to copy
        posts from
        count: The number of posts to copy from subreddit
        sort: The sorting method to use, one of 'hot', 'new',
        'controversial', or 'top'
        time: The timeframe to grab posts from, one of 'day', 'week',
        'month', 'year', or 'all'

    Returns:
        A praw.models.ListingGenerator containing the posts returned by
        the arguments
    """
    return {
        'hot': reddit.subreddit(subreddit).hot(limit=count),
        'new': reddit.subreddit(subreddit).new(limit=count),
        'controversial': reddit.subreddit(subreddit).controversial(time, limit=count),
        'top': reddit.subreddit(subreddit).top(time, limit=count),
    }[sort]


def mirror_posts(reddit, destination, posts):
    """Mirror (crosspost) posts from one subreddit to another

    Arguments:
        reddit: A praw.Reddit instance
        destination: A Subreddit model to post to
        posts: A ListingGenerator containing the posts to crosspost
    """
    successful_posts = 0
    posts = list(posts)
    progress = Bar('Crossposting...', max=len(posts))
    progress.check_tty = False

    if reddit.user.me().name in reddit.subreddit(destination).moderator():
        for post in posts:
            post.crosspost(destination, send_replies=False)
            successful_posts += 1
            progress.next()
        progress.finish()
    else:
        raise NotModeratorError("You are not a moderator of this subreddit.")

    return successful_posts
