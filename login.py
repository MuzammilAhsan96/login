from tkinter import*
from tkinter import messagebox
class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1366x768+0+0")

        #========All Images======
        self.bg_icon=PhotoImage(file="images/bg_img.png")
        self.user_icon=PhotoImage(file="images/user.png")
        self.pass_icon=PhotoImage(file="images/password.png")
        self.logo_icon=PhotoImage(file="images/logo.png")

        #=========Variables=========

        self.uname=StringVar();
        self.upass=StringVar();


        bg_lbl=Label(self.root,image=self.bg_icon).pack()

        title=Label(self.root,text="Login System",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        Login_Frame=Frame(self.root,bg="white")
        Login_Frame.place(x=400,y=150)

        logolbl=Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=0,columnspan=2,pady=20)

        lbluser=Label(Login_Frame,text="USERNAME",image=self.user_icon,bd=0,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
        txtuser=Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)

        lblpass=Label(Login_Frame,text="PASSWORD",image=self.pass_icon,bd=0,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=2,column=0,padx=20,pady=10)
        txtpass=Entry(Login_Frame,bd=5,textvariable=self.upass,relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=20)
 
        btn_log=Button(Login_Frame,text="Login",width=15,command=self.login1,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=1,pady=10)
        print(self.uname)
        
    def login1(self):
        if self.uname.get()=="" or self.upass.get()=="":
            messagebox.showerror("Error","All Fields are Required!")
        elif self.uname.get()=="Muzammil" and self.upass.get()=="123456":
            messagebox.showinfo("Successful!",f"Welcome {self.uname.get()}")
        else:
            messagebox.showerror("Error","Invalid Username or Password!")
        
root=Tk()
obj =Login_System(root)
root.mainloop()