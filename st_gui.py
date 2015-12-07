# UI class
from Tkinter import *
from PIL import Image, ImageTk
import time
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
        self.font_header2 = tkFont.Font(family="Helvetica", size=36, weight="bold")

    def initGui(self):
        self.c = Canvas(self.root, width=self.c_w, height=self.c_h, bg="grey")

        # make everything centered, that way we can deal with different resolutions easier instead of
        # anchoring everything to the top left
        self.imageBG = Image.open("resources/bg.jpg")
        self.photoBG = ImageTk.PhotoImage(self.imageBG)
        self.bg = self.c.create_image(self.c_w/2,self.c_h/2,image=self.photoBG)

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
        self.circleBlue = self.c.create_oval(self.c_w/7-40, self.c_h/7*2-40, self.c_w/7+40, self.c_h/7*2+40, fill = "blue", tags = "circle")
        self.circleGreen = self.c.create_oval(self.c_w/7-40, self.c_h/7*3-40, self.c_w/7+40, self.c_h/7*3+40, fill = "green", tags = "circle")
        self.circleRed = self.c.create_oval(self.c_w/7-40, self.c_h/7*4-40, self.c_w/7+40, self.c_h/7*4+40, fill = "red", tags = "circle")
        self.circleWhite = self.c.create_oval(self.c_w/7-40, self.c_h/7*5-40, self.c_w/7+40, self.c_h/7*5+40, fill = "white", tags = "circle")
        self.circleYellow = self.c.create_oval(self.c_w/7-40, self.c_h/7*6-40, self.c_w/7+40, self.c_h/7*6+40, fill = "yellow", tags = "circle")
        
        # Answers
        self.textBlue = self.c.create_text(self.c_w/5, self.c_h/7*2.1, text=self.stblue, font=self.font_header2, fill="black", anchor = "w")
        self.textGreen = self.c.create_text(self.c_w/5, self.c_h/7*3.1, text=self.stgreen, font=self.font_header2, fill="black", anchor = "w")
        self.textRed = self.c.create_text(self.c_w/5, self.c_h/7*4.1, text=self.stred, font=self.font_header2, fill="black", anchor = "w")
        self.textWhite = self.c.create_text(self.c_w/5, self.c_h/7*5.1, text=self.stwhite, font=self.font_header2, fill="black", anchor = "w")
        self.textYellow = self.c.create_text(self.c_w/5, self.c_h/7*6, text=self.styellow, font=self.font_header2, fill="black", anchor = "w")

        # Scores
        self.textBluescore = self.c.create_text(self.c_w/7, self.c_h/7*2, text="0", font=self.font_header2, fill="blue", state = "hidden", tags = "score")
        self.textGreenscore = self.c.create_text(self.c_w/7, self.c_h/7*3, text="0", font=self.font_header2, fill="green", state = "hidden", tags = "score")
        self.textRedscore = self.c.create_text(self.c_w/7, self.c_h/7*4, text="0", font=self.font_header2, fill="red", state = "hidden", tags = "score")
        self.textWhitescore = self.c.create_text(self.c_w/7, self.c_h/7*5, text="0", font=self.font_header2, fill="white", state = "hidden", tags = "score")
        self.textYellowscore = self.c.create_text(self.c_w/7, self.c_h/7*6, text="0", font=self.font_header2, fill="yellow", state = "hidden", tags = "score")

        # Pie chart
        self.pieCenter = self.c_w/2-200,self.c_h/3-200,self.c_w/2+200,self.c_h/3+200
        self.pieBlue = self.c.create_arc(self.pieCenter, start=0, extent=72, fill = "blue", state = "hidden")
        self.pieGreen = self.c.create_arc(self.pieCenter, start=72, extent=72, fill = "green", state = "hidden")
        self.pieRed = self.c.create_arc(self.pieCenter, start=144, extent=72, fill = "red", state = "hidden")
        self.pieWhite = self.c.create_arc(self.pieCenter, start=216, extent=72, fill = "white", state = "hidden")
        self.pieYellow = self.c.create_arc(self.pieCenter, start=288, extent=72, fill = "yellow", state = "hidden")

        self.updateUI()

        self.c.pack()

    def updateUI(self):
        'update the UI to display scores every 200ms'
        self.c.itemconfig(self.textBluescore, text = self.io.scoreblue)
        self.c.itemconfig(self.textGreenscore, text = self.io.scoregreen)
        self.c.itemconfig(self.textRedscore, text = self.io.scorered)
        self.c.itemconfig(self.textYellowscore, text = self.io.scoreyellow)
        self.c.itemconfig(self.textWhitescore, text = self.io.scorewhite)

        if time.time() - self.io.lastTime < 5:      
            self.c.itemconfig("circle", state="hidden")
            self.c.itemconfig("score", state="normal")
        else:
            self.c.itemconfig("circle", state="normal")
            self.c.itemconfig("score", state="hidden")

        self.root.after(200,self.updateUI)
