# pip3 install pytube

import pytube
import time
import datetime
import os

from FileOperations import move_files

links = [
    "https://www.youtube.com/watch?v=Fg3R5QU5jJE",
    "https://www.youtube.com/watch?v=a73eydgJkMo"
]
destination = "/home/sangee/Videos"
movingDirectory = "/home/sangee/Videos/ArjunSongs"


def download_videos(youtube_links):
    resolutions = ["1080p", "720p", "480p", "360p"]
    for link in youtube_links:
        yt = pytube.YouTube(link)
        for resolution in resolutions:
            stream = yt.streams.filter(res=resolution).first()
            if stream is not None:
                break;
        start_time = time.time();
        print("Start Time for Download Link " + link + " " + str(datetime.datetime.now()))
        print("Download Started ".center(50, "*"))
        stream.download(output_path=destination)
        finish_time = time.time();
        print("Download finished ".center(50, "*"))
        print("Finish Time for Download Link " + link + " " + str(datetime.datetime.now()))
        interval = finish_time - start_time
        duration = str(round(interval / 60, 3)) + " Minutes " + str(round(interval % 60, 3)) + " Seconds"
        print(("Time taken for downloading " + link + " is " + duration).center(50, "*"))


# Downloading the links
download_videos(links)

# check whether directory is present
if not os.path.exists(movingDirectory):
    os.makedirs(movingDirectory)


print(("Files are copied from "+destination+" to "+movingDirectory).center(70, "*"))
# moving downloads to directory
move_files(destination, movingDirectory)
