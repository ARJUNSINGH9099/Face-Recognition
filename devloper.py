from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os




class Devloper:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text="DEVLOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top= Image.open(r"C:\Users\ARJUN RANA\OneDrive\Desktop\project_facerecognition\College_images\j.png")
        img_top= img_top.resize((1530,720),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        # frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1120,y=240,width=390,height=450)

        img_top1= Image.open(r"C:\Users\ARJUN RANA\OneDrive\Desktop\project_facerecognition\College_images\arjun.jpg")
        img_top1= img_top1.resize((200,220),Image.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=150,y=0,width=280,height=208)

        # devloper info

        dev_lbl=Label(main_frame,text="Hii!! I'm Arjun Singh.",font=("times new roman",12,"bold"),bg="white")
        dev_lbl.place(x=0,y=5)

        dev_label=Label(main_frame,text="I'm Python devloper.",font=("times new roman",12,"bold"),bg="white")
        dev_label.place(x=0,y=40)

        dev_label1=Label(main_frame,text="Qualification:B.Sc(PCM),\nMCA(AI & DS)",font=("times new roman",12,"bold"),bg="white")
        dev_label1.place(x=0,y=80)

        img2= Image.open(r"C:\Users\ARJUN RANA\OneDrive\Desktop\project_facerecognition\College_images\dev1.jpeg")
        img2= img2.resize((500,300),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)


        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=200,width=500,height=300)









if __name__ == "__main__":
    root = Tk()
    obj = Devloper(root)
    root.mainloop()
