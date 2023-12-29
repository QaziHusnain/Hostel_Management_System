from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import mysql.connector


class Student:
    def __init__(self, root):

        self.root = root
        self.root.title("Student Management")
        self.root.geometry("1230x615+250+82")
        self.root.resizable(False, False)
        self.root["bg"] = "cadet blue"

        # ================Heading label======================
        label = Label(self.root, text="Manage Student", bg="Black", fg="gold",
                      font=("Time New Romen", 20, "bold")).pack(fill=X)

        # ==================creating labels and entry fields==========

        label2 = Label(self.root, text="Record Student", font=("Time New Romen", 16, "bold"), bg="#2F4F4F",
                       fg="white").place(x=110, y=60)

        self.id_value = IntVar()
        label_id = Label(self.root, text="ID", font=("Time New Romen", 12, "bold"), bg="cadet blue", fg="white").place(
            x=20, y=120)
        id_entry = Entry(self.root, width=30, textvariable=self.id_value).place(x=160, y=125)

        self.name_value = StringVar()
        label_name = Label(self.root, text="Name", font=("Time New Romen", 12, "bold"), bg="cadet blue",
                           fg="white").place(x=20, y=170)
        name_entry = Entry(self.root, width=30, textvariable=self.name_value).place(x=160, y=175)

        self.fname_value = StringVar()
        label_fname = Label(self.root, text="Father Name", font=("Time New Romen", 12, "bold"), bg="cadet blue",
                            fg="white").place(x=20, y=220)
        fname_entry = Entry(self.root, width=30, textvariable=self.fname_value).place(x=160, y=225)

        self.Contact_value = StringVar()
        label_Contact = Label(self.root, text="Contact", font=("Time New Romen", 12, "bold"), bg="cadet blue",
                              fg="white").place(x=20, y=270)
        Contact_entry = Entry(self.root, width=30, textvariable=self.Contact_value).place(x=160, y=275)

        self.Address_value = StringVar()
        label_Address = Label(self.root, text="Address", font=("Time New Romen", 12, "bold"), bg="cadet blue",
                          fg="white").place(x=20, y=320)
        Address_entry = Entry(self.root, width=30, textvariable=self.Address_value).place(x=160, y=325)

        self.Class_value = StringVar()
        label_Class = Label(self.root, text="Class", font=("Time New Romen", 12, "bold"), bg="cadet blue",
                          fg="white").place(x=20, y=370)
        Class_entry = Entry(self.root, width=30, textvariable=self.Class_value).place(x=160, y=375)

        self.Student_value = StringVar()
        label_contact = Label(self.root, text="Fee Amount", font=("Time New Romen", 12, "bold"), bg="cadet blue",
                              fg="white").place(x=20, y=420)
        contact_entry = Entry(self.root, width=30, textvariable=self.Student_value).place(x=160, y=425)

        # ===================creating buttons=====================

        add_button = Button(self.root, text="Add", bg="black", command=self.add, fg="gold", bd=2, width=12,
                            font=("time new romens", 14, "bold"))
        add_button.place(x=20, y=470)

        del_button = Button(self.root, text="Delete", command=self.delete_command, bg="black", fg="gold", bd=2, width=12,
                            font=("time new romens", 14, "bold"))
        del_button.place(x=190, y=470)

        update_button = Button(self.root, text="Update", bg="black", command=self.update_command, fg="gold", bd=2, width=12,
                               font=("time new romens", 14, "bold"))
        update_button.place(x=20, y=520)

        home_button = Button(self.root, text="Search", bg="black", fg="gold", bd=2, width=12,
                             font=("time new romens", 14, "bold"), command=self.search_command)
        home_button.place(x=190, y=520)

        Reset_button = Button(self.root, text="Reset", bg="black", fg="gold", bd=2, width=12,
                             font=("time new romens", 14, "bold"), command=self.reset_command)
        Reset_button.place(x=100, y=570)

        # =========== frame for separation ==========
        sep_frame = Frame(self.root, bd=5, width=4, height=500, bg="black")
        sep_frame.place(x=360, y=60)

        # =============================frame for tree==========================
        Tree_frame = Frame(self.root, bd=5, width=700, height=450, bg="cadet blue", relief=RIDGE)
        Tree_frame.place(x=380, y=60)

        scroll_x = Scrollbar(Tree_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Tree_frame, orient=VERTICAL)
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hostel"
        )
        cursor = conn.cursor()

        self.st_detail = ttk.Treeview(Tree_frame, height=15, columns=(
            "StdID", "Name", "Father Name", "Contact", "Address", "Class", "Fee"),
                                      xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        # Add the binding for TreeviewSelect event
        self.st_detail.bind("<<TreeviewSelect>>", self.on_treeview_select)



        scroll_x.config(command=self.st_detail.xview)
        scroll_y.config(command=self.st_detail.yview)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.st_detail.heading("StdID", text="ID")
        self.st_detail.heading("Name", text="Name")
        self.st_detail.heading("Father Name", text="Father Name")
        self.st_detail.heading("Contact", text="Contact")
        self.st_detail.heading("Address", text="Address")
        self.st_detail.heading("Class", text="Class")
        self.st_detail.heading("Fee", text="Fee")

        self.st_detail["show"] = "headings"

        self.st_detail.column("StdID", anchor=tk.CENTER, width=120)
        self.st_detail.column("Name", anchor=tk.CENTER, width=120)
        self.st_detail.column("Father Name", anchor=tk.CENTER, width=120)
        self.st_detail.column("Contact", anchor=tk.CENTER, width=120)
        self.st_detail.column("Address", anchor=tk.CENTER, width=120)
        self.st_detail.column("Class", anchor=tk.CENTER, width=120)
        self.st_detail.column("Fee", anchor=tk.CENTER, width=120)

        self.st_detail.pack(fill=tk.BOTH, expand=1)
        self.view_command()

    def add(self):
        ID = self.id_value.get()
        Name = self.name_value.get()
        FName = self.fname_value.get()
        Contact = self.Contact_value.get()
        Address = self.Address_value.get()
        Class = self.Class_value.get()
        Student = self.Student_value.get()

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hostel"
        )
        cursor = conn.cursor()
        query = "INSERT INTO Student (ID, Name, FName, Contact, Address, Class, Fee) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (ID, Name, FName, Contact, Address, Class, Student)
        cursor.execute(query, values)
        messagebox.showinfo("Success", "Student Record successful")

        # Commit and close
        conn.commit()
        conn.close()

        self.view_command()
        self.clear_entry_fields()


    def view_command(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hostel"
        )
        cursor = conn.cursor()
        query = "SELECT * FROM Student"
        cursor.execute(query)

        # Fetch all records
        rows = cursor.fetchall()

        # Clear existing data in the treeview
        for item in self.st_detail.get_children():
            self.st_detail.delete(item)

        # Insert new data into the treeview
        for row in rows:
            self.st_detail.insert("", tk.END, values=row)

            # Close the connection
        conn.close()
        self.clear_entry_fields()

    def search_command(self):
        # Connect to MySQL
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hostel"
        )
        cursor = conn.cursor()

        # Get values from entry fields
        ID = self.id_value.get()
        Name = self.name_value.get()
        FName = self.fname_value.get()
        Contact = self.Contact_value.get()
        Address = self.Address_value.get()
        Class = self.Class_value.get()
        Student = self.Student_value.get()

        # Check if any search criteria is provided
        if any((ID, Name, FName, Contact, Address, Class, Student)):
            # Execute MySQL query for searching data
            query = "SELECT * FROM Student WHERE ID = %s OR Name = %s OR FName = %s OR Contact = %s OR Address = %s OR Class = %s OR Fee = %s"
            values = (ID, Name, FName, Contact, Address, Class, Student)
            cursor.execute(query, values)
        else:
            # Fetch all records if no search criteria is provided
            query = "SELECT * FROM Student"
            cursor.execute(query)

        # Fetch all records
        rows = cursor.fetchall()

        # Clear existing data in the treeview
        self.st_detail.delete(*self.st_detail.get_children())

        # Insert new data into the treeview
        for row in rows:
            self.st_detail.insert("", tk.END, values=row)

        # Close the connection
        conn.close()
        self.clear_entry_fields()

    def delete_command(self):
        # Get the selected item from the treeview
        selected_item = self.st_detail.selection()

        if not selected_item:
            return  # No item selected, do nothing

        # Connect to MySQL
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hostel"
        )
        cursor = conn.cursor()

        # Get the ID of the selected item
        selected_id = self.st_detail.item(selected_item, "values")[0]

        # Execute MySQL query for deleting data
        query = "DELETE FROM Student WHERE ID = %s"
        values = (selected_id,)
        cursor.execute(query, values)

        # Commit and close
        conn.commit()
        conn.close()

        # Refresh the treeview after deletion
        self.view_command()

    def update_command(self):
        # Get the selected item from the treeview
        selected_item = self.st_detail.selection()

        if not selected_item:
            messagebox.showwarning("Warning", "Please select a record to update.")
            return  # No item selected, do nothing

        # Get the ID of the selected item
        selected_id = self.st_detail.item(selected_item, "values")[0]

        # Update the record in the database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hostel"
        )
        cursor = conn.cursor()

        # Prepare and print the values before executing the query
        query = "UPDATE Student SET Name=%s, FName=%s, Contact=%s, Address=%s, Class=%s, Fee=%s WHERE ID=%s"
        values = (
            self.name_value.get(),
            self.fname_value.get(),
            self.Contact_value.get(),
            self.Address_value.get(),
            self.Class_value.get(),
            self.Student_value.get(),
            selected_id  # Use the ID of the selected item for the WHERE clause
        )

        cursor.execute(query, values)
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Record updated successfully.")

        # Clear entry fields and refresh the treeview
        self.view_command()
        self.clear_entry_fields()


    def on_treeview_select(self, event):
        # Get the selected item from the Treeview
        selected_item = self.st_detail.selection()

        if selected_item:
            # Get the values of the selected item
            selected_values = self.st_detail.item(selected_item, "values")

            # Update the entry fields with the selected values
            self.id_value.set(selected_values[0])
            self.name_value.set(selected_values[1])
            self.fname_value.set(selected_values[2])
            self.Contact_value.set(selected_values[3])
            self.Address_value.set(selected_values[4])
            self.Class_value.set(selected_values[5])
            self.Student_value.set(selected_values[6])

    def clear_entry_fields(self):
        self.id_value.set("0")
        self.name_value.set("")
        self.fname_value.set("")
        self.Contact_value.set("")
        self.Address_value.set("")
        self.Class_value.set("")
        self.Student_value.set("")
    def reset_command(self):

        self.view_command()
        self.clear_entry_fields()
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()


