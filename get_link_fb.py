from youtube_dl import *

ydl_opts = {'outtmpl': 'videos/%(extractor)s/%(title)s [%(resolution)s] [%(id)s].%(ext)s'}

with YoutubeDL(ydl_opts) as ydl:
    yvd=ydl.download(['https://fb.watch/iBT0ZnYd1M/'])

print("")
print(yvd)