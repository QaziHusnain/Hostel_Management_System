from tkinter import *
from tkinter import Tk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from manage_std import Student
from manage_staff import Staff
from room import Room
from account import Account
from report import Report





class Hostel_Management:
    def __init__ (self,root):

        self.root= root
        self.root.title("Hostel Management System")
        self.root.geometry("1350x700+0+0")
        self.root.resizable(False,False)
        
   
        
        label= Label(self.root, text="Hostel Management System", bg= "black",fg="gold", font=("Time New Romen", 30,"bold")).pack(fill=X)#place(x=550,y=20)

        frame2=Frame (self.root,width=250,height=650,bg="#2F4F4F" ).place(x=0,y=52)
        label2= Label(frame2, text= "Menu", font=("Time New Romen",16,"bold"),bg="#2F4F4F", fg="white").place(x=90,y= 80)
        
        b1=Button(frame2, text="Manage Student", command=self.student_win, bg= "black", fg="gold",bd=0,width=20, font=("Time New Romen",14,"bold") )
        b1.place (x=2,y=120)

        b2=Button(frame2, text="Manage Staff", command=self.staff_win, bg= "black", fg="gold",bd=0,width=20, font=("Time New Romen",14,"bold") )
        b2.place (x=2,y=170)

        b3=Button(frame2, text="Manage Room",command = self.room_win, bg= "black", fg="gold",bd=0,width=20, font=("Time New Romen",14,"bold") )
        b3.place (x=2,y=220)

        b4=Button(frame2, text="Manage Account",command = self.account_win, bg= "black", fg="gold",bd=0,width=20, font=("Time New Romen",14,"bold") )
        b4.place (x=2,y=270)

        b4=Button(frame2, text="Manage Report",command = self.report_win, bg= "black", fg="gold",bd=0,width=20, font=("Time New Romen",14,"bold") )
        b4.place (x=2,y=320)

        b4=Button(frame2, text="Logout", command = self.exit_window, bg= "black", fg="gold",bd=0,width=20, font=("Time New Romen",14,"bold") )
        b4.place (x=2,y=370)


        #===========================add image=====================

        img = Image.open("image3.png")   # for giving path of the image always use forward slash
        img = img.resize((1100, 645), Image.NEAREST)

        self.photoimg = ImageTk.PhotoImage(img)

        label_image = Label(self.root, image = self.photoimg)
        label_image.place(x=250,y=51)




    def student_win(self):
        self.new_window = Toplevel(self.root) #stfwindow is a variable and Toplevel is a widgt used for open toplevel window in homepage.
        self.app = Student(self.new_window)     #app is a variable is mn hamain apni Staff class ko rakhna ha or is mn stfwindow ko rkhna ha 
            


    def staff_win(self):
        self.new_window = Toplevel(self.root) 
        self.app = Staff(self.new_window)     
        
  
    def account_win(self):
        self.new_window = Toplevel(self.root) 
        self.app = Account(self.new_window)     
        
    
    def room_win(self):
        self.new_window = Toplevel(self.root) 
        self.app = Room(self.new_window)   


    def report_win(self):
        self.new_window = Toplevel(self.root) 
        self.app = Report(self.new_window)  
        

    def exit_window(self):
        exit_window= messagebox.askyesno("Confirmation","Are you sure you want to logout?")
        if exit_window > 0:
            self.root.destroy()
            return



if __name__ == "__main__":
    root=Tk()
    obj= Hostel_Management(root)
    root.mainloop()