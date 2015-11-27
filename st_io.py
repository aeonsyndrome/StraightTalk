import os
import time
import RPi.GPIO as GPIO

class St_io:
    'hardware I/O class for StraightTalk voting system'

    #choose your GPIO pins here
    GPIOblue = 7
    GPIOgreen = 8
    GPIOred = 9
    GPIOwhite = 10
    GPIOyellow = 11
    
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False) 
        GPIO.cleanup()

        GPIO.setup(self.GPIOblue, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.GPIOgreen, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.GPIOred, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.GPIOwhite, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.GPIOyellow, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        self.scoreblue = 0
        self.scoregreen = 0
        self.scorered = 0
        self.scorewhite = 0
        self.scoreyellow = 0
                   
    #Record a vote agains the given object [CORRECT THIS]
    def registerVote(self,channel):
        if (channel == self.GPIOblue):
            self.scoreblue = self.scoreblue +1;
        elif (channel == self.GPIOgreen):
            self.scoregreen = self.scoregreen + 1;
        elif (channel == self.GPIOred):
            self.GPIOred = self.GPIOred + 1;
        elif (channel == self.GPIOwhite):
            self.GPIOwhite = self.GPIOwhite + 1;
        elif (channel == self.GPIOyellow):
            self.GPIOyellow = self.GPIOyellow + 1;
        else:
            print("unknown channel input detected on GPIO pin:" + channel)
    
    def resetScores(self):
        self.scoreblue = 0
        self.scoregreen = 0
        self.scorered = 0
        self.scorewhite = 0
        self.scoreyellow = 0



"""
In your code, implement the following

    GPIO.add_event_detect(St_io.GPIOblue, GPIO.RISING, callback=stio.registerVote, bouncetime=200)
    GPIO.add_event_detect(St_io.GPIOgreen, GPIO.RISING, callback=stio.registerVote, bouncetime=200)
    GPIO.add_event_detect(St_io.GPIOred, GPIO.RISING, callback=stio.registerVote, bouncetime=200)
    GPIO.add_event_detect(St_io.GPIOwhite, GPIO.RISING, callback=stio.registerVote, bouncetime=200)
    GPIO.add_event_detect(St_io.GPIOyellow, GPIO.RISING, callback=stio.registerVote, bouncetime=200)
"""
