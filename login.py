from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")



        self.bg=ImageTk.PhotoImage(file=r"C:\Users\GAGANDEEP N\Desktop\python_\hotel images\SDT_Zoom-Backgrounds_April-8_Windansea-1-logo-1.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)        #when window size changes the picture also changes its width 


        #frame
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\GAGANDEEP N\Desktop\python_\hotel images\LoginIconAppl.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)                           #antialias converts high level image into low level image
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        #get started label
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #*****label- username*****
        username_lbl = Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_lbl.place(x=70,y=155)
        

        #*****entry field- user*****

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        #label- password
        password_lbl = Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password_lbl.place(x=70,y=225)

        #entry- password
        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #*****icon images*****
        img2=Image.open(r"C:\Users\GAGANDEEP N\Desktop\python_\hotel images\LoginIconAppl.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)                          
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"C:\Users\GAGANDEEP N\Desktop\python_\hotel images\lock-512.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)                          
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=395,width=25,height=25)
        





















if __name__ =="__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()