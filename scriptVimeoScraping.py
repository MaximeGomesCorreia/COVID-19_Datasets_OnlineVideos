import socket
import requests
import math
import json
import vimeo

client = vimeo.VimeoClient(
  token='', #YOUR_ACCESS_TOKEN
  key='', #YOUR_CLIENT_ID
  secret='' #YOUR_CLIENT_SECRET
)

query = "covid-19"
numPerPage = "100"
numCommentsPerVideo = "100"

numVideos = 0
minDuration = 1
maxDuration = 30
durationGap = 30
numForDuration = 0
limitDuration = 100000
limitDate = '2020-06-26T00:00:00+00:00'
lastID = math.inf
strFileName = query + "_VimeoDataset.txt"
while minDuration <= limitDuration:
    strQuery = "https://api.vimeo.com/videos?query=" + query + "&per_page=" + numPerPage + "&min_duration=" + str(minDuration) + "&sort=date" + "&fields=duration,uri,name,link,description,created_time,tags.name,metadata.connections.comments.uri,user.name,user.link" #+ "&max_duration=" + str(maxDuration)
    while True:
        
        requested = False
        while requested == False:
            requested = True
            try:
                HTTPresults = client.get(strQuery)
            except (vimeo.exceptions.APIRateLimitExceededFailure, requests.exceptions.ReadTimeout, socket.timeout):
                requested = False
        results = HTTPresults.json()
        
        if 'data' not in results:
            break
        
        with open(strFileName, 'a+') as outfile:
            for item in results['data']:
                
                videoID = item['uri']
                
                duplicate = False
                currentID = float(videoID.split('/')[2])
                if currentID < lastID:
                    lastID = currentID
                else:
                    duplicate = True

                if duplicate == False:
                    if item['created_time'] < limitDate:

                        numVideos += 1
                        videoTitle=item['name']
                        videoURL = item['link']

                        outfile.write("<ENTRY ")
                        outfile.write(str(numVideos))
                        outfile.write(">\n")

                        outfile.write("<TITLE> ")
                        outfile.write(videoTitle)
                        outfile.write(" </TITLE>\n")

                        outfile.write("<URL> ")
                        outfile.write(videoURL)
                        outfile.write(" </URL>\n")

                        outfile.write("<TIMESTAMP> ")
                        outfile.write(item['created_time'])
                        outfile.write(" </TIMESTAMP>\n")

                        outfile.write("<DESCRIPTION>")
                        description = item['description']
                        if description != None:
                            outfile.write(" ")        
                            outfile.write(description)
                            outfile.write(" ")
                        outfile.write("</DESCRIPTION>\n")

                        outfile.write("<TAGS>")
                        for tag in item['tags']:
                            outfile.write(" #")
                            outfile.write(tag['name'])
                            outfile.write(" ")
                        outfile.write("</TAGS>\n")

                        requested = False
                        commentsRequest = item['metadata']['connections']['comments']['uri'] + "?per_page=" + numCommentsPerVideo + "&fields=text"
                        while requested == False:
                            requested = True
                            try:
                                HTTPcomments = client.get(commentsRequest)
                            except (vimeo.exceptions.APIRateLimitExceededFailure, requests.exceptions.ReadTimeout, socket.timeout):
                                requested = False
                        try:
                            comments = HTTPcomments.json()
                        except json.decoder.JSONDecodeError:
                            requested = False
                        if requested == True:
                            if "data" in comments:
                                i = 0
                                commentTexts = comments['data']
                                for comment in commentTexts:
                                    i = i + 1
                                    outfile.write("<COMMENT ")
                                    outfile.write(str(i))
                                    outfile.write("> ")
                                    outfile.write(comment['text'])
                                    outfile.write(" </COMMENT ")
                                    outfile.write(str(i))
                                    outfile.write(">\n")

                        outfile.write("<CHANNEL TITLE> ")
                        outfile.write(item['user']['name'])
                        outfile.write(" </CHANNEL TITLE>\n")

                        outfile.write("<CHANNEL URL> ")
                        outfile.write(item['user']['link'])
                        outfile.write(" </CHANNEL URL>\n")

                        outfile.write("</ENTRY ")
                        outfile.write(str(numVideos))
                        outfile.write(">\n")

        nextPage = results['paging']['next']
        if nextPage == None:
            break
        strQuery = nextPage
                    
    lastID = math.inf
    minDuration = minDuration + durationGap
    maxDuration = maxDuration + durationGap
