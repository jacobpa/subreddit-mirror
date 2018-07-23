import unittest
from argparse import ArgumentError
from subredditmirror import mirror


class MirrorTest(unittest.TestCase):
    def setUp(self):
        self.expected_dictionary = {'subreddit': 's1',
                                    'destination': 's2',
                                    'count': 15,
                                    'sort': 'new',
                                    'time': 'day'}

    def test_parse_args_required_args(self):
        args = mirror.parse_args(['s1', 's2'])

        self.assertDictEqual(vars(args), self.expected_dictionary)

    def test_parse_args_optional_args(self):
        self.expected_dictionary['count'] = 20
        self.expected_dictionary['sort'] = 'hot'
        self.expected_dictionary['time'] = 'month'

        args = mirror.parse_args('s1 s2 --count 20 --sort hot --time month'.split())
        self.assertDictEqual(vars(args), self.expected_dictionary)
