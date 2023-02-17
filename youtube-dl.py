import os
import time
import ffmpeg
# from ffprobe import *    # cho xu ly
import youtube_dl
from youtube_dl import YoutubeDL

class youtubedl:
    m4a = 140  # audio only
    mp4_144p = 160
    mp4_240p = 133
    mp4_360p = 134
    mp4_480p = 135
    mp4_720p = 136
    mp4_1080p = 137   # 640 * 360
    gp3_176_144 = 17  # 3gp: 176*144
    gp3_320_240 = 36
    flv = 5
    webm = 43
    mp4_640_360 = 18  # 640 * 360
    mp4_1280_720 = 22  # best
    path_music = 'C:/Users/01663/Downloads/Music/'
    path_video = 'C:/Users/01663/Downloads/Video/'
    def __init__(self, link, path):
        self.link = link
        self.path = path
    def music(self):
        try:
            youtubedl.status = False
            v_info = YoutubeDL().extract_info(url=self.link, download=False)
            video_title = v_info.get('title', None)
            print(video_title)
            f_mp3 = f"{self.path}{v_info['title']}.mp3"
            options = {
                'format': 'bestaudio/best',
                'keepvideo': False,
                'outtmpl': f_mp3}
            with YoutubeDL(options) as ydl:
                ydl.download([self.link])
                print('download successfully!')
        except youtube_dl.utils.DownloadError as e:
            print('Fix bug..')
    def video(self):
        try:
            youtubedl.status = True
            v_info = YoutubeDL().extract_info(url=self.link, download=False)
            video_title = v_info.get('title', None)
            print(video_title)
            f_mp4 = f"{self.path}{v_info['title']}.mp4"
            ydl_opts = {
                'format': f'{youtubedl.mp4_1080p}/best',
                'merge-output-format': 'mp4',
                'hls-use-mpegts': True,
                'outtmpl': f_mp4,
                # 'postprocessors': [{
                #     'key': 'FFmpegExtractAudio',
                #     'preferredcodec': 'mp3',
                #     'preferredquality': '192',
                # }]
            }
            # ydl_opts.update({})
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.link])
                print('download successfully!')
        except youtube_dl.utils.DownloadError as e:
            print('Fix bug..')
    def if_folder(self):
        pathm = youtubedl.path_music
        pathv = youtubedl.path_video
        if os.path.isdir(pathv) == True:
            print('folder already!')
        elif os.path.isdir(pathm) == True:
            print('folder already!')
        else:
            os.mkdir(pathv)
            os.mkdir(pathm)
            print('folder created successfully')
    def download_list_music_in_txt(self):
        with open(youtubedl.path_video + 'download_in_list.txt', 'a+', encoding='utf-8') as obj:
            count = 0
            obj.seek(0, 0)
            read_file = obj.readlines()
            for i in read_file:
                count += 1
                print(f'{count}. {i}', end='')
                download = youtubedl(i, youtubedl.path_music)
                download.music()
    def download_list_video_in_txt(self):
        with open(youtubedl.path_video + 'download_in_list.txt', 'a+', encoding='utf-8') as obj:
            count = 0
            obj.seek(0, 0)
            read_file = obj.readlines()
            for i in read_file:
                count += 1
                print(f'{count}. {i}', end='')
                download = youtubedl(i, youtubedl.path_video)
                download.video()

download = youtubedl('','')
download.download_list_music_in_txt()

# link = str(input('Add link: '))
# download = youtubedl(link, youtubedl.path_music)
# download.video()
