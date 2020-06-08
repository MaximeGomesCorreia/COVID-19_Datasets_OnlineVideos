# COVID-19_Datasets_OnlineVideos
COVID-19-related datasets made scraping OVPs (for the time being: YouTube), accompanied by the Python scripts used.

## About the Shared YouTube Dataset
Because of the low API quota (10,000) available for free, the text file only contains 370 entries. Thus, it serves more as an example or sample of what you can get with the script than a comprehensive dataset. 

## Dataset Formating
Here are the tags used to surround the scraped data:
* `<ENTRY number> </ENTRY number>`: Surround all the other tags for each video.
* `<TITLE> </TITLE>`: Surround the title of the video.
* `<URL> </URL>`: Surround the URL of the video.
* `<DESCRIPTION> </DESCRIPTION>`: Surround the description of the video.
* `<TAGS> </TAGS>`: Surround an array consisting of the video tags.
* (Optionnal) `<COMMENT number> </COMMENT number>`: Surround a comment from the comment section of the video. If the request for the comments threads returns an error (such as when comments are disabled), this section is skipped.
* `<CHANNEL TITLE> </CHANNEL TITLE>`: Surround the name of the channel to which the video is attached to.
* `<CHANNEL URL> </CHANNEL URL>`: Surround the URL of the channel to which the video is attached to.

