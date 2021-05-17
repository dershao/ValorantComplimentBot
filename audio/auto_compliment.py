import os
import random

from .audio_controls import play_audio
from .commands import push_to_talk

if __name__ == '__main__':

    audio_dir = "./assets/audio/"

    audio_files = list(map(lambda audio_file: os.path.join(audio_dir, audio_file), os.listdir('./assets/audio/')))
    n_of_audios = len(audio_files)

    random_audio = random.randint(0, n_of_audios - 1)
    chosen_audio = audio_files[random_audio]
    print(f'Chosen audio found at: {chosen_audio}')

    push_to_talk();
    play_audio(chosen_audio, 'CABLE Input (VB-Audio Virtual Cable)')
