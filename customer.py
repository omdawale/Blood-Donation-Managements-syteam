from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Cust_win:
    def __init__(self, root):
        self.root = root
        self.root.title("BLOOD DONOR DETAIL")
        self.root.geometry("1295x570+230+220")

#   ==================Variable ========================
        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_name = StringVar()
        self.var_gender = StringVar()
        self.var_surname = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_mail = StringVar()
        self.var_nation = StringVar()
        self.var_id = StringVar()
        self.var_idno = StringVar()
        self.var_address = StringVar()


#   ==================Title ========================
        lbl_title = Label(self.root, text="DONOR DETAILS", font=("Times new roman", 18, "bold"), bg="thistle1", fg="indianred1", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

#   ==================lable ========================
        lableframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="SPD MOTORS CUSTOMERS", padx=2,
                                    font=("Times new roman", 12, "bold"))
        lableframeleft.place(x=5, y=50, width=425, height=490)

#   ==================lables & entry ========================

        # DONOR REF
        lbl_cust_ref = Label(lableframeleft,  text="DONOR REF", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        entry_ref = ttk.Entry(lableframeleft, textvariable=self.var_ref, width=22, font=("arial", 13, "bold"),
                              state="readonly")
        entry_ref.grid(row=0, column=1)

        # NAME
        lbl_cust_nm = Label(lableframeleft, text="NAME", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_nm.grid(row=1, column=0, sticky=W)

        entry_nm = ttk.Entry(lableframeleft,  textvariable=self.var_name, width=22, font=("arial", 13, "bold"))
        entry_nm.grid(row=1, column=1)

        # SPD CUSTOMER SURNAME
        lbl_cust_surnm = Label(lableframeleft, text="SURNAME", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_surnm.grid(row=2, column=0, sticky=W)

        entry_surnm = ttk.Entry(lableframeleft, textvariable=self.var_surname, width=22, font=("arial", 13, "bold"))
        entry_surnm.grid(row=2, column=1)

        # SPD CUSTOMER GENDER
        lbl_cust_gnd = Label(lableframeleft, text="GENDER", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_gnd.grid(row=3, column=0, sticky=W)

        combo_gnd = ttk.Combobox(lableframeleft,  textvariable=self.var_gender, font=("arial", 12, "bold"), width=20,
                                 state="readonly")
        combo_gnd["value"] = ("Male", "Female", "Others")
        combo_gnd.current(0)
        combo_gnd.grid(row=3, column=1)

        # BLOOD GROUP
        lbl_cust_ptcode = Label(lableframeleft, text="BLOOD GROUP", fg="orange red2", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_ptcode.grid(row=4, column=0, sticky=W)

        entry_ptcode = ttk.Combobox(lableframeleft,  textvariable=self.var_post, width=20, font=("arial", 13, "bold"))
        entry_ptcode["value"] = ("O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-")
        entry_ptcode.current(0)
        entry_ptcode.grid(row=4, column=1)

        # SPD CUSTOMER CONTACT
        lbl_cust_cntc = Label(lableframeleft, text="CONTACT", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_cntc.grid(row=5, column=0, sticky=W)

        entry_cntc = ttk.Entry(lableframeleft, textvariable=self.var_mobile, width=22, font=("arial", 13, "bold"))
        entry_cntc.grid(row=5, column=1)

        # SPD CUSTOMER EMAIL
        lbl_cust_mail = Label(lableframeleft, text="MAIL", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_mail.grid(row=6, column=0, sticky=W)

        entry_mail = ttk.Entry(lableframeleft, textvariable =self.var_mail, width=22, font=("arial", 13, "bold"))
        entry_mail.grid(row=6, column=1)

        # SPD CUSTOMER NATION
        lbl_cust_ntn = Label(lableframeleft, text="State", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_ntn.grid(row=7, column=0, sticky=W)

        combo_nation = ttk.Combobox(lableframeleft, textvariable =self.var_nation, font=("arial", 12, "bold"), width=20,
                                    state="readonly")
        combo_nation["value"] = ("MAHARASHTRA", "GUJRAT", "MP", "UP", "KARNATKA", "DELHI", "PUNJAB", "J&K", "BIHAR", "BENGAL", "OTHERS")
        combo_nation.current(0)
        combo_nation.grid(row=7, column=1)

        # SPD CUSTOMER ID
        lbl_cust_id = Label(lableframeleft, text="ID", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_id.grid(row=8, column=0, sticky=W)

        combo_id = ttk.Combobox(lableframeleft, textvariable =self.var_id, font=("arial", 12, "bold"), width=20,
                                state="readonly")
        combo_id["value"] = ("DRIVING LICENCE", "PAN CARD", "PASSPORT", "AADHAR CARD")
        combo_id.current(0)
        combo_id.grid(row=8, column=1)

        # SPD CUSTOMER ID NUMBER
        lbl_cust_idno = Label(lableframeleft,  text="ID NUMBER", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_idno.grid(row=9, column=0, sticky=W)

        entry_idno = ttk.Entry(lableframeleft, textvariable =self.var_idno, width=22, font=("arial", 13, "bold"))
        entry_idno.grid(row=9, column=1)

        # SPD CUSTOMER ADDRESS
        lbl_cust_ads = Label(lableframeleft,  text="ADDRESS", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_ads.grid(row=10, column=0,  sticky=W)

        entry_ads = ttk.Entry(lableframeleft, textvariable =self.var_address, width=22, font=("arial", 13, "bold"))
        entry_ads.grid(row=10, column=1)


# =================================buttons==================================================

        btn_frame = Frame(lableframeleft, bd=0, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=420, height=40)

        addbtn = Button(btn_frame, text="ADD", command=self.add_data, font=("arial", 12, "bold"), bg="pale turquoise1", fg="dark orange", bd=0, cursor="hand1", width=10)
        addbtn.grid(row=0, column=0, padx=1)

        updatebtn = Button(btn_frame, text="UPDATE", command=self.update, font=("arial", 12, "bold"), bg="pale turquoise1", fg="dark orange", bd=0, cursor="hand1", width=10)
        updatebtn.grid(row=0, column=1, padx=1)

        deletebtn = Button(btn_frame, text="DELETE", command=self.mdelete, font=("arial", 12, "bold"), bg="pale turquoise1", fg="dark orange", bd=0, cursor="hand1", width=10)
        deletebtn.grid(row=0, column=2, padx=1)

        resetbtn = Button(btn_frame, text="RESET", command=self.reset, font=("arial", 12, "bold"), bg="pale turquoise1", fg="dark orange", bd=0, cursor="hand1", width=10)
        resetbtn.grid(row=0, column=3, padx=1)


#   ==================================TableFrame==================================================

        tb_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Details & Search System", padx=2,
                              font=("Times new roman", 12, "bold"))
        tb_frame.place(x=435, y=50, width=860, height=490)

        lbl_search = Label(tb_frame, text="SEARCH BY", font=("arial", 12, "bold"), bg="green", fg="yellow")
        lbl_search.grid(row=0, column=0, sticky=W, padx=1)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(tb_frame, textvariable=self.search_var, font=("arial", 12, "bold"), width=20,
                                    state="readonly")
        combo_search["value"] = ("customer", "mobile")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=1)

        self.txt_search = StringVar()
        entry_search = ttk.Entry(tb_frame, textvariable=self.txt_search, width=20, font=("arial", 13, "bold"))
        entry_search.grid(row=0, column=2, padx=1)

        searchbtn = Button(tb_frame, text="SEARCH", command=self.search, font=("arial", 12, "bold"), bg="black",
                           fg="grey", bd=0, cursor="hand1", width=10)
        searchbtn.grid(row=0, column=3, padx=1)

        showbtn = Button(tb_frame, text="SHOW", command=self.fetch_data, font=("arial", 12, "bold"), bg="black",
                         fg="grey", bd=0, cursor="hand1",  width=10)
        showbtn.grid(row=0, column=4, padx=1)


#   ========================== show data table ==========================

        table_frame = Frame(tb_frame, bd=2, relief=RIDGE)
        table_frame.place(x=0, y=50, width=860, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.cust_Details = ttk.Treeview(table_frame, column=("customer","name","gender","surname","post","mobile",
            "email", "nation", "id", "idnumber", "address"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.cust_Details.xview)
        scroll_y.config(command=self.cust_Details.yview)

        self.cust_Details.heading("customer", text="Donor")
        self.cust_Details.heading("name", text="Name")
        self.cust_Details.heading("gender", text=" Gender")
        self.cust_Details.heading("surname", text=" Surname")
        self.cust_Details.heading("post", text=" Blood Group")
        self.cust_Details.heading("mobile", text=" Mobile")
        self.cust_Details.heading("email", text=" Email")
        self.cust_Details.heading("nation", text=" Nation")
        self.cust_Details.heading("id", text="Id")
        self.cust_Details.heading("idnumber", text="Id Number")
        self.cust_Details.heading("address", text="Address")

        self.cust_Details["show"]="headings"

        self.cust_Details.column("customer",width=100)
        self.cust_Details.column("name",width=100)
        self.cust_Details.column("gender",width=100)
        self.cust_Details.column("surname",width=100)
        self.cust_Details.column("post",width=100)
        self.cust_Details.column("mobile",width=100)
        self.cust_Details.column("email",width=100)
        self.cust_Details.column("nation",width=100)
        self.cust_Details.column("id",width=100)
        self.cust_Details.column("idnumber",width=100)
        self.cust_Details.column("address",width=100)
        self.cust_Details.bind("<ButtonRelease-1>", self.get_cursor)
        self.cust_Details.pack(fill=BOTH, expand=1)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get() == "" or self.var_surname.get() == "":
            messagebox.showerror("error", "All fields required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="omk@rd@w@le9",
                                               database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                                                        (
                                                                            self.var_ref.get(),
                                                                            self.var_name.get(),
                                                                            self.var_gender.get(),
                                                                            self.var_surname.get(),
                                                                            self.var_post.get(),
                                                                            self.var_mobile.get(),
                                                                            self.var_mail.get(),
                                                                            self.var_nation.get(),
                                                                            self.var_id.get(),
                                                                            self.var_idno.get(),
                                                                            self.var_address.get(),
                                                                           ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success", "Customer has been Added", parent=self.root)
            except Exception as es:
                messagebox.showinfo("Warning", f"Something went wrong{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="omk@rd@w@le9", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        if len(rows)!= 0:
            self.cust_Details.delete(*self.cust_Details.get_children())
            for i in rows:
                self.cust_Details.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row=self.cust_Details.focus()
        content=self.cust_Details.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0])
        self.var_name.set(row[1])
        self.var_gender.set(row[2])
        self.var_surname.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_mail.set(row[6])
        self.var_nation.set(row[7])
        self.var_id.set(row[8])
        self.var_idno.set(row[9])
        self.var_address.set(row[10])

    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("error", "Please Enter mobile Number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="omk@rd@w@le9",
                                           database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("update customer set name=%s,gender=%s,surname=%s,post=%s,mobile=%s,email=%s,nation=%s,"
                              "id=%s,idnumber=%s,address=%s where customer=%s",(
                                                                                                self.var_name.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_surname.get(),
                                                                                                self.var_post.get(),
                                                                                                self.var_mobile.get(),
                                                                                                self.var_mail.get(),
                                                                                                self.var_nation.get(),
                                                                                                self.var_id.get(),
                                                                                                self.var_idno.get(),
                                                                                                self.var_address.get(),
                                                                                                self.var_ref.get()
                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Customer details has been updated succesfully", parent=self.root)

    def mdelete(self):
        mdelete = messagebox.askyesno("SPDMOTORS MANAGEMENT", "Do You Want Delete This Customer", parent=self.root)
        if mdelete > 0:
            cnx = mysql.connector.connect(host="localhost", username="root", password="omk@rd@w@le9", database="management")
            my_cursor = cnx.cursor()
            query = "delete from customer where customer=%s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query, value)
        else:
            if not mdelete:
                return mdelete

        cnx.commit()
        self.fetch_data()
        cnx.close()

    def reset(self):

        self.var_ref.set("")
        self.var_name.set("")
        self.var_gender.set("")
        self.var_surname.set("")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_mail.set("")
        self.var_nation.set("")
        self.var_id.set("")
        self.var_idno.set("")
        self.var_address.set("")
        x = random.randint(1000,9999);
        self.var_ref.set(str(x))

    def search(self):
        cnx = mysql.connector.connect(host="localhost", username="root", password="omk@rd@w@le9", database="management")
        my_cursor = cnx.cursor()
        my_cursor.execute("select * from customer where"
                          +str(self.search_var.get()) +" LIKE '%"+str(self.txt_search.get())+ "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.cust_Details.delete(*self.cust_Details.get_children())
            for i in rows:
                self.cust_Details.insert("", END, values=i)
            cnx.commit()
        cnx.close()


if __name__ == '__main__':
    root = Tk()
    obj = Cust_win(root)
    root.mainloop()
