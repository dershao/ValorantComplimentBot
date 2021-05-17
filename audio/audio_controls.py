import time

import pygame
import keyboard
from pygame import mixer

def play_audio(audio_file, devicename):
    mixer.init(devicename=devicename)
    mixer.music.load(audio_file)
    mixer.music.play()
    time.sleep(5) # sleep to allow the audio to play
