import tkinter as tk
import threading
import imageio
from PIL import Image, ImageTk
from pip._vendor.distlib.compat import raw_input
from tkinter import *

from tkinter import *

window = Tk()

window.title("AED")

window.geometry('350x200')

lbl = Label(window, text="AED instruction")

lbl.grid(column=0, row=0)




class Video(object):
    def __init__(self,path):
        self.path = path

    def play(self):
        from os import startfile
        startfile(self.path)


class Movie_MP4(Video):
    type = "MP4"
movie = Movie_MP4(r"C:\Users\haech\Videos\aed.mp4")


def clicked():
    lbl.configure(movie.play())


btn = Button(window, text="Click Me", command=clicked)

btn.grid(column=1, row=0)

window.mainloop()