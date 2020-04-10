from tkinter import *
import sqlite3
from tkinter import messagebox as box
from tkinter import ttk
from PIL import Image, ImageTk
import  student_attendence_management
from tkinter import simpledialog

# initializing variables for student data



class Stundent_panel:

    def __init__(self, tr1,username):

        self.tr1 = tr1
        self.tr1.title('Student page')
        self.username=username
        self.f = Canvas(tr1, bg='white', height=600, width=800)
        self.image11 = PhotoImage(file="pics/vu.png")
        self.f.create_image(0, 0, anchor=NW, image=self.image11)
        self.f.pack()

        self.h = Label(tr1, text="Department of Computer Science", font=('times 20 bold italic'), fg='steelblue')
        self.h.place(x=300, y=50)

        self.b1 = Button(tr1, text="LOGIN", font=('arial 15 bold'), width=120, height=70, bg='steelblue',
                         command=self.gotoStudents)
        self.stu = Label(tr1, text=" Manage Students", font=('times 20 bold italic'), fg='black')
        self.stu.place(x=380, y=200)

        self.okb1 = PhotoImage(file="pics\student.png")
        self.tmi = self.okb1.subsample(1, 1)
        self.b1.config(image=self.tmi)


        self.b1.place(x=200, y=200)

        self.b2 = Button(tr1, font=('arial 15 bold'), width=120, height=65, bg='steelblue',
                         command=self.attendence)
        self.stu1 = Label(tr1, text="Attendence Details ", font=('times 20 bold italic'), fg='black')
        self.stu1.place(x=380, y=300)

        self.okb2 = PhotoImage(file="pics\student.png")
        self.tmi1 = self.okb2.subsample(1, 1)
        self.b2.config(image=self.tmi1)
        self.b2.place(x=200, y=300)

        self.b3 = Button(tr1, font=('arial 15 bold'), width=120, height=65, bg='steelblue',
                         command=self.total_students)
        self.stu2 = Label(tr1, text="Total Students Details", font=('times 20 bold italic'), fg='black')
        self.stu2.place(x=380, y=400)

        self.okb3 = PhotoImage(file="pics\student.png")
        self.tmi2 = self.okb3.subsample(1, 1)
        self.b3.config(image=self.tmi2)
        self.b3.place(x=200, y=400)

        self.b4 = Button(tr1, text="FACULTY INFO", font=('arial 15 bold'), width=120, height=65, bg='steelblue', command=self.gotoStudents)
        self.stu3 = Label(tr1, text=" Result Card Generation", font=('times 20 bold italic'), fg='black')
        self.stu3.place(x=380, y=500)

        self.okb4 = PhotoImage(file="pics\student.png")
        self.tmi3 = self.okb4.subsample(1, 1)
        self.b4.config(image=self.tmi3)
        self.b4.place(x=200, y=500)

        self.b5 = Button(tr1, font=('arial 15 bold'), width=150, height=40, bg='black',
                         command=exit)

        self.okb5 = PhotoImage(file="pics\logout.png")
        self.tmi05 = self.okb5.subsample(1, 1)
        self.b5.config(image=self.tmi05)
        self.b5.place(x=0, y=200)
        tr1.resizable(False, False)
        tr1.mainloop()

    def attendence(self):
        hr = Toplevel()
        j = student_attendence_management.students_attendence(hr,"")

    def total_students(self):
        tm = Toplevel()
        k = no_of_students(tm)

    def fog(self):
        we = Toplevel()
        k = App2(we)
    def gotoStudents(self):
        answer = simpledialog.askstring("Input", "Which semester?",
                                        parent=self.tr1)
        print(answer)
        if(answer!=""):

             we = Toplevel()

             b = Manage_students(we,'cs',answer)

class Manage_students:

    def __init__(self,root,department,semester):
        self.username=department
        self.Fullname = StringVar()
        self. Email = StringVar()
        self.var = IntVar()
        self.c = StringVar()
        self.c.set(semester)
        self.c1 = StringVar()
        self.c1.set("")
        self. var1 = IntVar()
        self.attendence = StringVar()
        self.attendence.set(department)
        self.Error = StringVar()
        self. Error = "*"
        self.courses=['1', '2', '3', '4', '5', '6', '7', '8']
        self.search_Courses()
        self.root = root
        self.root.title('Student Management')
        self.fro1 = Canvas(root, bg='white', height=600, width=1200)

        self.image02 = PhotoImage(file="pics//vu.png")

        self.fro1.create_image(0, 0, anchor=NW, image=self.image02)

        self.fro1.pack()
        self.label_0 = Label(root, text="Student Management form", width=20, bg=("white"),fg=("steelblue"),font=('times 20 bold italic'))
        self.label_0.place(x=300, y=53)

        self.label_1 = Label(root, text="FullName", width=20, fg=("steelblue"),font=("times bold", 15))
        self.label_1.place(x=10, y=200)

        self.entry_1 = Entry(root, textvar=self.Fullname, width=30,fg=("black"),font=("times bold", 15) )
        self.entry_1.place(x=200, y=200)

        self.label_2 = Label(root, text="ID", width=20, fg=("steelblue"),font=("times bold", 15))
        self.label_2.place(x=10, y=230)
        self.entry_2 = Entry(root, textvar=self.Email, width=15,fg=("black"),font=("times bold", 15))
        self.entry_2.place(x=200, y=230)
        Button(root, text='Search', width=15, bg='black', fg='white', command=self.searchStudent).place(x=410, y=230)

        """self.label_3 = Label(root, text="Department", width=20, fg=("steelblue"),font=("times bold", 15))
        self.label_3.place(x=10, y=270)

        self.entry_3 = Entry(root, textvar=self.attendence,width=14,fg=("black"),font=("times bold", 15))
        self.entry_3.place(x=200, y=270)"""

        self.label_3 = Label(root, text="Gender", width=20, fg=("steelblue"),font=("times bold", 15))
        self.label_3.place(x=10, y=280)

        Radiobutton(root, text="Male", padx=5, variable=self.var, value=1).place(x=205, y=280)
        Radiobutton(root, text="Female", padx=20, variable=self.var, value=2).place(x=260, y=280)

        """"self.label_4 = Label(root, text="Semester", width=20, fg=("steelblue"),font=("times bold", 15))
        self.label_4
        self.box = ttk.Combobox(root, text=self.c, state='readonly')
        self.box["values"] = ['select semester','1', '2', '3', '4', '5', '6', '7', '8']
        self.box.current(0)
        self.box.bind("<<ComboboxSelected>>", self.on_select_semester)
        self.box.place(x=200, y=350)"""


        self.label_5 = Label(root, text="course", width=20, fg=("steelblue"), font=("times bold", 15))
        self.label_5.place(x=10, y=335)
        self.droplist2 = OptionMenu(root, self.c1, *self.courses)
        self.droplist2.config(width=15)
        self.c1.set('select course')
        self.droplist2.place(x=200, y=335)

        self.label_4 = Label(root, text="Fee", width=20, fg=("steelblue"),font=("times bold", 15))
        self.label_4.place(x=10, y=390)
        self.var2 = IntVar()
        # Checkbutton(root, text="java", variable=var1).place(x=235, y=330)

        # Checkbutton(root, text="python", variable=var2).place(x=290, y=330)
        Radiobutton(root, text="Paid", padx=5, variable=self.var1, value=1).place(x=200, y=390)
        Radiobutton(root, text="Unpaid", padx=20, variable=self.var1, value=2).place(x=260, y=390)
        self.error = Label(root, text=self.Error, width=20,fg=("red"), font=("bold italic", 14))
        self.error.place(x=300, y=165)

        self.a = Button(root, text="Register", width=130, height=50, bg='steelblue', command=self.database)
        self.stu1 = Label(root, text="Register", font=('times 18 bold italic'), fg='black')
        self.stu1.place(x=15, y=440)

        self.okb1 = PhotoImage(file="pics\ord.png")
        self.tmi = self.okb1.subsample(1, 1)
        self.a.config(image=self.tmi)
        self.a.place(x=0, y=480)
        self.a1 = Button(root, width=130, height=50, bg='red', command=self.deleteRow)
        self.stu1 = Label(root, text="Delete", font=('times 18 bold italic'), fg='black')
        self.stu1.place(x=160, y=440)

        self.okb2 = PhotoImage(file="pics\Delete.png")
        self.tm2 = self.okb2.subsample(1, 1)
        self.a1.config(image=self.tm2)
        self.a1.place(x=140, y=480)
        self.a2 = Button(root, width=130, height=50, bg='black', command=self.updateRow)
        self.stu2 = Label(root, text="Update", font=('times 18 bold italic'), fg='black')
        self.stu2.place(x=305, y=440)

        self.okb3 = PhotoImage(file="pics//update.png")
        self.tm3 = self.okb3.subsample(1, 1)
        self.a2.config(image=self.tm3)
        self.a2.place(x=280, y=480)
        self.a3 = Button(root, width=130, height=50, bg='white', command=self.resetAll)
        self.stu3 = Label(root, text="Reset", font=('times 18 bold italic'), fg='black')
        self.stu3.place(x=440, y=440)

        self.okb4 = PhotoImage(file="pics//restore.png")
        self.tm4 = self.okb4.subsample(1, 1)
        self.a3.config(image=self.tm4)
        self.a3.place(x=420, y=480)

        tbLabel =Label(root, text="Students Data", font=("Arial", 30))
        tbLabel.place(x=750,y=100)
        # create Treeview with  columns
        cols = ('ID', 'Name', 'Gender', 'Semester', 'Fee', 'Attendence')
        self.listBox = ttk.Treeview(root, columns=cols, show='headings' )
        self.listBox.place(x=600,y=200)
        # set column headings
        for col in cols:
            self.listBox.heading(col, text=col,)
            self.listBox.column(col, width=100)
        self.listBox.bind("<Double-1>", self.onclick)
        ttk.Style().configure("Treeview", font =('times bold italic',20), background="black",forground="red",fieldbackground="yellow"
                              ,rowheight=35 )




        self.fro1.pack()
        self.root.resizable(False, False)
        self.root.mainloop()

        # Method to update a Record
    def on_select_semester(self,event):
       self.c.set(event.widget.get())
       print(event.widget.get())
       self.search_Courses()
    def updateRow(self):
        self.error['text'] = "*"
        conn = sqlite3.connect('CollegeDataBase1.db')
        name1 = self.Fullname.get()
        email = self.Email.get()
        gender = self.var.get()
        semester = self.c.get()
        course = self.c1.get()
        fee =self.var1.get()
        att = self.attendence.get()


        if (email!="" and name1!="" and gender!="" and semester!="" and course!="" and fee!="" and att!="" ):
            # get the connection
            with conn:
                cur = conn.cursor()
                cur.execute(
                    """UPDATE Student
                                 SET Fullname = ? ,
                                     Gender= ? ,
                                     Semester = ?,
                                     Fee=?,
                                     Attendence=?
                                 WHERE Email = ? """,
                    (name1, gender, semester, fee, att, email))
                cur.execute(
                    """UPDATE Enrollment
                                 SET en_course = ? ,
                                     en_semester= ? 
                                    
                                 WHERE en_student = ? """,
                    (course,semester,email,))

                conn.commit()
                self.error['text'] = "*" + "Number of rows updated:"+ str(cur.rowcount)
                self.resetAll()
                self.searchStudent()
        else:
         self.error['text'] = "*"+"Empty Field"
        # method to search student
    def search_Courses(self,):
        print("I AM IN SEARCH COURSES")
        self.courses.clear()
        self.courses.append('')
        semester=self.c.get()
        department=self.attendence.get()
        sqlite_select_query =  """SELECT * from Courses WHERE semester=? and department=?"""
        try:
                sqliteConnection = sqlite3.connect('CollegeDataBase1.db')
                cursor = sqliteConnection.cursor()
                cursor.execute(sqlite_select_query, (semester,department,))

                records = cursor.fetchall()
                """ print("Total rows are:  ", len(records))
                print("Printing each row")"""
                for row in records:

                    print("Id: ", row[0])
                    print("Name: ", row[1])

                    print("Semester: ", row[2])
                    print("Faculty: ", row[3])

                    print("\n")
                    self.courses.append(row[0])

                cursor.close()

        except sqlite3.Error as error:
                self.error['text'] = "*" + "Failed to read courses"

        finally:
                if (sqliteConnection):
                    sqliteConnection.close()
                    print("The SQLite connection is closed")

    def searchStudent(self, ):
            bool = FALSE
            sqlite_select_query = StringVar()
            self.listBox.delete(*self.listBox.get_children())
            self.error['text'] = "*"
            email = self.Email.get()
            if (email != ""):
                sqlite_select_query = """SELECT * from Student WHERE Email =?"""
                bool = TRUE

            else:
                sqlite_select_query = """SELECT * from Student  """
            try:
                sqliteConnection = sqlite3.connect('CollegeDataBase1.db')
                cursor = sqliteConnection.cursor()
                print("Connected to SQLite")
                if (bool):
                    cursor.execute(sqlite_select_query, (email,))
                else:
                    cursor.execute(sqlite_select_query)
                records = cursor.fetchall()
                print("Total rows are:  ", len(records))
                print("Printing each row")
                for row in records:
                    """ print("Id: ", row[1])
                    print("Name: ", row[0])
                    print("Gender: ", row[2])
                    print("Semester: ", row[3])
                    print("Fee: ", row[4])
                    print("Attendence: ", row[5])
                    print("\n")"""
                    self.listBox.insert("", "end", values=(row[1], row[0], row[2], row[3], row[4], row[5]))
                cursor.close()

            except sqlite3.Error as error:
                self.Error.set("Failed to read data from sqlite table", error)
                self.error['text'] = "*" + Error
                print("Failed to read data from sqlite table", error)
            finally:
                if (sqliteConnection):
                    sqliteConnection.close()
                    print("The SQLite connection is closed")

        # DELETE ROW
    def deleteRow(self):

         self.error['text'] = "*"
         email = self.Email.get()
         print(email)
         if (email!="")   :
            con = sqlite3.connect('CollegeDataBase1.db')
            with con:
                # cur = con.cursor()
                sql = 'DELETE FROM Student WHERE Email=?'
                sql1='DELETE FROM Enrollment WHERE en_student=?'
                cur = con.cursor()
                cur.execute(sql, (email,))
                cur.execute(sql1, (email,))
                con.commit()
                # cur.execute("DELETE FROM Student WHERE ID = %s", email)
                self.entry_1.setvar("Deleted")

                self.error['text']="*"+"Number of rows deleted:"+ str(cur.rowcount)
                self.resetAll()
                self.searchStudent()
         else:
             self.error['text'] = "*"+"Field is Empty"

             # connectiong to database
    def database(self):

         name1 = self.Fullname.get()
         email = self.Email.get()
         gender = self.var.get()
         semester =self. c.get()
         course=self.c1.get()
         print("COURSE IS "+course)
         fee = self.var1.get()
         att = self.attendence.get()
         if (email != "" and name1 != "" and gender != "" and semester != "" and course != "" and fee != "" and att != ""):
            conn = sqlite3.connect('CollegeDataBase1.db')
            with conn:
                cursor = conn.cursor()
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,Semester TEXT,Fee TEXT, Attendence TEXT,PRIMARY KEY("Email"))')
            cursor.execute("""CREATE TABLE IF NOT EXISTS "Enrollment" (
	         "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	         "en_student"	INTEGER,
	         "en_course"	INTEGER,
	         "en_semester"	INTEGER,
	         FOREIGN KEY("en_course") REFERENCES "Courses1"("id"),
	         FOREIGN KEY("en_student") REFERENCES "Student"("Email")
	         
             );""")
            cursor.execute('INSERT INTO Student (FullName,Email,Gender,Semester,Fee,Attendence) VALUES(?,?,?,?,?,?)',
                           (name1, email, gender, semester, fee, att,))

            cursor.execute('INSERT INTO Enrollment (en_course,en_student,en_semester) VALUES(?,?,?)',
                           (course,email,semester))
            conn.commit()
            conn.close()
            self.listBox.insert("", "end", values=( email,name1, gender, semester, fee, att,))
         else:
            self.error['text']="* Error ! some Field is empty "
    # Reset all the input fields
    def resetAll(self):

        self.Fullname.set("")
        self.Email.set("")

        self.c.set("Select Semester")
        self.c1.set("Select Course")

        self.attendence.set("0")
# Method to fill all the fields on double click at tables row of record
    def onclick(self, event):
        item = self.listBox.item(self.listBox.selection())
        print("you clicked on", type(item), item, '\n')
        it = self.listBox.selection()[0]
        print('item clicked', it)
        get = self.listBox.item(it)
        print("values are:", get)
        row = get['values']
        print(row)
        self.Fullname.set(row[1])
        self.Email.set(row[0])
        self.var.set(row[2])
        self.c.set(row[3])
        self.var1.set(row[4])
        self.attendence.set(row[5])


class no_of_students:

    def __init__(self,root):
        self.total_stud = StringVar()
        self.Email = StringVar()
        self.var = IntVar()
        self. c = StringVar()
        self.root = root
        self.root.title('Total Students')
        self.fro1 = Canvas(root, bg='white', height=600, width=800)

        self.image02 = PhotoImage(file="pics//vu.png")

        self.fro1.create_image(0, 0, anchor=NW, image=self.image02)

        self.fro1.pack()
        self.label_0 = Label(root, text="Student Management form", width=20, bg=("white"),fg=("steelblue"),font=('times 20 bold italic'))
        self.label_0.place(x=300, y=53)


        self.label_2 = Label(root, text="ID", width=20, fg=("steelblue"),font=("times bold", 15))
        self.label_2.place(x=10, y=230)
        self.entry_2 = Entry(root, textvar=self.Email, width=15,fg=("black"),font=("times bold", 15))
        self.entry_2.place(x=200, y=230)
        self.a = Button(root, text="Register", width=130, height=50, bg='black', command=self.searchStudent)


        self.okb1 = PhotoImage(file="pics\ord.png")
        self.tmi = self.okb1.subsample(1, 1)
        self.a.config(image=self.tmi)
        self.a.place(x=400, y=230)




        self.label_4 = Label(root, text="Semester", width=20, fg=("steelblue"),font=("times bold", 15))
        self.label_4.place(x=10, y=350)

        list1 = ['1', '2', '3', '4', '5', '6', '7', '8'];

        self.droplist = OptionMenu(root, self.c, *list1)
        self.droplist.config(width=15)
        self.c.set("")
        self.droplist.place(x=200, y=350)

        self.label_2 = Label(root, text="No Of Students:", width=20, fg=("red"), font=("times bold", 15))
        self.label_2.place(x=10, y=470)
        self.entry_2 = Entry(root, textvar=self.total_stud, width=15, fg=("black"), font=("times bold", 15))
        self.entry_2.place(x=200, y=470)








        self.fro1.pack()
        self.root.resizable(False, False)
        self.root.mainloop()

        # Method to update a Record

    def searchStudent(self):
        bool=FALSE
        sqlite_select_query=StringVar()


        email = self.Email.get()
        course=self.c.get()

        if (course!=""):
            print("i am in if ;)  ")

            sqlite_select_query =  """SELECT * from Student WHERE Semester=?"""
            bool=TRUE

        else:
            print("i am in else ")
            sqlite_select_query = """SELECT * from Student  """
        try:
                sqliteConnection = sqlite3.connect('CollegeDataBase1.db')
                cursor = sqliteConnection.cursor()
                print("Connected to SQLite")
                if(bool):
                 cursor.execute(sqlite_select_query, (course,))
                else:
                 cursor.execute(sqlite_select_query)
                records = cursor.fetchall()

                print("Total rows are:  ", len(records))
                self.total_stud.set(str(len(records)))

                print("Printing each row")
                for row in records:

                    print("Id: ", row[1])
                    print("Name: ", row[0])
                    print("Gender: ", row[2])
                    print("Semester: ", row[3])
                    print("Fee: ", row[4])
                    print("Attendence: ", row[5])
                    print("\n")

                cursor.close()

        except sqlite3.Error as error:

                print("Failed to read data from sqlite table", error)
        finally:
                if (sqliteConnection):
                    sqliteConnection.close()
                    print("The SQLite connection is closed")
