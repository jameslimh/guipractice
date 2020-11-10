from guizero import App, Text, PushButton, Picture, MenuBar
import serial
import os

numberstring = "3012781238"
gifs = ["aed.gif"]

app = App(title="Instructive", layout="grid")

#pic1 = Picture(app, image="aed.gif", grid=[4, 4])

# make a variable "gif" that changes based on button press?, run function which changes variable name, initialize variables as different gif files, ...

# pic2= Picture(app, image="gif2.gif", grid=[4,4])

# pic3= Picture(app, image="gif3.gif", grid=[4,4])

# pic4= Picture(app, image="gif4.gif", grid=[4,4])

#pic1.hide()

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
    
def killwindow():
    app.destroy()

 
def displaypicture(n):
    print("displaying")
    os.system("xterm -e omxplayer -o hdmi -r --win '100 100 1340 980' /home/pi/Desktop/DRONEGUI/aed.mp4")
    #pic1.show()


def killpicture():
    #pic1.hide()
    print("hiding")


def fixwindow():
    app.set_full_screen()


app.set_full_screen()
print("Initialising Modem..")
serialport = serial.Serial("/dev/ttyAMA0", 115200, timeout=0.5)
serialport.write("AT\r".encode())
response = serialport.readlines(None)
serialport.write("ATE0\r".encode())
response = serialport.readlines(None)
serialport.write("AT\r".encode())
response = serialport.readlines(None)
print(response)

menubar = MenuBar(app,

                  toplevel=["Options"],

                  options=[

                      [["Fix Window", fixwindow], ["Quit", killwindow]],

                  ])

text1 = Text(app, text="Step 1) Retrieve package from box in drone", grid=[0, 0], color="black")

text2 = Text(app, text="Step 2) Power on device", grid=[0, 1], color="black")
##
text3 = Text(app, text="Step 3) Place paddles on chest of patient", grid=[0, 2], color="black")
##
text4 = Text(app, text="Step 4) Wait until central light turns green", grid=[0, 3], color="black")
##
#exitb = PushButton(app, text="Exit", grid=[7,0], command=killwindow)


button1 = PushButton(app, text='Display Video', command=displaypicture, grid=[1, 0], args=[0])

killbutton = PushButton(app, text='Hide Video', command=killpicture, grid=[2, 0])


b1 = PushButton(app, text="Call", command=call, grid=[0,4])
b2= PushButton(app, text= "Hang Up", command=hangup, grid=[1,4])

button2 = PushButton(app, text='Display Video', command=displaypicture, grid=[1, 1], args=[1])
##
killbutton2 = PushButton(app, text='Hide Video', command=killpicture, grid=[2, 1])
##
button3 = PushButton(app, text='Display Video', command=displaypicture, grid=[1, 2], args=[2])
##
killbutton3 = PushButton(app, text='Hide Video', command=killpicture, grid=[2, 2])
##
button4 = PushButton(app, text='Display Video', command=displaypicture, grid=[1, 3], args=[3])
##
killbutton4 = PushButton(app, text='Hide Video', command=killpicture, grid=[2, 3])

