from pytube import YouTube
from pytube.cli import on_progress


def run():
    try:
        videos_url = input("Please input video url : ")
        yt = YouTube(videos_url, on_progress_callback=on_progress)

        title = yt.title
        print("Downloading Videos with Title \"" + title + "\"")
        video = yt.streams.filter(
            progressive=True, file_extension='mp4').first()
        video.download()
        print("|||||||||||||||||||||||||||||||||||||||||||||")
        print("Video Download \"" + str(title) + "\" Completed ")

    except Exception as e:
        print(e)


if __name__ == '__main__':
    run()
