from datetime import datetime
from tkinter import *
from tkinter import Tk
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from AddNewRoom import Fee


class Room:
    def __init__ (self,root):

        self.root= root

        self.root.title("Manage Room")
        self.root.geometry("1600x700+200+50")
        self.root.resizable(False,False)
        self.root["bg"] = "cadet blue"



        toplabel=Label(self.root, text="Manage Room",font=("Time New Romen",22,"bold"), bg="black",fg="gold").pack(fill=X)

        #frame2=Frame (self.root,width=350,height=655,bg="cadet blue",bd=4, relief=RIDGE ).place(x=0,y=38)

        #label2= Label(frame2, text= "Register Staff", font=("Time New Romen",16,"bold"),bg="#2F4F4F", fg="white").place(x=110,y= 60)
        id_value = IntVar()
        self.id_value = id_value  # Define as instance variable
        label_id = Label(self.root, text="ID", font=("Time New Romen", 12, "bold"), bg="cadet blue", fg="white").place(x=20, y=50)
        id_entry = Entry(self.root, width=30, textvariable=id_value).place(x=160, y=55)

        name = StringVar()
        self.name = name
        label_name = Label(self.root, text="Name", font=("Time New Romen", 12, "bold"), bg="cadet blue", fg="white").place(x=20, y=100)
        name_entry = Entry(self.root, width=30, textvariable=name).place(x=160, y=105)

        fname = StringVar()
        self.fname = fname  # Change this line
        label_fname = Label(self.root, text="Father Name", font=("Time New Romen", 12, "bold"), bg="cadet blue",fg="white").place(x=20, y=150)
        fname_entry = Entry(self.root, width=30, textvariable=fname).place(x=160, y=155)
        addres = StringVar()
        self.addres=addres
        label_address = Label(self.root, text="Address", font=("Time New Romen", 12, "bold"), bg="cadet blue",fg="white").place(x=20, y=200)
        address_entry = Entry(self.root, width=30, textvariable=addres).place(x=160, y=205)
        DOB= StringVar()
        self.DOB=DOB
        label_dob = Label(self.root, text="Date of Birth", font=("Time New Romen", 12, "bold"), bg="cadet blue",fg="white").place(x=20, y=250)
        dob_entry = Entry(self.root, width=30, textvariable=DOB).place(x=160, y=255)
        age = StringVar()
        self.age=age
        label_age = Label(self.root, text="Age", font=("Time New Romen", 12, "bold"), bg="cadet blue", fg="white").place(x=20,y=300)
        age_entry = Entry(self.root, width=30, textvariable=age).place(x=160, y=305)
        contact = StringVar()
        self.contact=contact
        label_contact = Label(self.root, text="Contact Number", font=("Time New Romen", 12, "bold"), bg="cadet blue",fg="white").place(x=20, y=350)
        contact_entry = Entry(self.root, width=30, textvariable=contact).place(x=160, y=355)
        roomn = StringVar()
        self.roomn=roomn
        label_room_no = Label(self.root, text="Room No", font=("Time New Romen", 12, "bold"), bg="cadet blue",fg="white").place(x=20, y=400)
        room_no_entry = Entry(self.root, width=30, textvariable=roomn).place(x=160, y=405)
        fee = StringVar()
        self.fee=fee
        label_room_fee = Label(self.root, text="Room Fee", font=("Time New Romen", 12, "bold"), bg="cadet blue",fg="white").place(x=20, y=455)
        room_fee_entry = Entry(self.root, width=30, textvariable=fee).place(x=160, y=455)


         #=========== frame for separation ==========
        sep_frame = Frame(self.root, bd=5, width=4, height=500, bg="black")
        sep_frame.place(x=360, y=60)


#===========Button Frame and Buttons=================
        #btn_frame=Frame (self.root,width=750,height=207,bg="cadet blue",bd=4, relief=RIDGE ).place(x=350,y=38)

        btn1 = Button(self.root, text="Allocate Room",command=self.add_room, bg="black", fg="gold", bd=2, width=14,
                            font=("time new romens", 14, "bold"))
        btn1.place(x=400, y=48)

        btn1 = Button(self.root, text="Remove Allocation", command=self.remove, bg="black", fg="gold", bd=2, width=16,
                            font=("time new romens", 14, "bold"))
        btn1.place(x=635, y=48)

        btn1 = Button(self.root, text="Add New Room", command =self.open, bg="black", fg="gold", bd=2, width=14,
                            font=("time new romens", 14, "bold"))
        btn1.place(x=870, y=48)
        btn_insert_student = Button(self.root, text="Insert Student", command=self.insert_student, bg="black",
                                    fg="gold", bd=2, width=14, font=("time new romens", 14, "bold"))
        btn_insert_student.place(x=1100, y=48)
        btn_clear = Button(self.root, text="Clear Entry", command=self.clear_entry, bg="black", fg="gold", bd=2,
                           width=14, font=("time new romens", 14, "bold"))
        btn_clear.place(x=100, y=510)


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
        cursor = conn.cursor()

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
        self.fetch_data()
    def open(self):

        addroom_window = Toplevel(self.root)
        room_obj = Fee(addroom_window)

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
            print(f"Deleting record with ID: {record_id}")

            # Retrieve RoomNo before deleting the record
            query_select_roomno = "SELECT RoomNo FROM Allocation WHERE id=%s"
            my_connection.execute(query_select_roomno, (record_id,))
            room_no = my_connection.fetchone()

            query_delete = "DELETE FROM Allocation WHERE id=%s"
            my_connection.execute(query_delete, (record_id,))
            connection.commit()

            if room_no:
                # Update the occupancy in the Rooms table
                query_update_occupancy = "UPDATE Rooms SET Occupancy = Occupancy - 1 WHERE RoomNo = %s"
                my_connection.execute(query_update_occupancy, room_no)
                connection.commit()

                # Check if occupancy becomes less than capacity
                query_room_info = "SELECT Capacity, Occupancy FROM Rooms WHERE RoomNo = %s"
                my_connection.execute(query_room_info, room_no)
                room_info = my_connection.fetchone()

                if room_info:
                    capacity, occupancy = room_info

                    if occupancy < capacity:
                        # Update status to "Active" in the Rooms table
                        update_status_query = "UPDATE Rooms SET Status = 'Active' WHERE RoomNo = %s"
                        my_connection.execute(update_status_query, room_no)
                        connection.commit()

            self.fetch_data()
        else:
            messagebox.showinfo("Please", "select a record to delete")

        # Close the cursor and connection
        my_connection.close()
        connection.close()

    def add_room(self):
        id = self.id_value.get()
        name = self.name.get()
        fname = self.fname.get()
        address = self.addres.get()
        try:
            DOB = datetime.strptime(self.DOB.get(), "%Y-%m-%d").date()
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")
            return
        age = self.age.get()
        contact = self.contact.get()
        roomn = self.roomn.get()
        fee = self.fee.get()

        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            port='3306',
            database='hostel'
        )
        my_connection = connection.cursor()

        if roomn == "" or age == "" or contact == "" or name == "" or fname == "" or fee == "" or address == "" or DOB == "" or id == "":
            messagebox.showerror("Error", "Please fill in all fields")
        else:
            # Check if the room is available (occupancy is less than capacity)
            query_room_info = "SELECT Capacity, Occupancy FROM Rooms WHERE RoomNo = %s"
            my_connection.execute(query_room_info, (roomn,))
            room_info = my_connection.fetchone()

            if room_info:
                capacity, occupancy = room_info

                if occupancy < capacity:
                    # Update the Allocation table
                    insert_query = "INSERT INTO Allocation (ID, Name, FName, Address, DOB, Age, Contact, RoomNo, Fee) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    data = (id, name, fname, address, DOB, age, contact, roomn, fee)
                    my_connection.execute(insert_query, data)
                    connection.commit()

                    # Update the occupancy in the Rooms table
                    update_query = "UPDATE Rooms SET Occupancy = Occupancy + 1 WHERE RoomNo = %s"
                    my_connection.execute(update_query, (roomn,))
                    connection.commit()

                    # Check if occupancy will become equal to capacity
                    if occupancy + 1 == capacity:
                        # Update status to "Deactive" in the Rooms table
                        update_status_query = "UPDATE Rooms SET Status = 'Deactive' WHERE RoomNo = %s"
                        my_connection.execute(update_status_query, (roomn,))
                        connection.commit()

                    messagebox.showinfo("Congrats", "Room Allocated")
                else:
                    messagebox.showerror("Error", "Room is already occupied. Please choose another room.")
            else:
                messagebox.showerror("Error", "Invalid room number.")

            # Close the cursor and connection
            my_connection.close()
            connection.close()

            # Fetch updated data
            self.fetch_data()
            self.clear_entry()
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hostel"
        )
        cursor = conn.cursor()
        query = "SELECT * FROM Allocation"
        cursor.execute(query)

        # Fetch all records
        rows = cursor.fetchall()

        # Clear existing data in the treeview
        for item in self.room_detail.get_children():
            self.room_detail.delete(item)

        # Insert new data into the treeview
        for row in rows:
            self.room_detail.insert("", tk.END, values=row)

        # Close the connection
        conn.close()

    def insert_student(self):
        # Create a new window to display student information
        student_window = Toplevel(self.root)
        student_window.title("Insert Student")
        student_window.geometry("900x500")

        # Create a Treeview to display student information
        student_tree = ttk.Treeview(student_window, columns=(
            "StdID", "Name", "Father Name", "Contact", "Address", "Class", "Fee"),
                                    show="headings")

        scroll_x = Scrollbar(student_tree, orient=HORIZONTAL)
        scroll_y = Scrollbar(student_tree, orient=VERTICAL)

        student_tree.bind("<<TreeviewSelect>>",
                          lambda event: self.on_student_select(event, student_tree, student_window))

        scroll_x.config(command=student_tree.xview)
        scroll_y.config(command=student_tree.yview)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        student_tree.heading("StdID", text="ID")
        student_tree.heading("Name", text="Name")
        student_tree.heading("Father Name", text="Father Name")
        student_tree.heading("Contact", text="Contact")
        student_tree.heading("Address", text="Address")
        student_tree.heading("Class", text="Class")
        student_tree.heading("Fee", text="Fee")

        student_tree["show"] = "headings"

        student_tree.column("StdID", anchor=tk.CENTER, width=120)
        student_tree.column("Name", anchor=tk.CENTER, width=120)
        student_tree.column("Father Name", anchor=tk.CENTER, width=120)
        student_tree.column("Contact", anchor=tk.CENTER, width=120)
        student_tree.column("Address", anchor=tk.CENTER, width=120)
        student_tree.column("Class", anchor=tk.CENTER, width=120)
        student_tree.column("Fee", anchor=tk.CENTER, width=120)

        student_tree.pack(fill=tk.BOTH, expand=1)

        # Fetch data from the Student table and insert into the Treeview
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hostel"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT ID, Name, FName, Contact, Address, Class, Fee FROM Student")
        students = cursor.fetchall()
        for student in students:
            student_tree.insert("", "end", values=student)

    def on_student_select(self, event, treeview, window):
        # Get the selected student's information
        selected_item = treeview.selection()
        if selected_item:
            student_info = treeview.item(selected_item, "values")

            # Populate the entry fields in the Manage Room window
            self.id_value.set(student_info[0])
            self.name.set(student_info[1])
            self.fname.set(student_info[2])
            self.contact.set(student_info[3])
            self.addres.set(student_info[4])


            # Close the student window
            window.destroy()

    def clear_entry(self):
        # Clear all entry fields
        self.id_value.set("")
        self.name.set("")
        self.fname.set("")
        self.addres.set("")
        self.DOB.set("")
        self.age.set("")
        self.contact.set("")
        self.roomn.set("")
        self.fee.set("")


if __name__ == "__main__":
    root=Tk()
    obj= Room(root)
    root.mainloop()