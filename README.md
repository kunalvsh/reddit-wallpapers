### Personal Projects

Hello! This is a repository for several of my personal side projects -- let the hacking commence. 

### RedditImages.py

My first try at a more robust Reddit bot. I'm using PRAW, as well as the urllib library. This bot takes in a subreddit as a command-line argument. Depending on what is put in the resolutions array, the bot will then travel the specified subreddit, looking through the hottest 15 submissions and download them if the resolution is correct. The images will be downloaded to the directory the Python script is in.

To execute this bot, type:

`
python redditimages.py [subreddit]
`

An example would be:

`
python redditimages.py wallpapers
`

You need PRAW to run this. 

`
pip install praw` or `easy_install praw` should do the trick.

### FizzBuzzKoding.py

This is FizzBuzz coded in Python for the Koding Summer 2014 Summer Internship application.

### CommentParser.py

This is an extremely simple bot -- mainly used for testing out PRAW capabilities. 