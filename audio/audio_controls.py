import os
import time
import uuid
import random
import pygame
from pygame import mixer
from pathlib import Path

# play audio in a distinct order
glob_audio_count = 0

def play_audio(audio_file, devicename, pause_after_audio=0):
    mixer.init(devicename=devicename)
    mixer.music.load(audio_file)
    mixer.music.play()
    # this is needed in the main loop
    # otherwise, the while loop will interrupt the audio and
    # look for the next kill image
    time.sleep(pause_after_audio)


def choose_audio(audio_dir=Path(__file__).parent.parent / 'assets' / 'audio' / 'compliment'):
    global glob_audio_count
    audio_files = list(map(lambda audio_file: os.path.join(audio_dir, audio_file), os.listdir(audio_dir)))
    n_of_audios = len(audio_files)

    chosen_audio = audio_files[glob_audio_count]
    glob_audio_count += 1

    print(f'Chosen audio found at: {chosen_audio}')

    return chosen_audio


def get_name_audio(name, audio_dir=Path(__file__).parent.parent / 'assets' / 'audio' / 'agent'):

    name_audio = f'{str(audio_dir / name)}.mp3'
    print(f'Loading agent audio at: {name_audio}')

    return name_audio


def combine_audio(first_audio_file, second_audio_file, temp_dir=Path(__file__).parent.parent / 'tmp'):

    with open(first_audio_file, 'rb') as f:
        first_audio = f.read()
    
    with open(second_audio_file, 'rb') as f:
        second_audio = f.read()

    combined_audio = first_audio + second_audio

    tempAudioFile = temp_dir / f'{str(uuid.uuid4())}.mp3'

    with open(tempAudioFile, 'wb') as f:
        f.write(combined_audio)

    return tempAudioFile
