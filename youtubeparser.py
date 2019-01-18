import praw
import re



# This script parses all the links from the eureddision thread and outputs into a txt file.
# The links than can be used in playlist generators online.
# Also planning to do a script that will post all submissions randomly.

# Needs a file named credentials.txt with client_id client_secre




file = open("credentials.txt", "r")

creds = file.readlines()

file.close()

songs = []

reddit = praw.Reddit(client_id = creds[0].strip() ,
                     client_secret = creds[1].strip() ,
                     username = creds[2].strip() ,
                     password = creds[3].strip() ,
                     user_agent = 'Youtube Link Parser')

subreddit = reddit.subreddit('greece')

thread_id = reddit.submission(id='agyb3i')

comments = thread_id.comments

file = open("output.txt", "w")

for top_level_comment in comments:
    # print(top_level_comment.body)
    body = top_level_comment.body
    for line in body.split("\n"):
        if 'yout' in line: #making sure it only parses youtube links
            print(10*'-')   
            line = line.replace('*','').replace('[','|').replace(']','|').replace('(','|').replace(')','|').replace(' ','|').replace(':', '|',1)
            line = line.strip().strip('|')
            line = line.split("|")
            # print(line)
            print(line[-1].strip())
            songs.append(line[-1])
            
            file.write("%s\n" % line[-1].strip())




#generating the playlists
file.write("\n ----------------- \nAuto generated playlists\n")

domain = "https://www.youtube.com/watch_videos?video_ids="
count = 0
songlist = []

for i in songs:
    i = i.replace('=', ' ').replace('/', ' ')
    i = i.strip()
    i = i.split()
    print(i[-1])
    songlist.append(i[-1])

tempdomain = domain

for i in songlist:
    
    tempdomain += i
    count += 1

    if count == 50:
        file.write("%s\n" % tempdomain.strip())
        print(tempdomain)
        tempdomain = domain
        count = 0
    else:
        tempdomain += ","

if tempdomain[-1] == ",":
   tempdomain = tempdomain[:-1]     
file.write("%s\n" % tempdomain.strip())



    

    




file.close()            
            
