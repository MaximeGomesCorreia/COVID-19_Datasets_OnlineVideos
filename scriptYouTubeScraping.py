from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def get_video_comments(service, **kwargs):
    comments = []
    results = service.commentThreads().list(**kwargs).execute()
    for item in results['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)
    return comments

def scrap_videos_by_keyword(service, numPages, **kwargs):
    page = 1
    numVideos = 0
    results = service.search().list(**kwargs).execute()
    while results:
        with open(f"{kwargs.get('q')}_YouTubeDataset.txt", 'a+') as outfile:
            for item in results['items']:
                numVideos += 1
                video_id=item['id']['videoId']
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
                try:
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
                outfile.write('</ENTRY {numVideos}>\n')
                print('%d. %s / %s' % (numVideos, video_title, video_id))
        if page < numPages and 'nextPageToken' in results:
                kwargs['pageToken'] = results['nextPageToken']
                results = service.search().list(**kwargs).execute()
                page += 1
        else:
            break
                

api_key = "AIzaSyCO6WT__ir5rhRSp_7jtUDpP0YZwLaZRC0"

api_service_name = 'youtube'
api_version = 'v3'
youtube = build(api_service_name, api_version, developerKey=api_key)

numPages = 10000

scrap_videos_by_keyword(youtube, numPages, part='id, snippet', q='covid19', relevanceLanguage="en", type='video')