#     modules

import customtkinter
import tkinter
from tkinter import *
import tkvideo
from tkvideo import tkvideo
from tkinter import messagebox
import mysql.connector
from atexit import register

# root 

root=tkinter.Tk()
root.state("zoomed")

#frames

fsplash=tkinter.Frame(root)
fstartup=tkinter.Frame(root)
fhome=tkinter.Frame(root)
flogin=tkinter.Frame(root)
fsignup=tkinter.Frame(root)
fmain=tkinter.Frame(root)
fvoice=tkinter.Frame(root)
ftext=tkinter.Frame(root)


# splash

# csplash=Canvas(fsplash,height=1080,width=1920,bg="white")
# csplash.place(x=0,y=0)

# lblvideo=Label(csplash)
# lblvideo.place(x=-150,y=-150)

# player=tkvideo("jumping.mp4",lblvideo,loop=1,size=(1920,1080))

# player.play()

# def main():
#     csplash.place_forget()
fstartup.place(x=0,y=0,height=1080,width=1920)

# csplash.after(7700,main)


# starup 

cstartup=Canvas(fstartup,height=1080,width=1920)
cstartup.place(x=0,y=0)

img1=PhotoImage(file="jump.png")
bgstartup=cstartup.create_image(766,400,image=img1)

b1=customtkinter.CTkButton(cstartup,text="START",
    font=("Times new roman",25,"bold") ,
    corner_radius=10,
    bg_color="#7c7c7c",width=150,height=50,
    command=lambda:[fstartup.place_forget(),fhome.place(x=0,y=0,height=1080,width=1920)])

b1.place(x=550,y=650)

def destroy():
    root.destroy()

b2=customtkinter.CTkButton(cstartup,text="QUIT",
    font=("Times new roman",25,"bold"),
    corner_radius=10,
    bg_color="#7c7c7c",width=150,height=50,
    command=destroy)

b2.place(x=850,y=650)


# home


def userlogin():

    mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="signon",autocommit=True)
    mycur=mydb.cursor()
    if e1.get()=='' or e2.get()=='':
        messagebox.showerror("Error","all field required")
        
    url3=("select * from register;")
    mycur.execute(url3)
    datas=mycur.fetchall()
    flag1=0
    flag2=0
    if e1.get():
           
        #print(datas)
        #print(datas[1][1])
        for i in range(len(datas)):
            if datas[int(i)][0]==e1.get():   
                flag1=1
                break
                    
        if flag1==0:
            messagebox.showerror("Error","user Doesnt  exists !!!")
    if e2.get() and flag1:
        url4=("select pass from register where uname=%s;")
        #print(logentry0.get())
        pass2=[e1.get()]
        #print(pass2)
        mycur.execute(url4,pass2)
        uname1=mycur.fetchone()
        #print(uname1)
        #print(datas[1][1])
        if uname1[0]==e2.get():
            flag2=1
                    
        if flag2==0:
            messagebox.showerror("Error","Invalid password !!!")        
        else:
            flogin.place_forget(),fmain.place(x=0,y=0,height=1080,width=1920)

chome=Canvas(fhome,height=1080,width=1920,bg="black")
chome.place(x=0,y=0)
b3=customtkinter.CTkButton(chome,text="BACK",fg_color="cyan",
    font=("times new roman",20,"bold"),
    height=50,width=150,text_color="black",
    corner_radius=10,
    command=lambda:[fhome.place_forget(),fstartup.place(x=0,y=0,height=1080,width=1920)],
    )
b3.place(x=1300,y=70)

l1=customtkinter.CTkLabel(chome,text=" ",height=500,width=500,fg_color="grey")
l1.place(x=650,y=180)

l2=customtkinter.CTkLabel(chome,text="LOGIN",
    fg_color="grey",text_color="white",
    font=("times new roman",25,"bold"),
    height=50,width=150)

l2.place(x=720,y=200)

img2=PhotoImage(file="login_white.png")

l3=Label(chome,image=img2,border=0,borderwidth=0,bg="grey")
l3.place(x=700,y=205)

l4=Label(chome,text=" ",width=35,height=5,bg="cyan")
l4.place(x=899,y=180)

b4=customtkinter.CTkButton(chome,text="SIGNUP",
    fg_color="cyan",text_color="black",
    bg_color="cyan",
    font=("times new roman",25,"bold"),hover_color="#FFFFFF",
    height=50,width=100,
    command=lambda:[fhome.place_forget(),fsignup.place(x=0,y=0,height=1080,width=1920)])

b4.place(x=970,y=200)

img3=PhotoImage(file="signup_black.png")

l5=Label(chome,image=img3,border=0,borderwidth=0)
l5.place(x=925,y=205)

l8=Label(chome,text=" ",height=3,width=60,bg="white")
l8.place(x=690,y=350)

e1=customtkinter.CTkEntry(chome,placeholder_text="ENTER YOUR USERNAME",
    font=("candara",20,"italic"),
    height=50,width=350,bg_color="white",border_width=0)
e1.place(x=760,y=350)

img6=PhotoImage(file="user.png")

l9=Label(chome,image=img6,border=0,bg="white")
l9.place(x=710,y=355)

l10=Label(chome,text=" ",height=3,width=60,bg="white")
l10.place(x=690,y=450)

e2=customtkinter.CTkEntry(chome,placeholder_text="ENTER YOUR PASSWORD",
    font=("candara",20,"italic"),
    height=50,width=350,bg_color="white",
    border_width=0,show="*")
e2.place(x=760,y=450)

img7=PhotoImage(file="password.png")

l11=Label(chome,image=img7,border=0,bg="white")
l11.place(x=710,y=455)

b6=customtkinter.CTkButton(chome,text="LOGIN",
    fg_color="cyan",text_color="black",
    bg_color="grey",
    font=("times new roman",25,"bold"),hover_color="#FFFFFF",
    height=50,width=100,
    corner_radius=20,
    command=userlogin)

b6.place(x=835,y=550)

l12=Label(chome,text="Don't have an account ? click on",
    border=0,bg="grey",fg="white",
    font=("timesnewroman",15,"italic"))
l12.place(x=700,y=610)

b8=customtkinter.CTkButton(chome,text="SIGNUP",
    font=("times new roman",20,"bold"),
    fg_color="grey",
    text_color="cyan",
    border_width=0,width=7,
    bg_color="grey",
    command=lambda:[fhome.place_forget(),fsignup.place(x=0,y=0,height=1080,width=1920)])

b8.place(x=990,y=610)

# signup

def register():
    
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="signon",autocommit=True)
            mycur=mydb.cursor()
            if e3.get()=='' or e4.get()=='' or e5.get()=='':
                messagebox.showerror("Error","all field required")
            
            fmail=0
            funame=0
            fpass=0

            if e3.get():
                url=("select * from register;")
                mycur.execute(url)
                datas=mycur.fetchall()
                #print(datas)
                #print(datas[1][1])
                for i in range(len(datas)):
                    if datas[int(i)][0]==e3.get():
                        messagebox.showerror("Error","User already exist ...Please use login tab to login")
                    else:
                        funame=1
            if e4.get():
                flag1=0
                for i in e4.get():
                    if i=="@":
                        flag1 =1
                if flag1==0:
                    messagebox.showerror("Error","Invalid email!!!")
                else:
                    fmail=1
            if e5.get():
                paschk=e5.get()
                l=int(0)
                u=int(0)
                d=int(0)
                p=int(0)
                if (len(paschk) >= 8):
                    for i in paschk:
            
                        # counting lowercase alphabets
                        if (i.islower()):
                            l+=1           
                
                        # counting uppercase alphabets
                        if (i.isupper()):
                            u+=1           
                
                        # counting digits
                        if (i.isdigit()):
                            d+=1           
                
                        # counting the mentioned special characters
                        if(i=='!'or i=='@' or i=='#' or i=='$' or i=='%' or i=='^' or i=='&' or i=='*' or i=='(' or i==')' or i=='_' or i=='-' or i=='+' or i=='=' or i=='[' or i==']' or i=='{' or i=='}' or i==';' or i==':' or i=='"' or i=='/' or i==' \ ' or i=='?' or i=='>' or i=='<' or i=='.' or i==',') or i=='|':
                            p+=1          
                        
                if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(paschk)):
                        fpass=1
                else:
                        messagebox.showerror("Error","\t"+"Invalid password format!!!"+"\n"+
                        "Password should contain atleast one uppercase letter, lowercase letter,numeric character and special symbol")   
            if funame==1 and fmail==1 and fpass==1:
                val=(e3.get(),e4.get(),e5.get())
                url1=("insert into register value(%s,%s,%s)")
                mycur.execute(url1,val)
                messagebox.showinfo("success","Account has been Created Successfully!!!")

            mydb.close()

csignup=Canvas(fsignup,height=1080,width=1920,bg="black")
csignup.place(x=0,y=0)
b5=customtkinter.CTkButton(csignup,text="BACK",fg_color="cyan",
    font=("times new roman",20,"bold"),
    height=50,width=150,text_color="black",
    corner_radius=10,
    command=lambda:[fsignup.place_forget(),fstartup.place(x=0,y=0,height=1080,width=1920)],
    )
b5.place(x=1300,y=70)

l6=customtkinter.CTkLabel(csignup,text=" ",height=500,width=500,fg_color="grey")
l6.place(x=650,y=180)

l7=customtkinter.CTkLabel(csignup,text="SIGNUP",
    fg_color="grey",text_color="white",
    font=("times new roman",25,"bold"),
    height=50,width=150)

l7.place(x=970,y=200)


l4=Label(csignup,text=" ",width=35,height=5,bg="cyan")
l4.place(x=650,y=180)

img4=PhotoImage(file="login_black.png")

l3=Label(csignup,image=img4,border=0,borderwidth=0,bg="grey")
l3.place(x=700,y=205)

b4=customtkinter.CTkButton(csignup,text="LOGIN",
    fg_color="cyan",text_color="black",
    bg_color="cyan",
    font=("times new roman",25,"bold"),hover_color="#FFFFFF",
    height=50,width=100,
    command=lambda:[fsignup.place_forget(),fhome.place(x=0,y=0,height=1080,width=1920)])

b4.place(x=740,y=200)

img5=PhotoImage(file="signup_white.png")

l5=Label(csignup,image=img5,border=0,borderwidth=0)
l5.place(x=925,y=205)

l13=Label(csignup,text=" ",height=3,width=60,bg="white")
l13.place(x=690,y=300)

l14=Label(csignup,image=img6,border=0,bg="white")
l14.place(x=710,y=305)


e3=customtkinter.CTkEntry(csignup,placeholder_text="ENTER YOUR USERNAME",
    font=("candara",20,"italic"),
    height=50,width=350,bg_color="white",border_width=0)
e3.place(x=760,y=300)

img8=PhotoImage(file="gmail.png")

l15=Label(csignup,text=" ",height=3,width=60,bg="white")
l15.place(x=690,y=400)

l16=Label(csignup,image=img8,border=0,bg="white")
l16.place(x=710,y=405)

e4=customtkinter.CTkEntry(csignup,placeholder_text="ENTER YOUR EMAIL ID",
    font=("candara",20,"italic"),
    height=50,width=350,bg_color="white",border_width=0)
e4.place(x=760,y=400)


l17=Label(csignup,text=" ",height=3,width=60,bg="white")
l17.place(x=690,y=500)

l18=Label(csignup,image=img7,border=0,bg="white")
l18.place(x=710,y=505)


e5=customtkinter.CTkEntry(csignup,placeholder_text="ENTER NEW PASSWORD",
    font=("candara",20,"italic"),
    height=50,width=350,bg_color="white",border_width=0,show="*")
e5.place(x=760,y=500)

b7=customtkinter.CTkButton(csignup,text="SIGNUP",
    fg_color="cyan",text_color="black",
    bg_color="grey",
    font=("times new roman",25,"bold"),hover_color="#FFFFFF",
    height=50,width=100,
    corner_radius=20,
    command=register)

b7.place(x=835,y=580)

l19=Label(csignup,text="Already have an account ? click on",
    font=("times new roman",16,"bold"),fg="white",
    bg="grey")

l19.place(x=700,y=637)

b9=customtkinter.CTkButton(csignup,text="LOGIN",
    font=("times new roman",18,"bold"),fg_color="grey",
    bg_color="grey",
    text_color="cyan",width=8,
    command=lambda:[fsignup.place_forget(),fhome.place(x=0,y=0,height=1080,width=1920)])

b9.place(x=1016,y=640)


b10=customtkinter.CTkButton(csignup,text="!",font=("times new roman",35,"bold"),
    height=25,width=26,border_width=0,bg_color="white",fg_color="#FFFFFF",
    text_color="#FF0000",hover_color="white")

b10.place(x=1080,y=503)

def pass_hover(e):
    global l20

    Txt=("Password should contain the following : "+"\n"+
        "*Uppercase letter"+"\n"+"*Lowercase letter"+"\n"+
        "*Integer number"+"\n"+"*Special symbol")

    l20=Label(csignup,text=Txt)
    l20.place(x=1155,y=490)

b10.bind("<Enter>",pass_hover)

def pass_leave(e):
    l20.place_forget()

b10.bind("<Leave>",pass_leave)
# end

fsplash.place(x=0,y=0,height=1080,width=1920)
root.mainloop()