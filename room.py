from tkinter import *
from tkinter import Tk
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import mysql.connector


class Room:
    def __init__ (self,root):

        self.root= root
        self.root.title("Manage Room")
        self.root.geometry("1100x615+250+82")
        self.root.resizable(False,False)
        self.root["bg"] = "cadet blue"

   

        toplabel=Label(self.root, text="Manage Room",font=("Time New Romen",22,"bold"), bg="black",fg="gold").pack(fill=X)

        #frame2=Frame (self.root,width=350,height=655,bg="cadet blue",bd=4, relief=RIDGE ).place(x=0,y=38)

        #label2= Label(frame2, text= "Register Staff", font=("Time New Romen",16,"bold"),bg="#2F4F4F", fg="white").place(x=110,y= 60)
        id_value = IntVar()
        label_id = Label(self.root, text="ID", font=("Time New Romen", 12, "bold"), bg="cadet blue", fg="white").place(x=20,y=50)
        id_entry = Entry(self.root, width=30, textvariable=id_value).place(x=160, y=55)

        name = StringVar()
        label_name = Label(self.root, text="Name", font=("Time New Romen", 12, "bold"), bg="cadet blue", fg="white").place(x=20, y=100)
        name_entry = Entry(self.root, width=30, textvariable=name).place(x=160, y=105)
        fname = StringVar()
        label_fname = Label(self.root, text="Father Name", font=("Time New Romen", 12, "bold"), bg="cadet blue",fg="white").place(x=20, y=150)
        fname_entry = Entry(self.root, width=30, textvariable=fname).place(x=160, y=155)
        addres = StringVar()
        label_address = Label(self.root, text="Address", font=("Time New Romen", 12, "bold"), bg="cadet blue",fg="white").place(x=20, y=200)
        address_entry = Entry(self.root, width=30, textvariable=addres).place(x=160, y=205)
        DOB= StringVar()
        label_dob = Label(self.root, text="Date of Birth", font=("Time New Romen", 12, "bold"), bg="cadet blue",fg="white").place(x=20, y=250)
        dob_entry = Entry(self.root, width=30, textvariable=DOB).place(x=160, y=255)
        age = StringVar()
        label_age = Label(self.root, text="Age", font=("Time New Romen", 12, "bold"), bg="cadet blue", fg="white").place(x=20,y=300)
        age_entry = Entry(self.root, width=30, textvariable=age).place(x=160, y=305)
        contact = StringVar()
        label_contact = Label(self.root, text="Contact Number", font=("Time New Romen", 12, "bold"), bg="cadet blue",fg="white").place(x=20, y=350)
        contact_entry = Entry(self.root, width=30, textvariable=contact).place(x=160, y=355)
        roomn = StringVar()
        label_room_no = Label(self.root, text="Room No", font=("Time New Romen", 12, "bold"), bg="cadet blue",fg="white").place(x=20, y=400)
        room_no_entry = Entry(self.root, width=30, textvariable=roomn).place(x=160, y=405)
        fee = StringVar()
        label_room_fee = Label(self.root, text="Room Fee", font=("Time New Romen", 12, "bold"), bg="cadet blue",fg="white").place(x=20, y=455)
        room_fee_entry = Entry(self.root, width=30, textvariable=fee).place(x=160, y=455)

       
         #=========== frame for separation ==========
        sep_frame = Frame(self.root, bd=5, width=4, height=500, bg="black")
        sep_frame.place(x=360, y=60)


#===========Button Frame and Buttons=================       
        #btn_frame=Frame (self.root,width=750,height=207,bg="cadet blue",bd=4, relief=RIDGE ).place(x=350,y=38)

        btn1 = Button(self.root, text="Allocate Room", bg="black", fg="gold", bd=2, width=14,
                            font=("time new romens", 14, "bold"))
        btn1.place(x=400, y=48)
        
        btn1 = Button(self.root, text="Remove Allocation", command=self.remove, bg="black", fg="gold", bd=2, width=16,
                            font=("time new romens", 14, "bold"))
        btn1.place(x=635, y=48)
        
        btn1 = Button(self.root, text="Add New Room", command =self.open, bg="black", fg="gold", bd=2, width=14,
                            font=("time new romens", 14, "bold"))
        btn1.place(x=870, y=48)


# =============================frame for tree==========================
        Tree_frame = Frame(self.root, bd=5, width=700, height=450, bg="cadet blue", relief=RIDGE)
        Tree_frame.place(x=380, y=100)


        scroll_x = Scrollbar(Tree_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Tree_frame, orient=VERTICAL)
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hostel"
        )
        cursor = conn.cursur()

        self.room_detail = ttk.Treeview(Tree_frame, height=15, columns=(
        "StdID", "Name", "Father Name", "Address", "DOB", "Age", "Contact No", "Room No", "Room Fee"),
                                 xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.room_detail.heading("StdID", text="ID")
        self.room_detail.heading("Name", text="Name")
        self.room_detail.heading("Father Name", text="Father Name")
        self.room_detail.heading("Address", text="Address")
        self.room_detail.heading("DOB", text="DOB")
        self.room_detail.heading("Age", text="Age")
        self.room_detail.heading("Contact No", text="Contact No")
        self.room_detail.heading("Room No", text="Room No")
        self.room_detail.heading("Room Fee", text="Room Fee")

        self.room_detail["show"] = "headings"

        self.room_detail.column("StdID", anchor=tk.CENTER, width=120)
        self.room_detail.column("Name", anchor=tk.CENTER, width=120)
        self.room_detail.column("Father Name", anchor=tk.CENTER, width=120)
        self.room_detail.column("Address", anchor=tk.CENTER, width=120)
        self.room_detail.column("DOB", anchor=tk.CENTER, width=120)
        self.room_detail.column("Age", anchor=tk.CENTER, width=120)
        self.room_detail.column("Contact No", anchor=tk.CENTER, width=120)
        self.room_detail.column("Room No", anchor=tk.CENTER, width=120)
        self.room_detail.column("Room Fee", anchor=tk.CENTER, width=120)

        self.room_detail.pack(fill = BOTH, expand=1)
    def open(self):
        import AddNewRoom

    def remove(self):
        connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password='1234',
                                             port='3306',
                                             database='hostel')
        my_connection = connection.cursor()
        selected_item = self.room_detail.selection()
        if selected_item:
            record_id = self.room_detail.item(selected_item)['values'][0]
            query = "DELETE FROM Allocation WHERE id=%s"
            my_connection(query, (record_id,))
            # refresh_data()
        else:
            messagebox.showinfo("Please", "select a record to delete")

    def add_room(self):

        id = self.id_value.get()
        name = self.name.get()
        fname = self.fname.get()
        address = self.addres.get()
        DOB = self.DOB.get()
        age = self.age.get()
        contact = self.contact.get()
        roomn = self.roomn.get()
        fee = self.fee.get()

        connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password='1234',
                                             port='3306',
                                             database='hostel')
        my_connection = connection.cursor()

        if roomn == "" or age == ""or contact == "" or name == "" or fname == "" or fee == "" or address == "" or DOB == "" or id == "":
            messagebox.showerror("Error", "Please fill in all fields")
        else:
            insert_query = "INSERT INTO Allocation (ID,Name, FName,Address,DOB,Age,Contact,RoomNo,Fee) VALUES (%s, %s,%s,%s, %s,%s,%s, %s,%s)"
            data = (id, name,fname,address, DOB, age, contact, roomn, fee )

            my_connection.execute(insert_query, data)

            connection.commit()
            messagebox.showinfo("Congrats", "Room Allocated")

            # Close the cursor and connection
            my_connection.close()
            connection.close()


if __name__ == "__main__":
    root=Tk()
    obj= Room(root)
    root.mainloop()