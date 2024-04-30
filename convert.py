#!/usr/bin/env python3

import urllib.request
import urllib.error

import re
import sys
import time
import os

from pytube import YouTube
from os import walk

#function added to get audio files along with the video files from the playlist
def convert_Video_2_Audio(path):

    try:
        for dirpath, dirnames, filenames in walk(path):
            for filename in filenames:
                if filename.endswith(".mp4"):
                    dest = str(filename[:-4])+'.wav'
                    aud = 'ffmpeg -i '+ '"' + os.path.join(dirpath, filename) +'" "' + os.path.join(dirpath, dest) + '"'
                    print('aud:', aud)
                    os.system(aud)

                    #final_audio='lame '+ os.path.join(dirpath, dest)+' '+ path + '/' + str(file_no)+'.mp3'
                    #mp3_dest = str(dest[:-4])+'.mp3'
                    #final_audio = 'lame '+ '"' + os.path.join(dirpath, dest) +'" "' + os.path.join(dirpath, mp3_dest) + '"'

            #print('final_audio:', final_audio)
            #os.system(final_audio)
    except OSError as  err:
        print('{0}'.format(err))
        sys.exit(1)
 
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('USAGE: python convert.py path')
        exit(1)
    else:
        directory = sys.argv[1]

    convert_Video_2_Audio(directory)

