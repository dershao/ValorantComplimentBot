import os
import time
import uuid
import random
import pygame
from pygame import mixer
from pathlib import Path


def play_audio(audio_file, devicename):
    mixer.init(devicename=devicename)
    mixer.music.load(audio_file)
    mixer.music.play()
    time.sleep(5) # sleep to allow the audio to play


def choose_audio(audio_dir=Path(__file__).parent.parent / 'assets' / 'audio' / 'compliment'):

    audio_files = list(map(lambda audio_file: os.path.join(audio_dir, audio_file), os.listdir(audio_dir)))
    n_of_audios = len(audio_files)

    random_audio = random.randint(0, n_of_audios - 1)
    chosen_audio = audio_files[random_audio]
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
