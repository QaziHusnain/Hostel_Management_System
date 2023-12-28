from tkinter import *
from tkinter import ttk
import tkinter as tk
import mysql.connector


class Weekly_Report:
    def __init__ (self,root):

        self.root= root
        self.root.title("Weekly Report")
        self.root.geometry("1100x480+250+215")
        self.root.resizable(False,False)


        #=======top label for Heading=======
        toplabel=Label(self.root, text="Weekly Report",font=("Time New Romen",14,"bold"), bg="black",fg="gold").pack(fill=X)

        label_id = Label(self.root, text="Total Student Registered :", font=("Time New Romen", 16, "bold")).place(x=350,y=120)
        self.total_label = Label(self.root, text="Total Amount: 0:", font=("Time New Romen", 16, "bold")).place(x=400,
                                                                                                                  y=120)
        label_id = Label(self.root, text="Total Fee Collected:", font=("Time New Romen", 16, "bold")).place(x=350,y=160)
        label_id = Label(self.root, text="Total Discount Given :", font=("Time New Romen", 16, "bold")).place(x=350,y=200)
        label_id = Label(self.root, text="Discount given :", font=("Time New Romen", 16, "bold")).place(x=350,y=240)

        add_button = Button(self.root, text="Add", bg="black", command=self.calculate_total, fg="gold", bd=2, width=12,
                        font=("time new romens", 14, "bold"))
        add_button.place(x=400, y=370)


    def calculate_total(self):
        # Connect to MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hostel"
        )
        cursor = conn.cursor()


        # Execute SQL query to get the sum of the 'amount' field
        cursor.execute("SELECT SUM(Fee) FROM Fee")
        result = cursor.fetchone()
        total_amount = result[0]

        # Close the database connection
        cursor.close()
        conn.close()

        # Update the label with the total amount
        self.total_label.config(text=f'Total Amount: {total_amount}')








if __name__ == "__main__":
    root=Tk()
    obj= Weekly_Report(root)
    root.mainloop()