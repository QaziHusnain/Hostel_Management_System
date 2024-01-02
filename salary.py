from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import mysql.connector


class Salary:
    def __init__(self, root):

        self.root = root
        self.root.title("Manage Staff Salary")
        self.root.geometry("1400x480+250+215")
        self.root.resizable(False, False)

        self.id_value = IntVar()
        self.name_value = StringVar()
        self.fname_value = StringVar()
        self.contact_value = StringVar()
        self.month_value = StringVar()
        self.discount_value = StringVar()
        self.fee_value = StringVar()

        # =======top label for Heading=======
        toplabel = Label(self.root, text="Manage Staff Salary", font=("Time New Romen", 14, "bold"), bg="black",
                         fg="gold").pack(fill=X)

        # =======labels and entries fields ========
        id_label = Label(self.root, text="ID :", font=("Time New Romen", 12, "bold"), fg="black").place(x=20, y=60)
        id_entry = Entry(self.root, width=15, textvariable=self.id_value).place(x=140, y=60)

        name_label = Label(self.root, text="Name", font=("Time New Romen", 12, "bold"), fg="black").place(x=20, y=100)
        name_entry = Entry(self.root, width=30, textvariable=self.name_value).place(x=140, y=100)

        fname_label = Label(self.root, text="Father Name", font=("Time New Romen", 12, "bold"), fg="black").place(x=20,
                                                                                                                  y=140)
        fname_entry = Entry(self.root, width=30, textvariable=self.fname_value).place(x=140, y=140)

        contact_Name = Label(self.root, text="Contact No", font=("Time New Romen", 12, "bold"), fg="black").place(x=20,
                                                                                                                  y=180)
        contact_entry = Entry(self.root, width=30, textvariable=self.contact_value).place(x=140, y=180)

        month_label = Label(self.root, text="Month", font=("Time New Romen", 12, "bold"), fg="black").place(x=20, y=220)
        month_entry = Entry(self.root, width=30, textvariable=self.month_value).place(x=140, y=220)

        discount_label = Label(self.root, text="Discount", font=("Time New Romen", 12, "bold"), fg="black").place(x=20,
                                                                                                                  y=260)
        discount_entry = Entry(self.root, width=30, textvariable=self.discount_value).place(x=140, y=260)

        fee_label = Label(self.root, text="Fee Amount", font=("Time New Romen", 12, "bold"), fg="black").place(x=20,
                                                                                                               y=300)
        fee_entry = Entry(self.root, width=30, textvariable=self.fee_value).place(x=140, y=300)

        # ========search, save, and clear buttons=============
        search_btn = Button(self.root, text="Search", font=("Time New Romen", 12, "bold"), bg="black", fg="gold").place(
            x=255, y=60)

        save_btn = Button(self.root, text="Save", command=self.add, font=("Time New Romen", 12, "bold"), bg="black",
                          fg="gold", width=12).place(x=20, y=360)

        clear_btn = Button(self.root, text="Clear", font=("Time New Romen", 12, "bold"), bg="black", fg="gold",
                           width=12).place(x=200, y=360)

        # Insert Staff Member button
        insert_staff_btn = Button(self.root, text="Insert Staff", command=self.open_staff_window,
                                  font=("Time New Romen", 12, "bold"), bg="black", fg="gold", width=12)
        insert_staff_btn.place(x=20, y=410)

        # ========= frame for saparation =========
        frame = Frame(self.root, width=4, height=435, bg="cadet blue").place(x=400, y=30)

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hostel"
        )
        cursor = conn.cursor()

        self.tree = ttk.Treeview(self.root, height=18,
                                 columns=("ID", "Name", "FName", "Contact","Month", "Discount", "Fee Amount"))

        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("FName", text="FName")
        self.tree.heading("Contact", text="Contact")
        self.tree.heading("Month", text="Month")
        self.tree.heading("Discount", text="Discount")
        self.tree.heading("Fee Amount", text="Fee Amount")

        self.tree["show"] = "headings"

        self.tree.column("ID", anchor=tk.CENTER, width=120)
        self.tree.column("Name", anchor=tk.CENTER, width=120)
        self.tree.column("FName", anchor=tk.CENTER, width=120)
        self.tree.column("Contact", anchor=tk.CENTER, width=120)
        self.tree.column("Month", anchor=tk.CENTER, width=120)
        self.tree.column("Discount", anchor=tk.CENTER, width=120)
        self.tree.column("Fee Amount", anchor=tk.CENTER, width=120)

        self.tree.place(x=450, y=50)

    def add(self):
        id = self.id_value.get()
        name = self.name_value.get()
        fname = self.fname_value.get()
        contact = self.contact_value.get()
        month = self.month_value.get()
        discount = self.discount_value.get()
        fee = self.fee_value.get()

        connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password='1234',
                                             port='3306',
                                             database='hostel')
        my_connection = connection.cursor()

        if id == "" or discount == "" or contact == "" or name == "" or fname == "" or fee == "" or month == "" or contact == "":
            messagebox.showerror("Error", "Please fill in all fields")
        else:
            insert_query = "INSERT INTO Fee (ID,Name, FName,Contact,Month,Discount,Fee) VALUES (%s,%s, %s,%s,%s, %s,%s)"
            data = (id, name, fname, month, discount, contact, fee)

            my_connection.execute(insert_query, data)

            connection.commit()
            messagebox.showinfo("Congrats", "Fee Recorded")

            # Close the cursor and connection
            my_connection.close()
            connection.close()


    def open_staff_window(self):
        staff_window = Toplevel(self.root)
        staff_window.title("Staff Members")
        staff_window.geometry("1400x400+300+200")

        staff_tree = ttk.Treeview(staff_window, columns=(
            "ID", "Name", "Father Name", "Address", "DOB", "Age", "Contact"), show="headings")
        # Bind the TreeviewSelect event to a function
        staff_tree.bind("<<TreeviewSelect>>", lambda event: self.on_staff_select(event, staff_tree, staff_window))

        staff_tree.heading("ID", text="ID")
        staff_tree.heading("Name", text="Name")
        staff_tree.heading("Father Name", text="Father Name")
        staff_tree.heading("Address", text="Address")
        staff_tree.heading("DOB", text="DOB")
        staff_tree.heading("Age", text="Age")
        staff_tree.heading("Contact", text="Contact")

        staff_tree.pack(pady=20)



        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hostel"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Staff")
        staff_data = cursor.fetchall()

        for staff in staff_data:
            staff_tree.insert("", tk.END, values=staff)

    def on_staff_select(self, event, treeview, window):
        selected_item = treeview.selection()
        if selected_item:
            staff_info = treeview.item(selected_item, "values")

            # Print debug information
            print("Selected Staff Info:", staff_info)
            print("ID Value:", self.id_value.get())
            print("Name Value:", self.name_value.get())
            print("FName Value:", self.fname_value.get())
            print("Contact Value:", self.contact_value.get())

            # Populate the entry fields in the Manage Room window
            self.id_value.set(staff_info[0])  # Assuming ID is at index 0
            self.name_value.set(staff_info[1])  # Assuming Name is at index 1
            self.fname_value.set(staff_info[2])  # Assuming Father Name is at index 2
            self.contact_value.set(staff_info[6])

            # Close the student window
            window.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Salary(root)
    root.mainloop()