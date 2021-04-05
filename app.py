from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_win
from patientdata import Carbooking
from Details import Detail



class SPDMOTORS:
    def __init__(self,root):
        self.root = root
        self.root.title("BLOOD DONOATE")
        self.root.geometry("1550x800+0+0")

#   ================================img1================================
        img1 = Image.open("b.jpg")
        img1 = img1.resize((1450, 150), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=115, y=0, width=1550, height=140)

#   ================================Logo================================
        img2 = Image.open("logo.png")
        img2 = img2.resize((250, 150), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)

#   ================================Title================================
        lbl_title = Label(self.root, text="BLOOD DONATION SYSTEM", font=("Times new roman", 40, "bold"),bg="thistle1", fg="indianred1", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

#   ================================Main frame================================
        Main_frame = Frame(self.root, bd=4, relief=RIDGE)
        Main_frame.place(x=0, y=190, width=1550, height=620)

#   ================================Menu================================
        lbl_Menu = Label(Main_frame, text="Menu", font=("Times new roman", 20, "bold"), bg="khaki1", fg="coral", bd=4,relief=RIDGE)
        lbl_Menu.place(x=0, y=0, width=228)

#   ==================Main frame========================
        btn_frame = Frame(Main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        member_btn = Button(btn_frame, text="MEMBER", command=self.cust_details,  width=22, font=("Times new roman", 14, "bold"), bg="pale green", fg="salmon", bd=0, cursor="hand1")
        member_btn.grid(row=0, column=0, pady=1)

        member_data_btn = Button(btn_frame, text="PATIENT DATA", command=self.car_book, width=22, font=("Times new roman", 14, "bold"), bg="pale green", fg="salmon", bd=0, cursor="hand1")
        member_data_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="DETAILS", command=self.detail, width=22, font=("Times new roman", 14, "bold"), bg="pale green", fg="salmon", bd=0, cursor="hand1")
        details_btn.grid(row=2,column=0, pady=1)

#   ================================Right side img================================

        img3 = Image.open("right main.jpg")
        img3 = img3.resize((1310, 590), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(Main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1310, height=610)

#   ==================down side img ========================

        img4 = Image.open("3.jpg")
        img4 = img4.resize((230, 450), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lblimg1 = Label(Main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=150, width=228, height=460)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.apps = Cust_win(self.new_window)

    def car_book(self):
        self.new_window = Toplevel(self.root)
        self.apps = Carbooking(self.new_window)

    def detail(self):
        self.new_window = Toplevel(self.root)
        self.apps = Detail(self.new_window)


if __name__ =="__main__":
    root = Tk()
    obj = SPDMOTORS(root)
    root.mainloop()
