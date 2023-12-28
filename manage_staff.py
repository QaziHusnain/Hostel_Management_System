from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import mysql.connector


class Staff:
    def __init__(self, root):

        self.root = root
        self.root.title("Manage Staff")
        self.root.geometry("1230x615+250+82")
        self.root.resizable(False, False)
        self.root["bg"] = "cadet blue"

        # ================Heading label======================
        label = Label(self.root, text="Manage Staff", bg="Black", fg="gold",
                      font=("Time New Romen", 20, "bold")).pack(fill=X)

        # ==================creating labels and entry fields==========

        label2 = Label(self.root, text="Register Staff", font=("Time New Romen", 16, "bold"), bg="#2F4F4F",
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

        self.address_value = StringVar()
        label_address = Label(self.root, text="Address", font=("Time New Romen", 12, "bold"), bg="cadet blue",
                              fg="white").place(x=20, y=270)
        address_entry = Entry(self.root, width=30, textvariable=self.address_value).place(x=160, y=275)

        self.dob_value = StringVar()
        label_dob = Label(self.root, text="Date of Birth", font=("Time New Romen", 12, "bold"), bg="cadet blue",
                          fg="white").place(x=20, y=320)
        dob_entry = Entry(self.root, width=30, textvariable=self.dob_value).place(x=160, y=325)

        self.age_value = StringVar()
        label_age = Label(self.root, text="Age", font=("Time New Romen", 12, "bold"), bg="cadet blue",
                          fg="white").place(x=20, y=370)
        age_entry = Entry(self.root, width=30, textvariable=self.age_value).place(x=160, y=375)

        self.Contact_value = StringVar()
        label_contact = Label(self.root, text="Contact Number", font=("Time New Romen", 12, "bold"), bg="cadet blue",
                              fg="white").place(x=20, y=420)
        contact_entry = Entry(self.root, width=30, textvariable=self.Contact_value).place(x=160, y=425)

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

        home_button = Button(self.root, text="search", bg="black", fg="gold", bd=2, width=12,
                             font=("time new romens", 14, "bold"))
        home_button.place(x=190, y=520)

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
            "StdID", "Name", "Father Name", "Address", "DOB", "Age", "Contact No"),
                                      xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.config(command=self.st_detail.xview)
        scroll_y.config(command=self.st_detail.yview)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.st_detail.heading("StdID", text="ID")
        self.st_detail.heading("Name", text="Name")
        self.st_detail.heading("Father Name", text="Father Name")
        self.st_detail.heading("Address", text="Address")
        self.st_detail.heading("DOB", text="DOB")
        self.st_detail.heading("Age", text="Age")
        self.st_detail.heading("Contact No", text="Contact No")

        self.st_detail["show"] = "headings"

        self.st_detail.column("StdID", anchor=tk.CENTER, width=120)
        self.st_detail.column("Name", anchor=tk.CENTER, width=120)
        self.st_detail.column("Father Name", anchor=tk.CENTER, width=120)
        self.st_detail.column("Address", anchor=tk.CENTER, width=120)
        self.st_detail.column("DOB", anchor=tk.CENTER, width=120)
        self.st_detail.column("Age", anchor=tk.CENTER, width=120)
        self.st_detail.column("Contact No", anchor=tk.CENTER, width=120)

        self.st_detail.pack(fill=tk.BOTH, expand=1)
        self.view_command()

    def add(self):
        ID = self.id_value.get()
        Name = self.name_value.get()
        Father = self.fname_value.get()
        Address = self.address_value.get()
        DOB = self.dob_value.get()
        Age = self.age_value.get()
        Contact = self.Contact_value.get()

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hostel"
        )
        cursor = conn.cursor()
        query = "INSERT INTO Staff (ID, Name, Father, Address, DOB, Age, Contact) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (ID, Name, Father, Address, DOB, Age, Contact)
        cursor.execute(query, values)
        messagebox.showinfo("Success", "Staff registered successful")
        self.view_command()
        # Commit and close
        conn.commit()
        conn.close()

    def view_command(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hostel"
        )
        cursor = conn.cursor()
        query = "SELECT * FROM Staff"
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
        Father = self.fname_value.get()
        Address = self.address_value.get()
        DOB = self.dob_value.get()
        Age = self.age_value.get()
        Contact = self.Contact_value.get()

        # Execute MySQL query for searching data
        query = "SELECT * FROM Staff WHERE ID = %s OR Name = %s OR Father = %s OR Address = %s OR DOB = %s OR Age = %s OR Contact = %s"
        values = (ID, Name, Father, Address, DOB, Age, Contact)
        cursor.execute(query, values)

        # Fetch all records
        rows = cursor.fetchall()

        # Clear existing data in the treeview
        self.st_detail.delete(*self.st_detail.get_children())

        # Insert new data into the treeview
        for row in rows:
            self.st_detail.insert("", tk.END, values=row)

        # Close the connection
        conn.close()

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
        query = "DELETE FROM Staff WHERE ID = %s"
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
            messagebox.showinfo("Update", "Please select a record to update.")
            return

        # Retrieve the values of the selected item
        selected_values = self.st_detail.item(selected_item, "values")

        # Populate entry fields with selected values
        self.id_value.set(selected_values[0])
        self.name_value.set(selected_values[1])
        self.fname_value.set(selected_values[2])
        self.address_value.set(selected_values[3])
        self.dob_value.set(selected_values[4])
        self.age_value.set(selected_values[5])
        self.Contact_value.set(selected_values[6])
        ID = self.id_value.get()
        Name = self.name_value.get()
        Father = self.fname_value.get()
        Address = self.address_value.get()
        DOB = self.dob_value.get()
        Age = self.age_value.get()
        Contact = self.Contact_value.get()

        # Update the record in the database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hostel"
        )
        cursor = conn.cursor()

        # Execute MySQL query for updating data
        query = "UPDATE Staff SET Name = %s, Father = %s, Address = %s, DOB = %s, Age = %s, Contact = %s WHERE ID = %s"
        values = (self.name_value.get(), self.fname_value.get(), self.address_value.get(),
                  self.dob_value.get(), self.age_value.get(), self.Contact_value.get(), self.id_value.get())

        cursor.execute(query, values)
        messagebox.showinfo("Congrats", "Record Updated.")
        # Commit and close
        conn.commit()
        conn.close()

        # Refresh the treeview after updating
        self.view_command()

        # Clear the entry fields after updating
        self.clear_entry_fields()

    def clear_entry_fields(self):
        # Clear entry fields
        self.id_value.set("")
        self.name_value.set("")
        self.fname_value.set("")
        self.address_value.set("")
        self.dob_value.set("")
        self.age_value.set("")
        self.Contact_value.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Staff(root)
    root.mainloop()


