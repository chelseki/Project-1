from tkinter import *
import csv

class GUI:
    def __init__(self,window):
        self.window = window

        self.frame_one = Frame(self.window)
        self.text_label = Label(self.frame_one, text='BALLOT', font=('Arial', 24, 'bold'))
        self.text_label.pack(side='top')
        self.frame_one.pack(pady=5)

        self.frame_two = Frame(self.window)
        self.label_name = Label(self.frame_two, text='Name',font=('Arial', 24))
        self.input_name = Entry(self.frame_two, width=40)
        self.label_name.pack(side='left')
        self.input_name.pack()
        self.frame_two.pack(pady=10)

        self.frame_three = Frame(self.window)
        self.label_id = Label(self.frame_three, text='ID',font=('Arial', 24))
        self.input_id = Entry(self.frame_three, width=40)
        self.label_id.pack(side='left')
        self.input_id.pack()
        self.frame_three.pack(pady=10)


        self.frame_four = Frame(self.window)
        self.cand_label = Label(self.frame_four, text='Candidates: ', font=('Arial', 24))
        self.radio_answer = IntVar()
        self.radio_answer.set(0)
        self.radio_jane = Radiobutton(self.frame_four, text='Jane ', variable=self.radio_answer,value=1, font=('Arial', 24))
        self.radio_john = Radiobutton(self.frame_four, text='John ', variable=self.radio_answer, value=2,font=('Arial', 24))
        self.radio_jack = Radiobutton(self.frame_four, text='Jack ', variable=self.radio_answer, value=3, font=('Arial', 24))
        self.cand_label.pack(side='left')
        self.radio_jane.pack(side='left')
        self.radio_john.pack(side='left')
        self.radio_jack.pack(side='left')
        self.frame_four.pack(pady=10)

        self.frame_five = Frame(self.window)
        self.radio_answer = IntVar()
        self.radio_answer.set(0)
        self.radio_misc = Radiobutton(self.frame_five, text='', variable=self.radio_answer, value=4)
        self.input_misc = Entry(self.frame_five, width=40)
        self.radio_misc.pack(side='left')
        self.input_misc.pack(side='left')
        self.frame_five.pack()




        # self.frame_five = Frame(self.window)
        # self.vote_button = Button(self.window, text='VOTE', font=('Arial',20,'bold'), command=self.submit)
        # self.vote_button.pack(side='top')
        # self.frame_five.pack(pady=50)

    def submit(self):
        name = self.input_name.get().strip()
        id = self.input_id.get()
        candidates = self.radio_answer.get()