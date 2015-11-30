# UI class
from Tkinter import *
from PIL import Image, ImageTk
import tkFont

class St_gui:
    'UI controller for st voting system'

    # seconds to show results
    timerSeconds = 5
    i = 1

    # init using the root Tk() instance, and the st_io library
    def __init__(self, root, io):
        self.root = root
        self.io = io
        self.timeRemaining = self.timerSeconds
        self.c_h = root.winfo_screenheight()-40
        self.c_w  = root.winfo_screenwidth()
        self.font_header = tkFont.Font(family="Helvetica", size=70, weight="bold")
        self.font_header2 = tkFont.Font(family="Helvetica", size=50, weight="bold")

    def initGui(self):
        self.c = Canvas(self.root, width=self.c_w, height=self.c_h, bg="grey")

        # make everything centered, that way we can deal with different resolutions easier instead of
        # anchoring everything to the top left
        # self.imageBG = Image.open("resources/bg.jpg")
        # self.photoBG = ImageTk.PhotoImage(self.imageBG)
        # self.bg = self.c.create_image(self.c_w/2,self.c_h/2,image=self.photoBG)

        # moveable background
        self.bg = self.c.create_rectangle(0,0,self.c_w,self.c_h, fill = "grey")

        self.questions = open('questions/question1.txt', 'r')
        self.stquestion = self.questions.readline()
        self.stblue = self.questions.readline()
        self.stgreen = self.questions.readline()
        self.stred = self.questions.readline()
        self.stwhite = self.questions.readline()
        self.styellow = self.questions.readline()
        self.questions.close()

        # Question
        self.textQuestion = self.c.create_text(self.c_w/2, self.c_h/7, text=self.stquestion, font=self.font_header, fill="black")

        # Dots
        self.circleBlue = self.c.create_oval(self.c_w/7-40, self.c_h/7*2-40, self.c_w/7+40, self.c_h/7*2+40, fill = "blue")
        self.circleGreen = self.c.create_oval(self.c_w/7-40, self.c_h/7*3-40, self.c_w/7+40, self.c_h/7*3+40, fill = "green")
        self.circleRed = self.c.create_oval(self.c_w/7-40, self.c_h/7*4-40, self.c_w/7+40, self.c_h/7*4+40, fill = "red")
        self.circleWhite = self.c.create_oval(self.c_w/7-40, self.c_h/7*5-40, self.c_w/7+40, self.c_h/7*5+40, fill = "white")
        self.circleYellow = self.c.create_oval(self.c_w/7-40, self.c_h/7*6-40, self.c_w/7+40, self.c_h/7*6+40, fill = "yellow")
        
        # Answers
        self.textBlue = self.c.create_text(self.c_w/5, self.c_h/7*2.1, text=self.stblue, font=self.font_header2, fill="black", anchor = "w")
        self.textGreen = self.c.create_text(self.c_w/5, self.c_h/7*3.1, text=self.stgreen, font=self.font_header2, fill="black", anchor = "w")
        self.textRed = self.c.create_text(self.c_w/5, self.c_h/7*4.1, text=self.stred, font=self.font_header2, fill="black", anchor = "w")
        self.textWhite = self.c.create_text(self.c_w/5, self.c_h/7*5.1, text=self.stwhite, font=self.font_header2, fill="black", anchor = "w")
        self.textYellow = self.c.create_text(self.c_w/5, self.c_h/7*6, text=self.styellow, font=self.font_header2, fill="black", anchor = "w")

        # Scores
        self.textBluescore = self.c.create_text(self.c_w/6*5, self.c_h/7*2, text="0", font=self.font_header2, fill="blue")
        self.textGreenscore = self.c.create_text(self.c_w/6*5, self.c_h/7*3, text="0", font=self.font_header2, fill="green")
        self.textRedscore = self.c.create_text(self.c_w/6*5, self.c_h/7*4, text="0", font=self.font_header2, fill="red")
        self.textWhitescore = self.c.create_text(self.c_w/6*5, self.c_h/7*5, text="0", font=self.font_header2, fill="white")
        self.textYellowscore = self.c.create_text(self.c_w/6*5, self.c_h/7*6, text="0", font=self.font_header2, fill="yellow")

        # Pie chart
        self.total = self.io.scoreblue + self.io.scoregreen + self.io.scorered + self.io.scoreyellow + self.io.scorewhite
        def frac(n, total):
            return 360 * n / total
        self.pieCenter = self.c_w/6*5-200,self.c_h/2-200,self.c_w/6*5/2+200,self.c_h/2+200
        self.pieBlue = self.c.create_arc(self.pieCenter, start=0, extent=72, fill = "blue", state = "hidden")
        self.pieGreen = self.c.create_arc(self.pieCenter, start=72, extent=72, fill = "green", state = "hidden")
        self.pieRed = self.c.create_arc(self.pieCenter, start=144, extent=72, fill = "red", state = "hidden")
        self.pieWhite = self.c.create_arc(self.pieCenter, start=216, extent=72, fill = "white", state = "hidden")
        self.pieYellow = self.c.create_arc(self.pieCenter, start=288, extent=72, fill = "yellow", state = "hidden")

        self.textTimer = self.c.create_text(self.c_w/2, self.c_h/2, text="COUNTDOWN", font=self.font_header, fill="red")

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

    def timerReached(self):
        if self.i == 1:
            #self.c.itemconfig(ALL, state = "hidden")
            # self.c.itemconfig(self.textQuestion, state = "normal")        
            self.c.itemconfig(self.pieBlue, state = "normal")
            self.c.itemconfig(self.pieGreen, state = "normal")
            self.c.itemconfig(self.pieRed, state = "normal")
            self.c.itemconfig(self.pieWhite, state = "normal")
            self.c.itemconfig(self.pieYellow, state = "normal")
            self.i = 0
            self.timeRemaining = 5
        else:
            #self.c.itemconfig(ALL, state = "hidden")
            # self.c.itemconfig(self.textQuestion, state = "hidden")        
            self.c.itemconfig(self.pieBlue, state = "hidden")
            self.c.itemconfig(self.pieGreen, state = "hidden")
            self.c.itemconfig(self.pieRed, state = "hidden")
            self.c.itemconfig(self.pieWhite, state = "hidden")
            self.c.itemconfig(self.pieYellow, state = "hidden")
            self.i = 1
            self.timeRemaining = 5
        
        # dislpay the voting results screen, plus a countdown to the next vote session

    def updateUI(self):
        'update the UI to display scores every 200ms'
        self.c.itemconfig(self.textBluescore, text = self.io.scoreblue)
        self.c.itemconfig(self.textGreenscore, text = self.io.scoregreen)
        self.c.itemconfig(self.textRedscore, text = self.io.scorered)
        self.c.itemconfig(self.textYellowscore, text = self.io.scoreyellow)
        self.c.itemconfig(self.textWhitescore, text = self.io.scorewhite)
        self.c.itemconfig(self.textTimer, text= self.timeRemaining);
        self.root.after(200,self.updateUI)
