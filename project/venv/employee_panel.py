from tkinter import *
import sqlite3
from tkinter import messagebox as box
from tkinter import ttk
from PIL import Image, ImageTk


# initializing variables for student data





class Employee_panel:

    def __init__(self,root):
        self.Fullname = StringVar()
        self. Email = StringVar()
        self.var = IntVar()
        self. c = StringVar()
        self. var1 = IntVar()
        self.attendence = IntVar()
        self.Error = StringVar()
        self. Error = "*"
        self.root = root
        self.root.title('Student Management')
        self.fro1 = Canvas(root, bg='white', height=600, width=1200)

        self.image02 = PhotoImage(file="pics//vu.png")

        self.fro1.create_image(0, 0, anchor=NW, image=self.image02)

        self.fro1.pack()
        self.label_0 = Label(root, text="Employee Management form", width=20, bg=("white"),fg=("steelblue"),font=('times 20 bold italic'))
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

        self.label_3 = Label(root, text="Attendence", width=20, fg=("steelblue"),font=("times bold", 15))
        self.label_3.place(x=10, y=270)

        self.entry_3 = Entry(root, textvar=self.attendence,width=14,fg=("black"),font=("times bold", 15))
        self.entry_3.place(x=200, y=270)

        self.label_3 = Label(root, text="Gender", width=20, fg=("steelblue"),font=("times bold", 15))
        self.label_3.place(x=10, y=310)

        Radiobutton(root, text="Male", padx=5, variable=self.var, value=1).place(x=205, y=310)
        Radiobutton(root, text="Female", padx=20, variable=self.var, value=2).place(x=260, y=310)

        self.label_4 = Label(root, text="Department", width=20, fg=("steelblue"),font=("times bold", 15))
        self.label_4.place(x=10, y=350)

        list1 = ['1', '2', '3', '4', '5', '6', '7', '8'];

        self.droplist = OptionMenu(root, self.c, *list1)
        self.droplist.config(width=15)
        self.c.set('select Department')
        self.droplist.place(x=200, y=350)

        self.label_4 = Label(root, text="Salary", width=20, fg=("steelblue"),font=("times bold", 15))
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

        tbLabel =Label(root, text="Employee Data", font=("Arial", 30))
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
    def updateRow(self):
        self.error['text'] = "*"
        conn = sqlite3.connect('CollegeDataBase1.db')
        name1 = self.Fullname.get()
        email = self.Email.get()
        gender = self.var.get()
        semester = self.c.get()
        fee =self.var1.get()
        att = self.attendence.get()


        if (email!="" and name1!="" and gender!="" and semester!="" and fee!="" and att!="" ):
            # get the connection
            with conn:
                cur = conn.cursor()
                cur.execute(
                    """UPDATE Employee
                                 SET Fullname = ? ,
                                     Gender= ? ,
                                     Semester = ?,
                                     Fee=?,
                                     Attendence=?
                                 WHERE Email = ? """,
                    (name1, gender, semester, fee, att, email))

                conn.commit()
                self.error['text'] = "*" + "Number of rows updated:"+ str(cur.rowcount)
                self.resetAll()
                self.searchStudent()
        else:
         self.error['text'] = "*"+"Empty Field"
        # method to search student
    def searchStudent(self,):
        bool=FALSE
        sqlite_select_query=StringVar()
        self.listBox.delete(*self.listBox.get_children())
        self.error['text'] = "*"
        email = self.Email.get()
        if (email!=""):
            sqlite_select_query =  """SELECT * from Employee WHERE Email =?"""
            bool=TRUE

        else:
            sqlite_select_query = """SELECT * from Employee  """
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
                    print("Semester: ", row[3])
                    print("Fee: ", row[4])
                    print("Attendence: ", row[5])
                    print("\n")
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
                sql = 'DELETE FROM Employee WHERE Email=?'
                cur = con.cursor()
                cur.execute(sql, (email,))
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
            fee = self.var1.get()
            att = self.attendence.get()
            conn = sqlite3.connect('CollegeDataBase1.db')
            with conn:
                cursor = conn.cursor()
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS Employee (Fullname TEXT,Email TEXT,Gender TEXT,Semester TEXT,Fee TEXT, Attendence TEXT)')
            cursor.execute('INSERT INTO Employee (FullName,Email,Gender,Semester,Fee,Attendence) VALUES(?,?,?,?,?,?)',
                           (name1, email, gender, semester, fee, att,))
            conn.commit()
            conn.close()

            self.listBox.insert("", "end", values=(email, name1, gender, semester, fee, att,))

    def resetAll(self):

        self.Fullname.set("")
        self.Email.set("")

        self.c.set("Select Your Semester")

        self.attendence.set("0")

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
