from tkinter import *
import sqlite3
from tkinter import messagebox as box
from tkinter import ttk
from PIL import Image, ImageTk



class students_attendence:

    def __init__(self,root,course):

        if(course!=""):
         self.course=course
        else:
         self.course=StringVar()
        self.total_stud = StringVar()
        self.Email = StringVar()
        self.var = IntVar()
        self. c = StringVar()
        self.root = root
        self.root.title('Students Attendence')
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
        if(self.course!=""):
            print("YEAHHHHHHHHHHHH")
            self.label_4 = Label(root, text="Semester", width=20, fg=("steelblue"), font=("times bold", 15))
            self.label_4.place(x=10, y=350)

            list1 = ['1', '2', '3', '4', '5', '6', '7', '8'];

            self.droplist = OptionMenu(root, self.c, *list1)
            self.droplist.config(width=15)
            self.c.set('select your semester')
            self.droplist.place(x=200, y=350)

        self.label_2 = Label(root, text="Total No of Students:", width=20, fg=("red"), font=("times bold", 15))
        self.label_2.place(x=10, y=410)
        self.entry_2 = Entry(root, textvar=self.total_stud, width=15, fg=("black"), font=("times bold", 15))
        self.entry_2.place(x=230, y=410)
        tbLabel = Label(root, text="Students Data", font=("Arial", 30))
        tbLabel.place(x=750, y=100)
        # create Treeview with  columns
        cols = ('ID', 'Name',  'Gender','Register_No', 'Date', 'Mark')
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

            sqlite_select_query =  """ SELECT * FROM Student st  Join records1 rc on(st.Email=rc.student_id) join Attendence at on (rc.at_id=at.id) WHERE at.course_id=?"""
            bool=TRUE

        else:
            print("i am in else ")
            sqlite_select_query = """ SELECT * FROM Student st  Join records1 rc on(st.Email=rc.student_id) join Attendence at on (rc.at_id=at.id) WHERE rc.student_id=? and at.course_id=?"""
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

                    self.listBox.insert("", "end", values=(row[1], row[0], row[3], row[8], row[11], row[7]))
                cursor.close()

        except sqlite3.Error as error:

                print("Failed to read data from sqlite table", error)
        finally:
                if (sqliteConnection):
                    sqliteConnection.close()
                    print("The SQLite connection is closed")
