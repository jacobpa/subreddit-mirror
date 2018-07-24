import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="subreddit-mirror",
    version="0.0.1",
    author="Jacob Patterson",
    author_email="jacob@jacobpa.com",
    description="Copy posts from one subreddit to another",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['subredditmirror'],
    entry_points={
        "console_scripts": ['subreddit-mirror = subredditmirror.mirror:main']
    }
)
