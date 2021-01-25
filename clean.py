"""
just clean the filenames a bit
"""

import os

# access the audio directory
os.chdir(os.path.join('audio'))

# get all the files in the directory
files = os.listdir()

# for every filename
for file in files:
    # clean the youtube url and the '.mp4' from the filename
    # this is a hack and i wouldnt rely on this for long term support but it
    # works for now since the youtube extension is 12 characters long
    new_fname = file.split('.')[0][:-12] + ".mp3"

    print(new_fname)

    # rename the file
    try: # windows machines
        os.system('move "' + file + '" "' + new_fname + '"')
    except: # basically everything else
        os.system('move "' + file + '" "' + new_fname + '"')
