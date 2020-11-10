from guizero import App, Text, PushButton, Picture, MenuBar
import serial
from pygame import mixer
from time import sleep
gifs = ["gif1.gif", "gif2.gif", "gif3.gif", "gif4.gif"]
numberstring = "3012781238"
app = App(title="Instructive", layout="grid")
def call():
    print("Calling " + numberstring);
    serialport.write("AT\r".encode())
    response = serialport.readlines(None)
    serialport.write("ATD".encode() + numberstring.encode() + ';\r'.encode())
    response = serialport.readlines(None)
    print(response)

def hangup():
    print("Hanging Up...")
    serialport.write("AT\r".encode())
    response = serialport.readlines(None)
    serialport.write("ATH\r".encode())
    response = serialport.readlines(None)
    print(response)
pic1 = Picture(app, image="gif1.gif", grid=[4, 4])
# print("Initialising Modem..")
# serialport = serial.Serial("/dev/ttyAMA0", 115200, timeout=0.5)
# serialport.write("AT\r".encode())
# response = serialport.readlines(None)
# serialport.write("ATE0\r".encode())
# response = serialport.readlines(None)
# serialport.write("AT\r".encode())
# response = serialport.readlines(None)
# print(response)
# make a variable "gif" that changes based on button press?, run function which changes variable name, initialize variables as different gif files, ...
#
# pic2= Picture(app, image="gif2.gif", grid=[4,4])
#
# pic3= Picture(app, image="gif3.gif", grid=[4,4])
#
# pic4= Picture(app, image="gif4.gif", grid=[4,4])

pic1.hide()


def killwindow():
    app.destroy()


def displaypicture(n):
    pic1.image = gifs[n]
    mixer.init()
    mixer.music.load(str(n+1)+'.mp3')
    mixer.music.play()

    pic1.show()


def killpicture():
    pic1.hide()
    mixer.music.stop()

def fixwindow():
    app.set_full_screen()


app.set_full_screen()

menubar = MenuBar(app,

                  toplevel=["Options"],

                  options=[

                      [["Fix Window", fixwindow], ["Quit", killwindow]],

                  ])

text1 = Text(app, text="Step 1) Retrieve package from box in drone", grid=[0, 0], color="black")

text2 = Text(app, text="Step 2) Power on device", grid=[0, 1], color="black")

text3 = Text(app, text="Step 3) Place paddles on chest of patient", grid=[0, 2], color="black")

text4 = Text(app, text="Step 4) Wait until central light turns green", grid=[0, 3], color="black")

# exitb = PushButton(app, text="Exit", grid=[7,0], command=killwindow)

b1 = PushButton(app, text="Call",  grid=[0,4])
b2= PushButton(app, text= "Hang Up", grid=[1,4])
button1 = PushButton(app, text='Display Video', command=displaypicture, grid=[1, 0], args=[0])

killbutton = PushButton(app, text='Hide Video', command=killpicture, grid=[2, 0])

button2 = PushButton(app, text='Display Video', command=displaypicture, grid=[1, 1], args=[1])

killbutton2 = PushButton(app, text='Hide Video', command=killpicture, grid=[2, 1])

button3 = PushButton(app, text='Display Video', command=displaypicture, grid=[1, 2], args=[2])

killbutton3 = PushButton(app, text='Hide Video', command=killpicture, grid=[2, 2])

button4 = PushButton(app, text='Display Video', command=displaypicture, grid=[1, 3], args=[3])

killbutton4 = PushButton(app, text='Hide Video', command=killpicture, grid=[2, 3])

app.display()