from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import mysql.connector


class Fee:
    def __init__(self, root):

        self.root = root
        self.root.title("Fee Management")
        self.root.geometry("1230x615+250+82")
        self.root.resizable(False, False)
        self.root["bg"] = "cadet blue"

        # ================Heading label======================
        label = Label(self.root, text="Manage Fee", bg="Black", fg="gold",
                      font=("Time New Romen", 20, "bold")).pack(fill=X)

        # ==================creating labels and entry fields==========

        label2 = Label(self.root, text="Record Fee", font=("Time New Romen", 16, "bold"), bg="#2F4F4F",
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

        self.Month_value = StringVar()
        label_Month = Label(self.root, text="Date of Birth", font=("Time New Romen", 12, "bold"), bg="cadet blue",
                          fg="white").place(x=20, y=320)
        Month_entry = Entry(self.root, width=30, textvariable=self.Month_value).place(x=160, y=325)

        self.Discount_value = StringVar()
        label_Discount = Label(self.root, text="Discount", font=("Time New Romen", 12, "bold"), bg="cadet blue",
                          fg="white").place(x=20, y=370)
        Discount_entry = Entry(self.root, width=30, textvariable=self.Discount_value).place(x=160, y=375)

        self.Fee_value = StringVar()
        label_contact = Label(self.root, text="Fee Amount", font=("Time New Romen", 12, "bold"), bg="cadet blue",
                              fg="white").place(x=20, y=420)
        contact_entry = Entry(self.root, width=30, textvariable=self.Fee_value).place(x=160, y=425)

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
            "StdID", "Name", "Father Name", "Contact", "Month", "Discount", "Fee"),
                                      xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.config(command=self.st_detail.xview)
        scroll_y.config(command=self.st_detail.yview)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.st_detail.heading("StdID", text="ID")
        self.st_detail.heading("Name", text="Name")
        self.st_detail.heading("Father Name", text="Father Name")
        self.st_detail.heading("Contact", text="Contact")
        self.st_detail.heading("Month", text="Month")
        self.st_detail.heading("Discount", text="Discount")
        self.st_detail.heading("Fee", text="Fee")

        self.st_detail["show"] = "headings"

        self.st_detail.column("StdID", anchor=tk.CENTER, width=120)
        self.st_detail.column("Name", anchor=tk.CENTER, width=120)
        self.st_detail.column("Father Name", anchor=tk.CENTER, width=120)
        self.st_detail.column("Contact", anchor=tk.CENTER, width=120)
        self.st_detail.column("Month", anchor=tk.CENTER, width=120)
        self.st_detail.column("Discount", anchor=tk.CENTER, width=120)
        self.st_detail.column("Fee", anchor=tk.CENTER, width=120)

        self.st_detail.pack(fill=tk.BOTH, expand=1)
        self.view_command()

    def add(self):
        ID = self.id_value.get()
        Name = self.name_value.get()
        FName = self.fname_value.get()
        Contact = self.Contact_value.get()
        Month = self.Month_value.get()
        Discount = self.Discount_value.get()
        Fee = self.Fee_value.get()

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hostel"
        )
        cursor = conn.cursor()
        query = "INSERT INTO Fee (ID, Name, FName, Contact, Month, Discount, Fee) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (ID, Name, FName, Contact, Month, Discount, Fee)
        cursor.execute(query, values)
        messagebox.showinfo("Success", "Fee Record successful")
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
        query = "SELECT * FROM Fee"
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
        FName = self.fname_value.get()
        Contact = self.Contact_value.get()
        Month = self.Month_value.get()
        Discount = self.Discount_value.get()
        Contact = self.Contact_value.get()

        # Execute MySQL query for searching data
        query = "SELECT * FROM Fee WHERE ID = %s OR Name = %s OR FName = %s OR Contact = %s OR Month = %s OR Discount = %s OR Fee = %s"
        values = (ID, Name, FName, Contact, Month, Discount, Fee)
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
        query = "DELETE FROM Fee WHERE ID = %s"
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
        self.Contact_value.set(selected_values[3])
        self.Month_value.set(selected_values[4])
        self.Discount_value.set(selected_values[5])
        self.Fee_value.set(selected_values[6])


        # Update the record in the database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hostel"
        )
        cursor = conn.cursor()

        # Execute MySQL query for updating data
        query = "UPDATE Fee SET Name = %s, FName = %s, Contact = %s, Month = %s, Discount = %s, Fee = %s WHERE ID = %s"
        values = (self.name_value.get(), self.fname_value.get(), self.Contact_value.get(),
                  self.Month_value.get(), self.Discount_value.get(), self.Contact_value.get(), self.id_value.get())

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
        self.Contact_value.set("")
        self.Month_value.set("")
        self.Discount_value.set("")
        self.Fee_value.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Fee(root)
    root.mainloop()


