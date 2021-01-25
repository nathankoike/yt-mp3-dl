import os
from moviepy.editor import *

# the path to the install location of youtube-dl and the url of the youtube
# video/playlist is stored in a separate file that i have decided not to upload
from options import *

# used to clean the audio directory
from clean import *

# the current directory
CWD = os.getcwd()

# download all the videos in a playlist
def download(url):
    # change to the directory of the youtube downloader
    os.chdir(Path)
    # print(os.listdir())

    # the command to download the videos
    dl_cmd = "python __main__.py"

    # options for the video downloader
    options = [
        "-i", # ignore videos with errors
        "-f best", # download the highest quality video and audio
        url # the only truly necessary thing here
        ]

    # finish making the command
    for option in options:
        dl_cmd += (" " + option)

    # download all the videos
    os.system(dl_cmd)

    # move all the video files to this directory
    try: # batch for windows
        os.system(("move *.mp4 " + os.path.join(CWD, "videos")))
    except: # bash for everything else
        os.system(("mv *.mp4 " + os.path.join(CWD, "videos")))

    # switch back to the current directory
    os.chdir(CWD)

# rip the audio from every video file in the directory
def rip_audio():
    # change to the audio directory
    os.chdir("videos")

    # get a list of every file in the directory
    files = os.listdir()

    # for every video in the directory
    for file in files:
        print(files.index(file), "of", len(files))
        # if we dont have a video file
        if ".mp4" not in file:
            continue

        # the base filename
        base = file[:-4]
        print(base)

        # open the video and rip the audio into a different folder
        video = VideoFileClip(file)
        video.audio.write_audiofile(os.path.join("..", "audio", file + ".mp3"))

    # return to the original directory
    os.chdir(CWD)

    # clean the filenames
    clean()

def main():
    # check to see if the necessary subdirectories exist
    dir = os.listdir()

    print(os.getcwd())

    # make the subdirectories if necessary
    if "audio" not in dir:
        print("making audio directory")
        os.system("mkdir audio")
    if "videos" not in dir:
        print("making video directory")
        os.system("mkdir videos")

    # the url to the video/playlist to download
    download(url)
    rip_audio()

if __name__ == "__main__":
    main()
