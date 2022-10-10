# ----------------- WARNING! -----------------
# -----------------RUN this script in the directory where you want the videos to be dowloaded-----------------


# Printing ASCII art for the script
print(''' __     _________   _____                      _                 _                       _____ _____  
 \ \   / /__   __| |  __ \                    | |               | |                     / ____|  __ \ 
  \ \_/ /   | |    | |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __   ______  | (___ | |__) |
   \   /    | |    | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__| |______|  \___ \|  ___/ 
    | |     | |    | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |              ____) | |     
    |_|     |_|    |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|             |_____/|_|     
                                                                                                      
                                                                                                      ''')

print('Developed by Shubham Pandey\n\n')
import os
# from pydoc import resolve


def startScript():
    playlistUrl = input('Enter Playlist Url: ').strip()
    resolution = input('\nEnter video resolution(144p, 240p, 360p, 720p, 1080p)\nDefault Resolution: 720p [Press Enter]: ').strip()

    if resolution == '':
        resolution = '720p'
        
    # Can use inquirer to make is more user friendly later
    # https://stackoverflow.com/questions/37565793/how-to-let-the-user-select-an-input-from-a-finite-list


    #---------------ADD proper Exception Handling---------------
    playlist = Playlist(playlistUrl)

    print(f'\nDownloading videos from playlist : {playlist.title}\n')

    for videos in playlist.videos:
        print(f'     Downloading - {videos.title}...........')
        videos.streams.filter(res=resolution).first().download()
        # Put a try catch block to handle Exception like, Private video. they cant be downloaded, so skip them
        
        
        
try:
    from pytube import Playlist
    startScript()
    #art is for displaying ASCII ART, without copy pasting
    # from art import *
    
except KeyboardInterrupt as e:
    print('\nError: Download Interrupted.\nKeyboardInterrupt')
    
    
except ModuleNotFoundError:
    print('pytube not found on your device\nDownloading pytube...\n\n')
    os.system('pip install pytube')
    # os.system('pip install art')
    print('\n\nRE-RUN SCRIPT NOW, pytube DOWNLOADED!')
        
        
except Exception as e:
    print(e)
    
# tprint('YT Downloader - SP')