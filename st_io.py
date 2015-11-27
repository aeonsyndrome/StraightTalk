import os
import time
import RPi.GPIO as GPIO

class St_Event(object):
    pass

class St_io:
    'hardware I/O class for joypad voting system'

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
        self.callbacks = []
                   
    #Record a vote agains the given object
    def registerVote(self,channel):
        if (channel == self.GPIOteamA):
            self.scoreA = self.scoreA +1;
            self.fire(action='vote', team='a');
        elif (channel == self.GPIOteamB):
            self.scoreB = self.scoreB + 1;
            self.fire(action='vote', team='b');
        else:
            print("unknown channel input detected on GPIO pin:" + channel)
    
    def resetScores(self):
        self.scoreA = 0
        self.scoreB = 0
        
    #callback handling
    def subscribe(self, callback):
        self.callbacks.append(callback)
    def fire(self, **attrs):
        e = JoypadioEvent()
        e.source = self;
        for k, v in attrs.iteritems():
            setattr(e,k,v)
        for fn in self.callbacks:
            fn(e)


"""
In your code, implement the following

   GPIO.add_event_detect(Joypadio.GPIOteamA, GPIO.RISING, callback=JoypadioObject.registerVote, bouncetime=200)
   GPIO.add_event_detect(Joypadio.GPIOteamB, GPIO.RISING, callback=JoypadioObject.registerVote, bouncetime=200)
"""
