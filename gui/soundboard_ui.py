import tkinter as tk
import os
import math
import logging

from common.constants import GENERAL_AUDIO_FOLDER_PATH, AUDIO_DEVICE_VB_VIRTUAL_CABLE

from audio.commands import push_to_talk
from audio.audio_controls import play_audio



class SoundBoardUI(tk.Tk):

    def __init__(self):
        
        super().__init__()
        self.title('Soundboard')
        self.populate_soundboard()
        super().mainloop()

    def populate_soundboard(self):

        list_of_audios = os.listdir(GENERAL_AUDIO_FOLDER_PATH)
        n_of_audios = len(list_of_audios)
        n_of_rows = math.ceil(n_of_audios / 3)

        for row in range(n_of_rows):
            for col in range(3):

                audio_index = row * 3 + col
                if audio_index > n_of_audios - 1:
                    logging.info("Finished populating soundboard")
                    break

                frame = tk.Frame(
                    master=self,
                    relief=tk.RAISED,
                    borderwidth=1
                )
                frame.grid(row=row, column=col)
                button = tk.Button(master=frame, text=f"{list_of_audios[audio_index][:-4]}")
                button.pack()
                button.bind('<Button-1>', self.soundboard_button_handler)
    
    def soundboard_button_handler(self, event):
        selected_audio = event.widget.cget('text')
        push_to_talk()
        play_audio(f'{GENERAL_AUDIO_FOLDER_PATH}/{selected_audio}.mp3', AUDIO_DEVICE_VB_VIRTUAL_CABLE)
        push_to_talk()
