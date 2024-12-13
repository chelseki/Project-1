from gui import *

def main():
    window = Tk()
    window.title('VOTING APPLICATION')
    window.geometry('500x700')
    window.resizable(False,False)

    GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()