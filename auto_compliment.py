import numpy as np
import sklearn
import pickle
import time
import os

from vision.image_grabber import get_kill_image, get_name_image, read_text_from_image, find_valorant_agent
from common.constants import VALORANT_AGENTS, GENERAL_GREETINGS_AUDIO_PATH, AUDIO_DEVICE_VB_VIRTUAL_CABLE

from audio.commands import push_to_talk
from audio.audio_controls import play_audio, choose_audio, get_name_audio, combine_audio

from gui.auto_compliments_info_ui import AutoComplimentInfoUI

def load_pca(path='assets/preprocess/pca_preprocess.pkl'):

    with open(path, 'rb') as f:
        pca = pickle.load(f)
        return pca


def load_scaler(path='assets/preprocess/scaler_preprocess.pkl'):

    with open(path, 'rb') as f:
        scaler = pickle.load(f)
        return scaler


def initialize_ui(scaler, pca):
    name_image = get_name_image()
    kill_image = get_kill_image()
    scaled = scaler.transform(np.array(kill_image).reshape(1, -1))
    pca_components = pca.transform(scaled)

    return AutoComplimentInfoUI(name_image, kill_image, pca_components)


if __name__ == '__main__':

    print("Loading pca...")
    pca = load_pca()
    print("Loading scaler...")
    scaler = load_scaler()
    print("Ready")

    info_ui = initialize_ui(scaler, pca)

    while True:
        
        name_image = get_name_image()
        text = read_text_from_image(name_image)
        agent = find_valorant_agent(text, VALORANT_AGENTS)

        kill_image = get_kill_image()
        scaled = scaler.transform(np.array(kill_image).reshape(1, -1))
        pca_components = pca.transform(scaled)

        info_ui.update_ui(name_image, kill_image, pca_components)

        if pca_components[0][1] > 0 and pca_components[0][0] < 0 and agent is not None:
            chosen_audio = choose_audio()
            name_audio = get_name_audio(agent)
            temp_audio = combine_audio(chosen_audio, name_audio)
            push_to_talk()
            play_audio(temp_audio, AUDIO_DEVICE_VB_VIRTUAL_CABLE, 5)
            push_to_talk()
        
        time.sleep(0.25)

