from tkinter import *
from tkinter import ttk, simpledialog
import tkinter as tk
from tkinter import messagebox
import mysql.connector


class Salary:
    def __init__(self, root):

        self.root = root
        self.root.title("Manage Staff Salary")
        self.root.geometry("1400x580+250+215")
        self.root.resizable(False, False)

        self.id_value = IntVar()
        self.name_value = StringVar()
        self.fname_value = StringVar()
        self.contact_value = StringVar()
        self.month_value = StringVar()
        self.fee_value = StringVar()
        self.year_value = StringVar()
        self.payment_status_value = StringVar()

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
        month_combobox = ttk.Combobox(self.root, textvariable=self.month_value, values=self.get_all_months())
        month_combobox.place(x=140, y=220)

        fee_label = Label(self.root, text="Salary Amount", font=("Time New Romen", 12, "bold"), fg="black").place(x=20,
                                                                                                               y=260)
        fee_entry = Entry(self.root, width=30, textvariable=self.fee_value).place(x=140, y=260)

        year_label = Label(self.root, text="Year", font=("Time New Romen", 12, "bold"), fg="black").place(x=20, y=300)
        year_entry = Entry(self.root, width=10, textvariable=self.year_value).place(x=140, y=300)

        payment_status_label = Label(self.root, text="Payment Status", font=("Time New Romen", 12, "bold"), fg="black").place(x=20, y=340)
        payment_status_combobox = ttk.Combobox(self.root, textvariable=self.payment_status_value, values=["Paid", "Unpaid"])
        payment_status_combobox.place(x=170, y=340)

        # =======search, save, and clear buttons=======


        save_btn = Button(self.root, text="Save", command=self.add, font=("Time New Romen", 12, "bold"), bg="black",
                          fg="gold", width=12).place(x=20, y=380)

        clear_btn = Button(self.root, text="Clear", command=self.clear_fields, font=("Time New Romen", 12, "bold"), bg="black", fg="gold",
                           width=12).place(x=200, y=380)

        delete_all_btn = Button(self.root, text="Delete All", command=self.delete_all,
                                font=("Time New Romen", 12, "bold"),
                                bg="black", fg="gold", width=12)
        delete_all_btn.place(x=200, y=420)

        # Insert Staff Member button
        insert_staff_btn = Button(self.root, text="Insert Staff", command=self.open_staff_window,
                                  font=("Time New Romen", 12, "bold"), bg="black", fg="gold", width=12)
        insert_staff_btn.place(x=20, y=420)

        # ========= frame for separation =========
        frame = Frame(self.root, width=4, height=435, bg="cadet blue").place(x=400, y=30)

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hostel"
        )
        cursor = conn.cursor()

        self.tree = ttk.Treeview(self.root, height=18,
                                 columns=("ID", "Name", "FName", "Contact", "Month", "Salary Amount", "Year", "Payment Status"))

        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("FName", text="FName")
        self.tree.heading("Contact", text="Contact")
        self.tree.heading("Month", text="Month")
        self.tree.heading("Salary Amount", text="Salary Amount")
        self.tree.heading("Year", text="Year")
        self.tree.heading("Payment Status", text="Payment Status")

        self.tree["show"] = "headings"

        self.tree.column("ID", anchor=tk.CENTER, width=80)
        self.tree.column("Name", anchor=tk.CENTER, width=120)
        self.tree.column("FName", anchor=tk.CENTER, width=120)
        self.tree.column("Contact", anchor=tk.CENTER, width=120)
        self.tree.column("Month", anchor=tk.CENTER, width=80)
        self.tree.column("Salary Amount", anchor=tk.CENTER, width=120)
        self.tree.column("Year", anchor=tk.CENTER, width=80)
        self.tree.column("Payment Status", anchor=tk.CENTER, width=120)

        self.tree.place(x=450, y=50)
        self.display_records()

    def get_all_months(self):
        return ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    def add(self):
        id = self.id_value.get()
        name = self.name_value.get()
        fname = self.fname_value.get()
        contact = self.contact_value.get()
        month = self.month_value.get()
        fee = self.fee_value.get()
        year = self.year_value.get()
        payment_status = self.payment_status_value.get()

        connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password='1234',
                                             port='3306',
                                             database='hostel')
        my_connection = connection.cursor()

        if id == "" or contact == "" or name == "" or fname == "" or fee == "" or month == "" or year == "" or payment_status == "":
            messagebox.showerror("Error", "Please fill in all fields")
        else:
            insert_query = "INSERT INTO Salary(ID, Name, FName, Contact, Month, SalaryAmount, Year, PaymentStatus) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            data = (id, name, fname, contact, month, fee, year, payment_status)

            my_connection.execute(insert_query, data)

            connection.commit()
            messagebox.showinfo("Congrats", "Fee Recorded")

            # Close the cursor and connection
            my_connection.close()
            connection.close()
        self.display_records()
        self.clear_fields()


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



            # Populate the entry fields in the Manage Room window
            self.id_value.set(staff_info[0])  # Assuming ID is at index 0
            self.name_value.set(staff_info[1])  # Assuming Name is at index 1
            self.fname_value.set(staff_info[2])  # Assuming Father Name is at index 2
            self.contact_value.set(staff_info[6])

            # Close the student window
            window.destroy()

    def clear_fields(self):
        # Clear all the entry and combobox fields
        self.id_value.set("")
        self.name_value.set("")
        self.fname_value.set("")
        self.contact_value.set("")
        self.month_value.set("")
        self.fee_value.set("")
        self.year_value.set("")
        self.payment_status_value.set("")

    def delete_all(self):
        result = messagebox.askquestion("Delete All Records", "Are you sure you want to delete all records?")
        if result == "yes":
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                port='3306',
                database='hostel'
            )
            my_connection = connection.cursor()

            delete_query = "DELETE FROM Salary"
            my_connection.execute(delete_query)

            connection.commit()
            messagebox.showinfo("Success", "All records deleted successfully")

            # Close the cursor and connection
            my_connection.close()
            connection.close()

            # Refresh the Treeview after deletion
            self.refresh_treeview()

    def refresh_treeview(self):
        # Clear the existing items in the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Retrieve and display the updated data in the Treeview
        self.display_records()

    def display_records(self):
        # Clear the existing items in the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Retrieve and display the updated data in the Treeview
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            port='3306',
            database='hostel'
        )
        my_connection = connection.cursor()

        my_connection.execute("SELECT * FROM Salary")
        records = my_connection.fetchall()

        for record in records:
            self.tree.insert("", tk.END, values=record)

        # Close the cursor and connection
        my_connection.close()
        connection.close()



if __name__ == "__main__":
    root = Tk()
    obj = Salary(root)
    root.mainloop()