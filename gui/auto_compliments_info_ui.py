from PIL import Image, ImageTk
import tkinter as tk

class AutoComplimentInfoUI(tk.Tk):

    def __init__(self, name_image, kill_image, pca_components):
        
        super().__init__()

        self.agentLabel = tk.Label(self, text = "Agent: ")
        self.imageLabel = tk.Label(self, text = "Image: ")
        self.pcaComponentsTextLabel = tk.Label(self, text = "PCA: ")
        self.pcaComponentsLabel = tk.Label(self, text = str(pca_components))

        nameImageTk = ImageTk.PhotoImage(name_image)
        killImageTk = ImageTk.PhotoImage(kill_image)

        self.agentImageLabel = tk.Label(image = nameImageTk)
        self.agentImageLabel.image = nameImageTk
        self.killImageLabel = tk.Label(image = killImageTk)
        self.killImageLabel.image = killImageTk

        self.agentLabel.grid(row = 0, column = 0, sticky = tk.W, pady = 2)
        self.imageLabel.grid(row = 1, column = 0, sticky = tk.W, pady = 2)
        self.pcaComponentsTextLabel.grid(row = 2, column = 0, sticky = tk.W, pady = 2)

        self.agentImageLabel.grid(row = 0, column = 1, pady = 2)
        self.killImageLabel.grid(row = 1, column = 1, pady = 2)
        self.pcaComponentsLabel.grid(row = 2, column = 1, sticky = tk.W, pady = 2)

    def update_ui(self, name_image, kill_image, pca_components):

        nameImageTk = ImageTk.PhotoImage(name_image)
        killImageTk = ImageTk.PhotoImage(kill_image)

        self.agentImageLabel = tk.Label(image = nameImageTk)
        self.agentImageLabel.image = nameImageTk
        self.killImageLabel = tk.Label(image = killImageTk)
        self.killImageLabel.image = killImageTk

        self.pcaComponentsLabel = tk.Label(self, text = str(pca_components))
        self.pcaComponentsLabel.text = str(pca_components)

        self.agentImageLabel.grid(row = 0, column = 1, pady = 2)
        self.killImageLabel.grid(row = 1, column = 1, pady = 2)
        self.pcaComponentsLabel.grid(row = 2, column = 1, sticky = tk.W, pady = 2)

        super().update()