# Import general libraries
from Tkinter import *
import RPi.GPIO as GPIO
from st_io import St_io
from st_gui import St_gui

# Import local libraries
root = Tk()
stio = St_io()

straighttalk = St_gui(root,stio)

straighttalk.initGui()

# add callbacks for GPIo events
# bouncetime = number of milliseconds before registering another button push
GPIO.add_event_detect(St_io.GPIOblue, GPIO.RISING, callback=stio.registerVoteBlue, bouncetime=300)
GPIO.add_event_detect(St_io.GPIOgreen, GPIO.RISING, callback=stio.registerVoteGreen, bouncetime=300)
GPIO.add_event_detect(St_io.GPIOred, GPIO.RISING, callback=stio.registerVoteRed, bouncetime=300)
GPIO.add_event_detect(St_io.GPIOwhite, GPIO.RISING, callback=stio.registerVoteWhite, bouncetime=300)
GPIO.add_event_detect(St_io.GPIOyellow, GPIO.RISING, callback=stio.registerVoteYellow, bouncetime=300)

root.mainloop()
