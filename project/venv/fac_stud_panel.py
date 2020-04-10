from tkinter import *
import sqlite3
from tkinter import messagebox as box
from tkinter import ttk
from PIL import Image, ImageTk
import Attendence_sheet,student_attendence_management
# initializing variables for student data



class fac_student_panel:

    def __init__(self, tr1,name,dept_name,course_code):
        self.fac_name=name
        self.course_code=course_code
        self.dept_name=dept_name
        self.tr1 = tr1
        self.tr1.title('Faculty page')

        self.f = Canvas(tr1, bg='white', height=600, width=800)
        self.image11 = PhotoImage(file="pics/vu.png")
        self.f.create_image(0, 0, anchor=NW, image=self.image11)
        self.f.pack()

        self.h = Label(tr1, text="Department of "+self.dept_name, font=('times 20 bold italic'), fg='steelblue')
        self.h.place(x=300, y=50)
        self.h11 = Label(tr1, text="Wellcome :"+self.fac_name, font=('times 20 bold italic'), fg='purple')
        self.h11.place(x=300, y=100)

        self.b1 = Button(tr1, text="LOGIN", font=('arial 15 bold'), width=120, height=70, bg='steelblue',
                         command=self.gotoStudents)
        self.stu = Label(tr1, text=" Student Details", font=('times 20 bold italic'), fg='black')
        self.stu.place(x=380, y=200)

        self.okb1 = PhotoImage(file="pics\student.png")
        self.tmi = self.okb1.subsample(1, 1)
        self.b1.config(image=self.tmi)


        self.b1.place(x=200, y=200)

        self.b2 = Button(tr1, font=('arial 15 bold'), width=120, height=65, bg='steelblue',
                         command=self.attendence)
        self.stu1 = Label(tr1, text="Attendence Sheet ", font=('times 20 bold italic'), fg='black')
        self.stu1.place(x=380, y=300)

        self.okb2 = PhotoImage(file="pics\student.png")
        self.tmi1 = self.okb2.subsample(1, 1)
        self.b2.config(image=self.tmi1)
        self.b2.place(x=200, y=300)

        self.b3 = Button(tr1, font=('arial 15 bold'), width=120, height=65, bg='steelblue',
                         command=self.gotoStudents)
        self.stu2 = Label(tr1, text="Attendence Management", font=('times 20 bold italic'), fg='black')
        self.stu2.place(x=380, y=400)

        self.okb3 = PhotoImage(file="pics\student.png")
        self.tmi2 = self.okb3.subsample(1, 1)
        self.b3.config(image=self.tmi2)
        self.b3.place(x=200, y=400)

        self.b4 = Button(tr1, text="FACULTY INFO", font=('arial 15 bold'), width=120, height=65, bg='steelblue', command=self.logout)
        self.stu3 = Label(tr1, text=" Logout ", font=('times 20 bold italic'), fg='black')
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
        at_id = simpledialog.askstring("Input", "Enter Attendence Id?",
                                        parent=self.tr1)

        if (at_id != ""):

            # Establish Connection
            with sqlite3.connect('CollegeDataBase1.db') as db:
                c = db.cursor()

            # Find Existing username if any take proper action
            find_user = ('SELECT * FROM Attendence WHERE id= ?')
            #c.execute(find_user, (id,))
            c.execute(find_user, (at_id,))
            if c.fetchall():
                box.showinfo('Error!', 'already taken')
                we = Toplevel()
                j = Attendence_sheet.attendence_register(we, at_id, self.course_code)
            else:
                date = simpledialog.askstring("Input", "Enter Date?",
                                              parent=self.tr1)
                insert = 'INSERT INTO Attendence(id,Date,course_id) VALUES(?,?,?)'
                c.execute(insert, [at_id, date, self.course_code])
                db.commit()
                we = Toplevel()
                j = Attendence_sheet.attendence_register(we, at_id, self.course_code)





            # self.log()

    def total_students(self):
        tm = Toplevel()
        k = no_of_students(tm,self.course_code)


    def gotoStudents(self):
        we = Toplevel()
        b = student_attendence_management.students_attendence(we,self.course_code)
    def logout(self):
           print("logout")


class no_of_students:

    def __init__(self,root,course):
        self.course=course
        self.total_stud = StringVar()
        self.Email = StringVar()
        self.var = IntVar()
        self. c = StringVar()
        self.root = root
        self.root.title('Total Students')
        self.fro1 = Canvas(root, bg='white', height=600, width=1200)

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


        self.label_2 = Label(root, text="Total No of Students:", width=20, fg=("red"), font=("times bold", 15))
        self.label_2.place(x=10, y=410)
        self.entry_2 = Entry(root, textvar=self.total_stud, width=15, fg=("black"), font=("times bold", 15))
        self.entry_2.place(x=230, y=410)
        tbLabel = Label(root, text="Students Data", font=("Arial", 30))
        tbLabel.place(x=750, y=100)
        # create Treeview with  columns
        cols = ('ID', 'Name', 'Gender', 'Semester', 'Fee', 'Attendence')
        self.listBox = ttk.Treeview(root, columns=cols, show='headings')
        self.listBox.place(x=600, y=200)
        # set column headings
        for col in cols:
            self.listBox.heading(col, text=col, )
            self.listBox.column(col, width=100)
        #self.listBox.bind("<Double-1>", self.onclick)
        ttk.Style().configure("Treeview", font=('times bold italic', 20), background="black", forground="red",
                              fieldbackground="yellow"
                              , rowheight=35)

        self.fro1.pack()
        self.root.resizable(False, False)
        self.root.mainloop()

        # Method to update a Record

    def searchStudent(self):
        bool=FALSE
        sqlite_select_query=StringVar()
        self.listBox.delete(*self.listBox.get_children())

        email = self.Email.get()
        course=self.course

        if (email==""):
            print("i am in if ;)  ")

            sqlite_select_query =  """SELECT * FROM Student  JOIN Enrollment on(Email=en_student) Where en_course=?"""
            bool=TRUE

        else:
            print("i am in else ")
            sqlite_select_query = """SELECT * FROM Student  JOIN Enrollment on(Email=en_student) Where en_student=? and en_course=?"""
        try:
                sqliteConnection = sqlite3.connect('CollegeDataBase1.db')
                cursor = sqliteConnection.cursor()
                print("Connected to SQLite")
                if(bool):
                 cursor.execute(sqlite_select_query, (course,))
                else:
                 cursor.execute(sqlite_select_query,(email,course))
                records = cursor.fetchall()

                print("Total rows are:  ", len(records))
                if(bool):
                 self.total_stud.set(str(len(records)))

                print("Printing each row")
                for row in records:

                    print("Id: ", row[1])
                    print("Name: ", row[0])
                    print("Gender: ", row[2])
                    print("Semester: ", row[3])
                    print("Fee: ", row[4])
                    print("Attendence: ", row[5])
                    print("x: ", row[8])
                    print("\n")

                    self.listBox.insert("", "end", values=(row[1], row[0], row[2], row[3], row[4], row[5]))
                cursor.close()

        except sqlite3.Error as error:

                print("Failed to read data from sqlite table", error)
        finally:
                if (sqliteConnection):
                    sqliteConnection.close()
                    print("The SQLite connection is closed")
"""root = Tk()
fac_student_panel(root,"Waqas","Computer Science","1")
root.mainloop()"""