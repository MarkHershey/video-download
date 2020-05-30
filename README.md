# Convenient Script to Download Video from URL with Default Settings

### Dependencies
- [youtube-dl](https://github.com/ytdl-org/youtube-dl)
- [aria2c](https://aria2.github.io/)
- [FFmpeg](https://ffmpeg.org/)

Refer to their respective official installation guides.

##### For macOS user:

Use the following commands in Terminal:

- `brew install youtube-dl`
- `brew aria2`
- `brew ffmpeg`




### Default Settings

- Default to download the `best video-only file` and the `best audio-only file`, then merge them into `mp4` using `FFmpeg`
- Default to name video file as `<Video Title>_<Resolution>.<Extension>`
- Default to save file into system download folder under current user's home directory.
- If the script cannot find the system download folder, file will be saved into `Downloads` folder under current working directory.


### Usage

Use without aria2:
```
python3 dl.py <URL of Video>
```
or

Use aria2 to download:
```
python3 dl.py <URL of Video> <Number of Threads for aria2>
```

Example Usage:
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
