from tkinter import *
from tkinter import messagebox
import mysql.connector


def register_user():
    username = uservalue.get()
    password = passvalue.get()
    role = option.get()

    if not (username and password and role):
        messagebox.showerror("Error", "Please fill in all fields")
        return

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        port='3306',
        database='hostel'
    )
    my_connection = connection.cursor()

    try:
        insert_query = "INSERT INTO users (username, password, Role) VALUES (%s, %s, %s)"
        data = (username, password, role)
        my_connection.execute(insert_query, data)
        connection.commit()
        messagebox.showinfo("Congrats", "Registration successful")
    except Exception as e:
        messagebox.showerror("Error", f"Registration failed: {str(e)}")
    finally:
        my_connection.close()
        connection.close()

def login_user():
    username = uservalue.get()
    password = passvalue.get()
    role = option.get()

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        port='3306',
        database='hostel'
    )
    my_connection = connection.cursor()

    try:
        my_connection.execute("SELECT * FROM users WHERE username=%s AND password=%s AND Role=%s",
                              (username, password, role))
        user = my_connection.fetchone()

        if user is None:
            messagebox.showinfo("Error", "Login failed")
        else:
            # Import and create the Home window
            import Home
            home_window = Toplevel(root)
            home_app = Home.Hostel_Management(home_window)
            home_window.deiconify()  # Make the window visible

            # Close the login window
            root.withdraw()

            messagebox.showinfo("Success", "Login successful")

    except Exception as e:
        messagebox.showerror("Error", f"Login failed: {str(e)}")
    finally:
        my_connection.close()
        connection.close()


root = Tk()
root.geometry("800x500")
root.title("Login")
# ===================================================Creating frames===============================================

f1=Frame(root, bg="grey",border=0,relief=SUNKEN)
f1.pack(side=TOP, fill=X, padx=155)

# Creating frame over another frame
f2=Frame(f1,bg="gray95", border=0,relief=SUNKEN)
f2.pack(side=TOP,fill=X, padx=10, pady=10)

f3=Frame(f2,bg="white", border=0,relief=SUNKEN)
f3.pack(side=RIGHT,fill=X, padx=30,pady=60)

f4=Frame(f1,bg="gray95", border=0,relief=SUNKEN)
f4.pack(side=BOTTOM,fill=X, padx=10, pady=10)

#=========================================== Creating Label for Heading===============================================

label= Label(f2, text= "Registration & Login Form",font=("Time New Romen", 22,"bold"),bg= "teal")
label.place(x=55,y=20)


# ======================================Creating label of username and Passward========================================

label1= Label(f2, text= "Username:",font=("Aril",14,"bold"),fg="blue")
label1.place(x=90,y=65)

label2=Label(f2,text="Passward:",font=("Aril",14,"bold"))
label2.place(x=90,y=110)


#========================================Creating variables for username and passward===================================

uservalue=StringVar()
passvalue=StringVar()
option = StringVar()
#====================================================Creating entry fields==============================================

userentry=Entry(f3, width=30, textvariable= uservalue)
userentry.pack(padx=35,pady=10)
passentry=Entry(f3, width=30,textvariable= passvalue, show="*")
passentry.pack(padx=35,pady=10)


option.set("Radio")
# Create radio buttons
W_radio = Radiobutton(f2, text="WARDEN", font=2, variable=option, value="WARDEN")
W_radio.place(x=90,y=155)
W_radio = Radiobutton(f3, text="ACCOUNTANT", font=2, variable=option, value="ACCOUNTANT")
W_radio.pack(padx=35,pady=20)



# =================================================Creating buttoms=====================================================



Button(f2, text="Register",font=("Aril",10,"bold"), border=6,width=15, command= register_user).place(x=100,y=220)
Button(f2, text="login",font=("Aril",10,"bold"), border=6,width=15, command= login_user).place(x=280,y=220)


root.mainloop()