from tkinter import *
from tkinter import Tk
from tkinter import messagebox
from PIL import Image, ImageTk
from StaffReport import MySQLTkinterApp




class Report:
    def __init__ (self,root):

        self.root= root
        self.root.title("Manage Reports")
        self.root.geometry("1100x615+250+82")
        self.root.resizable(False,False)
        self.root["bg"] = "cadet blue"


        

    
        toplabel=Label(self.root, text="Manage Reports",font=("Time New Romen",20,"bold"), bg="black",fg="gold").pack(fill=X)


        report1_btn= Button(self.root, text="Student Report", width=17,font=("Time New Romens",14,"bold"),command = self.Student).place (x=145,y=48)
        report2_btn= Button(self.root, text="Fee Report",width=17, font=("Time New Romens",14,"bold"),command = self.Fee).place (x=445,y=48)
        report3_btn= Button(self.root, text="Staff Report",width=17, font=("Time New Romens",14,"bold"),command = self.Staff).place (x=745,y=48)
        


        #===========================add image=====================

        img = Image.open("report4.png")   # for giving path of the image always use forward slash
        img = img.resize((1095,510),Image.Resampling.NEAREST)
        self.photoimg = ImageTk.PhotoImage(img)

        label_image = Label(self.root, image = self.photoimg)
        label_image.place(x=0,y=100)



    def Student(self):
        messagebox.showinfo("Success", "Student Report Generated")

        import StudentReport


    def Fee(self):
        messagebox.showinfo("Success", "Fee Report Generated")

        import FeeReport


    def Staff(self):
        messagebox.showinfo("Success", "Staff Report Generated")

        # Create an instance of StaffReport and run it
        staff_report_root = Tk()
        staff_report_instance = MySQLTkinterApp(staff_report_root)
        staff_report_instance.run()



       




if __name__ == "__main__":
    root=Tk()
    obj= Report(root)
    root.mainloop()