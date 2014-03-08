# This bot will (hopefully) traverse subreddits, look for submissions
# with 1920 by XXXX, XXXX by 1080, a 1200 by XXXX, or a XXXX by 1200 resolution, 
# and download them to a local directory.
# suggested subreddits: wallpapers, EarthPorn, HistoryPorn, SpacePorn, etc. (not actually porn)
# by kunal shah

import re
import praw
import urllib 
import os
import requests
import sys

if len(sys.argv) < 2:
  # no command line options
  print('You need to give me a subreddit to look through!')
  sys.exit()
elif len(sys.argv) >= 2:
  # the subreddit was specified
  desiredSubreddit = sys.argv[1]

r = praw.Reddit("Let's get some wallpapers, eh?")

subreddit = r.get_subreddit(desiredSubreddit)

submissions = subreddit.get_hot(limit = 15)
# or, alternatively use one of these
#                                       .get_top_from_year(limit=25)
#                                       .get_top_from_month(limit=25)
#                                       .get_top_from_week(limit=25)
#                                       .get_top_from_day(limit=25)
#                                       .get_top_from_hour(limit=25)
#                                       .get_top_from_all(limit=25)

already_done = set()
resolution = ['1920', '1080', '1200']

# function for downloading image using urllib
def downloadImage (imageUrl, fileName):
  urllib.urlretrieve(imageUrl, fileName + ".jpg")

print "Looking for images..."

try:

  for submission in submissions:
    # check to see if resolution is right
    my_res = any(string in submission.title for string in resolution)
    if submission.id not in already_done and my_res:
      # checking to see if submission is an imgur URL
      if "imgur.com/" not in submission.url:
        print "No imgur, no go"
        continue 
      if 'http://i.imgur.com/' in submission.url:
        # direct link to image
        print "Found one! Downloading: " + submission.title
        downloadImage(submission.url, submission.title)
        already_done.add(submission.id)
        
# make sure user entered a valid subreddit
except:
  print "That wasn't a correct subreddit. Please enter a valid one."
  sys.exit()

# didn't find any :(
if len(already_done) == 0:
  print "Looks like no images matched your specifications."
  print "Try a different subreddit or a different get_() command!"

# some general stats  
elif len(already_done) > 0:
  print "We downloaded %i images from r/%s." % (len(already_done), desiredSubreddit)
      