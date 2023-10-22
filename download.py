from pytube import YouTube
import time
import os 
def download_video(url):
    yt = YouTube(url=url)
    video = yt.streams.get_highest_resolution()
    print("Filename: ")
    print(str(yt.streams[0].title) + ".mp4")
    filename = str(yt.streams[0].title) + ".mp4"
    video.download()
    print("Waiting 1 seconds!")
    time.sleep(1)
    print("Removing!")
    os.remove(filename)


download_video("https://www.youtube.com/shorts/xB0ZtzOzwbo")