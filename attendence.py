from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog



mydata=[]
class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # =======text variable
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendence=StringVar()
       


        # for images first
        img = Image.open(r"C:\Users\ARJUN RANA\OneDrive\Desktop\project_facerecognition\College_images\smart-attendance.png")
        img = img.resize((800,200),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)

        # for images second
        img1 = Image.open(r"C:\Users\ARJUN RANA\OneDrive\Desktop\project_facerecognition\College_images\z.jpg")
        img1 = img1.resize((800,200),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)

        # for  background images 
        img3 = Image.open(r"C:\Users\ARJUN RANA\OneDrive\Desktop\project_facerecognition\College_images\studentbg.jpg")
        img3 = img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img =Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_lbl = Label(bg_img,text="ATTENDENCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1510,height=600)

        # left side label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendence Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=580)

        img_left = Image.open(r"C:\Users\ARJUN RANA\OneDrive\Desktop\project_facerecognition\College_images\y.png")
        img_left = img_left.resize((720,90),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=5,y=135,width=720,height=370)

        # Labels and entry
        # attendence id
        attendenceId_lbl=Label(left_inside_frame,text=" Attendence ID :",font=("times new roman",12,"bold"),bg="white")
        attendenceId_lbl.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendenceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
        attendenceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

         # Roll
        rollLabel=Label(left_inside_frame,text=" Roll :",bg="white",font="comicsansns 11 bold")
        rollLabel.grid(row=0,column=2,padx=4,pady=8,sticky=W)

        atten_roll=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_roll,font="comicsansns 11 bold")
        atten_roll.grid(row=0,column=3,padx=10,pady=8,sticky=W)

        # Name
        nameLabel=Label(left_inside_frame,text=" Name :",bg="white",font="comicsansns 11 bold")
        nameLabel.grid(row=1,column=0,padx=4,pady=8,sticky=W)

        atten_name=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_name,font="comicsansns 11 bold")
        atten_name.grid(row=1,column=1,padx=10,pady=8,sticky=W)

        # Department
        depLabel=Label(left_inside_frame,text=" Department :",bg="white",font="comicsansns 11 bold")
        depLabel.grid(row=1,column=2,padx=4,pady=8,sticky=W)

        atten_dep=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_dep,font="comicsansns 11 bold")
        atten_dep.grid(row=1,column=3,padx=10,pady=8,sticky=W)

        # Time
        timeLabel=Label(left_inside_frame,text=" Time :",bg="white",font="comicsansns 11 bold")
        timeLabel.grid(row=2,column=0,padx=4,pady=8,sticky=W)

        atten_time=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_time,font="comicsansns 11 bold")
        atten_time.grid(row=2,column=1,padx=10,pady=8,sticky=W)

        # Time
        timeLabel=Label(left_inside_frame,text=" Time :",bg="white",font="comicsansns 11 bold")
        timeLabel.grid(row=2,column=0,padx=4,pady=8,sticky=W)

        atten_time=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_time,font="comicsansns 11 bold")
        atten_time.grid(row=2,column=1,padx=10,pady=8,sticky=W)

        # Date
        dateLabel=Label(left_inside_frame,text=" Date :",bg="white",font="comicsansns 11 bold")
        dateLabel.grid(row=2,column=2,padx=4,pady=8,sticky=W)

        atten_date=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_date,font="comicsansns 11 bold")
        atten_date.grid(row=2,column=3,padx=10,pady=8,sticky=W)

        # attendence
        attendenceLabel=Label(left_inside_frame,text="Attendence Status :",bg="white",font="comicsansns 11 bold")
        attendenceLabel.grid(row=3,column=0,padx=4,pady=8,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendence,font="comicsansns 11 bold")
        self.atten_status["values"]=("Select","Persent","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        # button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)

        # save button
        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        # update button
        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        # delete button
        delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        # Reset button
        reset_btn=Button(btn_frame,text="Reset",width=17,command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        # Right side label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendence Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=710,height=580)

        # button frame
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=695,height=455)

        # ==============Sxroll bar and table==========
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendenceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)
        
        self.AttendenceReportTable.heading("id",text="Attendence ID")
        self.AttendenceReportTable.heading("roll",text="Roll")
        self.AttendenceReportTable.heading("name",text="Name")
        self.AttendenceReportTable.heading("department",text="Department")
        self.AttendenceReportTable.heading("time",text="Time")
        self.AttendenceReportTable.heading("date",text="Date")
        self.AttendenceReportTable.heading("attendence",text="Attendence")

        self.AttendenceReportTable["show"]="headings"
        self.AttendenceReportTable.column("id",width=100)
        self.AttendenceReportTable.column("roll",width=100)
        self.AttendenceReportTable.column("name",width=100)
        self.AttendenceReportTable.column("department",width=100)
        self.AttendenceReportTable.column("time",width=100)
        self.AttendenceReportTable.column("date",width=100)
        self.AttendenceReportTable.column("attendence",width=100)


        self.AttendenceReportTable.pack(fill=BOTH,expand=1)

        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)

    # ===============fetch data
    def fetchData(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)

# ======import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)


    # ============export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to be"+os.path.basename(fln)+"Successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


            # ==========get cursor
    def get_cursor(self,event=""):
        cursor_row=self.AttendenceReportTable.focus()
        content=self.AttendenceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendence.set(rows[6])


    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendence.set("")







            
















if __name__ == "__main__":
    root = Tk()
    obj = Attendence(root)
    root.mainloop()