from pytubefix import YouTube
YouTube(input("url: ")).streams.get_highest_resolution().download("vids")
