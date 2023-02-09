from youtube_dl import *

ydl_opts = {'outtmpl': 'videos/%(extractor)s/%(title)s [%(resolution)s] [%(id)s].%(ext)s'}

with YoutubeDL(ydl_opts) as ydl:
    yvd=ydl.download(['https://www.youtube.com/watch?v=NXMx8bZphwU&list=RDNXMx8bZphwU&start_radio=1'])

print("")
print(yvd)