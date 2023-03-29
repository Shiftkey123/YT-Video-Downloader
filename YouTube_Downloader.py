from  pytube import *
import pytube
from pytube import YouTube
import time
import os
import requests
import imageio
import imageio_ffmpeg
from imageio import *
import moviepy.editor as mp
from moviepy.editor import VideoFileClip
from moviepy.audio.fx.audio_fadein import audio_fadein
from moviepy.audio.fx.audio_fadeout import audio_fadeout
from moviepy.audio.fx.audio_left_right import audio_left_right
from moviepy.audio.fx.audio_loop import audio_loop
from moviepy.audio.fx.audio_normalize import audio_normalize
from moviepy.audio.fx.volumex import volumex
from moviepy.video.fx.accel_decel import accel_decel
from moviepy.video.fx.blackwhite import blackwhite
from moviepy.video.fx.blink import blink
from moviepy.video.fx.colorx import colorx
from moviepy.video.fx.crop import crop
from moviepy.video.fx.even_size import even_size
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout
from moviepy.video.fx.freeze import freeze
from moviepy.video.fx.freeze_region import freeze_region
from moviepy.video.fx.gamma_corr import gamma_corr
from moviepy.video.fx.headblur import headblur
from moviepy.video.fx.invert_colors import invert_colors
from moviepy.video.fx.loop import loop
from moviepy.video.fx.lum_contrast import lum_contrast
from moviepy.video.fx.make_loopable import make_loopable
from moviepy.video.fx.margin import margin
from moviepy.video.fx.mask_and import mask_and
from moviepy.video.fx.mask_color import mask_color
from moviepy.video.fx.mask_or import mask_or
from moviepy.video.fx.mirror_x import mirror_x
from moviepy.video.fx.mirror_y import mirror_y
from moviepy.video.fx.painting import painting
from moviepy.video.fx.resize import resize
from moviepy.video.fx.rotate import rotate
from moviepy.video.fx.scroll import scroll
from moviepy.video.fx.speedx import speedx
from moviepy.video.fx.supersample import supersample
from moviepy.video.fx.time_mirror import time_mirror
from moviepy.video.fx.time_symmetrize import time_symmetrize
from tkinter import *
from tkinter import filedialog
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import *

#function that actually does the download
def downloader():
    link = input("Video Link: ")
    file_name = input("File name: ")
    file_extension2 = input("Audio/Video: ").lower()

    if file_extension2 == "video":
        print("")
        print("<Choose video resolution>")
        file_extension = input("High/Low: ").lower()

    elif file_extension2 == "audio":
        file_extension = "audio"
    
    #Select where to save file
    root = Tk()
    root.withdraw()
    SAVE_PATH = filedialog.askdirectory()

    yt = YouTube(link)

    if file_extension == "high":
        video = yt.streams.get_highest_resolution()
        video.download(output_path = SAVE_PATH, filename = file_name + ".mp4")
    
    elif file_extension == "low":
        video = yt.streams.get_lowest_resolution()
        video.download(output_path = SAVE_PATH, filename = file_name + ".mp4")

    elif file_extension == "audio":
        video = yt.streams.get_lowest_resolution()
        video.download(output_path = SAVE_PATH, filename = file_name + ".mp4")

        #convert from video to audio
        video = VideoFileClip(f"{SAVE_PATH}/{file_name}.mp4")
        audio = video.audio
        audio.write_audiofile(f"{SAVE_PATH}/{file_name}.mp3")

        video.close()
        audio.close()

        if os.path.exists(f"{SAVE_PATH}/{file_name}.mp4"):
            os.remove(f"{SAVE_PATH}/{file_name}.mp4")
            
        else:
            print("Error, file does not exists.")

    else:
        print("Error, incorrect file type | Returning to start menu")
        time.sleep(2)
        start_menu()

    print("Video Successfully Downloaded!")
    print(f"Save Path: {SAVE_PATH}")
    time.sleep(5)
    start_menu()

#This displays information about the program such as creator and version
def INFO1():
    print("Creator: Shiftkey")
    print("Discord: ShiftKey#7872")
    print("Discord Server: https://discord.gg/R7JfEafZMq")
    print("Language: English")
    print("Program langauge: Python")
    print("Version: 3.0")
    time.sleep(1)
    user_input2 = input("Back/Close: ").lower()
    if user_input2 == "back":
        print("Returning to menu...")
        time.sleep(1.5)
        start_menu()

    elif user_input2 == "close":
        print("Closing program")
        time.sleep(2)
        exit()

    else:
        print("Unexpected error. Returning to menu.")
        time.sleep(2)
        start_menu()

#This is the section that tells users how to use the program.
def HELP():
    print("This is the help menu, here you will find out how to use the program and what to do if you encounter bugs.")
    print("")
    print("<<<TO USE>>>")
    print("First: Once prompted type 'open', this will start the program and the download process.")
    print("Next: Input the link of the desired YouTube video, then give the file that will be downloaded a name.")
    print("Next: Give the file it's extension. This can be any video/audio extension, mp4, mp3, mov, etc.")
    print("Final step: Choose the directory where you wish the file to be saved. Once file is done downloading you can safely exit the program.")
    print("")
    print("<<<ANY ERRORS>>>")
    print("Currently there are no known 'bugs' however, if you mistype anything it will cause an error.")
    print("Fix: Just restart the program and make sure to type everything correctly. If you find anything else contact me on discord.")
    print("My discord can be found in the info menu.")
    print("")
    print("Hope you enjoy the program!")

    time.sleep(1)

    user_input = input("Back/Close: ").lower()
    if user_input == "back":
        print("Returning to menu...")
        time.sleep(1.5)
        start_menu()
    
    elif user_input == "close":
        print("Closing program")
        time.sleep(2)
        exit()
    
    else:
        print("Unexpected error. Returning to menu.")
        time.sleep(2)
        start_menu()

#main menu of program, very simple and can be edited later
def start_menu():
    print("================================")
    print("====YouTube Video Downloader====")
    print("================================")
    print("")
    print("         <<<Welcome>>>          ")
    print("")
    print("<<Type help if it's your first time using this program>>")
    print("")
    ask = input("Open/Close/Help/Info: ").lower()
    if ask == "open":
        print("Thanks for choosing my YT Video Downloader!")
        time.sleep(2)
        downloader()
        
    elif ask == "close":
        print("I hope you enjoyed the downloader, bye!")
        time.sleep(2)
        print("Closing...")
        time.sleep(2)
        exit()

    elif ask == "help":
        HELP()

    elif ask == "info":
        INFO1()

    else:
        print("An error occured, restarting...")
        time.sleep(2)
        start_menu()

start_menu()
