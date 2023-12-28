from tkinter import *
from tkinter import ttk
import tkinter as tk


class Daily_Report:
    def __init__ (self,root):

        self.root= root
        self.root.title("Daily Report")
        self.root.geometry("1100x480+250+215")
        self.root.resizable(False,False)


        #=======top label for Heading=======
        toplabel=Label(self.root, text="Daily Report",font=("Time New Romen",14,"bold"), bg="black",fg="gold").pack(fill=X)


        label_id = Label(self.root, text="Student Registered :", font=("Time New Romen", 16, "bold")).place(x=350,y=120)
        label_id = Label(self.root, text="Staff Registered :", font=("Time New Romen", 16, "bold")).place(x=350,y=160)
        label_id = Label(self.root, text="Fee Collected :", font=("Time New Romen", 16, "bold")).place(x=350,y=200)
        label_id = Label(self.root, text="Discount given :", font=("Time New Romen", 16, "bold")).place(x=350,y=240)
        





if __name__ == "__main__":
    root=Tk()
    obj= Daily_Report(root)
    root.mainloop()