from tkinter import *
import tkinter.font

import RPi.GPIO as GPIO
exited = False
GPIO.setmode(GPIO.BOARD)
## Hardware 

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

pwm_yellow = GPIO.PWM(11, 50)
pwm_blue = GPIO.PWM(7, 50)
pwm_green = GPIO.PWM(13, 50)
pwm_blue.start(0)
pwm_green.start(0)
pwm_yellow.start(0)


## GUI DEFINITIONS
win = Tk()
win.title("LED Sliders")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

##Widget definitions
exitButton = Button(win, text = "exit", font = myFont, bg = 'bisque2', height = 1, width = 24)

yellowSlider = Scale(win, from_=0, to=99, orient=HORIZONTAL)
blueSlider = Scale(win, from_=0, to=99, orient=HORIZONTAL)
greenSlider = Scale(win, from_=0, to=99, orient=HORIZONTAL)

yellow = Label(win, text="Yellow")
blue = Label(win, text="Blue")
green = Label(win, text="Green")

### EVENT FUNCTIONS
def exitProgram():
    global exited
    if not exited:
        pwm_yellow.stop()
        pwm_blue.stop()
        pwm_green.stop()
        GPIO.cleanup()
        exited = True
    exit()

win.protocol("WM_DELETE_WINDOW", exitProgram)

def updateyellow(dutyCycle):
    pwm_yellow.ChangeDutyCycle(int(dutyCycle))
def updateBlue(dutyCycle):
    pwm_blue.ChangeDutyCycle(int(dutyCycle))
def updateGreen(dutyCycle):
    pwm_green.ChangeDutyCycle(int(dutyCycle))

exitButton['command'] = exitProgram
yellowSlider['command'] = updateyellow
blueSlider['command'] = updateBlue
greenSlider['command'] = updateGreen

green.grid(row=1, column=1)
greenSlider.grid(row=0, column=1)

blue.grid(row=3, column=1)
blueSlider.grid(row=2, column=1)

yellow.grid(row=5, column=1)
yellowSlider.grid(row=4, column=1)

exitButton.grid(row=6, column=1)

