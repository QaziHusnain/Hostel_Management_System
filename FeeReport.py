import tkinter as tk
from tkinter import ttk
import mysql.connector

class MySQLTkinterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Total Fee Report")
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

        toplabel = tk.Label(self.root, text="Total Colected Fee", font=("Time New Romen", 14, "bold"), bg="black",
                            width=400, fg="gold").pack()

        # Button to trigger the calculation
        self.calculate_button = ttk.Button(root, text="Calculate Total", command=self.calculate_total)
        self.calculate_button.pack(pady=20)

        # Label to display the total amount
        self.total_label = ttk.Label(root, text="Total Fee: 0")
        self.total_label.pack(pady=20)

        # Label to display the total paid amount
        self.paid_label = ttk.Label(root, text="Total Paid Amount: 0")
        self.paid_label.pack(pady=20)

        # Label to display the total unpaid amount
        self.unpaid_label = ttk.Label(root, text="Total Unpaid Amount: 0")
        self.unpaid_label.pack(pady=20)

    def calculate_total(self):
        # Execute SQL query to get the sum of the 'Fee' field
        self.cursor.execute("SELECT SUM(Fee) FROM Fee")
        result = self.cursor.fetchone()
        total_amount = result[0]

        # Update the label with the total amount
        self.total_label.config(text=f'Total Amount: {total_amount}')

        # Calculate and update the total paid and unpaid amounts
        self.calculate_payment_amounts()

    def calculate_payment_amounts(self):
        # Execute SQL query to get the sum of paid amounts
        self.cursor.execute("SELECT SUM(Fee) FROM Fee WHERE Paid_Unpaid = 'Paid'")
        total_paid_amount = self.cursor.fetchone()[0]

        # Update the label with the total paid amount
        self.paid_label.config(text=f'Total Paid Amount: {total_paid_amount}')

        # Execute SQL query to get the sum of unpaid amounts
        self.cursor.execute("SELECT SUM(Fee) FROM Fee WHERE Paid_Unpaid = 'Unpaid'")
        total_unpaid_amount = self.cursor.fetchone()[0]

        # Update the label with the total unpaid amount
        self.unpaid_label.config(text=f'Total Unpaid Amount: {total_unpaid_amount}')

    def run(self):
        # Run the Tkinter event loop
        self.root.mainloop()

    def cleanup(self):
        # Close the cursor and connection
        self.cursor.close()
        self.connection.close()

# Create an instance of the application
app = MySQLTkinterApp(tk.Tk())

# Run the application
app.run()

# Cleanup after the application is closed
app.cleanup()
