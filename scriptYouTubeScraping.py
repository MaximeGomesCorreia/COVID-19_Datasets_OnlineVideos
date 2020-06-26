from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def get_video_comments(service, **kwargs): #Returns 20 top-level comments from the video.
    comments = []
    results = service.commentThreads().list(**kwargs).execute()
    for item in results['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)
    return comments

def scrap_videos_by_keyword(service, numPages, **kwargs):
    page = 1
    numVideos = 0
    IDList = []
    results = service.search().list(**kwargs).execute()
    while results:
        with open(f"{kwargs.get('q')}_YouTubeDataset.txt", 'a+') as outfile:
            for item in results['items']:
                video_id=item['id']['videoId']
                duplicate = False
                for ID in reversed(IDList):
                    if video_id == URL:
                        duplicate = True
                        break
                if duplicate == False:
                    IDList.append(video_id)
                    numVideos += 1
                    video_title=item['snippet']['title']
                    outfile.write(f"<ENTRY {numVideos}>\n")
                    outfile.write(f"<TITLE> {video_title} </TITLE>\n")
                    outfile.write(f"<URL> https://www.youtube.com/watch?v={video_id} </URL>\n")
                    outfile.write(f"<TIMESTAMP> {item['snippet']['publishedAt']} </TIMESTAMP>\n")
                    outfile.write(f"<DESCRIPTION> {item['snippet']['description']} </DESCRIPTION>\n")
                    outfile.write(f"<TAGS> ")
                    videoInfo = service.videos().list(part='snippet', id=video_id).execute()
                    outfile.write(str(videoInfo.get("items")[0].get("snippet").get("tags")))
                    outfile.write(f" </TAGS>\n")
                    try: #This try and except block allows to keep going with the scraping when the query for comment threads returns an error.
                        comments = get_video_comments(service, part='snippet', videoId=video_id, textFormat='plainText')
                        i = 0
                        for comment in comments:
                            i = i + 1
                            outfile.write(f"<COMMENT {i}> ")
                            outfile.write(comment)
                            outfile.write(f" </COMMENT {i}>\n")
                    except HttpError as err:
                        print(err)
                    outfile.write(f"<CHANNEL TITLE> {item['snippet']['channelTitle']} </CHANNEL TITLE>\n")
                    outfile.write(f"<CHANNEL URL> https://www.youtube.com/channel/{item['snippet']['channelId']} </CHANNEL URL>\n")
                    outfile.write(f"</ENTRY {numVideos}>\n")
                    print('%d. %s / %s' % (numVideos, video_title, video_id)) #Optionnal line used to see the progress of the querying.
        if page < numPages and 'nextPageToken' in results: #Updates the page token before running a new query.
                kwargs['pageToken'] = results['nextPageToken']
                results = service.search().list(**kwargs).execute()
                page += 1
        else:
            break
                

api_key = "" #Your API key.

api_service_name = 'youtube'
api_version = 'v3'
youtube = build(api_service_name, api_version, developerKey=api_key)

numPages = 10000 #= 50,000 videos

scrap_videos_by_keyword(youtube, numPages, part='id, snippet', q='covid19', relevanceLanguage="en", type='video')