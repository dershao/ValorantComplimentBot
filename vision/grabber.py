from PIL import Image
import PIL.ImageOps
import pyscreenshot as ImageGrab
import pytesseract
import argparse
import cv2
import os
import numpy as np
import time


VALORANT_AGENTS = [
    'Astra',
    'Jett',
    'Sage',
    'Sova',
    'Viper',
    'Killjoy',
    'Phoenix',
    'Omen',
    'Cypher',
    'Raze',
    'Brimstone',
    'Reyna',
    'Breach',
    'Yoru',
    'Skye'
]


def find_valorant_character(txt, agents):
    for agent in agents:
        if agent in txt:
            return agent
    
    return None


if __name__ == '__main__':
    while True:
        name_image = ImageGrab.grab(bbox=(160, 780, 270, 815)).convert('L')
        name_image_inverted = PIL.ImageOps.invert(name_image)

        text_from_tesseract = pytesseract.image_to_string(name_image_inverted)

        champion = find_valorant_character(text_from_tesseract, VALORANT_AGENTS)
        print(f'Found: {champion}')

        kill_image = ImageGrab.grab(bbox=(875, 750, 1050, 900)).convert('L')
        kill_image_inverted = PIL.ImageOps.invert(kill_image)
        # TODO: call function to determine if player killed someone at this moment 

        time.sleep(1)
