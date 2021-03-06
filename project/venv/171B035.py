from tkinter import *
import sqlite3
from tkinter import messagebox as box
from tkinter import ttk
from PIL import Image, ImageTk
import  student_Panel,employee_panel


root = Tk()

root.title("Welcome")


# initializing variables for Faculty data
fac_name = StringVar()
fac_id = StringVar()
fac_gender = IntVar()
fac_dep = StringVar()
fac_course = StringVar()
attendence = IntVar()
fac_fee= IntVar()

fac_Error = StringVar()
fac_Error="*"

class Application:
    """docstring for ClassName"""

    def __init__(self, master1):
        self.master1 = master1
        '''
        self.f=Frame(master1,width=650,height=600, bg='lightgreen')
        self.f.pack()
        '''


        self.fro = Canvas(root, bg='white', height=700, width=1100)
        self.image1 = PhotoImage(file="pics\ezpz-logo2017.png")
        self.image02 = PhotoImage(file="pics//vu.png")

        self.fro.create_image(260, 200, anchor=NW, image=self.image1)
        self.fro.create_image(0, 0, anchor=NW, image=self.image02)

        self.fro.pack()



        self.h = Label(root, text="Welcome to Virtual University Gujarkhan", font=('times 20 bold italic'), fg='black')
        self.h1 = Label(root, text="Campus Management System", font=('times 20 bold italic'), fg='steelblue')

        self.h.place(x=300, y=10)
        self.h1.place(x=300, y=70)

        self.a = Button(root, width=150 , height=80 ,bg='steelblue', command=self.stu1)
        self.stu = Label(root, text="Student Panel", font=('times 20 bold italic'), fg='black')
        self.stu.place(x=180, y=220)
        self.okb1 = PhotoImage(file="pics\student.png")
        self.tmi = self.okb1.subsample(1, 1)
        self.a.config(image=self.tmi)
        self.a.place(x=0, y=210)


        self.a1 = Button(root, width=150 , height=80 ,bg='steelblue',command=self.fac)
        self.okb11 = PhotoImage(file="pics\student.png")
        self.tmi1 = self.okb11.subsample(1, 1)
        self.a1.config(image=self.tmi1)
        self.a1.place(x=0, y=400)
        self.tea = Label(root, text="Faculty Panel", font=('times 20 bold italic'), fg='black')
        self.tea.place(x=180, y=410)



        self.b2 = Button(root, font=('arial 15 bold'),width=150 , height=80, bg='steelblue',
                         command=self.employees)
        self.stu1 = Label(root, text=" Employee Panel ", font=('times 20 bold italic'), fg='black')
        self.stu1.place(x=680, y=220)
        self.okb2 = PhotoImage(file="pics\student.png")
        self.tmi01 = self.okb2.subsample(1, 1)
        self.b2.config(image=self.tmi01)
        self.b2.place(x=900, y=200)


        #initializing Exit Button

        self.b4 = Button(root, font=('arial 15 bold'),width=150 , height=40, bg='red',
                         command=exit)
        self.stu4 = Label(root, text=" Exit ", font=('times 20 bold italic'), fg='black')
        self.stu4.place(x=680, y=420)
        self.okb3 = PhotoImage(file="pics\logout.png")
        self.tm02 = self.okb3.subsample(1, 1)
        self.b4.config(image=self.tm02)
        self.b4.place(x=900, y=420)

    def fac(self):
        fac1 = Toplevel()
        o = Faculty_panel(fac1,FALSE)

    def stu1(self):
        tr1 = Toplevel()
        m = student_Panel.Stundent_panel(tr1)

    def employees(self):
        hr = Toplevel()
        k = employee_panel.Employee_panel(hr)

class Faculty_panel:

    def __init__(self, tr1,bool):
        self.tr1 = tr1

        self.tr1.title('Faculty page')

        self.f = Canvas(tr1, bg='white', height=600, width=800)
        self.image11 = PhotoImage(file="pics/vu.png")
        self.f.create_image(0, 0, anchor=NW, image=self.image11)
        self.f.pack()

        self.h = Label(tr1, text="Department of Computer Science", font=('times 20 bold italic'), fg='steelblue')
        self.h.place(x=300, y=50)


        self.b1 = Button(tr1,  font=('arial 15 bold'), width=120, height=70, bg='steelblue',
        command=self.faculty)
        self.stu = Label(tr1, text=" Manage Faculty", font=('times 20 bold italic'), fg='black')
        self.stu.place(x=380, y=200)
        self.okb1 = PhotoImage(file="pics\student.png")
        self.tmi = self.okb1.subsample(1, 1)
        self.b1.config(image=self.tmi)
        self.b1.place(x=200, y=200)

        self.b2 = Button(tr1, font=('arial 15 bold'), width=120, height=65, bg='steelblue',
        command=self.employees)
        self.stu1 = Label(tr1, text=" Manage Employees ", font=('times 20 bold italic'), fg='black')
        self.stu1.place(x=380, y=300)

        self.okb2 = PhotoImage(file="pics\student.png")
        self.tmi1 = self.okb2.subsample(1, 1)
        self.b2.config(image=self.tmi1)
        self.b2.place(x=200, y=300)

        self.b3 = Button(tr1, text="FORGOT PASSWORD", font=('arial 15 bold'), width=120, height=65, bg='steelblue',
                         command=self.noe)
        self.stu2 = Label(tr1, text="  Total Facululty details ", font=('times 20 bold italic'), fg='black')
        self.stu2.place(x=380, y=400)

        self.okb3 = PhotoImage(file="pics\student.png")
        self.tmi2 = self.okb3.subsample(1, 1)
        self.b3.config(image=self.tmi2)
        self.b3.place(x=200, y=400)

        self.b4 = Button(tr1, text="FACULTY INFO", font=('arial 15 bold'), width=120, height=65, bg='steelblue', command=self.attendence)
        self.stu3 = Label(tr1, text=" Faculty Attendence ", font=('times 20 bold italic'), fg='black')
        self.stu3.place(x=380, y=500)

        self.okb4 = PhotoImage(file="pics\student.png")
        self.tmi3 = self.okb4.subsample(1, 1)
        self.b4.config(image=self.tmi3)
        self.b4.place(x=200, y=500)

        self.b5 = Button(tr1, font=('arial 15 bold'),width=150 , height=40, bg='black',
                         command=exit)

        self.okb5 = PhotoImage(file="pics\logout.png")
        self.tmi05 = self.okb5.subsample(1, 1)
        self.b5.config(image=self.tmi05)
        self.b5.place(x=0, y=200)



        tr1.resizable(False, False)
        tr1.mainloop()

    def employees(self):
        hr = Toplevel()
        k = employee_panel(hr)


    def faculty(self):
        tm = Toplevel()
        k = Manage_Faculty(tm)

    def attendence(self):
        we = Toplevel()
        k = Manage_Faculty(we)

    def  noe(self):
        we = Toplevel()
        k = no_of_faculty(we)


class Manage_Faculty:

    def __init__(self,root):
        self.root = root
        self.root.title('Faculty Management')
        self.fro1 = Canvas(root, bg='white', height=600, width=1200)

        self.image02 = PhotoImage(file="pics//vu.png")

        self.fro1.create_image(0, 0, anchor=NW, image=self.image02)

        self.fro1.pack()
        self.label_0 = Label(root, text="Faculty Management form", width=20, bg=("white"),fg=("steelblue"),font=('times 20 bold italic'))
        self.label_0.place(x=300, y=53)

        self.label_1 = Label(root, text="Full Name", width=20, fg=("steelblue"),font=("times bold", 15))
        self.label_1.place(x=10, y=200)

        self.entry_1 = Entry(root, textvar=fac_name, width=30,fg=("black"),font=("times bold", 15) )
        self.entry_1.place(x=200, y=200)

        self.label_2 = Label(root, text="ID", width=20, fg=("steelblue"),font=("times bold", 15))
        self.label_2.place(x=10, y=230)
        self.entry_2 = Entry(root, textvar=fac_id, width=15,fg=("black"),font=("times bold", 15))
        self.entry_2.place(x=200, y=230)
        Button(root, text='Search', width=15, bg='black', fg='white', command=self.searchStudent).place(x=410, y=230)

        self.label_3 = Label(root, text="Department", width=20, fg=("steelblue"),font=("times bold", 15))
        self.label_3.place(x=10, y=270)

        self.entry_3 = Entry(root, textvar=fac_dep,width=14,fg=("black"),font=("times bold", 15))
        self.entry_3.place(x=200, y=270)

        self.label_3 = Label(root, text="Gender", width=20, fg=("steelblue"),font=("times bold", 15))
        self.label_3.place(x=10, y=310)

        Radiobutton(root, text="Male", padx=5, variable=fac_gender, value=1).place(x=205, y=310)
        Radiobutton(root, text="Female", padx=20, variable=fac_gender, value=2).place(x=260, y=310)

        self.label_4 = Label(root, text="Course", width=20, fg=("steelblue"),font=("times bold", 15))
        self.label_4.place(x=10, y=350)

        list1 = ['1', '2', '3', '4', '5', '6', '7', '8'];

        self.droplist = OptionMenu(root, fac_course, *list1)
        self.droplist.config(width=15)
        fac_course.set('select your Course')
        self.droplist.place(x=200, y=350)

        self.label_4 = Label(root, text="Fee", width=20, fg=("steelblue"),font=("times bold", 15))
        self.label_4.place(x=10, y=390)
        self.var2 = IntVar()
        # Checkbutton(root, text="java", variable=var1).place(x=235, y=330)

        # Checkbutton(root, text="python", variable=var2).place(x=290, y=330)
        Radiobutton(root, text="Paid", padx=5, variable=fac_fee, value=1).place(x=200, y=390)
        Radiobutton(root, text="Unpaid", padx=20, variable=fac_fee, value=2).place(x=260, y=390)
        self.error = Label(root, text=fac_Error, width=20,fg=("red"), font=("bold italic", 14))
        self.error.place(x=300, y=165)
        #initializing Buttons having icon
        self.a = Button(root, text="Register" , width=130, height=50, bg='steelblue', command=self.database)
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

        # initializing table to fetch data from database
        tbLabel =Label(root, text=" Faculty Data", font=("Arial", 30))
        tbLabel.place(x=750,y=100)
        # create Treeview with  columns
        cols = ('ID', 'Name', 'Gender', 'Course', 'Fee', 'Department')
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
    def updateRow(self):
        self.error['text'] = "*"
        conn = sqlite3.connect('CollegeDataBase1.db')
        name1 = fac_name.get()
        email = fac_id.get()
        gender = fac_gender.get()
        semester = fac_course.get()
        fee = var1.get()
        att = fac_dep.get()

        if (email != "" and name1 != "" and gender != "" and semester != "" and fee != "" and att != ""):
            # get the connection
            with conn:
                cur = conn.cursor()
                cur.execute(
                    """UPDATE Faculty
                                 SET Fullname = ? ,
                                     Gender= ? ,
                                     Semester = ?,
                                     Fee=?,
                                     Attendence=?
                                 WHERE Email = ? """,
                    (name1, gender, semester, fee, att, email))

                conn.commit()
                self.error['text'] = "*" + "Number of rows updated:" + str(cur.rowcount)
                print("Number of rows updated:", cur.rowcount)
        else:
         self.error['text'] = "*"+"Empty Field"
        # method to search student
    def searchStudent(self,):
        bool=FALSE
        sqlite_select_query=StringVar()
        self.listBox.delete(*self.listBox.get_children())
        self.error['text'] = "*"
        email = fac_id.get()
        if (email!=""):
            sqlite_select_query =  """SELECT * from Faculty WHERE Email =?"""
            bool=TRUE

        else:
            sqlite_select_query = """SELECT * from Faculty """
        try:
                sqliteConnection = sqlite3.connect('CollegeDataBase1.db')
                cursor = sqliteConnection.cursor()
                print("Connected to SQLite")
                if(bool):
                 cursor.execute(sqlite_select_query, (email,))
                else:
                 cursor.execute(sqlite_select_query)
                records = cursor.fetchall()
                print("Total rows are:  ", len(records))
                print("Printing each row")
                for row in records:

                    print("Id: ", row[1])
                    print("Name: ", row[0])
                    print("Gender: ", row[2])
                    print("Course: ", row[3])
                    print("Fee: ", row[4])
                    print("Attendence: ", row[5])
                    print("\n")
                    self.listBox.insert("", "end", values=(row[1], row[0], row[2], row[3], row[4], row[5]))
                cursor.close()

        except sqlite3.Error as error:
                Error.set("Failed to read data from sqlite table", error)

                self.error['text'] = "*" + Error
                print("Failed to read data from sqlite table", error)
        finally:
                if (sqliteConnection):
                    sqliteConnection.close()
                    print("The SQLite connection is closed")

        # DELETE ROW
    def deleteRow(self):

         self.error['text'] = "*"
         email = fac_id.get()
         if (email!="")   :
            con = sqlite3.connect('CollegeDataBase1.db')
            with con:
                # cur = con.cursor()
                sql = 'DELETE FROM Faculty WHERE Email=?'
                cur = con.cursor()
                cur.execute(sql, (email,))
                con.commit()
                # cur.execute("DELETE FROM Student WHERE ID = %s", email)
                self.entry_1.setvar("Deleted")
                Error="Number of rows deleted:"+ str(cur.rowcount)
                self.error['text']="*"+Error
                print("Number of rows deleted:", cur.rowcount)
         else:
             self.error['text'] = "*"+"Field is Empty"

             # connectiong to database
    def database(self):

            name1 = fac_name.get()
            email = fac_id.get()
            gender = fac_gender.get()
            semester = fac_course.get()
            fee = fac_fee.get()
            att = fac_dep.get()
            conn = sqlite3.connect('CollegeDataBase1.db')
            with conn:
                cursor = conn.cursor()
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS Faculty (Fullname TEXT,Email TEXT,Gender TEXT,Semester TEXT,Fee TEXT, Attendence TEXT)')
            cursor.execute('INSERT INTO Faculty (FullName,Email,Gender,Semester,Fee,Attendence) VALUES(?,?,?,?,?,?)',
                           (name1, email, gender, semester, fee, att,))
            conn.commit()

    def resetAll(self):

        fac_name.set("")
        fac_id.set("")

        fac_course.set("Select Course")
        fac_dep.set("")

    def onclick(self, event):
        item = self.listBox.item(self.listBox.selection())
        print("you clicked on", type(item), item, '\n')
        it = self.listBox.selection()[0]
        print('item clicked', it)
        get = self.listBox.item(it)
        print("values are:", get)
        row = get['values']
        print(row)
        fac_id.set(row[0])
        fac_name.set(row[1])
        fac_gender.set(row[2])
        fac_course.set(row[3])
        fac_dep.set(row[5])
        fac_fee.set(row[4])

class no_of_faculty:

    def __init__(self,root):
        self.total_stud = StringVar()
        self.Email = StringVar()
        self.var = IntVar()
        self. c = StringVar()
        self.root = root
        self.root.title('Total Faculty panel')
        self.fro1 = Canvas(root, bg='white', height=600, width=800)

        self.image02 = PhotoImage(file="pics//vu.png")

        self.fro1.create_image(0, 0, anchor=NW, image=self.image02)

        self.fro1.pack()
        self.label_0 = Label(root, text="Faculty Management form", width=20, bg=("white"),fg=("steelblue"),font=('times 20 bold italic'))
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

        self.label_2 = Label(root, text="No Of faculty:", width=20, fg=("red"), font=("times bold", 15))
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

            sqlite_select_query =  """SELECT * from Faculty WHERE Semester=?"""
            bool=TRUE

        else:
            print("i am in else ")
            sqlite_select_query = """SELECT * from Faculty  """
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












b = Application(root)

root.resizable(False, False)
root.mainloop()