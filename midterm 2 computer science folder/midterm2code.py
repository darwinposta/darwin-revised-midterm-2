#darwin posta - R01504119

#import modules
from tkinter import *
from datetime import datetime

#create class
class GUI:
    def __init__(self):
        self.homepage() #opens up to the home page on start
        

    def homepage(self):
        self.hidden=0 #sets the hidden value to 0, used for removing frames and returning to the home page
        self.frame = Frame(window) #creates frame "frame"
        frame = self.frame #lets you use frame instead of having to type out self.frame, just me being lazy

        Button(frame, text="Return to homepage", command=self.goHome).grid(row=0, column=1) #next four lines are the return to homepage buttons, as well as the three buttons to the different "games" i put in

        convBtn = Button(frame, text="Calculate annual interest", command=self.interest).grid(row=1, column=1,sticky=N)
        convCelFahr = Button(frame, text="Convert Celsius and Fahrenheit", command=self.conversion).grid(row=1, column=2,sticky=N)
        timeBtn = Button(frame, text="Show the time", command=self.getTime).grid(row=2,column=1,sticky=N)

        frame.pack(side = TOP) #packs the frame to top

        window.mainloop()


    def interest(self): #creates the process to decide whether filled, as well as rectangle or oval

        self.hidden = 1 #sets hidden var to 1
        self.frame1 = Frame(window)
        frame1 = self.frame1 

        lbl1 = Label(frame1, text="Investment Amount").grid(row=1, column=1, sticky=W) #creates four labels stuck to the left side of the screen
        lbl2 = Label(frame1, text="Years").grid(row=2, column=1, sticky=W)
        lbl3 = Label(frame1, text="Annual Interest Rate").grid(row=3, column=1, sticky=W)
        lbl4 = Label(frame1, text="Future Value").grid(row=4, column=1, sticky=W)


        self.investmentAmount = StringVar() #creates entry boxes and one label to handle the interest calculations
        entry1 = Entry(frame1, textvariable=self.investmentAmount, justify=RIGHT).grid(row=1, column=2)

        self.annualIR = StringVar()
        entry2 = Entry(frame1, textvariable=self.annualIR, justify=RIGHT).grid(row=3, column=2)

        self.numberOfYears = StringVar()
        entry3 = Entry(frame1, textvariable=self.numberOfYears, justify=RIGHT).grid(row=2, column=2)

        self.futureValue = StringVar()
        Label(frame1, textvariable=self.futureValue).grid(row=4, column=2, sticky=E)

        computeBtn = Button(frame1, text="Calculate", command=self.compute).grid(row=6, column=2, sticky=E)

        frame1.pack(side = BOTTOM)

    def compute(self): #this class is used to do the math needed for the class above
        monthlyIR = float(self.annualIR.get()) / 1200

        f = float(self.investmentAmount.get()) * \
            (1 + monthlyIR) ** (float(self.numberOfYears.get()) * 12)

        self.futureValue.set("{0:10.2f}".format(f))

    def conversion(self): #this class deals with the temperature conversion part
        self.frame2 = Frame(window)
        frame2 = self.frame2

        self.hidden = 2 #sets hidden var to 2

        label1 = Label(frame2, text="Enter celsius here").grid(row=1,column=1,sticky=W) #this stuff is self explanatory, sets intvars for input and output of fahr and cel, has input boxes and all that good stuff

        self.inputCel = IntVar()
        Entry(frame2, textvariable=self.inputCel).grid(row=2,column=1,sticky=W)

        self.newFahr = IntVar()
        Label(frame2, textvariable=self.newFahr, justify = LEFT).grid(row=3,column=1,sticky=W)

        Button(frame2, text="Calculate C to F", command=self.celsiusToFahrenheit).grid(row=4,column=1,sticky=W)

        Label(frame2, text="Enter fahrenheit here").grid(row=1,column=2,sticky=E)

        self.inputFahr = IntVar()
        Entry(frame2, textvariable = self.inputFahr).grid(row=2,column=2,sticky=E)

        self.newCel = IntVar()
        Label(frame2, textvariable = self.newCel, justify = RIGHT).grid(row=3,column=2,sticky=E)

        Button(frame2, text="Calculate F to C", command = self.fahrenheitToCelsius).grid(row=4,column=2,sticky=E)

        frame2.pack(side = BOTTOM)

    def celsiusToFahrenheit(self): #class deals with calculations for the conversion class
        f = (9/5) * self.inputCel.get() + 32 

        self.newFahr.set("{0:10.2f}".format(f))

    def fahrenheitToCelsius(self): #came as above
        c = (5/9) * (self.inputFahr.get() - 32)

        self.newCel.set("{0:10.2f}".format(c))

    def getTime(self): 

        self.frame3 = Frame(window)
        frame3 = self.frame3

        self.hidden = 3

        now = datetime.now().strftime("%H:%M:%S") #gets hours minutes and seconds to display

        self.canvas = Canvas(window, width=500, height=500, bg="white") #creates a convas for the clock and the time to be put on

        self.canvas.pack() #packs canvas
        
        self.canvas.create_oval(50, 50, 450, 450)
        self.canvas.create_text(250, 50, text="12")
        self.canvas.create_text(50, 250, text="9")
        self.canvas.create_text(450, 250, text="3")
        self.canvas.create_text(250, 450, text="6")
        self.canvas.create_text(250, 470, text=now) #puts the time on the canvas
        self.canvas.create_line(250,250,100,160,width=2)
        self.canvas.create_line(250,250,230,360,width="3")
        self.canvas.create_line(250,250,300,300)

    def goHome(self): #this class basically just hides modules whenever you click the return to homepage
        if self.hidden == 1:
            self.frame1.destroy()
            self.hidden = 0
            print("Returned to homepage")
        elif self.hidden == 2:
            self.frame2.destroy()
            self.hidden = 0
            print("Returned to homepage")
        elif self.hidden == 3:
            self.canvas.destroy()
            self.hidden = 0
            print("Returned to homepage")   
        else:
            print("Cannot delete the homepage")

window = Tk() #makes window an object for the frames and canvas to be put on

GUI() #invokes big class