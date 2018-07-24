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

import unittest
import praw
from prawcore import exceptions
from argparse import ArgumentError
from subredditmirror import mirror
import subredditmirror.exceptions


class MirrorTest(unittest.TestCase):
    def setUp(self):
        self.expected_dictionary = {'subreddit': 's1',
                                    'destination': 's2',
                                    'count': 15,
                                    'sort': 'new',
                                    'time': 'day',
                                    'comments': False}
        self.reddit = mirror.bot_setup()

    def test_parse_args_required_args(self):
        args = mirror.parse_args(['s1', 's2'])

        self.assertDictEqual(vars(args), self.expected_dictionary)

    def test_parse_args_optional_args(self):
        self.expected_dictionary['count'] = 20
        self.expected_dictionary['sort'] = 'hot'
        self.expected_dictionary['time'] = 'month'
        self.expected_dictionary['comments'] = True

        args = mirror.parse_args('s1 s2 --count 20 --sort hot --time month --comments'.split())
        self.assertDictEqual(vars(args), self.expected_dictionary)

    def test_get_posts_defaults(self):
        posts = list(mirror.get_posts(self.reddit,
                                      'sneakerdeals',
                                      self.expected_dictionary['count'],
                                      self.expected_dictionary['sort'],
                                      self.expected_dictionary['time']))
        self.assertLessEqual(len(posts), self.expected_dictionary['count'])

    def test_get_posts_nondefaults(self):
        posts = list(mirror.get_posts(self.reddit,
                                      'sneakerdeals',
                                      10,
                                      'controversial',
                                      'year'))
        self.assertLessEqual(len(posts), 10)

    def test_mirror_subreddit_not_moderator(self):
        posts = list(mirror.get_posts(self.reddit,
                                      'sneakerdeals',
                                      self.expected_dictionary['count'],
                                      self.expected_dictionary['sort'],
                                      self.expected_dictionary['time']))
        with self.assertRaises(subredditmirror.exceptions.NotModeratorError):
            mirror.mirror_posts(self.reddit, 'hiphopheads', posts)

    def test_mirror_subreddit_moderator(self):
        posts = list(mirror.get_posts(self.reddit,
                                      'sneakerdeals',
                                      5,
                                      self.expected_dictionary['sort'],
                                      self.expected_dictionary['time']))
        successful_posts = len(mirror.mirror_posts(self.reddit, 'privatesub', posts))

        self.assertEqual(successful_posts, len(posts))
