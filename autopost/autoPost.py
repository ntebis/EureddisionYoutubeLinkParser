import praw
import re
import pandas
import time

# This script parses all the links from the eureddision thread and outputs into a txt file.
# The links than can be used in playlist generators online.
# Also planning to do a script that will post all submissions randomly.

# Needs a file named credentials.txt with client_id client_secre


with open("credentials2.txt", "r") as cred_file:
    creds = cred_file.readlines()

songs = []
titles = []
artist = []
date = []

# standard praw stuff

reddit = praw.Reddit(client_id=creds[0].strip(),
                     client_secret=creds[1].strip(),
                     username=creds[2].strip(),
                     password=creds[3].strip(),
                     user_agent='Youtube Link Parser')

subreddit = reddit.subreddit(creds[4])

thread_id = reddit.submission(id=creds[5])





songs = pandas.read_csv('songs.csv')

for index, row in songs.iterrows():
    body = "[%s - %s (%s)](%s)" % (row['Title'], row['Artist'], row['Date'], row['Link'])
    # print("Adding: %s - %s (%s) - %s" % (row['Title'], row['Artist'], row['Date'], row['Link']))
    print(body)
    # thread_id.reply(body)
    time.sleep(0.1)