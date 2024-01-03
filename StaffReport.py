import tkinter as tk
from tkinter import ttk
import mysql.connector

class MySQLTkinterApp:
    def __init__(self, root):
        self.root = root
        self.root.title(" Total Staff Report")
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

        toplabel = tk.Label(self.root, text="Total Staff Report", font=("Time New Romen", 14, "bold"), bg="black", width=400,
                            fg="gold").pack()

        # Button to trigger the calculation
        self.calculate_button = ttk.Button(root, text="Calculate Report", command=self.calculate_total)
        self.calculate_button.pack(pady=20)

        # Label to display the total staff count
        self.total_label = ttk.Label(root, text="Total Staff: 0")
        self.total_label.pack(pady=20)

        # Labels to display the total paid and unpaid salary
        self.paid_label = ttk.Label(root, text="Total Paid Salary: 0")
        self.paid_label.pack(pady=20)

        self.unpaid_label = ttk.Label(root, text="Total Unpaid Salary: 0")
        self.unpaid_label.pack(pady=20)

        # Label to display the total calculated salary
        self.std_label = ttk.Label(root, text="Total Calculated Salary: 0")
        self.std_label.pack(pady=20)

    def calculate_total(self):
        # Execute SQL query to get the count of 'Name' field (total staff)
        self.cursor.execute("SELECT COUNT(Name) FROM Staff")
        result = self.cursor.fetchone()
        total_staff = result[0]

        # Update the label with the total staff count
        self.total_label.config(text=f'Total Staff: {total_staff}')

        # Calculate total salary for both "Paid" and "Unpaid"
        self.calculate_salary("Paid", self.paid_label)
        self.calculate_salary("Unpaid", self.unpaid_label)

    def calculate_salary(self, payment_status, label):
        # Execute SQL query to get the sum of 'SalaryAmount' for the specified payment_status
        query = f"SELECT SUM(SalaryAmount) FROM Salary WHERE PaymentStatus = '{payment_status}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        total_salary = result[0] if result[0] is not None else 0

        # Update the label with the total salary for the specified payment_status
        label.config(text=f'Total {payment_status} Salary: {total_salary}')

        # Execute SQL query to get the sum of the 'amount' field
        self.cursor.execute("SELECT SUM(SalaryAmount) FROM Salary")
        result = self.cursor.fetchone()
        total_amount = result[0]

        # Update the label with the total amount
        self.std_label.config(text=f'Total Calculated Salary: {total_amount}')

    def run(self):
        # Run the Tkinter event loop
        self.root.mainloop()

    def cleanup(self):
        # Close the cursor and connection
        self.cursor.close()
        self.connection.close()

if __name__ == "__main__":
    root = tk.Tk()

    # Create an instance of the application
    app = MySQLTkinterApp(root)

    # Run the application
    app.run()
    app.cleanup()
