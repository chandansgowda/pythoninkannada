from pytube import YouTube

link = input("Enter Youtube URL >> ")

try:
    yt = YouTube(link)
    mp4files = yt.streams.filter(file_extension="mp4")
    video = mp4files.get_highest_resolution()
    video.download()
    print("Video was downloaded successfully!")
except:
    print("Connection Error")