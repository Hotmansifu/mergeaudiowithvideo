from pytube import YouTube

video_url = input("Enter the YouTube video URL: ")
yt = YouTube(video_url)
audio = yt.streams.filter(only_audio=True).first()
audio.download('./')
