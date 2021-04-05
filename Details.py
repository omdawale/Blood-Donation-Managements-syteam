from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Detail:
    def __init__(self, root):
        self.root = root
        self.root.title("BLOOD DONOR DETAIL")
        self.root.geometry("1295x570+230+230")


#    ==========================================Title==========================================
        lbl_title = Label(self.root, text="DETAILS", font=("Times new roman", 18, "bold"), bg="blanched almond", fg="red4", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

#   ================================Main frame================================
        Main_frame = Frame(self.root, bd=4, relief=RIDGE)
        Main_frame.place(x=0, y=45, width=1550, height=620)

#   ================================Right side img================================

        img3 = Image.open("image.jpg")
        img3 = img3.resize((1295, 570), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(Main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=0, width=1295, height=550)

#   ================================Project Detail========================================



if __name__ =="__main__":
    root = Tk()
    obj = Detail(root)
    root.mainloop()