import yt_dlp

# функции для загрузки видео
def download_video(url):
    ydl_opts = {
        'format': 'best',  # скачивание лучшего качество
        
        'noplaylist': True,  # отключаем скачивание плейлистов
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_youtube_shorts(url):
    ydl_opts = {
        'format': 'best',  # скачиваем лучшее кач.
        
        'noplaylist': True,  # невозможно скачать плейлисты
        'extractaudio': False,  # загрузка видео mp4, не mp3
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


downloaders = {
    '1': download_video,           
    '2': download_youtube_shorts,  
}

def main():
    print("Выберите действие:")
    print("1: Скачать видео с YouTube")
    print("2: Скачать YouTube Shorts")

    choice = input("Выберите 1 или 2: ")

    if choice in downloaders:
        url = input("Введите ссылку на видео: ")
        downloader = downloaders[choice]  # выбор метода
        downloader(url)  # загрузка видео
        print("Видео скачано")
    else:
        print("Напишите 1 или 2!")

if __name__ == "__main__":
    main()
