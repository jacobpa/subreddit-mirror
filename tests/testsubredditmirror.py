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
                                    'time': 'day'}
        self.reddit = mirror.bot_setup()

    def test_parse_args_required_args(self):
        args = mirror.parse_args(['s1', 's2'])

        self.assertDictEqual(vars(args), self.expected_dictionary)

    def test_parse_args_optional_args(self):
        self.expected_dictionary['count'] = 20
        self.expected_dictionary['sort'] = 'hot'
        self.expected_dictionary['time'] = 'month'

        args = mirror.parse_args('s1 s2 --count 20 --sort hot --time month'.split())
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
                                      self.expected_dictionary['count'],
                                      self.expected_dictionary['sort'],
                                      self.expected_dictionary['time']))
        successful_posts = mirror.mirror_posts(self.reddit, 'privatesub', posts)

        self.assertEqual(successful_posts, len(posts))
