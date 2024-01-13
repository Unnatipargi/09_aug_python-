from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

def create_conn():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bank'
    )

def register_banker():
    if e_b_username.get() == '' or e_b_password.get() == '':
        msg.showinfo('Registration Status', 'All fields are mandatory')
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query = 'INSERT INTO bankers(username, password) VALUES(%s, %s)'
        args = (e_b_username.get(), e_b_password.get())
        cursor.execute(query, args)
        conn.commit()
        conn.close()

        e_b_username.delete(0, 'end')
        e_b_password.delete(0, 'end')
        msg.showinfo('Registration Status', 'Banker registered successfully')

def insert_customer():
    if e_c_username.get() == '' or e_c_password.get() == '' or e_c_balance.get() == '':
        msg.showinfo('Insert Status', 'All fields are mandatory')
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query = 'INSERT INTO customers(username, password, balance) VALUES(%s, %s, %s)'
        args = (e_c_username.get(), e_c_password.get(), e_c_balance.get())
        cursor.execute(query, args)
        conn.commit()
        conn.close()

        e_c_username.delete(0, 'end')
        e_c_password.delete(0, 'end')
        e_c_balance.delete(0, 'end')
        msg.showinfo('Insert Status', 'Customer added successfully')

def view_customer():
    if e_c_id.get() == '':
        msg.showinfo('View Status', 'Customer ID is mandatory')
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query = 'SELECT * FROM customers WHERE id=%s'
        args = (e_c_id.get(),)
        cursor.execute(query, args)
        row = cursor.fetchall()
        conn.close()

        if row:
            for i in row:
                e_c_username.insert(0, i[1])
                e_c_password.insert(0, i[2])
                e_c_balance.insert(0, i[3])
        else:
            msg.showinfo('View Status', 'Customer ID not found')

root = Tk()
root.title('Banking Application')
root.geometry('400x300')
root.resizable(width=False, height=False)

# Banker Registration Widgets
l_b_username = Label(root, text='Banker Username')
l_b_username.place(x=20, y=20)
e_b_username = Entry(root)
e_b_username.place(x=150, y=20)

l_b_password = Label(root, text='Banker Password')
l_b_password.place(x=20, y=50)
e_b_password = Entry(root, show='*')
e_b_password.place(x=150, y=50)

register_banker_btn = Button(root, text='Register Banker', command=register_banker)
register_banker_btn.place(x=20, y=80)

# Customer Insertion Widgets
l_c_id = Label(root, text='Customer ID')
l_c_id.place(x=20, y=120)
e_c_id = Entry(root)
e_c_id.place(x=150, y=120)

l_c_username = Label(root, text='Username')
l_c_username.place(x=20, y=150)
e_c_username = Entry(root)
e_c_username.place(x=150, y=150)

l_c_password = Label(root, text='Password')
l_c_password.place(x=20, y=180)
e_c_password = Entry(root, show='*')
e_c_password.place(x=150, y=180)

l_c_balance = Label(root, text='Balance')
l_c_balance.place(x=20, y=210)
e_c_balance = Entry(root)
e_c_balance.place(x=150, y=210)

insert_customer_btn = Button(root, text='Insert Customer', command=insert_customer)
insert_customer_btn.place(x=20, y=240)

view_customer_btn = Button(root, text='View Customer', command=view_customer)
view_customer_btn.place(x=150, y=240)

root.mainloop()
