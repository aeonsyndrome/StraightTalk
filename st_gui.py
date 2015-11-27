# UI class
from Tkinter import *
from PIL import Image, ImageTk
import tkFont

class St_gui:
    'UI controller for st voting system'

    # seconds to show results
    timerSeconds = 5

    # init using the root Tk() instance, and the st_io library
    def __init__(self, root, io):
        self.root = root
        self.io = io
        self.timeRemaining = self.timerSeconds
        self.canvas_height = root.winfo_screenheight()-40
        self.canvas_width  = root.winfo_screenwidth()
        self.font_header = tkFont.Font(family="Helvetica", size=100, weight="bold")
        self.font_header2 = tkFont.Font(family="Helvetica", size=50, weight="bold")

    def initGui(self):
        self.c = Canvas(self.root, width=self.canvas_width, height=self.canvas_height)

        # make everything centered, that way we can deal with different resolutions easier instead of
        # anchoring everything to the top left
        self.imageBG = Image.open("resources/bg.jpg")
        self.photoBG = ImageTk.PhotoImage(self.imageBG)
        self.bg = self.c.create_image(self.canvas_width/2,self.canvas_height/2,image=self.photoBG)

        self.questions = open('questions/question1.txt', 'r')
        self.stquestion = self.questions.readline()
        self.stblue = self.questions.readline()
        self.stgreen = self.questions.readline()
        self.stred = self.questions.readline()
        self.stwhite = self.questions.readline()
        self.styellow = self.questions.readline()
        self.questions.close()

        self.textQuestion = self.c.create_text(self.canvas_width/6, self.canvas_height/7, text=self.stquestion, font=self.font_header, fill="black")

        self.textBlue = self.c.create_text(self.canvas_width/6, self.canvas_height/7*2, text=self.stblue, font=self.font_header2, fill="black")
        self.textGreen = self.c.create_text(self.canvas_width/6, self.canvas_height/7*3, text=self.stgreen, font=self.font_header2, fill="black")
        self.textRed = self.c.create_text(self.canvas_width/6, self.canvas_height/7*4, text=self.stred, font=self.font_header2, fill="black")
        self.textWhite = self.c.create_text(self.canvas_width/6, self.canvas_height/7*5, text=self.stwhite, font=self.font_header2, fill="black")
        self.textYellow = self.c.create_text(self.canvas_width/6, self.canvas_height/7*6, text=self.styellow, font=self.font_header2, fill="black")

        self.textBluescore = self.c.create_text(self.canvas_width/4, self.canvas_height/7*2, text="0", font=self.font_header2, fill="black")
        self.textGreenscore = self.c.create_text(self.canvas_width/4*3, self.canvas_height/7*3, text="0", font=self.font_header2, fill="black")
        self.textRedscore = self.c.create_text(self.canvas_width/4, self.canvas_height/7*4, text="0", font=self.font_header2, fill="black")
        self.textWhitescore = self.c.create_text(self.canvas_width/4*3, self.canvas_height/7*5, text="0", font=self.font_header2, fill="black")
        self.textYellowscore = self.c.create_text(self.canvas_width/4*3, self.canvas_height/7*6, text="0", font=self.font_header2, fill="black")

        self.textTimer = self.c.create_text(self.canvas_width/2, self.canvas_height/2, text="COUNTDOWN", font=self.font_header, fill="red")

        self.updateUI()
        self.countdownTimer()

        self.c.pack()

    def countdownTimer(self):
        if (self.timeRemaining <= 0):
            self.timerReached();
        else:
            self.timeRemaining = self.timeRemaining - 1;
            self.root.after(1000,self.countdownTimer);

    def resetCountdownTimer(self):
        self.timeRemaining = self.timerSeconds

    def timerReacher(self):
        'something'
        # dislpay the voting results screen, plus a countdown to the next vote session

    def updateUI(self):
        'update the UI to display scores every 200ms'
        self.c.itemconfig(self.textTeamAscore, text = self.io.scoreA)
        self.c.itemconfig(self.textTeamBscore, text = self.io.scoreB)
        self.c.itemconfig(self.textTimer, text= self.timeRemaining);
        self.root.after(200,self.updateUI)