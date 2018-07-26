# subreddit-mirror

This is a simple script which will copy posts from one subreddit to another,
ideally used for copying posts to a private subreddit for bot development
purposes. It requires you to be a moderator of the subreddit you are copying
posts to, and allows you to choose, along with the source/destination subreddit:

* The sort method of the posts chosen (hot, new, controversial, and top)
* The time frame to grab posts from (day, week, month, year, all)
* How many posts to grab
* Whether or not to include the comments from the post you mirrored (this
  functionality is very time consuming)

### Why?

Whenever I create reddit bots, I would normally manually create posts that mimic
the posts I would expect when using my bot. This becomes tedious, especially as
the bot grows more dynamic over time. Instead, I figured I could write a script
which would do this tedious work for me, and as an added bonus, the content
would be real data from the subreddits I would be targeting. 

#### Can't you use this for spam?

I suppose so, but you shouldn't. This script includes a simple check to make
sure that you're a moderator of the subreddit your mirroring posts to. Although
this is easy enough to remove, I figured that anyone who'd want to make a spam
bot could and probably would have without much effort.

## Installation

```
$ pip install subreddit-mirror
```

Alternatively, manually download and install the release file from the Github release page.

## Usage
```
usage: subreddit-mirror [-h] [--count COUNT]
                        [--sort {hot,new,controversial,top}]
                        [--time {day,week,month,year,all}] [--comments] [-v]
                        subreddit destination

Mirror posts from another subreddit.

positional arguments:
  subreddit             subreddit to copy posts from
  destination           destination subreddit to post to

optional arguments:
  -h, --help            show this help message and exit
  --count COUNT         how many posts to try to copy
  --sort {hot,new,controversial,top}
                        how to sort posts
  --time {day,week,month,year,all}
                        time frame to grab from
  --comments            [CAUTION] also mirror comments from threads, may take
                        a long time
  -v, --version         show program's version number and exit
```

### Optional Parameter Defaults

| Option       | Default Parameter |
|--------------|-------------------|
| `--count`    | `15`              |
| `--sort`     | `'new'`           |
| `--time`     | `'day'`           |
| `--comments` | `False`           |


### Examples

* `$ subreddit-mirror hiphopheads trapmuzik`

    Copies the newest 15 newest poststoday from /r/hiphopheads to /r/trapmuzik
* `$ subreddit-mirror calamariraceteam motorcycles --count 10 --sort top --time all`:

    Copies the top 10 posts of all time from /r/calamariraceteam to /r/motorcycles

## Dependencies
* [PRAW](https://github.com/praw-dev/praw)
* [progress](https://github.com/verigak/progress) 

## License
```
subreddit-mirror -- A script to copy posts from one subreddit to another.
Copyright (C) 2018  Jacob Patterson

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```
