# Autopost.
Automatic comment creation.

This script gets all the links from the csv and then posts a comment for each submission.

A file named *credentials2.txt* must be created with the following information in the specific order.

```
client_id
client_secret
username
password
subreddit
thread_id
```

This script must be run in Python 3 with PRAW and Pandas packages installed and the csv must be named *submissions.csv*
