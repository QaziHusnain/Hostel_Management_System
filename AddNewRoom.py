from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import mysql.connector


class Fee:
    def __init__(self, root):

        self.root = root
        self.root.title("Room Management")
        self.root.geometry("800x615+250+82")
        self.root.resizable(False, False)
        self.root["bg"] = "cadet blue"

        # ================Heading label======================
        label = Label(self.root, text="Manage Rooms", bg="Black", fg="gold",
                      font=("Time New Romen", 20, "bold")).pack(fill=X)

        # ==================creating labels and entry fields==========

        label2 = Label(self.root, text="Record Room", font=("Time New Romen", 16, "bold"), bg="#2F4F4F",
                       fg="white").place(x=110, y=60)

        self.No_value = IntVar()
        label_id = Label(self.root, text="Room No", font=("Time New Romen", 12, "bold"), bg="cadet blue", fg="white").place(
            x=20, y=120)
        id_entry = Entry(self.root, width=30, textvariable=self.No_value).place(x=160, y=125)

        # Create a StringVar for the dropdown
        self.Status_value = StringVar()

        # Label for "Active/Deactive"
        label_name = Label(self.root, text="Active/De-active", font=("Time New Romen", 12, "bold"), bg="cadet blue",
                           fg="white").place(x=20, y=170)

        # Combobox (Dropdown) for "Active/Deactive"
        status_combobox = ttk.Combobox(self.root, textvariable=self.Status_value, values=["", "Active", "Deactive"])
        status_combobox.place(x=160, y=175)
        status_combobox.set("")  # Set the default value

        self.Type_value = StringVar()

        # Label for "Room Type"
        label_fname = Label(self.root, text="Room Type", font=("Time New Romen", 12, "bold"), bg="cadet blue",
                            fg="white").place(x=20, y=220)

        # Combobox (Dropdown) for "Room Type"
        type_combobox = ttk.Combobox(self.root, textvariable=self.Type_value,
                                     values=["", "Single Seater", "Double Seater", "Three Seater"])
        type_combobox.place(x=160, y=225)
        type_combobox.set("")  # Set the default value

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
                             font=("time new romens", 14, "bold"),command=self.search_command)
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
            "RoomNo", "Status", "Type"),
                                      xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        self.st_detail.bind("<<TreeviewSelect>>", self.on_treeview_select)

        scroll_x.config(command=self.st_detail.xview)
        scroll_y.config(command=self.st_detail.yview)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.st_detail.heading("RoomNo", text="RoomNo")
        self.st_detail.heading("Status", text="Status")
        self.st_detail.heading("Type", text="Type")

        self.st_detail["show"] = "headings"

        self.st_detail.column("RoomNo", anchor=tk.CENTER, width=120)
        self.st_detail.column("Status", anchor=tk.CENTER, width=120)
        self.st_detail.column("Type", anchor=tk.CENTER, width=120)


        self.st_detail.pack(fill=tk.BOTH, expand=1)
        self.view_command()

    def add(self):
        No = self.No_value.get()
        Status = self.Status_value.get()
        Type = self.Type_value.get()


        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hostel"
        )
        cursor = conn.cursor()
        query = "INSERT INTO Rooms (RoomNo, Status, Type) VALUES (%s, %s, %s)"
        values = (No, Status, Type)
        cursor.execute(query, values)
        messagebox.showinfo("Success", "Room Recorded successful")

        # Commit and close
        conn.commit()
        conn.close()
        self.view_command()

    def view_command(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hostel"
        )
        cursor = conn.cursor()
        query = "SELECT RoomNo, Status,Type FROM Rooms"
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
        ID = self.No_value.get()
        Name = self.Status_value.get()
        FName = self.Type_value.get()

        # Execute MySQL query for searching data
        query = "SELECT * FROM Rooms WHERE RoomNo = %s OR Status = %s OR Type = %s"
        values = (ID, Name, FName)
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
        query = "DELETE FROM Rooms WHERE RoomNo = %s"
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

        # Execute MySQL query for updating data
        query = "UPDATE Rooms SET Status = %s, Type = %s WHERE RoomNo = %s"
        values = (self.Status_value.get(), self.Type_value.get(), self.No_value.get())

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
        self.No_value.set("0")
        self.Status_value.set("")
        self.Type_value.set("")
    def on_treeview_select(self, event):
        # Get the selected item from the Treeview
        selected_item = self.st_detail.selection()

        if selected_item:
            # Get the values of the selected item
            selected_values = self.st_detail.item(selected_item, "values")

            # Update the entry fields with the selected values
            self.No_value.set(selected_values[0])
            self.Status_value.set(selected_values[1])
            self.Type_value.set(selected_values[2])
    def reset_command(self):

        self.view_command()
        self.clear_entry_fields()


if __name__ == "__main__":
    root = Tk()
    obj = Fee(root)
    root.mainloop()


