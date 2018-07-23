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
