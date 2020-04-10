
# imports

from tkinter import *
from tkinter import messagebox as ms
import sqlite3
import Main_Application, fac_stud_panel




# make database and users (if not exists already) table at programme start up
with sqlite3.connect('CollegeDataBase1.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEX NOT NULL,user_type TEX NOT NULL);')
db.commit()
db.close()


# main Class
class main:
    def __init__(self ,master):
        # Window
        self.root = master
        self.root.title("Login Form")
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.type = IntVar()

        # Create Widgets
        self.widgets()

    # Login Function
    def login(self):
        find_user=StringVar()
        # Establish Connection
        with sqlite3.connect('CollegeDataBase1.db') as db:
            c = db.cursor()
        if (self.type.get()==1):
            print("i am going to check faculty")
            find_user = ('SELECT * FROM Faculty JOIN Courses1 on (Email=faculty_id) WHERE Email =?')
            c.execute(find_user, [(self.username.get())])
        else:
            find_user = ('SELECT * FROM user WHERE username = ? and password = ? and user_type=?')
            c.execute(find_user, [(self.username.get()), (self.password.get()), (self.type.get())])

        result = c.fetchall()

        if result:


            if (self.type.get()==1):
                print("yes it is in faculty ")
                for row in result:
                    fac_name = row[0]
                    course_code = row[6]
                    course_name = row[5]


                print(fac_name,course_code,course_name)
                self.root.withdraw()
                hr = Toplevel()
                b = fac_stud_panel.fac_student_panel(hr,fac_name,course_name,course_code)

            else:
                self.root.withdraw()
                hr = Toplevel()
                b = Main_Application.Application(hr, self.username.get())




            print("Logged in ")
        else:
            ms.showerror('Oops!' ,'Username Not Found.')

    def signup(self):
        # Establish Connection
        with sqlite3.connect('CollegeDataBase1.db') as db:
            c = db.cursor()

        # Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user ,[(self.username.get())])
        if c.fetchall():
            ms.showerror('Error!' ,'Username Taken Try a Diffrent One.')
        else:
            insert = 'INSERT INTO user(username,password,user_type) VALUES(?,?,?)'
            c.execute(insert, [(self.username.get()), (self.password.get()),(self.type.get())])
            db.commit()
            ms.showinfo('Success!' ,'Account Created!')
            #self.log()



        # Frame Packing Methords

    def check(self):
        if (self.type.get()==1):
            ms.showerror('Sorry', 'You can only signup as Department')
        else:
            self.signup()

    # Draw Widgets
    def widgets(self):

        self.logf = Canvas(self.root, bg='white', height=500, width=500)
        self.image02 = PhotoImage(file="pics//person.png")

        self.logf.create_image(220, 20, anchor=NW, image=self.image02)

        Label(self.logf ,text = 'Username: ' ,fg="steelblue",font=('times 20 bold italic') ,pady=5 ,padx=5).place(x=40,y=140)
        Entry(self.logf ,textvariable = self.username ,bd = 5 ,font = ('' ,15)).place(x=200,y=140)
        Label(self.logf ,text = 'Password: ',fg="steelblue" ,font=('times 20 bold italic'),pady=5 ,padx=5).place(x=40,y=235)
        Entry(self.logf ,textvariable = self.password ,bd = 5 ,font = ('' ,15) ,show = '*').place(x=200,y=235)
        Label(self.logf, text='Login As: ', fg="steelblue", font=('times 15 bold italic'), pady=5, padx=5).place(x=40,
                                                                                                                 y=310)
        Radiobutton(self.logf, text="Faculty", padx=5, variable=self.type, value=1).place(x=190, y=310)
        Radiobutton(self.logf, text="Department", padx=20, variable=self.type, value=2).place(x=280, y=310)

        Label(root, text="Login", font=('times 12 bold italic'), fg='black').place(x=100,y=370)
        self.b3 = Button(self.logf , font=('arial 15 bold'), width=120, height=60, bg='lightyellow',
                         command=self.login)

        self.okb3 = PhotoImage(file="pics\lock.png")
        self.tmi2 = self.okb3.subsample(1, 1)
        self.b3.config(image=self.tmi2)
        self.b3.place(x=70,y=390)
        Label(root, text="Signup", font=('times 12 bold italic'), fg='black').place(x=280,y=370)
        self.b4 = Button(self.logf , font=('arial 15 bold'), width=120, height=55, bg='white',
                         command=self.check)
        self.okb4 = PhotoImage(file="pics\login.png")
        self.tmi3 = self.okb4.subsample(1, 1)
        self.b4.config(image=self.tmi3)
        self.b4.place(x=280,y=390)
        self.logf.pack()


if __name__ == "__main__":
    root = Tk()
    main(root)
    root.mainloop()
    exit()
# create window and application object

