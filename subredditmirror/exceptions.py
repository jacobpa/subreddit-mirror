# subreddit-mirror -- A script to copy posts from one subreddit to another.
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

"""A collection of exceptions used by the module.
"""


class Error(Exception):
    """Base class for exceptions in this module"""
    pass


class NotModeratorError(Error):
    """Exception raised when user is not a moderator of a subreddit they
    are trying to post to.

    Attributes:
        message: Explanation of the error
    """
    def __init__(self, message):
        self.message = message
