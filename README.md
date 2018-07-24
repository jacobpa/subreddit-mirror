# subreddit-mirror

This is a simple reddit bot which will copy posts from one subreddit to another,
ideally used for copying posts to a private subreddit for bot development
purposes. It requires you to be a moderator of the subreddit you are copying
posts to, and allows you to choose, along with the source/destination subreddit:

* The sort method of the posts chosen (hot, new, controversial, and top)
* The time frame to grab posts from (day, week, month, year, all)
* How many posts to grab

## Usage
```
usage: subreddit-mirror [-h] [--count COUNT]
                        [--sort {hot,new,controversial,top}]
                        [--time {day,week,month,year,all}]
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
```

### Optional Parameter Defaults
* `--count`: `15`
* `--sort`: `new`
* `--time`: `day`

### Examples

* `$ subreddit-mirror hiphopheads trapmuzik`

    Copies the newest 15 newest poststoday from /r/hiphopheads to /r/trapmuzik
* `$ subreddit-mirror calamariraceteam motorcycles --count 10 --sort top --time all`:

    Copies the top 10 posts of all time from /r/calamariraceteam to /r/motorcycles

## License
```
A bot to copy posts from one subreddit to another.
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
