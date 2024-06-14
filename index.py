from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBase

jan = Tk()
jan.title("Teste - Painel de Login")
jan.geometry("600x300")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)

#logo = PhotoImage(file="logo.png")

LeftFrame = Frame(jan, width=200, height=300, bg="GREY", relief="raised")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="BLACK", relief="raised")
RightFrame.pack(side=RIGHT)

#LogoLabel = Label (LeftFrame, image=logo, width=100, height=100, bg="GREY")
#LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text="Username:", font=("Comic Sans", 20), bg="GREY", fg="White")
UserLabel.place(x=5, y=100)

UserEntry= ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

PassLabel = Label(RightFrame, text="Password:", font=("Comic Sans", 20), bg="GREY", fg="White")
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=30, show="*")
PassEntry.place(x=150, y=160)

#Buttons
def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    DataBase.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? and Password = ?)
    """, (User, Pass))
    print("Selecionou")
    VerifyLogin = DataBase.cursor.fetchone()
    try:
        if (User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="Login Info", message="acesso confimrado,bem vindo")
    except:
        messagebox.showinfo(title="Login Info", message="acesso negado, verifique se esta cadastrado no sistema")

LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=Login)
LoginButton.place(x=100, y=225)

def Register():
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    NomeLabel = Label(RightFrame, text="Name:", font=("Comic Sans",20), bg="MIDNIGHTBLUE", fg="white")
    NomeLabel.place(x=5, y=5)

    NomeEntry = Entry(RightFrame, width=30)
    NomeEntry.place(x=100, y=16)

    EmailLabel = Label(RightFrame, text="Email", font=("Comic Sans", 20), bg="MIDNIGHTBLUE", fg="white")
    EmailLabel.place(x=5, y=55)
 
    EmailEntry = Entry(RightFrame, width=30)
    EmailEntry.place(x=100, y=66)

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()
        
        if (Name == "" and Email == "" and User == "" and Pass == ""):
            messagebox.showerror(title="Register Error", message="Preencha Todos os Campos")
        else:
            DataBase.cursor.execute("""
                INSERT INTO users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
                """, (Name, Email, User, Pass))
            DataBase.conn.commit()
            messagebox.showinfo(title="Register Info", message="Conta Criada com sucesso")

    Register = ttk.Button(RightFrame, text="Register", width=30, command=RegisterToDataBase)
    Register.place(x=100, y=225)

    def BackToLogin():
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        LoginButton.place(x=100)
        RegisterButton.place(x=125)

    Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
    Back.place(x=125, y=260)

RegisterButton = ttk.Button(RightFrame, text="register", width=20, command=Register)
RegisterButton.place(x=125, y=260)

jan.mainloop()