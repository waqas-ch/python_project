from tkinter import Tk, StringVar, ttk, messagebox, PhotoImage
from tkinter import *
import time
import datetime
import sqlite3

# -------------------------GUI----------------------------
"""Start by setting up a GUI"""


 # background color

# ------------------------Frames--------------------------
"""Make frames (Left and Right)"""
class attendence_register:
    def __init__(self, root,at_id,course_id):

         self.root=root
         self.root.title("Attendance Register")  # title of GUI
         self.root.geometry("1350x650+0+0")  # dimensions of GUI
         self.root.configure(background='black')
         self.attendence_id=at_id
         self.course_id=course_id
         print("VALUES ARE ")
         print(at_id,course_id)
         self.Error = StringVar()
         self.Error = "*"
         self.leftMayFrame = Frame(root, width=1000, height=650, bd=8, relief="raise")
         self.leftMayFrame.pack(side=LEFT)  # left frame
         self.rightMayFrame = Frame(root, width=350, height=650, bd=8, relief="raise")
         self.rightMayFrame.pack(side=RIGHT)  # right frame

         """Divide left frame into two"""
         self. leftMayFrame_1 = Frame(self.leftMayFrame, width=1000, height=100, bd=8, relief="raise")
         self. leftMayFrame_1.pack(side=TOP)  # top frame
         self. leftMayFrame_2 = Frame(self.leftMayFrame, width=1000, height=550, bd=8, relief="raise")
         self.leftMayFrame_2.pack(side=TOP)  # bottom frame

         """Divide right frame into two"""
         self.rightMayFrame_1 = Frame(self.rightMayFrame, width=350, height=215, bd=8, relief="raise")
         self. rightMayFrame_1.pack(side=TOP)  # top frame
         self. rightMayFrame_2 = Frame(self.rightMayFrame, width=350, height=415, bd=8, relief="raise")
         self.rightMayFrame_2.pack(side=TOP)  # bottom frame

         """ Container Containing Buttons """
         self. cont1 = Canvas(self.rightMayFrame_2, width=350, height=425, bg="black")
         self.b1 = Button(self.rightMayFrame_2,  width=170, height=70, bg='black',
                          command=self.fetch_next)
         self.stu = Label(self.rightMayFrame_2, text=" Fetch Next", font=('times 20 bold italic'), fg='white' ,bg='black')
         self.stu.place(x=80, y=10)
         self.okb1 = PhotoImage(file="pics\student.png")
         self.tmi = self.okb1.subsample(1, 1)
         self.b1.config(image=self.tmi)
         self.b1.place(x=80, y=60)
         self.b2 = Button(self.rightMayFrame_2, width=170, height=70, bg='black',
                          command=self.enter_records_button)
         self.stu1 = Label(self.rightMayFrame_2, text=" Enter Records", font=('times 20 bold italic'),fg='white' ,bg='black')
         self.stu1.place(x=80, y=150)
         self.okb2 = PhotoImage(file="pics\paybook.png")
         self.tmi1 = self.okb2.subsample(1, 1)
         self.b2.config(image=self.tmi1)
         self.b2.place(x=80, y=180)
         self.error = Label(self.rightMayFrame_2, text=self.Error, width=20, fg=("red"),bg='black', font=("bold italic", 14))
         self.error.place(x=50, y=315)

         self.cont1.grid(row=0, column=1)





         # ------------------------Variables-----------------------
         self. DateofOrder = StringVar()  # stores date
         """value0 would be used to store letter
         that can be applied to all others when fill button is pressed"""
         self. value0 = StringVar()
         """Value for each box would be stored in variables below"""

         self.value1 = StringVar()
         self.value2 = StringVar()
         self.value3 = StringVar()
         self.value4 = StringVar()
         self.value5 = StringVar()
         self.value6 = StringVar()
         self.value7 = StringVar()
         self.value8 = StringVar()
         self.value9 = StringVar()
         self.value10 = StringVar()
         self.value11 = StringVar()
         #A list containing attendence of  10 students
         self.att_list=[self.value0,self.value1,self. value2, self. value3,
         self.value4,
         self. value5,
         self.value6,
         self.value7,
         self.value8,
         self.value9,
         self.value10,
         self.value11,
          ]
         #list of combo box widgets name
         self.box = []
         self.x = IntVar()
         #if students are more than 10 remaining students stored here
         self.remaining_data = []
         # students id's are stored here
         self.students=[]


         # ----------------------Functions for exit and reset button--------
         """Shows photo of vu"""
         self.cont = Canvas(self.rightMayFrame_1, width=270, height=180, bg="black")
         self.cont.grid(row=0, column=0)
         self.imagePhoto = PhotoImage(file="pics/vu.png")
         self.cont.create_image(130, 90, image=self.imagePhoto)
         # =========================Components=========================

         self.DateofOrder.set(time.strftime("%d/%m/%y"))  # set date

       # ------------------------leftMayFrame_1 (left top frame)----------------------

      # Label Number
         self.lblNo = Label(self.leftMayFrame_1, font=('arial', 10, 'bold'), text="No.", bd=16)
         self.lblNo.grid(row=0, column=0, sticky=W)
         # Student Number
         self.lblStudentNo = Label(self.leftMayFrame_1, font=('arial', 10, 'bold'), text="Student No.", bd=16)
         self.lblStudentNo.grid(row=0, column=1, sticky=W)
         # Student Name
         self.lblStudentName = Label(self.leftMayFrame_1, font=('arial', 10, 'bold'), text="Student Name.", bd=16)
         self.lblStudentName.grid(row=0, column=2, sticky=W)
         # Course No.
         self.lblCourseCode = Label(self.leftMayFrame_1, font=('arial', 10, 'bold'), text="Course Code", bd=16)
         self.lblCourseCode.grid(row=0, column=3, sticky=W)

         """create box with various attendance options. If the user selects attendence
         option, all students will be marked with that option."""
         self.box = ttk.Combobox(self.leftMayFrame_1, textvariable=self.value0, state='readonly')
         self. box["values"] = [' ', '/', 'L', '0', 'A', 'B']  # attendance options
         self.box.current(0)
         self.box.grid(row=0, column=4)

         # add buttons: fill, reset, exit
         self.btnArrow = Button(self.leftMayFrame_1, text="Fill", padx=2, pady=2, bd=2, fg="black",
                           font=('arial', 10, 'bold'), width=12, height=1, command=self.fill_all_box).grid(row=0, column=5)
         self. btnReset = Button(self.leftMayFrame_1, text="Reset", padx=2, pady=2, bd=2, fg="black",
                           font=('arial', 10, 'bold'), width=12, height=1, command=self.Reset).grid(row=0, column=6)
         self.btnExit = Button(self.leftMayFrame_1, text="Exit", padx=2, pady=2, bd=2, fg="black",
                          font=('arial', 10, 'bold'), width=12, height=1, command=self.qExit).grid(row=0, column=7)

         # date of attendance
         self.lblDateofOrder = Label(self.leftMayFrame_1, font=('ariel', 10, 'bold'), textvariable=self.DateofOrder,
                                padx=2, pady=2, fg="black", bg="white", relief="sunken")
         self.lblDateofOrder.grid(row=0, column=8, sticky=W)

         self.startfetch()
    def add_student_to_register(self,name, number,  i):
       """Ths functions add student to the registe at row i. Parameters:
           name, number, email, mobile, row, box-variable, photo of student"""

       """ values = [self.value1,self.value1, self.value2, self.value3, self.value4, self.value5, self.value6, self.value7, self.value8,
                self.value9,
                self.value10, self.value11]"""


       # Label Numbers
       self.lblNo = Label(self.leftMayFrame_2, font=('arial', 10, 'bold'), text=str(i), bd=16)
       self.lblNo.grid(row=i, column=0, sticky=W)
       # Student Numbers
       self.lblStudent_No_1 =Label(self.leftMayFrame_2, font=('arial', 10, 'bold'), text=str(number), padx=2,
                               pady=2, bd=2, fg="Black", width=16)
       self.lblStudent_No_1.grid(row=i, column=1, sticky=W)
       # Student Names
       self.lblStudent_Name = Label(self.leftMayFrame_2, font=('arial', 10, 'bold'), text=name, padx=2,
                               pady=2, bd=2, fg="Black", width=12)
       self.lblStudent_Name.grid(row=i, column=2, sticky=W)
       # Course No.
       self.lblCourse_Code = Label(self.leftMayFrame_2, font=('arial', 10, 'bold'), text=self.course_id, padx=2,
                              pady=2, bd=2, fg="Black", width=12)
       self.lblCourse_Code.grid(row=i, column=3, sticky=W)
       box_name="box"+str(i)
       # create box with various attendance options. If the user selects attendence option, all students will be marked with that option.
       self.box = ttk.Combobox(self.leftMayFrame_2, text=self.att_list[i],name=box_name, state='readonly')
       self.box["values"] = [' ', '/', 'L', '0', 'A', 'B']
       self.box.current(0)
       self.box.bind("<<ComboboxSelected>>",self.on_select_item)
       self.box.grid(row=i, column=4)
       """
       list1=[' ', '/', 'L', '0', 'A', 'B']

       self.box = OptionMenu(self.leftMayFrame_2,self.att_list[i], *list1)
       self.box.config(width=15)
       #self.var.set('')

       self.box.grid(row=i, column=4)"""
       # add buttons
       self.btnSpace = Label(self.leftMayFrame_2, text='', padx=2, pady=2, bd=2, fg="black",
                        font=('arial', 10, 'bold'), width=23, height=1).grid(row=i, column=5)
       self.btnSpace = Label(self.leftMayFrame_2, text='', padx=2, pady=2, bd=2, fg="black",
                        font=('arial', 10, 'bold'), width=11, height=1).grid(row=i, column=6)
       self.btnSpace = Label(self.leftMayFrame_2, text="", padx=2, pady=2, bd=2, fg="black",
                        font=('arial', 10, 'bold'), width=11, height=1).grid(row=i, column=7)


    def fill_all_box(self):
       """When fill is pressed, all box would fill with value0"""
       store = self.value0.get()
       self.value0.set(store)
       self.value1.set(store)
       self.value2.set(store)
       self.value3.set(store)
       self.value4.set(store)
       self.value5.set(store)
       self.value6.set(store)
       self.value7.set(store)
       self.value8.set(store)
       self.value9.set(store)
       self.value10.set(store)
       store = self.value0.get()
       print("GOING TO PRINT THE LIST ",len(self.att_list))
       for row in range(len(self.att_list)):
          self.att_list[row]=store
       print(*self.att_list)

    def qExit(self):
       """Ask the user whether he/she wants to exit the GUI"""
       qExit = messagebox.askyesno("Exit System", "Do you want to quit?")
       if qExit > 0:
           self.root.destroy()
           return


    def Reset(self):
       """When reset is pressed, all values are reset"""
       self.value0.set("")
       self.value1.set("")
       self.value2.set("")
       self.value3.set("")
       self.value4.set("")
       self.value5.set("")
       self.value6.set("")
       self.value7.set("")
       self.value8.set("")
       self.value9.set("")
       self.value10.set("")
       self.value11.set("")
       print("GOING TO PRINT THE LIST ", len(self.att_list))
       for row in range(len(self.att_list)):
           self.att_list[row] = ""
       print(*self.att_list)
    def on_select_item(self,event):
        print(event.widget._name)


        if (event.widget._name=='box1'):
            #print("its is box 1 with value",event.widget.get())
            self.value1.set(event.widget.get())
            self.att_list[0] = event.widget.get()
            print("the thing is :",self.att_list[0])

        elif (event.widget._name=='box2') :
            self.value2.set(event.widget.get())
            self.att_list[1]=event.widget.get()
        elif (event.widget._name == 'box3'):
            self.value3.set(event.widget.get())
            self.att_list[2] = event.widget.get()

        elif (event.widget._name == 'box4'):
            self.value4.set(event.widget.get())
            self.att_list[3] = event.widget.get()


        elif (event.widget._name == 'box5'):
            self.value5.set(event.widget.get())
            self.att_list[4] = event.widget.get()

        elif (event.widget._name == 'box6'):
            self.value6.set(event.widget.get())
            self.att_list[5] = event.widget.get()

        elif (event.widget._name == 'box7'):
            self.value7.set(event.widget.get())
            self.att_list[6] = event.widget.get()

        elif (event.widget._name == 'box8'):
            self.value8.set(event.widget.get())
            self.att_list[7] = event.widget.get()

        elif (event.widget._name == 'box9'):
            self.value9.set(event.widget.get())
            self.att_list[8] = event.widget.get()

        elif (event.widget._name == 'box10'):
            self.value10.set(event.widget.get())
            self.att_list[9] = event.widget.get()

    def fetch_next(self):
       self.error['text'] = "*"
       if(len(self.remaining_data)>0):
           print("I AM IN NEXT")
           self.enter_records()
           self.clear_things()
           print("i am in next")
           x = 1
           remaining_data1 = []
           print(*self.remaining_data)
           for row in range(len(self.remaining_data)):
               # print("i am here")
               # print("value of x:", row)
               # print(self.remaining_data[row])
               # print(self.remaining_data[row][0])
               if (x > 10):
                   print("im in if > 10 :D")
                   remaining_data1.append(self.remaining_data[row])

               else:
                   print("i came in else x<= 10 ")
                   self.add_student_to_register(self.remaining_data[row][0], self.remaining_data[row][1], x)
                   self.students.append(self.remaining_data[row][1])
               x += 1
           if (x < 10):
               print("less than 10 remaining")
               print(*self.att_list)
           else:
               print("10 or more than 10")
               print(*remaining_data1)
               self.make_copy(remaining_data1)
       else:
           self.error['text']="*No more data to fetch"
    def make_copy(self,a):


      self.remaining_data= a.copy()
      print("copied Array ")
      print(*self.remaining_data)
    def clear_things(self):
        for widget in self.leftMayFrame_2.winfo_children():
            widget.destroy()
        self.Reset()
        self.students.clear()
    def enter_records_button(self):
        if (len(self.remaining_data) > 0):
            messagebox.showerror("Use Fetch Next Button")
        else:
             self.enter_records()
    def enter_records(self):
        self.error['text'] = "*"
        #self.update_student_array()
        #print(*values)
        print("GOING TO ENTER RECORDS")
        print(*self.students)
        conn = sqlite3.connect('CollegeDataBase1.db')
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF Not Exists "records1" (
                 "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	             "value"	TEXT,
	             "at_id"	INTEGER NOT NULL,
	            "student_id"	INTEGER NOT NULL,
	            FOREIGN KEY("student_id") REFERENCES "Student"("Email"),
	        FOREIGN KEY("at_id") REFERENCES "Attendence"("id")
                   );""")
        for row in range(len(self.students)):

             if (row<10):
                 cursor.execute('INSERT INTO records1 (value ,at_id,student_id) VALUES(?,?,?)',
                      (self.att_list[row], self.attendence_id, self.students[row]))
                 print(self.students[row],self.att_list[row])

        conn.commit()
        conn.close()
        if(len(self.students)<10):
            self.error['text'] = "Records Are Updated :) "

    def view_array(self):
        print("GOING TO PRINT THE values ")
        print(self.value0.get(),self.value1.get(),self.value2.get())
        print(*self.att_list)

    def startfetch(self):
       # variables stored in array to process them with ease
       course=self.course_id
       sqlite_select_query = """SELECT * FROM Student  JOIN Enrollment on(Email=en_student) Where en_course=?"""
       sqliteConnection = sqlite3.connect('CollegeDataBase1.db')
       x=1

       try:

         cursor = sqliteConnection.cursor()
         print("Connected to SQLite")

         cursor.execute(sqlite_select_query,(course,))
         records = cursor.fetchall()
         print("Total rows are:  ", len(records))
         print("Printing each row")

         for row in records:
             """


             print("value of n:",x)

             print("Id: ", row[1])
             print("Name: ", row[0])
             print("Gender: ", row[2])
             print("Semester: ", row[3])
             print("Fee: ", row[4])
             print("Attendence: ", row[5])
             print("\n")
             """
             if (x> 10):
               print("im in if :D")
               self.remaining_data.append(row)

             else:
                 print("i came in else buddy :D")
                 self.add_student_to_register(row[0], row[1], x)
                 self.students.append(row[1])

             x+=1
         cursor.close()
         print(x)
         print(*self.remaining_data)
         #print(self.remaining_data[0][0])
         print(len(self.remaining_data))
       except sqlite3.Error as error:
          print("Failed to read data from sqlite table", error)
       finally:
         if (sqliteConnection):
           sqliteConnection.close()
           print("The SQLite connection is closed")
"""root = Tk()
attendence_register(root,'1','2')
root.mainloop()"""
