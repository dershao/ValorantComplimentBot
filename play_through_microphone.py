import time
import argparse
import pygame
from pygame._sdl2 import get_num_audio_devices, get_audio_device_name
from pygame import mixer

parser = argparse.ArgumentParser()
parser.add_argument('--audio_file' type=str, required=True, help="Audio file to play")
args = parser.parse_args()

def play_audio(audio_file, devicename):
    mixer.init(devicename=devicename)
    mixer.music.load(audio_file)
    mixer.music.play()
    time.sleep(5)
   

if __name__ == '__main__':
   play_audio(args._audio_file, 'CABLE Input (VB-Audio Virtual Cable)')

