# COVID-19_Datasets_OnlineVideos
COVID-19-related datasets made querying OVPs (for the time being: YouTube), accompanied by the Python scripts used.

## Regarding the Shared YouTube Dataset
It is based on the result of a “covid-19” query using [YouTube API](https://developers.google.com/youtube/v3/getting-started).

Because of the low API quota (10 000) available for free, the text file only contains 360 entries (free of duplicates, which are filtered out by the script). Thus, it serves more as an example or sample of what you can get with the script than a comprehensive and operable dataset.

Feel free to improve the script as you want.

## Dataset Formatting
Here are the tags used to surround the collected data:
* `<ENTRY number> </ENTRY number>`: Surround all the other tags for each video.
* `<TITLE> </TITLE>`: Surround the title of the video.
* `<URL> </URL>`: Surround the URL of the video.
* `<TIMESTAMP> </TIMESTAMP>`: Surround the ISO 8601 date the video was published.
* `<DESCRIPTION> </DESCRIPTION>`: Surround the description of the video.
* `<TAGS> </TAGS>`: Surround an array consisting of the video tags.
* (Optionnal) `<COMMENT number> </COMMENT number>`: Surround a comment from the comment section of the video. If the query for the comment threads returns an error (such as when comments are disabled), this section is skipped. As regards YouTube, 20 top‐level comments at most are obtained.
* `<CHANNEL TITLE> </CHANNEL TITLE>`: Surround the name of the channel to which the video is attached to.
* `<CHANNEL URL> </CHANNEL URL>`: Surround the URL of the channel to which the video is attached to.

