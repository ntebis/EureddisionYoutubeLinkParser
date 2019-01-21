# Eureddision Youtube Link Parser
A Youtube link parser and Youtube playlist Autogenerator.

This script was made to make easier the collection of all links for the Eureddision Contest on reddit. [More info](https://www.reddit.com/r/Eureddision/wiki/faq)

This script *youtubeparser.py* parses all the Youtube links from the top level comments on a thread. It seems to be working properly using the formatting of the [/r/greece thread](https://www.reddit.com/r/greece/comments/agyb3i/). There is a second version of the script named *youtubeparser_auto_title_gen.py* which automatically generates the Titles from the youtube links.

In order to use this script, you must have the Python 3 suite and have PRAW installed and SimpleJSON. Also, you need to create an app on Reddit by going Preferences -> Apps -> Create your App.

A file name credentials.txt must be made and the following in the specific order:

```
client_id
client_secret
username
password
subreddit
thread_id
```

This app may not work properly if you have 2FA activated.

Auto generated playlist, have a maximum limit of 50 songs. This script creates new playlist every 50 songs.

It now supports not formatted submissions for other subreddits, by autogenerating titles from the youtube links 


I will also try to create another script that will randomly post all song links with titles and year. It probably required to create a csv file instead the current implementation.

This is my first ever script on python and while I have programming experience, my python experience is close to none. Any tips are welcome.
