from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
from time import strptime
from datetime import datetime, date


class Carbooking:
    def __init__(self, root):
        self.root = root
        self.root.title("SPD MOTORS CUSTOMERS")
        self.root.geometry("1295x570+230+220")

#   ==================Variable ========================
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_cartype = StringVar()
        self.var_caravail = StringVar()
        self.var_oil = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_subtotal = StringVar()
        self.var_total = StringVar()

#   ===============================Title===============================
        lbl_title = Label(self.root, text="DONOR DATA ", font=("Times new roman", 18, "bold"), bg="red3", fg="sea green1", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

#   ===============================logo===============================
        img2 = Image.open("logo.png")
        img2 = img2.resize((100, 45), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=3, width=100, height=45)

#   =============================lable=============================
        lableframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="BLOOD DONATION", padx=2, font=("Times new roman", 12, "bold"))
        lableframeleft.place(x=5, y=50, width=425, height=490)

#   ======================Fetch data Button==================================
        btnfetch = Button(lableframeleft, command=self.Fetch_contact, text="Fetch Data", font=("arial", 8, "bold"), bg="green yellow", fg="black", bd=0, cursor="hand1", width=8)
        btnfetch.place(x=300, y=4)

        # Patient
        lbl_cust_contact = Label(lableframeleft, text="PATIENT DATA",  font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)
        entry_contact = ttk.Entry(lableframeleft, textvariable=self.var_contact, width=17, font=("arial", 13, "bold"))
        entry_contact.grid(row=0, column=1, sticky=W)

        # Admit Date
        check_in_date = Label(lableframeleft, text="Admit Date", font=("arial", 12, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)
        txtcheck_in = ttk.Entry(lableframeleft, textvariable=self.var_checkin, width=22, font=("arial", 13, "bold"))
        txtcheck_in.grid(row=1, column=1)

        # Discharge Date
        check_out_date = Label(lableframeleft, text="Discharge Date", font=("arial", 12, "bold"), padx=2, pady=6)
        check_out_date.grid(row=2, column=0, sticky=W)
        txtcheck_out = ttk.Entry(lableframeleft, textvariable=self.var_checkout, width=22, font=("arial", 13, "bold"))
        txtcheck_out.grid(row=2, column=1)

        # Blood Group
        lbl_cartype = Label(lableframeleft, fg="orange red2", text="Blood Group", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cartype.grid(row=3, column=0, sticky=W)

        combo_cartype = ttk.Combobox(lableframeleft, textvariable=self.var_cartype, font=("arial", 12, "bold"), width=20)
        combo_cartype["value"]=("O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-")
        combo_cartype.current(0)
        combo_cartype.grid(row=3, column=1)

        # Bed Number
        lblcaravailable = Label(lableframeleft, text="Bed Number",
                                font=("arial", 12, "bold"), padx=2, pady=6)
        lblcaravailable.grid(row=4, column=0, sticky=W)
        txtcaravailable = ttk.Entry(lableframeleft, textvariable=self.var_caravail,  width=22, font=("arial", 13, "bold"))
        txtcaravailable.grid(row=4, column=1)

        # Food
        lbl_oil = Label(lableframeleft, text="Food", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_oil.grid(row=5, column=0, sticky=W)
        txt_oil = ttk.Entry(lableframeleft, textvariable=self.var_oil, width=22, font=("arial", 13, "bold"))
        txt_oil.grid(row=5, column=1)

        # No of Days
        lblnoofdays = Label(lableframeleft, text="Total Time", font=("arial", 12, "bold"), padx=2, pady=6)
        lblnoofdays.grid(row=6, column=0, sticky=W)
        txtnoofdays = ttk.Entry(lableframeleft, textvariable=self.var_noofdays, width=22, font=("arial", 13, "bold"))
        txtnoofdays.grid(row=6, column=1)

#   =================================Right Side Image=================================================
        img3 = Image.open("right.jpg")
        img3 = img3.resize((520, 200), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg.place(x=760, y=55, width=520, height=200)

#   =================================Buttons==================================================

        btn_frame = Frame(lableframeleft, bd=0, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=420, height=40)

        addbtn = Button(btn_frame, text="ADD", command=self.add_data, font=("arial", 12, "bold"), bg="black", fg="light slate blue", bd=0, cursor="hand1",  width=10)
        addbtn.grid(row=0, column=0, padx=1)

        updatebtn = Button(btn_frame, command=self.update, text="UPDATE", font=("arial", 12, "bold"), bg="black", fg="light slate blue", bd=0, cursor="hand1",  width=10)
        updatebtn.grid(row=0, column=1, padx=1)

        deletebtn = Button(btn_frame, command=self.mdelete, text="DELETE", font=("arial", 12, "bold"), bg="black", fg="light slate blue", bd=0, cursor="hand1",  width=10)
        deletebtn.grid(row=0, column=2, padx=1)

        resetbtn = Button(btn_frame, command=self.reset, text="RESET",  font=("arial", 12, "bold"), bg="black", fg="light slate blue", bd=0, cursor="hand1", width=10)
        resetbtn.grid(row=0, column=3, padx=1)

#   ==================================TableFrame==================================================

        tb_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Details & Search System", padx=2,font=("Times new roman", 12, "bold"))
        tb_frame.place(x=435, y=280, width=860, height=260)

        lbl_search = Label(tb_frame, text="SEARCH BY", font=("arial", 12, "bold"), bg="green", fg="yellow")
        lbl_search.grid(row=0, column=0, sticky=W, padx=1)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(tb_frame, textvariable=self.search_var, font=("arial", 12, "bold"), width=20,state="readonly")
        combo_search["value"] = ("contact", "Bed number")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=1)

        self.txt_search = StringVar()
        entry_search = ttk.Entry(tb_frame, textvariable=self.txt_search, width=20, font=("arial", 13, "bold"))
        entry_search.grid(row=0, column=2, padx=1)

        searchbtn = Button(tb_frame, text="SEARCH", font=("arial", 12, "bold"), bg="black",
                           fg="grey", bd=0, cursor="hand1", width=10)
        searchbtn.grid(row=0, column=3, padx=1)

        showbtn = Button(tb_frame, text="SHOW", font=("arial", 12, "bold"), bg="black",
                         fg="grey", bd=0, cursor="hand1",  width=10)
        showbtn.grid(row=0, column=4, padx=1)

#   ========================== show data table ==========================

        table_frame = Frame(tb_frame, bd=2, relief=RIDGE)
        table_frame.place(x=0, y=50, width=860, height=180)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.car_table = ttk.Treeview(table_frame, column=("contact", "check in", "check out", "car type", "car avail", "oil", "no of days"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.car_table.xview)
        scroll_y.config(command=self.car_table.yview)

        self.car_table.heading("contact", text="contact")
        self.car_table.heading("check in", text="Admit Date")
        self.car_table.heading("check out", text="Discharge Date")
        self.car_table.heading("car type", text="Blood Group")
        self.car_table.heading("car avail", text="Bed Number")
        self.car_table.heading("oil", text="Food Number")
        self.car_table.heading("no of days", text="Total Time")

        self.car_table["show"] = "headings"

        self.car_table.column("contact", width=100)
        self.car_table.column("check in", width=100)
        self.car_table.column("check out", width=100)
        self.car_table.column("car type", width=100)
        self.car_table.column("car avail", width=90)
        self.car_table.column("oil", width=100)
        self.car_table.column("no of days", width=100)
        self.car_table.pack(fill=BOTH, expand=1)
        self.car_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    #ADD DATA
    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror("error", "All fields required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="omk@rd@w@le9", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into car values (%s,%s,%s,%s,%s,%s,%s)", (
                                                                                                self.var_contact.get(),
                                                                                                self.var_checkin.get(),
                                                                                                self.var_checkout.get(),
                                                                                                self.var_cartype.get(),
                                                                                                self.var_caravail.get(),
                                                                                                self.var_oil.get(),
                                                                                                self.var_noofdays.get()
                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("sucess", "Appointment Book", parent=self.root)
            except Exception as es:
                messagebox.showinfo("Warning", f"Something went wrong{str(es)}", parent=self.root)

    #FETCH DATA

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="omk@rd@w@le9",database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from car")
        rows = my_cursor.fetchall()
        if len(rows)!= 0:
            self.car_table.delete(*self.car_table.get_children())
            for i in rows:
                self.car_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row=self.car_table.focus()
        content=self.car_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_cartype.set(row[3])
        self.var_caravail.set(row[4])
        self.var_oil.set(row[5])
        self.var_noofdays.set(row[6])

    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("error", "Please Enter mobile Number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="omk@rd@w@le9",
                                           database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("update car set check_in=%s,check_out=%s, cartype=%s, caravail=%s,oil=%s, noofday=%s where contact=%s",
                                                                                            (
                                                                                                self.var_checkin.get(),
                                                                                                self.var_checkout.get(),
                                                                                                self.var_cartype.get(),
                                                                                                self.var_caravail.get(),
                                                                                                self.var_oil.get(),
                                                                                                self.var_noofdays.get(),
                                                                                                self.var_contact.get()
                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Car details has been updated successfully", parent=self.root)

    def mdelete(self):
        mdelete = messagebox.askyesno("BLOOD DONATION", "Do You Want Delete This Patient From Data", parent=self.root)
        if mdelete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="omk@rd@w@le9", database="management")
            my_cursor = conn.cursor()
            query = "delete from car where contact=%s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
        else:
            if not mdelete:
                return mdelete

        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_cartype.set("")
        self.var_caravail.set("")
        self.var_oil.set("")
        self.var_noofdays.set("")

#    =================================All Data Fetch=================================

    def Fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please Enter Patient Number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="omk@rd@w@le9", database="management")
            my_cursor = conn.cursor()
            query =("select Name from customer where mobile=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "This number not found", parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataframe.place(x=450, y=55, width=300, height=180)

                lblname = Label(showDataframe, text="Name", font=("arial", 12, "bold"))
                lblname.place(x=0, y=0)

                lbl = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90,y=0)

                # Gender
                conn = mysql.connector.connect(host="localhost", username="root", password="omk@rd@w@le9", database="management")
                my_cursor = conn.cursor()
                query = ("select Gender from customer where mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblgender = Label(showDataframe, text="Gender", font=("arial", 12, "bold"))
                lblgender.place(x=0, y=30)

                lbl2 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl2.place(x=90, y=30)

                # Mail
                conn = mysql.connector.connect(host="localhost", username="root", password="omk@rd@w@le9", database="management")
                my_cursor = conn.cursor()
                query = ("select Email from customer where mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblemail = Label(showDataframe, text="Email", font=("arial", 12, "bold"))
                lblemail.place(x=0, y=60)

                lbl3 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl3.place(x=90, y=60)

                # State
                conn = mysql.connector.connect(host="localhost", username="root", password="omk@rd@w@le9", database="management")
                my_cursor = conn.cursor()
                query = ("select Nation from customer where mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblNation = Label(showDataframe, text="Nation", font=("arial", 12, "bold"))
                lblNation.place(x=0, y=90)

                lbl4 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl4.place(x=90, y=90)

                # Address
                conn = mysql.connector.connect(host="localhost", username="root", password="omk@rd@w@le9", database="management")
                my_cursor = conn.cursor()
                query = ("select Address from customer where mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblAddress = Label(showDataframe, text="Address", font=("arial", 12, "bold"))
                lblAddress.place(x=0, y=120)

                lbl5 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl5.place(x=90, y=120)

    def total(self):
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()
        inDate = datetime.strptime(inDate, "%d/%m/%y")
        outDate = datetime.strptime(outDate, "%d/%m/%y")
        self.var_noofdays.set(abs(outDate-inDate).days)


if __name__ == '__main__':
    root = Tk()
    obj = Carbooking(root)
    root.mainloop()
