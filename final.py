from tkinter import *
from PIL import ImageTk, Image
import cv2
from pathlib import Path
from ffpyplayer.player import MediaPlayer



root = Tk()
# Create a frame
app = Frame(root, bg="white")
app.grid()
# Create a label in the frame
lmain = Label(app)
lmain.grid()

# Capture from camera
cap = cv2.VideoCapture(str(Path().absolute()) + '/test.mp4')
player = MediaPlayer(str(Path().absolute()) + '/test.mp4')
# function for video streaming
def video_stream():
    _, frame = cap.read()
    audio_frame, val = player.get_frame()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream)

video_stream()
root.mainloop()