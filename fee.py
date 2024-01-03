from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import StringVar



class Fee:
    def __init__(self, root):

        self.root = root
        self.root.title("Fee Management")
        self.root.geometry("1430x815+250+82")
        self.root.resizable(False, False)
        self.root["bg"] = "cadet blue"

        # ================Heading label======================
        label = Label(self.root, text="Manage Fee", bg="Black", fg="gold",
                      font=("Time New Romen", 20, "bold")).pack(fill=X)

        # ==================creating labels and entry fields==========

        label2 = Label(self.root, text="Record Fee", font=("Time New Romen", 16, "bold"), bg="#2F4F4F", fg="white").place(x=110, y=60)

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

        self.Month_value = tk.StringVar()

        # Label for the Month
        label_Month = tk.Label(self.root, text="Month", font=("Times New Roman", 12, "bold"), bg="cadet blue",
                               fg="white")
        label_Month.place(x=20, y=320)

        # Create a list of months
        months = [
            "January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"
        ]

        # Create a Combobox (Drop-down list) with the list of months
        Month_combobox = ttk.Combobox(self.root, textvariable=self.Month_value, values=months, state="readonly",
                                      width=27)
        Month_combobox.place(x=160, y=325)
        Month_combobox.set("Select Month")  # Default value displayed in the combobox


        self.Year_value = StringVar()
        label_Year = Label(self.root, text="Year", font=("Time New Romen", 12, "bold"), bg="cadet blue",
                           fg="white").place(x=20, y=370)
        year_entry = Entry(self.root, width=30, textvariable=self.Year_value).place(x=160, y=375)

        self.Fee_value = StringVar()
        label_contact = Label(self.root, text="Fee Amount", font=("Time New Romen", 12, "bold"), bg="cadet blue",
                              fg="white").place(x=20, y=420)
        contact_entry = Entry(self.root, width=30, textvariable=self.Fee_value).place(x=160, y=425)

        self.Paid_Unpaid_value = StringVar()

        # Label for Payment Status
        label_Paid_Unpaid = Label(self.root, text="Payment Status", font=("Times New Roman", 12, "bold"),
                                  bg="cadet blue", fg="white")
        label_Paid_Unpaid.place(x=20, y=470)

        # Create a Combobox (Dropdown list) for Payment Status
        paid_unpaid_combobox = ttk.Combobox(self.root, values=["Paid", "Unpaid"], textvariable=self.Paid_Unpaid_value,width=27,
                                            state="readonly")
        paid_unpaid_combobox.place(x=160, y=470)
        paid_unpaid_combobox.set("Paid")  # Set the default value to "Paid"



        # ===================creating buttons=====================

        add_button = Button(self.root, text="Add", bg="black", command=self.add, fg="gold", bd=2, width=12,
                            font=("time new romens", 14, "bold"))
        add_button.place(x=20, y=570)

        del_button = Button(self.root, text="Delete", command=self.delete_command, bg="black", fg="gold", bd=2, width=12,
                            font=("time new romens", 14, "bold"))
        del_button.place(x=190, y=570)

        clear_button = Button(self.root, text="Clear", bg="black", command=self.clear_entry_fields, fg="gold", bd=2, width=12,
                               font=("time new romens", 14, "bold"))
        clear_button.place(x=20, y=620)

        btn_insert_student = Button(self.root, text="Insert Student", command=self.insert_student, bg="black",
                                    fg="gold", bd=2, width=12, font=("time new romens", 14, "bold"))
        btn_insert_student.place(x=190, y=620)

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
            "StdID", "Name", "Father Name", "Contact", "Month", "Year", "Fee","Payment Status"),
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
        self.st_detail.heading("Year", text="Year")
        self.st_detail.heading("Fee", text="Fee")
        self.st_detail.heading("Payment Status", text="Payment Status")

        self.st_detail["show"] = "headings"

        self.st_detail.column("StdID", anchor=tk.CENTER, width=120)
        self.st_detail.column("Name", anchor=tk.CENTER, width=120)
        self.st_detail.column("Father Name", anchor=tk.CENTER, width=120)
        self.st_detail.column("Contact", anchor=tk.CENTER, width=120)
        self.st_detail.column("Month", anchor=tk.CENTER, width=120)
        self.st_detail.column("Year", anchor=tk.CENTER, width=120)
        self.st_detail.column("Fee", anchor=tk.CENTER, width=120)
        self.st_detail.column("Payment Status", anchor=tk.CENTER, width=120)

        self.st_detail.pack(fill=tk.BOTH, expand=1)
        self.view_command()

    def add(self):
        ID = self.id_value.get()
        Name = self.name_value.get()
        FName = self.fname_value.get()
        Contact = self.Contact_value.get()
        Month = self.Month_value.get()
        Year = self.Year_value .get()
        Fee = self.Fee_value.get()
        Paid_Unpaid=self.Paid_Unpaid_value.get()

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hostel"
        )
        cursor = conn.cursor()
        query = "INSERT INTO Fee (ID, Name, FName, Contact, Month, Year, Fee, Paid_Unpaid) VALUES (%s, %s, %s, %s, %s, %s, %s,%s)"
        values = (ID, Name, FName, Contact, Month, Year, Fee,Paid_Unpaid)
        cursor.execute(query, values)
        messagebox.showinfo("Success", "Fee Record successful")

        # Commit and close` 22dr3w
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

        # Bind the Treeview selection event to a method
        self.st_detail.bind("<<TreeviewSelect>>", self.on_tree_select)

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


    def clear_entry_fields(self):
        # Clear entry fields
        self.id_value.set("")
        self.name_value.set("")
        self.fname_value.set("")
        self.Contact_value.set("")
        self.Month_value.set("")
        self.Year_value.set("")
        self.Fee_value.set("")
        self.Paid_Unpaid_value.set("")

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

            self.name_value.set(student_info[1])
            self.fname_value.set(student_info[2])
            self.Contact_value.set(student_info[3])



            # Close the student window
            window.destroy()

    def on_tree_select(self, event):
        selected_item = self.st_detail.selection()
        if selected_item:
            # Retrieve the values of the selected item
            selected_values = self.st_detail.item(selected_item, "values")

            # Populate entry fields with selected values
            self.id_value.set(selected_values[0])
            self.name_value.set(selected_values[1])
            self.fname_value.set(selected_values[2])
            self.Contact_value.set(selected_values[3])
            self.Month_value.set(selected_values[4])
            self.Year_value.set(selected_values[5])
            self.Fee_value.set(selected_values[6])
            self.Paid_Unpaid_value.set(selected_values[7])


if __name__ == "__main__":
    root = Tk()
    obj = Fee(root)
    root.mainloop()


