from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import PIL.Image, PIL.ImageTk
import cv2, cv
from pathlib import Path
from ffpyplayer.player import MediaPlayer


class videoGUI:

    def __init__(self, window, window_title):

        self.window = window
        self.window.title(window_title)

        top_frame = Frame(self.window)
        top_frame.pack(side=TOP, pady=5)

        bottom_frame = Frame(self.window)
        bottom_frame.pack(side=BOTTOM, pady=5)

        self.pause = False  # Parameter that controls pause button
        self.play = False
        self.canvas = Canvas(top_frame)
        self.canvas.pack()

        # Select Button
        self.btn_select = Button(bottom_frame, text="aed", width=12, command=self.open_file0)
        self.btn_select.grid(row=0, column=0)

        self.btn_select = Button(bottom_frame, text="ems", width=12, command=self.open_file1)
        self.btn_select.grid(row=0, column=1)

        self.btn_select = Button(bottom_frame, text="drone", width=12, command=self.open_file2)
        self.btn_select.grid(row=0, column=2)

        # Play Button
        self.btn_play = Button(bottom_frame, text="Play", width=12, command=self.play_video)
        self.btn_play.grid(row=0, column=3)

        # Pause Button
        self.btn_pause = Button(bottom_frame, text="Pause", width=12, command=self.pause_video)
        self.btn_pause.grid(row=0, column=4)

        self.delay = 3  # ms

        self.window.mainloop()

    def open_file0(self):

        self.pause = False

        self.filename = str(Path().absolute()) + '/aed.mp4'
        print(self.filename)

        # Open the video file
        self.cap = cv2.VideoCapture(self.filename)
        self.player = MediaPlayer(self.filename)
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        self.canvas.config(width=self.width, height=self.height)

    def open_file1(self):

        self.pause = False

        self.filename = str(Path().absolute()) + '/ems.mp4'
        print(self.filename)

        # Open the video file
        self.cap = cv2.VideoCapture(self.filename)
        self.player = MediaPlayer(self.filename)
        # self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        # self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        self.width = 1000
        self.height = 500

        self.canvas.config(width=self.width, height=self.height)

    def open_file2(self):

        self.pause = False

        self.filename = str(Path().absolute()) + '/drone.mp4'
        print(self.filename)

        # Open the video file
        self.cap = cv2.VideoCapture(self.filename)
        self.player = MediaPlayer(self.filename)

        # self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        # self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        self.width = 1000
        self.height = 500

        self.canvas.config(width=self.width, height=self.height)

    def getFrame(self):  # get only one frame

        try:

            if self.cap.isOpened():
                ret, frame = self.cap.read()
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        except:
            messagebox.showerror(title='Video file not found', message='Please select a video file.')

    def play_video(self):

        # Get a frame from the video source, and go to the next frame automatically
        audio_frame, val = self.player.get_frame()
        ret, frame = self.getFrame()
        self.play = True
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

        if not self.pause:
            self.window.after(self.delay, self.play_video)

        if self.pause == True:
            self.pause = False
        return

    def pause_video(self):
        if self.pause == False:
            self.pause = True
        else:
            self.pause = False
            self.play_video()

    # Addition
    def resume_video(self):
        self.pause = False
        self.play_video()

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()


##### End Class #####


# Create a window and pass it to videoGUI Class
videoGUI(Tk(), "aed")