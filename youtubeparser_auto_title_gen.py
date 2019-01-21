import praw
import re
import urllib
import simplejson as json

# This is a simplier version that auto generates the Titles from the youtube links




with open("credentials.txt", "r") as cred_file:
    creds = cred_file.readlines()

songs = []

# standard praw stuff

reddit = praw.Reddit(client_id=creds[0].strip(),
                     client_secret=creds[1].strip(),
                     username=creds[2].strip(),
                     password=creds[3].strip(),
                     user_agent='Youtube Link Parser')

subreddit = reddit.subreddit(creds[4])

thread_id = reddit.submission(id=creds[5])

comments = thread_id.comments

with open("output.txt", "w") as output_file:
    # looking through comments
    for top_level_comment in comments:
        body = top_level_comment.body
        body = body  #.encode('utf-8') ## add this if running in python 3
        if "yout" in body:
            print(10 * '-')  # testing
            for line in body.split("\n"):
                if not line:
                    continue
                if 'yout' in line:  # making sure it only parses youtube links
                    # dodgy way to split the links and to get the youtube link
                    line = line.replace('[', '|').replace(']', '|').replace('(', '|').replace(')', '|').replace(' ', '|').replace(':', '|', 1)
                    line = line.strip().strip('|')  # deleting spaces and | from the start and the end
                    line = line.split("|")
                    # print(line) #testing
                    print(line[-1].strip())  # testing
                    songs.append(line[-1])

                    output_file.write("%s\n" % line[-1].strip())
                    continue

    # generating the playlists
    output_file.write("\n\n ----------------- Auto generated playlists -----------------\n\n")

    domain = "https://www.youtube.com/watch_videos?video_ids="  # template link for playlists. Maximum 50 per playlist
    count = 0
    songlist = []

    for i in songs:
        i = i.replace('=', ' ').replace('/', ' ')  # replacing '=' and '/' so they can be splitted and the id can be parsed.
        i = i.strip()
        i = i.split()
        # print(i[-1]) #testing
        songlist.append(i[-1])

    tempdomain = domain

    for i in songlist:  # appending video_id to the template

        tempdomain += i
        count += 1
        #naximum limit per playlist is 50
        if count == 50:
            output_file.write("%s\n" % tempdomain.strip())
            # print(tempdomain) #testing
            tempdomain = domain
            count = 0
        else:
            tempdomain += ","

    if tempdomain[-1] == ",":
        tempdomain = tempdomain[:-1]

    output_file.write("%s\n\n" % tempdomain.strip())

titles = []
print('\n\n------------ Generating Titles ------------\n')


for link in songlist:
    url = 'https://noembed.com/embed?url=https://www.youtube.com/watch?v=' + link # link provided from https://stackoverflow.com/questions/30084140/youtube-video-title-with-api-v3-without-api-key by rsp
    json_file = json.load(urllib.request.urlopen(url))
    titles.append(json_file['title'])
    print(json_file['title'])
    
print("\n----------- Finished Title Parsing -----------\n\n")    






# dirty way to make an csv
with open("songs.csv", "w") as result_file:
    result_file.write("Title,Link\n")

    for a, b in zip(titles, songs):
        result_file.write("%s,%s\n" % (a, b))
