import numpy as np
import sklearn
import pickle
import time
import os


from vision.image_grabber import get_kill_image, get_name_image, read_text_from_image, find_valorant_agent
from common.constants import VALORANT_AGENTS
from audio.commands import push_to_talk
from audio.audio_controls import play_audio, choose_audio, get_name_audio, combine_audio

def load_pca(path='assets/preprocess/pca_preprocess.pkl'):

    with open(path, 'rb') as f:
        pca = pickle.load(f)
        return pca


def load_scaler(path='assets/preprocess/scaler_preprocess.pkl'):

    with open(path, 'rb') as f:
        scaler = pickle.load(f)
        return scaler



if __name__ == '__main__':

    print("Loading pca...")
    pca = load_pca()
    print("Loading scaler...")
    scaler = load_scaler()
    print("Ready")

    while True:
        
        name_image = get_name_image()
        text = read_text_from_image(name_image)
        agent = find_valorant_agent(text, VALORANT_AGENTS)
        print(f'Found agent: {agent}')

        kill_image = get_kill_image()

        scaled = scaler.transform(np.array(kill_image).reshape(1, -1))
        pca_components = pca.transform(scaled)

        if pca_components[0][1] > 50 and agent is not None:
            chosen_audio = choose_audio()
            name_audio = get_name_audio(agent)
            temp_audio = combine_audio(chosen_audio, name_audio)
            
            push_to_talk();
            play_audio(chosen_audio, 'CABLE Input (VB-Audio Virtual Cable)')

        time.sleep(1)
