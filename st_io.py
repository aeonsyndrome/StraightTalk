import os
import time
import RPi.GPIO as GPIO

class St_io:
    'hardware I/O class for StraightTalk voting system'

    #choose your GPIO pins here
    GPIOblue = 3
    GPIOgreen = 2
    GPIOred = 4
    GPIOwhite = 17
    GPIOyellow = 27
    lastTime = 0
    
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        #GPIO.setwarnings(False) 
        GPIO.cleanup()

        GPIO.setup(self.GPIOblue, GPIO.IN)
        GPIO.setup(self.GPIOgreen, GPIO.IN)
        # GPIO.setup(self.GPIOred, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.GPIOred, GPIO.IN)
        GPIO.setup(self.GPIOwhite, GPIO.IN)
        GPIO.setup(self.GPIOyellow, GPIO.IN)

        self.scoreblue = 0
        self.scoregreen = 0
        self.scorered = 0
        self.scorewhite = 0
        self.scoreyellow = 0
                   
    #Record a vote agains the given object [CORRECT THIS]
    def registerVoteBlue(self,channel):
        if time.time() - self.lastTime > 5:
            self.scoreblue = self.scoreblue +1;
            print("blue pressed");
            self.lastTime = time.time();
    def registerVoteGreen(self, channel):
        if time.time() - self.lastTime > 5:
            self.scoregreen = self.scoregreen + 1;
            print("green pressed");
            self.lastTime = time.time();
    def registerVoteRed(self, channel):
        if time.time() - self.lastTime > 5:
            self.scorered = self.scorered + 1;
            print("red pressed");
            self.lastTime = time.time();
    def registerVoteWhite(self, channel):
        if time.time() - self.lastTime > 5:
            self.scorewhite = self.scorewhite + 1;
            print("white pressed");
            self.lastTime = time.time();
    def registerVoteYellow(self, channel):
        if time.time() - self.lastTime > 5:
            self.scoreyellow = self.scoreyellow + 1;
            print("yellow pressed");
            self.lastTime = time.time();
    
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
