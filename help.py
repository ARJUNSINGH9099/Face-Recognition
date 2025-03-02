from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os




class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top= Image.open(r"C:\Users\ARJUN RANA\OneDrive\Desktop\project_facerecognition\College_images\HELP1.jpg")
        img_top= img_top.resize((1530,720),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        dev_lbl=Label(f_lbl,text="Email: Arjunrana9099@gmail.com",font=("times new roman",32,"bold"),fg="white",bg="Slategray3")
        dev_lbl.place(x=460,y=200)



if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()