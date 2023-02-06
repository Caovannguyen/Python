from youtube_dl import YoutubeDL
import time


def readfile():
    obj = open("youtube_dl.txt", 'a+', encoding='utf-8')
    obj.seek(0, 0)
    read_file = obj.readlines()
    count = len(read_file)
    print(f'Danh sách tải gồm: {count}')
    for i in read_file:
        link = i  # input('Nhập Đia chỉ video: ')
        print(i)
        count = count - 1
        print(f'danh sách còn lại là: {count}')
        save_path = '/storage/emulated/0/Music/'
        v_info = YoutubeDL().extract_info(url=link, download=False)
        video_title = v_info.get('title', None)
        print(video_title)
        f_mp3 = f"{save_path}{v_info['title']}.mp3"
        options = {
            'format': 'bestaudio/best',
            'keepvideo': False,
            'outtmpl': f_mp3,
        }
        with YoutubeDL(options) as ydl:
            ydl.download([link])
        print('đã tải xong...!')
        time.sleep(0.25)
        obj.close()


time.sleep(3)
readfile()