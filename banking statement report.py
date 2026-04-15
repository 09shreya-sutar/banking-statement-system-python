import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import pymysql

skill = tk.Tk()
skill.title("Banking Statement Report")
skill.geometry("1200x700")
skill.configure(bg="#e6f2ff")

from tkinter import StringVar, IntVar

# Account Details
acc_no = StringVar()
acc_name = StringVar()
aadhar = StringVar()
mobile = StringVar()
ifsc = StringVar()
branch = StringVar()

# Transaction Details
trans_date = StringVar()
trans_type = StringVar()
mode = StringVar()
amount = StringVar()
balance = StringVar()


file=PhotoImage(file="sbi long 1.png")
label=Label(skill,image=file)
label.place(x=150,y=0,height=150)

#Label(skill,text='State Bank Of India',bg='deepsky blue4',fg='white',height=1,font='arial 20 bold').place(x=260,y=0,width=1270,height=60)

frame=LabelFrame(skill,bg="sky blue").place(x=0,y=150,height=15,width=1600)

ff=Frame(skill,bg="#cce6ff")
ff.place(x=0,y=160,height=700,width=1600)

frame2=LabelFrame(skill,bg="alice blue").place(x=10,y=175,height=330,width=680)
Label(skill,text="Account Details",fg='white',font='arial 15  ',bg='deepsky blue4').place(x=40,y=170)

# Account Details Section
Label(frame, text="Ac Holder Name", fg='black', font='arial 18', bg="alice blue").place(x=20, y=200)
acc_name_entry = Entry(frame, bg='white', fg='black', bd=4, font='arial 15 ',textvariable=acc_name)
acc_name_entry.place(x=240, y=205, width=370, height=30)

Label(frame, text="Account no", fg='black', font='arial 18', bg="alice blue").place(x=20, y=250)
acc_no_entry = Entry(frame, bg='white', fg='black', bd=4, font='arial 15 ',textvariable=acc_no)
acc_no_entry.place(x=240, y=255, width=250, height=30)

Label(frame, text="Aadhar no", fg='black', font='arial 18', bg="alice blue").place(x=20, y=300)
aadhar_entry = Entry(frame, bg='white', fg='black', bd=4, font='arial 15 ',textvariable=aadhar)
aadhar_entry.place(x=240, y=305, width=250, height=30)

Label(frame, text="Mobile no", fg='black', font='arial 18', bg="alice blue").place(x=20, y=350)
mobile_entry = Entry(frame, bg='white', fg='black', bd=4, font='arial 15 ',textvariable=mobile)
mobile_entry.place(x=240, y=355, width=250, height=30)

Label(frame, text="IFSC Code", fg='black', font='arial 18', bg="alice blue").place(x=20, y=400)
ifsc_entry = Entry(frame, bg='white', fg='black', bd=4, font='arial 15 ',textvariable=ifsc)
ifsc_entry.place(x=240, y=405, width=250, height=30)

Label(frame, text="Branch Name", fg='black', font='arial 18', bg="alice blue").place(x=20, y=450)
branch_entry = Entry(frame, bg='white', fg='black', bd=4, font='arial 15 ',textvariable=branch)
branch_entry.place(x=240, y=455, width=250, height=30)

# Transaction Details Section
frame3=LabelFrame(skill,bg="alice blue").place(x=10,y=520,height=280,width=680)
Label(skill, text="Transaction Details", fg='white', font='arial 15', bg='deepsky blue4').place(x=40, y=510)

Label(frame, text="Transaction Date", fg='black', font='arial 18', bg="alice blue").place(x=20, y=550)
trans_date_entry = Entry(frame, bg='white', fg='black', bd=4, font='arial 15 ',textvariable=trans_date)
trans_date_entry.place(x=240, y=555, width=250, height=30)

Label(frame, text="Transaction Type", fg='black', font='arial 18', bg="alice blue").place(x=20, y=600)
trans_type_combo = ttk.Combobox(frame, values=["Deposit", "Withdrawal"], font='arial 15', state="readonly",textvariable=trans_type)
trans_type_combo.place(x=240, y=605, width=250, height=30)

Label(frame, text="Mode", fg='black', font='arial 18', bg="alice blue").place(x=20, y=650)
mode_combo = ttk.Combobox(frame, values=["Cash", "Cheque", "Online"], font='arial 15', state="readonly",textvariable=mode)
mode_combo.place(x=240, y=655, width=250, height=30)

Label(frame, text="Amount", fg='black', font='arial 18', bg="alice blue").place(x=20, y=700)
amount_entry = Entry(frame, bg='white', fg='black', bd=4, font='arial 15 ',textvariable=amount)
amount_entry.place(x=240, y=705, width=250, height=30)

Label(frame, text="Balance", fg='black', font='arial 18', bg="alice blue").place(x=20, y=750)
balance_entry = Entry(frame, bg='white', fg='black', bd=4, font='arial 15 ',textvariable=balance)
balance_entry.place(x=240, y=755, width=250, height=30)

frame1 = Frame(skill, bg="white")
frame1.place(x=700, y=175, height=200, width=830)

y_scroll = Scrollbar(frame1, orient=VERTICAL)
x_scroll = Scrollbar(frame1, orient=HORIZONTAL)

student_table = ttk.Treeview(
    frame1,
    columns=("Account No.", "Account Name", "Aadhar no", "Mobile no", "IFSC code","Branch code","Transaction date","Transaction type","Mode","Amount","Balance"),
    yscrollcommand=y_scroll.set,
    xscrollcommand=x_scroll.set
)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)
y_scroll.pack(side=RIGHT, fill=Y)
x_scroll.pack(side=BOTTOM, fill=X)

for col in ("Account No.", "Account Name", "Aadhar no", "Mobile no", "IFSC code","Branch code","Transaction date","Transaction type","Mode","Amount","Balance"):
    student_table.heading(col, text=col)
student_table['show'] = "headings"

student_table.column("Account No.", width=200)
student_table.pack(fill=BOTH, expand=True)


frame2 = Frame(skill, bg="white")
frame2.place(x=1000, y=450, height=350, width=540)

billframe=Label(skill,text="MINI STATEMENT",fg='white',font='arial 15 bold ',bg='deepsky blue4').place(x=1000,y=400,width=530,height=50)


# Create vertical and horizontal scrollbars
y_scroll = Scrollbar(frame2, orient=VERTICAL)
x_scroll = Scrollbar(frame2, orient=HORIZONTAL)

# Create the Text widget
textaria = Text(
    frame2,
    height=14,
    width=60,
    bd=5,
    relief=GROOVE,
    font="arial 12 bold",
    wrap=NONE,  # Important for horizontal scrolling
    yscrollcommand=y_scroll.set,
    xscrollcommand=x_scroll.set
)

# Configure scrollbars
y_scroll.config(command=textaria.yview)
x_scroll.config(command=textaria.xview)

# Pack everything
y_scroll.pack(side=RIGHT, fill=Y)
x_scroll.pack(side=BOTTOM, fill=X)
textaria.pack(side=LEFT, fill=BOTH, expand=True)




def fetch_banking():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="Shreya@2709", database="bank")
        cur = conn.cursor()
        cur.execute("SELECT * FROM banking")
        rows = cur.fetchall()
        if len(rows) != 0:
            student_table.delete(*student_table.get_children())
            for row in rows:
                student_table.insert("", END, values=row)
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", f"Database error: {e}")


def upload():
    if (
        acc_no_entry.get() == "" or acc_name_entry.get() == "" or aadhar_entry.get() == "" or
        mobile_entry.get() == "" or ifsc_entry.get() == "" or branch_entry.get() == "" or
        trans_date_entry.get() == "" or trans_type_combo.get() == "" or mode_combo.get() == "" or
        amount_entry.get() == "" or balance_entry.get() == ""
    ):
        messagebox.showerror("Error", "Please fill all the fields")
    else:
        try:
            conn = pymysql.connect(host="localhost", user="root", password="Shreya@2709", database="bank")
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO banking (
                    acc_no, acc_name, aadhar, mobile, ifsc, branch,
                    trans_date, trans_type, mode, amount, balance
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                acc_no_entry.get(), acc_name_entry.get(), aadhar_entry.get(), mobile_entry.get(),
                ifsc_entry.get(), branch_entry.get(), trans_date_entry.get(), trans_type_combo.get(),
                mode_combo.get(), amount_entry.get(), balance_entry.get()
            ))
            conn.commit()
            conn.close()
            fetch_banking()  # Refresh Treeview or Text widget
            messagebox.showinfo("Success", "Transaction uploaded successfully")
        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")



def update_info():
    try:
        con = pymysql.connect(host="localhost", user="root", password="Shreya@2709", database="bank")
        cur = con.cursor()

        # Make sure the table name is correct: ministatement
        cur.execute("""
            UPDATE banking SET
                acc_name=%s, aadhar=%s, mobile=%s, ifsc=%s, branch=%s,
                trans_date=%s, trans_type=%s, mode=%s, amount=%s, balance=%s
            WHERE acc_no=%s
        """, (
            acc_name_entry.get(), aadhar_entry.get(), mobile_entry.get(), ifsc_entry.get(), branch_entry.get(),
            trans_date_entry.get(), trans_type_combo.get(), mode_combo.get(), amount_entry.get(), balance_entry.get(),
            acc_no_entry.get()
        ))

        con.commit()
        con.close()
        fetch_banking()  # Refresh Treeview or Text widget
        messagebox.showinfo("Updated", "Transaction updated successfully")

    except Exception as e:
        messagebox.showerror("Error", f"Update failed: {e}")



def generate_statement():
    acc_no = acc_no_entry.get()

    if acc_no == "":
        messagebox.showerror("Error", "Please enter Account Number")
        return

    try:
        conn = pymysql.connect(host="localhost", user="root", password="Shreya@2709", database="bank")
        cur = conn.cursor()
        cur.execute("""
            SELECT acc_no, acc_name, aadhar, mobile, ifsc, branch,
                   trans_date, trans_type, mode, amount, balance
            FROM banking WHERE acc_no=%s
        """, (acc_no,))
        rows = cur.fetchall()

        textaria.delete(1.0, END)

        if not rows:
            textaria.insert(END, "\nNo transactions found for this account.")
            return

        # Header
        textaria.insert(END, "\t\t*** State Bank of India ***\n")
        textaria.insert(END, f"\n Account Number   : {rows[0][0]}")
        textaria.insert(END, f"\n Account Holder   : {rows[0][1]}")
        textaria.insert(END, f"\n Mobile Number    : {rows[0][3]}")
        textaria.insert(END, f"\n Branch Name      : {rows[0][5]}")
        textaria.insert(END, f"\n IFSC CODE        : {rows[0][7]}")
        textaria.insert(END, "\n===============================================================================")
        textaria.insert(END, f"\n {'Date':<12} {'Type':<12} {'Mode':<12} {'Amount':>10} {'Balance':>12}")
        textaria.insert(END, "\n===============================================================================")

        # Transactions
        for row in rows:
            textaria.insert(END, f"\n\n {row[6]:<12} {row[7]:<12} {row[8]:<12} ₹{row[9]:>8} ₹{row[10]:>10}")

        textaria.insert(END, "\n\n===============================================================================")
        textaria.insert(END, "\n\t\t***Thank you for banking with us!***\n")

        conn.close()
    except Exception as e:
        messagebox.showerror("Database Error", f"Error due to: {e}")


def get_cursor(event):
    selected_row = student_table.focus()
    content = student_table.item(selected_row)
    row = content["values"]
    if row:
        acc_no.set(row[0])

        acc_name.set(row[1])

        aadhar.set( row[2])

        mobile.set( row[3])

        ifsc.set( row[4])

        branch.set( row[5])

        trans_date.set( row[6])

        trans_type.set(row[8])

        amount.set( row[9])

        balance.set(row[10])


def delete_all():
    try:
        con = pymysql.connect(host="localhost", user="root", password="Shreya@2709", database="bank")
        cur = con.cursor()
        cur.execute("DELETE FROM banking WHERE acc_no=%s", (acc_no_entry.get(),))
        con.commit()
        con.close()
        fetch_banking()  # Refresh Treeview or Text widget

        messagebox.showinfo("Deleted", "Transaction deleted successfully")
    except Exception as e:
        messagebox.showerror("Error", f"Delete failed: {e}")



def exit():
    skill.destroy()

def clear_all():
    acc_no.set("")
    acc_name.set("")
    aadhar.set("")
    mobile.set("")
    ifsc.set("")
    branch.set("")
    trans_date.set("")
    trans_type.set("")
    mode.set("")
    amount.set("")
    balance.set("")


Button(skill, text="UPLOAD", fg="black", bg="green", bd=3, font="arial 15 bold", height=1, width=20,command=upload).place(x=720, y=400)
Button(skill, text="UPDATE", fg="black", bg="#0073e6", bd=3, font="arial 15 bold", height=1, width=20,command=update_info ).place(x=720, y=460)
Button(skill, text="Mini statement", fg="black", bg="#117864", bd=3, font="arial 15 bold", height=1, width=20,command=generate_statement ).place(x=720, y=520)
Button(skill, text="DELETE", fg="black", bg="white", bd=3, font="arial 15 bold", height=1, width=20,command=delete_all ).place(x=720, y=580)
Button(skill, text="EXIT", fg="white", bg="red", bd=3, font="arial 15 bold", height=1, width=20 ,command=exit).place(x=720, y=630)
Button(skill, text="CLEAR", fg="black", bg="#f4a460", bd=3, font="arial 15 bold", height=1, width=20,command=clear_all ).place(x=720, y=690)


fetch_banking()
student_table.bind("<ButtonRelease-1>", get_cursor)



skill.mainloop()