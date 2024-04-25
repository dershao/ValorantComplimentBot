from PIL import Image
import PIL.ImageOps
import pyscreenshot as ImageGrab
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '<LOCAL_PATH_TO_TESSERACT_EXECUTABLE>'


def find_valorant_agent(txt, agents):
    for agent in agents:
        if agent in txt:
            return agent
    
    return None


def get_name_image():
    """
    The coordinates found in the 'bbox' are the coordinates of the screen to 
    capture the name of the agent when spectating a player. These coordinates
    will differ depending on game settings, screen resolution, etc.

    """
    name_image = ImageGrab.grab(bbox=(110, 800, 240, 850)).convert('L')
    name_image_inverted = PIL.ImageOps.invert(name_image)

    return name_image_inverted


def read_text_from_image(name_image_inverted):

    text_from_tesseract = pytesseract.image_to_string(name_image_inverted)

    return text_from_tesseract


def get_kill_image():
    """
    The coordinates found in the 'bbox' are the coordinates of the screen to 
    capture the kill icon when spectating a player. These coordinates
    will differ depending on game settings, screen resolution, etc.
    """
    kill_image = ImageGrab.grab(bbox=(891, 800, 1025, 950)).convert('L')
    return kill_image
