# Convenient Script to Download Video with Best Quality from URL

### Dependencies
- [youtube-dl](https://github.com/ytdl-org/youtube-dl)
- [aria2c](https://aria2.github.io/)
- [FFmpeg](https://ffmpeg.org/)


### How to Install Dependencies

##### For macOS user:

Use the following commands in Terminal:
- `brew install youtube-dl`
- `brew aria2`
- `brew ffmpeg`

##### For other OS user:

Refer to their respective official installation guides.


### Usage


```
# without using aria2
python3 dl.py <URL of Video>
```
or
```
# use aria2 to download
python3 dl.py <URL of Video> <Number of Threads for aria2>
```

Example:
```
python3 dl.py https://www.youtube.com/watch\?v\=F4a4X8iYOgQ 8
```

Expected log output:
```
INFO: Video will be downloaded into /Users/mark/Downloads
INFO: Calling youtube-dl
INFO: Using aria2 with 8 threads
[youtube] F4a4X8iYOgQ: Downloading webpage
[download] Destination: /Users/mark/Downloads/Work - Rihanna ft.Drake (R3hab Remix) _ May J Lee Choreography_1920x1080.f137.mp4
[download] 100% of 61.50MiB in 00:02
[download] Destination: /Users/mark/Downloads/Work - Rihanna ft.Drake (R3hab Remix) _ May J Lee Choreography_NA.f140.m4a
[download] 100% of 4.37MiB in 00:00
[ffmpeg] Merging formats into "/Users/mark/Downloads/Work - Rihanna ft.Drake (R3hab Remix) _ May J Lee Choreography_1920x1080.mp4"
Deleting original file /Users/mark/Downloads/Work - Rihanna ft.Drake (R3hab Remix) _ May J Lee Choreography_1920x1080.f137.mp4 (pass -k to keep)
Deleting original file /Users/mark/Downloads/Work - Rihanna ft.Drake (R3hab Remix) _ May J Lee Choreography_NA.f140.m4a (pass -k to keep)
```
