import tkinter as tk
from tkinter import ttk
import mysql.connector

class MySQLTkinterApp:
    def __init__(self, root):
        self.root = root
        self.root.title(" Total Student Report")
        self.root.geometry("1100x480+250+215")
        self.root.resizable(False, False)



        # Connect to MySQL database
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hostel"
        )
        self.cursor = self.connection.cursor()
        toplabel = tk.Label(self.root, text="Total Registered Student", font=("Time New Romen", 14, "bold"), bg="black", width=400,
                            fg="gold").pack()

        # Button to trigger the calculation
        self.calculate_button = ttk.Button(root, text="Calculate Report", command=self.calculate_total)
        self.calculate_button.pack(pady=20)

        # Label to display the total amount


        self.std_label = ttk.Label(root, text="Total Registered Student: 0")
        self.std_label.pack(pady=20)
        self.total_label = ttk.Label(root, text="Total Fee Deposit: 0")
        self.total_label.pack(pady=20)

    def calculate_total(self):
        # Execute SQL query to get the sum of the 'amount' field
        self.cursor.execute("SELECT SUM(Fee) FROM Fee")
        result = self.cursor.fetchone()
        total_amount = result[0]

        # Update the label with the total amount
        self.total_label.config(text=f'Total Amount: {total_amount}')
        self.calculate_Student()
    def calculate_Student(self):
        # Execute SQL query to get the sum of the 'amount' field
        self.cursor.execute("SELECT COUNT(Name) FROM Fee")
        result = self.cursor.fetchone()
        total_amount = result[0]

        # Update the label with the total amount
        self.std_label.config(text=f'Total Registered Student: {total_amount}')
    def run(self):
        # Run the Tkinter event loop
        self.root.mainloop()

    def __del__(self):
        # Close the database connection when the instance is deleted
        self.cursor.close()
        self.connection.close()

# Create an instance of the application
app = MySQLTkinterApp(tk.Tk())

# Run the application
app.run()
