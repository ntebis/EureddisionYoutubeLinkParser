import praw
import re
import pandas
import time

# Gets the info from the csv file and posts them as comments.
# It can be improved by going through all comments and removing the upvotes.
# Not sure if it violates any rules.
# Another Improvement. Newly generated playlists.


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





songs = pandas.read_csv('submissions.csv')

for index, row in songs.iterrows():
    body = "[%s - %s (%s)](%s)" % (row['Title'], row['Artist'], row['Date'], row['Link'])
    # print("Adding: %s - %s (%s) - %s" % (row['Title'], row['Artist'], row['Date'], row['Link'])) # Testing
    print(body)
    thread_id.reply(body)
    time.sleep(5) # must be 5 seconds!
