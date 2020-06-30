# COVID-19_Datasets_OnlineVideos
COVID-19-related datasets made querying OVPs (YouTube and Vimeo), accompanied by the Python scripts used (feel free to improve them as you want).

## Regarding the Shared Vimeo Dataset
It has been made using [Vimeo API](https://developer.vimeo.com/api/reference) and contains data on *all* videos which are returned by a “covid‐19” query and were uploaded before June 26, 2020 (93 896 entries, without duplicates). 

Because it was too big for GitHub, what’s in the repository is a text file which holds a [download link](https://mega.nz/file/bFID3QCB#iZ2XN2fj2pijqzPMNOrF_g0gfvg96aCsP9PLuP_cQW8) for the dataset.

## Regarding the Shared YouTube Dataset
It is based on the result of a “covid‐19” query using [YouTube API](https://developers.google.com/youtube/v3/getting-started).

Because of the low API quota (10 000) available for free, the text file only contains 360 entries (free of duplicates, which are filtered out by the script). Thus, it serves more as an example or sample of what you can get with the script than a comprehensive and operable dataset.

## Dataset Formatting
Here are the tags used to surround the collected data:
* `<ENTRY number> </ENTRY number>`: Surround all the other tags for each video.
* `<TITLE> </TITLE>`: Surround the title of the video.
* `<URL> </URL>`: Surround the URL of the video.
* `<TIMESTAMP> </TIMESTAMP>`: Surround the ISO 8601 date the video was published.
* `<DESCRIPTION> </DESCRIPTION>`: Surround the description of the video.
* `<TAGS> </TAGS>`: For **YouTube**: Surround an array consisting of the video tags. For **Vimeo**: Surround spaced tags, each of them beginning with a hashtag.
* (Optionnal) `<COMMENT number> </COMMENT number>`: Surround a comment from the comment section of the video. If the query for the comment threads returns an error (such as when comments are disabled), this section is skipped. As regards **YouTube**, 20 (top‐level) comments at most are obtained; as regards **Vimeo**, it’s 100 (top-level too) comments.
* `<CHANNEL TITLE> </CHANNEL TITLE>`: Surround the name of the channel to which the video is attached to.
* `<CHANNEL URL> </CHANNEL URL>`: Surround the URL of the channel to which the video is attached to.

