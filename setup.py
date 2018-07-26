import setuptools
import subredditmirror

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="subreddit-mirror",
    version=subredditmirror.__version__,
    author="Jacob Patterson",
    author_email="jacob@jacobpa.com",
    entry_points={
        "console_scripts": ['subreddit-mirror = subredditmirror.mirror:main']
    },
    classifiers=['Programming Language :: Python :: 3.6',
                 'Operating System :: OS Independent',
                 'Natural Language :: English'],
    description="A script to copy posts from one subreddit to another.",
    install_requires=['progress==1.4', 'praw==5.4.0'],
    keywords='reddit mirror crosspost bot script',
    license="GPLv3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['subredditmirror'],
    project_urls={
        "Github": "https://github.com/jacobpa/subreddit-mirror",
    },
)
