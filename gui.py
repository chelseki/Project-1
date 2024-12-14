from tkinter import *
import csv

class GUI:
    """
    A class that sets up the GUI
    """
    def __init__(self,window) -> None:
        """
        Initializes the window.

        :param window: Main window
        """
        self.window = window

        self.frame_one = Frame(self.window)
        self.text_label = Label(self.frame_one, text='BALLOT', font=('Courier', 24, 'bold'))
        self.text_label.pack(side='top')
        self.frame_one.pack(pady=5)

        self.frame_two = Frame(self.window)
        self.label_name = Label(self.frame_two, text='Name',font=('Courier', 24))
        self.input_name = Entry(self.frame_two, width=40)
        self.label_name.pack(side='left')
        self.input_name.pack()
        self.frame_two.pack(pady=10)

        self.frame_three = Frame(self.window)
        self.label_id = Label(self.frame_three, text='ID',font=('Courier', 24))
        self.input_id = Entry(self.frame_three, width=40)
        self.label_id.pack(side='left')
        self.input_id.pack()
        self.frame_three.pack(pady=10)

        self.frame_four = Frame(self.window)
        self.cand_label = Label(self.frame_four, text='Candidates:', font=('Courier', 24, 'bold'))
        self.cand_label.pack(side='top')
        self.frame_four.pack()

        self.frame_five = Frame(self.window)
        self.radio_answer = IntVar()
        self.radio_answer.set(0)
        self.radio_jane = Radiobutton(self.frame_five, text='Jane', variable=self.radio_answer,value=1, font=('Times New Roman', 24))
        self.radio_jane.pack(side='left')
        self.frame_five.pack(pady=15)

        self.frame_six = Frame(self.window)
        self.radio_john = Radiobutton(self.frame_six, text='John', variable=self.radio_answer, value=2,font=('Times New Roman', 24))
        self.radio_john.pack(side='left')
        self.frame_six.pack(pady=10)

        self.frame_seven = Frame(self.window)
        self.radio_misc = Radiobutton(self.frame_seven, text='', variable=self.radio_answer, value=3)
        self.input_misc = Entry(self.frame_seven, width=20)
        self.radio_misc.pack(side='left')
        self.input_misc.pack(side='left')
        self.frame_seven.pack(pady=15)

        self.frame_eight = Frame(self.window)
        self.vote_button = Button(self.window, text='VOTE', font=('Courier',24, 'bold'), command=self.submit)
        self.result_button = Button(self.window, text='RESULTS', font=('Courier', 24, 'bold'), command=self.result)
        self.text_label = Label(self.frame_eight, text='Cast your vote!', font=('Arial',17))
        self.text_label.pack(side='bottom')
        self.vote_button.pack(side='top')
        self.result_button.pack(side='bottom')
        self.frame_eight.pack(pady=10)

    def submit(self) -> None:
        """
        Submits the vote the user inputs into a data.csv file.

        Verifies name, ID, and vote are valid inputs.
        If the input is invalid it will return an error message. If valid, the name, ID, and vote are stored in the CSV file.

        """
        name: str = self.input_name.get().strip()
        id: str = self.input_id.get().strip()
        candidates: str  = self.radio_answer.get()
        third_candidate: str = self.input_misc.get().strip()

        try:
            if name == "":
                raise ValueError()
            if not name.isalpha():
                raise ValueError()
        except ValueError:
            self.text_label.config(text='Invalid name, try again')
            return

        try:
            id:int = int(id)
            if id == "" and id < 0:
                raise ValueError()
        except ValueError:
            self.text_label.config(text='Enter correct ID value')
            return

        try:
            if candidates != 1 and candidates != 2 and candidates != 3:
                raise ValueError()
        except ValueError:
            self.text_label.config(text='Pick a candidate')
            return

        try:
            if candidates == 3:
                if third_candidate == "":
                    raise ValueError()
                if not name.isalpha():
                    raise ValueError()
        except ValueError:
            self.text_label.config(text='Invalid candidate name, try again')
            return

        if candidates == 1:
            candidate_name: str = 'Jane'
        elif candidates == 2:
            candidate_name: str = 'John'
        elif candidates == 3:
            candidate_name: str = third_candidate

        try:
            with open('data.csv','r', newline='') as filee:
                reader = csv.reader(filee)
                for word in reader:
                    if word[1] == str(id):
                        raise ValueError()
        except ValueError:
            self.text_label.config(text='Already voted')
            return

        with open('data.csv','a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name,id,candidate_name])

        self.input_name.delete(0,END)
        self.input_id.delete(0, END)
        self.radio_answer.set(0)
        self.input_misc.delete(0, END)
        self.text_label.config(text='Thanks for voting!')

    def result(self) -> None:
        """
        Displays the voting results.

        Reads the CSV file and counts up the votes for each candidate then calculates the total number of votes.
        """
        total_vote: int = 0
        vote_dict: dict[str, int] = {}

        with open('data.csv','r',newline='') as file2:
            reader=csv.reader(file2)
            next(reader)
            for word in reader:
                candidate = word[2].strip()
                if candidate in vote_dict:
                    vote_dict[candidate] += 1
                else:
                    vote_dict[candidate] = 1
                total_vote += 1

            the_results: str = "Vote Results:\n\n"
            for candidate, num in vote_dict.items():
                the_results += f'{candidate} - {num} votes\n'
            the_results += f'\n Total Votes: {total_vote}'

            self.text_label.config(text=the_results)