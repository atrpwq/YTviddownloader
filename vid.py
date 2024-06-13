from pytube import YouTube
url = input("url: ")
yt = YouTube(url)
print(f"title {yt.title}")
yt.streams.get_highest_resolution().download("vids")
