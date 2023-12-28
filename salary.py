from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import mysql.connector


class Salary:
    def __init__ (self,root):

        self.root= root
        self.root.title("Manage Staff Salary")
        self.root.geometry("1100x480+250+215")
        self.root.resizable(False,False)

        #=======top label for Heading=======
        toplabel=Label(self.root, text="Manage Staff Salary",font=("Time New Romen",14,"bold"), bg="black",fg="gold").pack(fill=X)

        #=======labels and entries fields ========
        id_value = IntVar()
        id_label = Label(self.root, text="ID :", font=("Time New Romen", 12, "bold"), fg="black").place(x=20, y=60)
        id_entry = Entry(self.root, width=15, textvariable=id_value).place(x=140, y=60)
        name_value = StringVar()
        name_label = Label(self.root, text="Name", font=("Time New Romen", 12, "bold"), fg="black").place(x=20, y=100)
        name_entry = Entry(self.root, width=30, textvariable=name_value).place(x=140, y=100)
        fname_value = StringVar()
        fname_label = Label(self.root, text="Father Name", font=("Time New Romen", 12, "bold"), fg="black").place(x=20,
                                                                                                                  y=140)
        fname_entry = Entry(self.root, width=30, textvariable=fname_value).place(x=140, y=140)
        contact_value = StringVar()
        contact_Name = Label(self.root, text="Contact No", font=("Time New Romen", 12, "bold"), fg="black").place(x=20,
                                                                                                                  y=180)
        contact_entry = Entry(self.root, width=30, textvariable=contact_value).place(x=140, y=180)
        month_value = StringVar()
        month_label = Label(self.root, text="Month", font=("Time New Romen", 12, "bold"), fg="black").place(x=20, y=220)
        month_entry = Entry(self.root, width=30, textvariable=month_value).place(x=140, y=220)
        discount_value = StringVar()
        discount_label = Label(self.root, text="Discount", font=("Time New Romen", 12, "bold"), fg="black").place(x=20,
                                                                                                                  y=260)
        discount_entry = Entry(self.root, width=30, textvariable=discount_value).place(x=140, y=260)
        fee_value = StringVar()
        fee_label = Label(self.root, text="Fee Amount", font=("Time New Romen", 12, "bold"), fg="black").place(x=20,                                                                                                            y=300)
        fee_entry = Entry(self.root, width=30, textvariable=fee_value).place(x=140, y=300)

        #========search, save, and clear buttons=============
        search_btn =Button(self.root, text="Search",font=("Time New Romen", 12, "bold"),bg= "black", fg="gold" ).place(x=255,y=60)
        
        save_btn =Button(self.root, text="Save", command=self.add, font=("Time New Romen", 12, "bold"),bg= "black", fg="gold", width = 12 ).place(x=20,y=360)

        clear_btn =Button(self.root, text="Clear",font=("Time New Romen", 12, "bold"),bg= "black", fg="gold", width= 12 ).place(x=200,y=360)
        
        #========= frame for saparation =========
        frame= Frame(self.root, width =4, height =435,bg= "cadet blue").place(x=400,y=30)

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hostel"
        )
        cursor = conn.cursur()

        self.tree = ttk.Treeview(self.root, height=18,
                                 columns=("ID", "Name", "FName", "Contact" "Month", "Discount", "Fee Amount"))

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


if __name__ == "__main__":
    root=Tk()
    obj= Salary(root)
    root.mainloop()