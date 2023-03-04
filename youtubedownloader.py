import pytube
link = " link for youtube video"
yt = pytube.Youtube(link)
stream = yt.stream.first()
stream.download()