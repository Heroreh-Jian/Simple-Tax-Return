from tkinter import *

root = Tk()  # creates the window

root.title("2016 Tax Return Form - 1040NR-EZ")


# frame = Frame(root)  # basic frame to include all other frames in the form
# frame.pack()

# Form Title
titleframe = Frame(root)
titleframe.pack(side=TOP, fill=X)

formnum = Label(titleframe, text="Form 1040NR-EZ",
                highlightbackground="black",
                highlightthickness=1,
                padx=78).grid(row=0, column=0, sticky=W + E + N + S)
formname = Label(titleframe,
                 text="U.S. Income Tax Return for Certain\nNonresident Aliens With No Dependents",
                 highlightbackground="black",
                 highlightthickness=1,
                 padx=200,
                 pady=10).grid(row=0, column=1, sticky=W + E + N + S)
formyear = Label(titleframe, text="2016",
                 highlightbackground="black",
                 highlightthickness=1,
                 anchor=SW,
                 padx=60).grid(row=0, column=2, sticky=W + E + N + S)

# Basic Info 
infoframe = Frame(root, highlightbackground="black",
                  highlightthickness= 1) # add color temporarily
infoframe.pack(side=TOP, fill=X)

Label(infoframe, text="Your first name and initial",
      width=40,
      anchor=W).grid(row=0, column=0, sticky=W + E + N + S)
Label(infoframe, text="Last name",
      width=40,
      anchor=W).grid(row=0, column=1, sticky=W + E + N + S)
Label(infoframe, text="Identifying number",
      width=40,
      anchor=W).grid(row=0, column=2, sticky=W + E + N + S)


firstname = Entry(infoframe,bg="#ACE5EE").grid(row=1, column=0, sticky=W + E + N + S)
lastname = Entry(infoframe,bg="#ACE5EE").grid(row=1, column=1, sticky=W + E + N + S)
idnumber = Entry(infoframe,bg="#ACE5EE").grid(row=1, column=2, sticky=W + E + N + S)


Label(infoframe, text= "Present home address (number, street, and apt. no., or rural route). If you have a P.O. box, see instructions.",
      width=40,
      anchor=W).grid(row=2, column=0, columnspan=3, sticky=W + E + N + S)

address = Entry(infoframe,bg="#ACE5EE")
address.grid(row=3, column=0, columnspan=3, sticky=W + E + N + S)


Label(infoframe, text= "City, town or post office, state, and ZIP code. If you have a foreign address, also complete spaces below (see instructions).",
      width=40,
      anchor=W).grid(row=4, column=0, columnspan=3, sticky=W + E + N + S)

city = Entry(infoframe,bg="#ACE5EE").grid(row=5, column=0,
                             columnspan=3, sticky=W + E + N + S)


Label(infoframe, text="Foreign country name",
      width=40,
      anchor=W).grid(row=6, column=0)
Label(infoframe, text="Foreign province/state/county",
      width=40,
      anchor=W).grid(row=6, column=1)
Label(infoframe, text="Foreign postal code",
      width=40,
      anchor=W).grid(row=6, column=2)

fcountryname = Entry(infoframe,bg="#ACE5EE").grid(row=7, column=0, sticky=W + E + N + S)
fstate = Entry(infoframe,bg="#ACE5EE").grid(row=7, column=1, sticky=W + E + N + S)
fpostalcode = Entry(infoframe,bg="#ACE5EE").grid(row=7, column=2, sticky=W + E + N + S)


# Fill-in Form
bodyframe = Frame(root, highlightbackground="red",
                  highlightthickness=1)
bodyframe.pack(side=TOP, fill=BOTH, expand=1)

canvas = Canvas(bodyframe,
                width=1000,
                height=300)

# put a frame inside of the canvas to scroll the widgets in this frame
incanvasframe = Frame(canvas,
                      width=1000,
                      height=600)

yscrollbar = Scrollbar(bodyframe, orient=VERTICAL,
                       command=canvas.yview)
canvas.configure(yscrollcommand=yscrollbar.set)

yscrollbar.pack(side=RIGHT, fill=Y)
canvas.pack(side=LEFT, fill=BOTH, expand=1)



taxcontent = [
    "  3. Wages, salaries, tips, etc. Attach Form(s) W-2 . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  ",
    "  4. Taxable refunds, credits, or offsets of state and local income taxes . . . . . . . . . .  . . .  . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . ",
    "  5. Scholarship and fellowship grants. Attach Form(s) 1042-S or required statement. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ",
    "  6. Total income exempt by a treaty from page 2, Item J(1)(e) . . . . . .  . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  ",
    "  7. Add lines 3, 4, and 5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  ",
    "  8. Scholarship and fellowship grants excluded. . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  ",
    "  9. Student loan interest deduction  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . ",
    "  10. Subtract the sum of line 8 and line 9 from line 7. This is your adjusted gross income . .  .  . . . . . . . . . . . . . . . . . . . . . . . . . . .",
    "  11. Itemized deductions (see instructions). . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  ",
    "  12.Subtract line 11 from line 10 . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . ",
    "  13. Exemption (see instructions). . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  ",
    "  14. Taxable income. Subtract line 13 from line 12. If line 13 is more than line 12, enter -0-. .  . . . . . . . . . . . . . . . . . . . . . . ",
    "  15. Tax. Find your tax in the tax table in the instructions . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ",
    "  16. Unreported social security and Medicare tax from Form:. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .",
    "  17. Add lines 15 and 16. This is your total tax  . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .",
    "  18 a. Federal income tax withheld from Form(s) W-2 and 1099-R . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ",
    "     b. Federal income tax withheld from Form(s) 1042-S . .. . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .",
    "  19. 2015 estimated tax payments and amount applied from 2014 return.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .",
    "  20. Credit for amount paid with Form 1040-C . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ",
    "  21. Add lines 18a through 20. These are your total payments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .",
    "__________________________________________________________________________________________________________________________________________________________",
    "  22. If line 21 is more than line 17, subtract line 17 from line 21. This is the amount you overpaid  . . . . .  . . . . . . . . . . . . . .",
    "  25. Amount you owe. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ",
    ]


def show_taxcontent():
    x = 0
    for content in taxcontent:
            Label(incanvasframe,
                  text=content).grid(row=x, column=0, sticky=W + N)
            x = x + 1

show_taxcontent()

def canvas_function(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


canvas.create_window((0, 0), window=incanvasframe, anchor=W)
incanvasframe.bind("<Configure>", canvas_function)



# Submit to calculate the tax
submitbutton = Button(root, text="Submit")
submitbutton.pack(side=TOP)


class SampleApp(Tk):
    def __init__(self, root, bodyframe, button):
       
        self.frame = bodyframe
        self.button = button
        self.button.config(command=self.on_button)
        self.entry3 = StringVar()
        self.entry4 = StringVar()
        self.entry5 = StringVar()
        self.entry6 = StringVar()
        self.entry8 = StringVar()
        self.entry9 = StringVar()
        self.entry11 = StringVar()
        self.entry13 = StringVar()
        self.entry15 = StringVar()
        self.entry16 = StringVar()
        self.label7 = StringVar()
        self.label10 = StringVar()
        self.label12 = StringVar()
        self.label14 = StringVar()
        self.label17 = StringVar()
        self.label18 = StringVar()
        self.entry17 = StringVar()
        self.entry18 = StringVar()
        self.entry19 = StringVar()
        self.entry20 = StringVar()
        self.label19 = StringVar()
        self.label20 = StringVar()
        
        self.ans_3 = Entry(self.frame, textvariable=self.entry3,bg="#ACE5EE").grid(row=0,
                           column=2, sticky=W + E + N + S)
        self.ans_4 = Entry(self.frame, textvariable=self.entry4,bg="#ACE5EE").grid(row=1,
                           column=2, sticky=W + E + N + S)
        self.ans_5 = Entry(self.frame, textvariable=self.entry5,bg="#ACE5EE").grid(row= 2, column= 2, sticky= W+E+N+S)
        self.ans_6 = Entry(self.frame, textvariable=self.entry6,bg="#ACE5EE").grid(row= 3, column= 1, sticky= W+E+N+S)
        self.ans_7 = Label(self.frame, textvariable=self.label7, bg="light blue").grid(row= 4, column= 2, sticky= W+E+N+S)
        self.ans_8 = Entry(self.frame, textvariable=self.entry8,bg="#ACE5EE").grid(row= 5, column= 1, sticky= W+E+N+S)
        self.ans_9 = Entry(self.frame, textvariable=self.entry9,bg="#ACE5EE").grid(row= 6, column= 1, sticky= W+E+N+S)
        self.ans_10 = Label(self.frame, textvariable=self.label10, bg="light blue").grid(row= 7, column= 2, sticky= W+E+N+S)
        self.ans_11 = Entry(self.frame, textvariable=self.entry11,bg="#ACE5EE").grid(row= 8, column= 2, sticky= W+E+N+S)
        self.ans_12 = Label(self.frame, textvariable=self.label12, bg="light blue").grid(row= 9, column= 2, sticky= W+E+N+S)
        self.ans_13 = Entry(self.frame, textvariable=self.entry13,bg="#ACE5EE").grid(row= 10, column= 2, sticky= W+E+N+S)
        self.ans_14 = Label(self.frame, textvariable=self.label14,bg="#5DADEC").grid(row= 11, column= 2, sticky= W+E+N+S)
        self.ans_15 = Entry(self.frame, textvariable=self.entry15,bg="#ACE5EE").grid(row= 12, column= 2, sticky= W+E+N+S)
        self.ans_16 = Entry(self.frame, textvariable=self.entry16,bg="#ACE5EE").grid(row= 13, column= 2, sticky= W+E+N+S)
        self.ans_17 = Label(self.frame, textvariable=self.label17, bg="light blue").grid(row= 14, column= 2, sticky= W+E+N+S)
        self.ans_18a = Entry(self.frame,textvariable=self.entry17,bg="#ACE5EE").grid(row= 15, column= 1, sticky= W+E+N+S)
        self.ans_18b = Entry(self.frame,textvariable=self.entry18,bg="#ACE5EE").grid(row= 16, column= 1, sticky= W+E+N+S)
        self.ans_19 = Entry(self.frame,textvariable=self.entry19,bg="#ACE5EE").grid(row= 17, column= 1, sticky= W+E+N+S)
        self.ans_20 = Entry(self.frame,textvariable=self.entry20,bg="#ACE5EE").grid(row= 18, column= 1, sticky= W+E+N+S)
        self.ans_21 = Label(self.frame, textvariable=self.label18, bg="light blue").grid(row= 19, column= 2, sticky= W+E+N+S)
        self.ans_22 = Label(self.frame, textvariable=self.label19, bg="light blue").grid(row= 21, column= 2, sticky= W+E+N+S)
        self.ans_25 = Label(self.frame, textvariable=self.label20, bg="light blue").grid(row= 22, column= 2, sticky= W+E+N+S)

    def on_button(self):
        ans7_output = int(float(self.entry3.get())) + int(float(self.entry4.get())) + int(float(self.entry5.get()))
        print(ans7_output)
        self.label7.set(str(ans7_output))
        ans10_output = ans7_output - int(float(self.entry6.get())) -int(float(self.entry8.get()))- int(float(self.entry9.get()))
        print(ans7_output)
        self.label10.set(str(ans10_output))
        ans12_output = ans10_output - int(float(self.entry11.get()))
        print(ans12_output)
        self.label12.set(str(ans12_output))
        ans14_output = ans12_output - int(float(self.entry13.get()))
        self.label14.set(str(ans14_output))
        ans17_output = int(float(self.entry15.get())) + int(float(self.entry16.get()))
        self.label17.set(str(ans17_output))
        ans21_output = int(float(self.entry17.get())) + int(float(self.entry18.get()))+int(float(self.entry19.get()))+ int(float(self.entry20.get()))
        self.label18.set(str(ans21_output))
        result=ans17_output-ans21_output
        if result<=0:
            ans22_output = ans21_output-ans17_output
            self.label19.set(str(ans22_output))
        else:
            ans25_output = abs(ans17_output-ans21_output)
            self.label20.set(str(ans25_output))

app = SampleApp(root, incanvasframe, submitbutton)


root.mainloop()
