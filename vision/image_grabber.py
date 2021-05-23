from PIL import Image
import PIL.ImageOps
import pyscreenshot as ImageGrab
import pytesseract
import argparse
import cv2
import os
import numpy as np
import time
import pickle
import sklearn


def find_valorant_agent(txt, agents):
    for agent in agents:
        if agent in txt:
            return agent
    
    return None


def get_name_image():
    name_image = ImageGrab.grab(bbox=(170, 800, 275, 840)).convert('L')
    name_image_inverted = PIL.ImageOps.invert(name_image)

    return name_image_inverted


def read_text_from_image(name_image_inverted):

    text_from_tesseract = pytesseract.image_to_string(name_image_inverted)

    return text_from_tesseract


def get_kill_image():

    kill_image = ImageGrab.grab(bbox=(875, 775, 1050, 925)).convert('L')
    return kill_image
