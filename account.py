from tkinter import *
from tkinter import Tk
from PIL import Image, ImageTk
from fee import Fee
from salary import Salary


class Account:
    def __init__ (self,root):

        self.root= root
        self.root.title("Manage Accounts")
        self.root.geometry("1100x615+250+82")
        self.root.resizable(False,False)
        self.root["bg"] = "cadet blue"


        

    
        toplabel=Label(self.root, text="Manage Accounts",font=("Time New Romen",20,"bold"), bg="black",fg="gold").pack(fill=X)


        fee_btn= Button(self.root, text="Student Fee", width=17, font=("Time New Romens",14,"bold"), command = self.fee_win).place (x=300,y=48)
        salary_btn= Button(self.root, text="Staff salary",width=17, font=("Time New Romens",14,"bold"), command = self.salary_win).place (x=600,y=48)
        

        #===========================add image=====================

        img = Image.open("account.png")   # for giving path of the image always use forward slash
        img = img.resize((1095,510),Image.Resampling.NEAREST)
        self.photoimg = ImageTk.PhotoImage(img)

        label_image = Label(self.root, image = self.photoimg)
        label_image.place(x=0,y=100)



    def fee_win(self):

        self.new_window = Toplevel(self.root) #stfwindow is a variable and Toplevel is a widgt used for open toplevel window in homepage.
        self.app = Fee(self.new_window)     #app is a variable is mn hamain apni Staff class ko rakhna ha or is mn stfwindow ko rkhna ha 
            

    def salary_win(self):

        self.new_window = Toplevel(self.root) 
        self.app = Salary(self.new_window)     




if __name__ == "__main__":
    root=Tk()
    obj= Account(root)
    root.mainloop()