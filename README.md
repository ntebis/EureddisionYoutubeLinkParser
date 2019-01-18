# Eureddision Youtube Link Parser
A Youtube link parser and Youtube playlist Autogenerator.

This script was made to make easier the collection of all links for the Eureddision Contest on reddit. [More info](https://www.reddit.com/r/Eureddision/wiki/faq)

This script parses all the Youtube links from the top level comments on a thread. It seems to be working properly on the [/r/greece thread](https://www.reddit.com/r/greece/comments/agyb3i/).

In order to use this script, you must have the Python suite and have PRAW installed. Also, you need to create an app by going Preferences -> Apps -> Create your App.

A file name credentials.txt must be made and the following in the specific order:

client_id

client_secret

username

password

subreddit

thread_id

This app may not work properly if you have 2FA activated.

I will also try to create another script that will randomly post all song links with titles and year. It probably required to create a csv file instead the current implementation.

This is my first ever script on python and while I have programming experience, my python experience is close to none. Any tips are welcome.
