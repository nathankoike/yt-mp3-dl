# yt-mp3-dl
A quick and dirty command line script to download an entire YouTube playlist and rip the audio from every video

### Setup and Usage
Please make sure you install the required packages. To do this, you can run the command `pip install -r requirements.txt` to install all the required packages.

Next, create a file called `options.py` and define the variables `Path` and `url`. Define `Path` to be the path to the installation directory of the `youtube-dl` package; this will be used to force the command line script to run properly (since it didn't on my Windows 10 machine) Define `url` to be URL to the song or playlist you want to download; this must be a full URL as it will be piped into the script accessed by the `Path` variable.

After this, you should be able to run the script `dl.py` from the command line like normal, and the videos and audio will appear in their own folders within the directory containing this project.

### Closing Remarks
If you have any suggestions for improvements, please let me know. My logic behind leaving the original video files is to be able to reserve a copy of the song/audio for later, if/when you decide to clean out the `audio` folder that this project uses as its end goal. This also allows you to easily combine playlists without having duplicates of songs, so I decided to leave it in for my own personal convenience. 

In all honesty, this project was borne from my own laziness with downloading songs I like that I can't find available on other services. I've easily spent hours of my life downloading things manually, and this just speeds up the process. I hope you find this useful!
