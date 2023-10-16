################### importing modules ####################

import tkinter as tk
from tkinter import *
import customtkinter
from tkinter import messagebox,ttk   
import tkvideo
from tkvideo import tkvideo
import mysql.connector
import googletrans
from googletrans import Translator
import socket
from playsound import playsound
import speech_recognition as sr
from gtts import gTTS
import os
import time
import webbrowser
import app
from app import main


#################### creating tkinter ####################

root=tk.Tk()
root.state("zoomed")
root.overrideredirect(True)

#################### creating frames ####################

fstartup=tk.Frame(root)
flogin=tk.Frame(root)
fsignup=tk.Frame(root)
fmain=tk.Frame(root)
ft_t=tk.Frame(root)
ft_v=tk.Frame(root)
fv_t=tk.Frame(root)
fv_v=tk.Frame(root)
fhand=tk.Frame(root)
fdelete=tk.Frame(root)

#################### function to check the button working or not ####################

def clicked():
    messagebox.showinfo("button clicked","User have clicked the button")


################## function to open website #########################

def webopen_about():
    webbrowser.open_new("file:///C:/Users/asus/OneDrive/Desktop/signon/website/index.html#home")

def webopen_help():
    webbrowser.open_new("file:///C:/Users/asus/OneDrive/Desktop/signon/website/index.html#contact")



#################### Internet connection #####################

# img24=PhotoImage(file="wifiok.png")

# img25=PhotoImage(file="nowifi.png")

# l48=Label(root,image=img24,background="white")


# def test_net():
#     try:
#         socket.create_connection(('google.com',80))
#         l48.configure(image=img24)
#         l48.place(x=1350,y=20)     
#     except OSError:
#         l48.configure(image=img25)
#         l48.place(x=1350,y=20)

#     root.after(1000,test_net)
        



#################### startup page ####################

cstartup=Canvas(fstartup,height=1080,width=1920,
    background="black",bd=0,highlightthickness=0,relief="ridge")
cstartup.place(x=0,y=0)

img1=PhotoImage(file="logo_title.png")

l1=Label(cstartup,image=img1,background="black",border=0,height=540,width=960)
l1.place(x=250,y=20)

img2=PhotoImage(file="mic.png")

l2=Label(cstartup,image=img2,background="black",height=100,width=100)
l2.place(x=230,y=650)

img3=PhotoImage(file="text.png")

l3=Label(cstartup,image=img3,background="black",height=100,width=100)
l3.place(x=730,y=650)

img4=PhotoImage(file="hand.png")

l4=Label(cstartup,image=img4,background="black",height=100,width=100)
l4.place(x=1230,y=650)

l10=customtkinter.CTkLabel(cstartup,text=" ",fg_color="#EEEEEE",
    width=1300,height=54,bg_color="black",corner_radius=50)
l10.place(x=150,y=20)

b1=customtkinter.CTkButton(cstartup,text="Help",font=("times",25,"underline"),bg_color="#EEEEEE",
    fg_color="#EEEEEE",hover_color="grey",text_color="black",command=webopen_help)
b1.place(x=900,y=30)

b2=customtkinter.CTkButton(cstartup,text="About",font=("times",25,"underline"),bg_color="#EEEEEE",
    fg_color="#EEEEEE",hover_color="grey",text_color="black",command=webopen_about)
b2.place(x=1050,y=30)

def quit():
    root.destroy()

b3=customtkinter.CTkButton(cstartup,text="Quit",font=("times",25,"underline"),bg_color="#EEEEEE",
    fg_color="#EEEEEE",hover_color="grey",text_color="black",command=quit)
b3.place(x=1200,y=30)

b4=customtkinter.CTkButton(cstartup,text=("Get started →"),font=("ROBOT",20),fg_color="yellow",
    text_color="black",hover_color="grey",height=40,width=250,
    command=lambda:[fstartup.place_forget(),flogin.place(x=0,y=0,height=1080,width=1920)])
b4.place(x=650,y=500)

img5=PhotoImage(file="line.png")

l5=Label(cstartup,image=img5,background="black")
l5.place(x=550,y=660)

l6=Label(cstartup,image=img5,background="black")
l6.place(x=1050,y=660)

l7=Label(cstartup,text="Voice Translation",background="black",fg="white",font=("verdana",15,"italic"))
l7.place(x=195,y=750)

l8=Label(cstartup,text="Text Translation",background="black",fg="white",font=("verdana",15,"italic"))
l8.place(x=695,y=750)

l9=Label(cstartup,text="Sign translation",background="black",fg="white",font=("verdana",15,"italic"))
l9.place(x=1195,y=750)


#################### Login page ####################

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

clogin=Canvas(flogin,height=1080,width=1920,relief="ridge",highlightthickness=0,background="white")
clogin.place(x=0,y=0)


def login_reset():
    for widget in clogin.winfo_children():
        if isinstance(widget,tk.Entry):
            widget.delete(0,'end')
    
b5=customtkinter.CTkButton(clogin,text="Back",font=("Times",25,"underline"),
    width=50,hover_color="grey",fg_color="White",text_color="black",
    command=lambda:[login_reset(),flogin.place_forget(),fstartup.place(x=0,y=0,height=1080,width=1920)])
b5.place(x=80,y=100)

l11=Label(clogin,text="Welcome Back",font=("harrington",60,"bold"),background="white",fg="black")
l11.place(x=200,y=150)

l12=Label(clogin,text="Please enter your details",font=("footlight mt light",25),background="white",fg="grey")
l12.place(x=300,y=250)

l45=Label(clogin,text="Username : ",font=("times",22),bg="white",fg="#555555")
l45.place(x=120,y=345)

l46=Label(clogin,text="Password  : ",font=("times",22),bg="white",fg="#555555")
l46.place(x=120,y=445)



e1=Entry(clogin,bg="white",fg="grey",font=("Bahnschrift",20),width=25)
e1.place(x=270,y=350)



e2=Entry(clogin,bg="white",fg="grey",font=("Bahnschrift",20),show="*",width=25)
e2.place(x=270,y=450)

img22=PhotoImage(file="eye1.png")

img23=PhotoImage(file="eye2.png")

b20=Button(clogin,image=img22,borderwidth=0,background="white")

def view3(e):
    e2.configure(show="")
    b19.place_forget()
    b20.place(x=660,y=450)

def view4(e):
    e2.configure(show="*")
    b20.place_forget()
    b19.place(x=660,y=450)

b19=Button(clogin,image=img23,borderwidth=0,background="white")
b19.place(x=660,y=450)

b19.bind('<Button-1>',view3)

b20.bind('<Button-1>',view4)

b6=customtkinter.CTkButton(clogin,text="Login",font=("informal roman regular",30),fg_color="black",
    text_color="white",corner_radius=5,width=200,
    command=userlogin)
b6.place(x=370,y=550)

l13=Label(clogin,text="Don't have an account ? ",font=("footlight mt light",18),background="white",fg="grey")
l13.place(x=310,y=620)

img7=PhotoImage(file="under.png")

l14=Label(clogin,image=img7,background="white")
l14.place(x=563,y=615)

def clearsignup():
    flogin.place_forget(),fsignup.place(x=0,y=0,height=1080,width=1920)
    e1.delete(0,END)

b7=customtkinter.CTkButton(clogin,text="Signup",font=("informal roman regular",20),fg_color="white",
    text_color="black",border_width=0,width=45,hover_color="grey",
    command=lambda:[login_reset(),clearsignup()])
b7.place(x=567,y=622)

vdo1=Label(clogin,borderwidth=0,border=0)
vdo1.place(x=750,y=100)

player=tkvideo("loginvdeo1.mp4",vdo1,loop=1,size=(800,600))

player.play()

############### signup page ################

def register():
    
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="signon",autocommit=True)
            mycur=mydb.cursor()
            if e3.get()=='' or e4.get()=='' or e5.get()=='':
                messagebox.showerror("Error","all field required")
            
            fmail=0
            funame=0
            fpass=0
            fcheck=0

            if e3.get():
                url=("select * from register;")
                mycur.execute(url)
                datas=mycur.fetchall()

                
                for i in range(len(datas)):
                    fcheck=fcheck+0
                    if datas[int(i)][0]==e3.get():
                        messagebox.showerror("Error","User already exist ...Please use login tab to login")
                        fcheck=1
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
                else:
                    messagebox.showerror("Error","Password should have minimum 8 characters !!!")
                        
                if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(paschk)):
                        fpass=1
                else:
                        messagebox.showerror("Error","\t"+"Invalid password format!!!"+"\n"+
                        "Password should contain atleast one uppercase letter, lowercase letter,numeric character and special symbol")   

            if funame==1 and fmail==1 and fpass==1 and fcheck==0:
                val=(e3.get(),e4.get(),e5.get())
                url1=("insert into register value(%s,%s,%s)")
                mycur.execute(url1,val)
                messagebox.showinfo("success","Account has been Created Successfully!!!")

            mydb.close()
            signup_reset()

csignup=Canvas(fsignup,height=1090,width=1920,background="white",relief="ridge")
csignup.place(x=0,y=0)

def signup_reset():
    for widget in csignup.winfo_children():
        if isinstance(widget,tk.Entry):
            widget.delete(0,'end')

b8=customtkinter.CTkButton(csignup,text="Back",font=("Times",25,"underline"),
    width=50,hover_color="grey",fg_color="White",text_color="black",
    command=lambda:[signup_reset(),fsignup.place_forget(),fstartup.place(x=0,y=0,height=1080,width=1920)])
b8.place(x=1380,y=80)


l15=Label(csignup,text="Create an account",font=("harrington",60,"bold"),background="white",fg="black")
l15.place(x=800,y=150)

l16=Label(csignup,text="Let's get started with us",font=("footlight mt light",25),background="white",fg="grey")
l16.place(x=970,y=250)

l47=Label(csignup,text="Username :",font=("Times",20),bg="white",fg="#555555")
l47.place(x=800,y=325)

l47=Label(csignup,text="Mail id     :",font=("Times",20),bg="white",fg="#555555")
l47.place(x=800,y=395)

l47=Label(csignup,text="Password  :",font=("Times",20),bg="white",fg="#555555")
l47.place(x=800,y=465)

e3=Entry(csignup,bg="white",fg="black",font=("Times",20),width=30)
e3.place(x=935,y=330)

e4=Entry(csignup,bg="white",fg="black",font=("Times",20),width=30)
e4.place(x=935,y=400)

e5=Entry(csignup,bg="white",fg="black",font=("Times",20),width=30,show="*")
e5.place(x=935,y=470)

img20=PhotoImage(file="eye1.png")

img21=PhotoImage(file="eye2.png")

b18=Button(csignup,image=img20,borderwidth=0,background="white")

def view1(e):
    e5.configure(show="")
    b17.place_forget()
    b18.place(x=1375,y=470)

def view2(e):
    e5.configure(show="*")
    b18.place_forget()
    b17.place(x=1375,y=470)

b17=Button(csignup,image=img21,borderwidth=0,background="white")
b17.place(x=1375,y=470)

b17.bind('<Button-1>',view1)

b18.bind('<Button-1>',view2)

b9=customtkinter.CTkButton(csignup,text="Create Account",font=("informal roman regular",30),fg_color="black",
    text_color="white",corner_radius=5,width=250,
    command=register)
b9.place(x=1030,y=550)

l17=Label(csignup,text="Already have an account ? ",font=("footlight mt light",18),background="white",fg="grey")
l17.place(x=990,y=620)

img8=PhotoImage(file="under.png")

l18=Label(csignup,image=img8,background="white")
l18.place(x=1255,y=615)

b10=customtkinter.CTkButton(csignup,text="Login",font=("informal roman regular",20),fg_color="white",
    text_color="black",border_width=0,width=45,hover_color="grey",
    command=lambda:[signup_reset(),fsignup.place_forget(),flogin.place(x=0,y=0,height=1080,width=1920)])
b10.place(x=1265,y=622)

img9=PhotoImage(file="signup4.png")

l20=Label(csignup,image=img9,background="white")
l20.place(x=-2,y=-2)


################# main page ################

cmain=Canvas(fmain,height=1080,width=1920,background="white",relief="ridge")
cmain.place(x=0,y=0)

def askokcancel():
    logoutanswer=messagebox.askyesno("WARNING","ARE YOU SURE YOU WANT TO LOG OUT ?")
    if(logoutanswer==True):
        login_reset()
        fmain.place_forget()
        fstartup.place(x=0,y=0,height=1080,width=1920)
    elif(logoutanswer==False):
        return

b11=customtkinter.CTkButton(cmain,text="Logout",font=("Times",25,"underline"),border_width=2,
    width=120,hover_color="grey",fg_color="white",text_color="black",border_color="white",corner_radius=20,
    command=askokcancel)
b11.place(x=300,y=80)

l19=Label(cmain,text=" ",height=1080,width=40,background="#222222")
l19.place(x=0,y=0)

b12=customtkinter.CTkButton(cmain,text="Help",font=("times",20,"underline"),bg_color="#222222",
    fg_color="#222222",hover_color="black",text_color="white",command=webopen_help)
b12.place(x=80,y=700)

b13=customtkinter.CTkButton(cmain,text="About",font=("times",20,"underline"),bg_color="#222222",
    fg_color="#222222",hover_color="black",text_color="white",command=webopen_about)
b13.place(x=80,y=750)

l21=Label(fmain,text="\"Good communication \nis the bridge between \nconfusion and clarity.\"\n\n— Nat Turner",
    font=("Times",20,"italic"),fg="white",background="#222222")
l21.place(x=8,y=350)

img10=PhotoImage(file="logo.png")

l22=Label(fmain,image=img10,background="#222222")
l22.place(x=80,y=60)

img11=PhotoImage(file="signgirl.png")

l23=Label(fmain,image=img11,borderwidth=0)
l23.place(x=350,y=200)

img17=PhotoImage(file="voicetran.png")

l29=Label(fmain,image=img17,borderwidth=0)

def micenter(e):
    l29.place(x=498,y=75)
    b14.configure(bg="grey")

def micleave(e):
    l29.place_forget()
    b14.configure(bg="#e5e5e5")

img14=PhotoImage(file="mic1.png")

b14=Button(fmain,image=img14,relief="flat",bg="#e5e5e5",
    command=lambda:[fmain.place_forget(),fv_t.place(x=0,y=0,height=1080,width=1920)])
b14.place(x=585,y=370)

b14.bind("<Enter>",micenter)
b14.bind("<Leave>",micleave)

l26=Label(fmain,text="Voice\nTranslation",bg="#e5e5e5",font=("times",14))
l26.place(x=570,y=426)

img12=PhotoImage(file="signboy.png")

l24=Label(fmain,image=img12,borderwidth=0)
l24.place(x=750,y=210)

img18=PhotoImage(file="texttran.png")

l30=Label(fmain,image=img18,borderwidth=0)

def textenter(e):
    l30.place(x=770,y=15)
    b15.configure(bg="grey")

def textleave(e):
    l30.place_forget()
    b15.configure(bg="#d8d8d8")

img15=PhotoImage(file="text1.png")

b15=Button(fmain,image=img15,relief="flat",bg="#d8d8d8",
    command=lambda:[fmain.place_forget(),ft_t.place(x=0,y=0,height=1080,width=1920)])
b15.place(x=975,y=335)

b15.bind("<Enter>",textenter)
b15.bind("<Leave>",textleave)

l27=Label(fmain,text="Text\nTranslation",bg="#d8d8d8",font=("times",14))
l27.place(x=955,y=400)

img13=PhotoImage(file="signgirl4.png")

l25=Label(fmain,image=img13,borderwidth=0)
l25.place(x=1150,y=205)

img19=PhotoImage(file="handtran.png")

l31=Label(fmain,image=img19,borderwidth=0)

def handenter(e):
    l31.place(x=1100,y=15)
    b16.configure(bg="grey")

def handleave(e):
    l31.place_forget()
    b16.configure(bg="#dfdfdf")

img16=PhotoImage(file="hand1.png")

b16=Button(fmain,image=img16,relief="flat",bg="#dfdfdf",
    command=lambda:[fmain.place_forget(),fhand.place(x=0,y=0,height=1080,width=1920)])
b16.place(x=1275,y=390)

b16.bind("<Enter>",handenter)
b16.bind("<Leave>",handleave)


def deleteaccount():

    def delete():
    
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="signon",autocommit=True)
        mycur=mydb.cursor()
        val=(e1.get(),e2.get())
        url4=("delete from register where uname = %s and pass =%s")
        mycur.execute(url4,val)
        messagebox.showinfo("success","Account has been deleted Successfully!!!")
        fmain.place_forget(),flogin.place(x=0,y=0,height=1080,width=1920)       
        login_reset()

        mydb.close()

    deleteanswer=messagebox.askyesno("WARNING","ARE YOU SURE YOU WANT TO DELETE YOUR ACCOUNT ?")
    if(deleteanswer==True):
        delete()
    elif(deleteanswer==False):
        return
    

b48=customtkinter.CTkButton(cmain,text="Delete Account ?",font=("times",20,"underline"),bg_color="#222222",
    fg_color="#222222",hover_color="black",text_color="white",command=deleteaccount)
b48.place(x=80,y=800)

l28=Label(fmain,text="Sign Language\nTranslation",bg="#dfdfdf",font=("times",16))
l28.place(x=1245,y=460)

################ voice to text ################

cv_t=Canvas(fv_t,height=1080,width=1920,background="white",relief="ridge")
cv_t.place(x=0,y=0)

img30=PhotoImage(file="vtbgpic.png")

l63=Label(cv_t,image=img30,bg="white",border=0)
l63.place(x=-50,y=-70)

def reset_vt():
    for widget in fv_t.winfo_children():
        if isinstance(widget,tk.Text):
            widget.delete('1.0','end')

b21=customtkinter.CTkButton(cv_t,text="Home",font=("Times",25,"underline"),border_width=2,
    width=120,hover_color="grey",fg_color="white",text_color="black",border_color="white",corner_radius=20,
    command=lambda:[reset_vt(),fv_t.place_forget(),fmain.place(x=0,y=0,height=1080,width=1920)])
b21.place(x=300,y=80)

l32=Label(cv_t,text=" ",height=1080,width=40,background="#222222")
l32.place(x=0,y=0)

b22=customtkinter.CTkButton(cv_t,text="Help",font=("times",20,"underline"),bg_color="#222222",
    fg_color="#222222",hover_color="black",text_color="white",command=webopen_help)
b22.place(x=80,y=700)

b23=customtkinter.CTkButton(cv_t,text="About",font=("times",20,"underline"),bg_color="#222222",
    fg_color="#222222",hover_color="black",text_color="white",command=webopen_about)
b23.place(x=80,y=750)

l33=Label(cv_t,text="\"The most important \nthing in communication \nis to hear what\nisn't being said.\"\n\n— Peter Drucker",
    font=("Times",19,"italic"),fg="white",background="#222222")
l33.place(x=15,y=350)


l34=Label(fv_t,image=img10,background="#222222")
l34.place(x=80,y=60)

lang_list = ('afrikaans','albanian','amharic','arabic',
    'armenian','azerbaijani','basque','belarusian',
    'bengali','bosnian','bulgarian','catalan','cebuano',
    'chichewa','chinese (simplified)','chinese (traditional)',
    'corsican','croatian','czech','danish','dutch',
    'english','esperanto','estonian','filipino','finnish',
    'french','frisian','galician','georgian','german',
    'greek','gujarati','haitian creole','hausa',
    'hawaiian','hebrew','hindi','hmong','hungarian',
    'icelandic','igbo','indonesian',
    'irish','italian','japanese','javanese',
    'kannada','kazakh','khmer','korean','kurdish (kurmanji)',
    'kyrgyz','lao','latvian','lithuanian','luxembourgish',
    'macedonian','malagasy','malay','malayalam','maltese',
    'maori','marathi','mongolian','myanmar (burmese)',
    'nepali','norwegian','odia','pashto','persian',
    'polish','portuguese','punjabi','romanian','russian',
    'samoan','scots gaelic','serbian','sesotho',
    'shona','sindhi','sinhala','slovak','slovenian',
    'somali','spanish','sundanese','swahili','swedish',
    'tajik','tamil','telugu','thai','turkish',
    'ukrainian','urdu','uyghur','uzbek','vietnamese','welsh',
    'xhosa','yiddish','yoruba','zulu')


lang_code = ('afrikaans', 'af', 'albanian', 'sq',
    'amharic', 'am', 'arabic', 'ar',
    'armenian', 'hy', 'azerbaijani', 'az',
    'basque', 'eu', 'belarusian', 'be',
    'bengali', 'bn', 'bosnian', 'bs', 'bulgarian',
    'bg', 'catalan', 'ca', 'cebuano',
    'ceb', 'chichewa', 'ny', 'chinese (simplified)',
    'zh-cn', 'chinese (traditional)',
    'zh-tw', 'corsican', 'co', 'croatian', 'hr',
    'czech', 'cs', 'danish', 'da', 'dutch',
    'nl', 'english', 'en', 'esperanto', 'eo',
    'estonian', 'et', 'filipino', 'tl', 'finnish',
    'fi', 'french', 'fr', 'frisian', 'fy', 'galician',
    'gl', 'georgian', 'ka', 'german',
    'de', 'greek', 'el', 'gujarati', 'gu',
    'haitian creole', 'ht', 'hausa', 'ha',
    'hawaiian', 'haw', 'hebrew', 'he', 'hindi',
    'hi', 'hmong', 'hmn', 'hungarian',
    'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian',
    'id', 'irish', 'ga', 'italian',
    'it', 'japanese', 'ja', 'javanese', 'jw',
    'kannada', 'kn', 'kazakh', 'kk', 'khmer',
    'km', 'korean', 'ko', 'kurdish (kurmanji)',
    'ku', 'kyrgyz', 'ky', 'lao', 'lo',
    'latin', 'la', 'latvian', 'lv', 'lithuanian',
    'lt', 'luxembourgish', 'lb',
    'macedonian', 'mk', 'malagasy', 'mg', 'malay',
    'ms', 'malayalam', 'ml', 'maltese',
    'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian',
    'mn', 'myanmar (burmese)', 'my',
    'nepali', 'ne', 'norwegian', 'no', 'odia', 'or',
    'pashto', 'ps', 'persian', 'fa',
    'polish', 'pl', 'portuguese', 'pt', 'punjabi',
    'pa', 'romanian', 'ro', 'russian',
    'ru', 'samoan', 'sm', 'scots gaelic', 'gd',
    'serbian', 'sr', 'sesotho', 'st',
    'shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si',
    'slovak', 'sk', 'slovenian', 'sl',
    'somali', 'so', 'spanish', 'es', 'sundanese',
    'su', 'swahili', 'sw', 'swedish',
    'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu',
    'te', 'thai', 'th', 'turkish',
    'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur',
    'ug', 'uzbek', 'uz',
    'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
    'yiddish', 'yi', 'yoruba',
    'yo', 'zulu', 'zu')

l68=Label(cv_t,text="Select your input language  : ",font=("Times",19),bg="white",fg="black")
l68.place(x=580,y=190)

combo5=customtkinter.CTkComboBox(cv_t,values=lang_list,font=("Robot",15),
    button_color="#28869D",button_hover_color="cyan",bg_color="white",text_color="black",
    width=250)
combo5.place(x=900,y=200)
combo5.set("english")

l69=Label(cv_t,text="Select your output language : ",font=("Times",19),bg="white",fg="black")
l69.place(x=580,y=290)

combo6=customtkinter.CTkComboBox(cv_t,values=lang_list,font=("Robot",15),
    button_color="#28869D",button_hover_color="cyan",bg_color="white",text_color="black",
    width=250)
combo6.place(x=900,y=300)
combo6.set("english")


def v_t_function1():
    
    def takecommand():

        r = sr.Recognizer()
        with sr.Microphone() as source:
            #print("listening.....")
            messagebox.showinfo("listening","say something....")
            r.pause_threshold = 1
            audio = r.listen(source)
    
        try:
            #print("Recognizing.....")
            messagebox.showinfo("Please wait","\t\tRecognizing....\nThis may take some time according to the content you have said.")
            query = r.recognize_google(audio, language=input_lang)
            #print(f"The User said {query}\n")
        except Exception as e:
            #print("say that again please.....")
            messagebox.showinfo("Error while listening","say that again please....")
            return "None"
        return query

    input_lang=combo5.get()

    input_lang=lang_code[lang_code.index(input_lang)+1]

    output_lang=combo6.get()

    output_lang=lang_code[lang_code.index(output_lang)+1]

    query = takecommand()
    while (query == "None"):
        query = takecommand()

    to_lang = output_lang

    translator = Translator()

    text_to_translate = translator.translate(query, dest=to_lang)

    text = text_to_translate.text

    t4.delete(1.0,END)
    t4.insert(END,text)


t4=Text(fv_t,font="Robot 16",bg="light blue",relief="groove",wrap="word",fg="black")
t4.place(x=563,y=520,height=192,width=605)

scrollbar4=Scrollbar(t4,width=20,cursor="hand2")
scrollbar4.pack(side="right",fill="y")

scrollbar4.configure(command=t4.yview)
t4.configure(yscrollcommand=scrollbar4.set)

b39=customtkinter.CTkButton(cv_t,text="Start Recording",font=("Robot",20),
    fg_color="#28869D",text_color="white",hover_color="blue",bg_color="white",
    border_width=0,height=45,command=v_t_function1)
b39.place(x=680,y=400)

b40=customtkinter.CTkButton(cv_t,text="Reset",font=("Robot",20),
    fg_color="#28869D",text_color="white",hover_color="red",bg_color="white",
    border_width=0,height=45,command=reset_vt)
b40.place(x=880,y=400)

l62=Label(cv_t,text="Want to  translate into speech ? click here",bg="black",fg="white",
    font=("Times",20,"italic"))
l62.place(x=620,y=790)

b42=Button(cv_t,image=img2,bg="black",relief="flat",
    command=lambda:[reset_vt(),fv_t.place_forget(),fv_v.place(x=0,y=0,width=1920,height=1920)])
b42.place(x=1100,y=770)

################ voice to voice  #########################

cv_v=Canvas(fv_v,height=1080,width=1920,background="white",relief="ridge")
cv_v.place(x=0,y=0)

img31=PhotoImage(file="vvbgpic.png")

l64=Label(cv_v,image=img31,bg="white",border=0)
l64.place(x=-28,y=-28)

b41=customtkinter.CTkButton(cv_v,text="Home",font=("Times",25,"underline"),border_width=2,
    width=120,hover_color="grey",fg_color="white",text_color="black",border_color="white",corner_radius=20,
    command=lambda:[fv_v.place_forget(),fmain.place(x=0,y=0,height=1080,width=1920)])
b41.place(x=300,y=80)

l65=Label(cv_v,text=" ",height=1080,width=40,background="#222222")
l65.place(x=0,y=0)

b42=customtkinter.CTkButton(cv_v,text="Help",font=("times",20,"underline"),bg_color="#222222",
    fg_color="#222222",hover_color="black",text_color="white",command=webopen_help)
b42.place(x=80,y=700)

b43=customtkinter.CTkButton(cv_v,text="About",font=("times",20,"underline"),bg_color="#222222",
    fg_color="#222222",hover_color="black",text_color="white",command=webopen_about)
b43.place(x=80,y=750)

l66=Label(cv_v,text="\"My belief is that \ncommunication is the \nbest way to create \nstrong relationships.\"\n\n— Jada Pinkett Smith",
    font=("Times",19,"italic"),fg="white",background="#222222")
l66.place(x=34,y=350)


l67=Label(cv_v,image=img10,background="#222222")
l67.place(x=80,y=60)

l70=Label(cv_v,text="Select your input language  : ",font=("Times",19),bg="white",fg="black")
l70.place(x=580,y=120)

combo7=customtkinter.CTkComboBox(cv_v,values=lang_list,font=("Robot",15),
    button_color="#28869D",button_hover_color="cyan",bg_color="white",text_color="black",
    width=250)
combo7.place(x=900,y=130)
combo7.set("english")

l71=Label(cv_v,text="Select your output language : ",font=("Times",19),bg="white",fg="black")
l71.place(x=580,y=220)

combo8=customtkinter.CTkComboBox(cv_v,values=lang_list,font=("Robot",15),
    button_color="#28869D",button_hover_color="cyan",bg_color="white",text_color="black",
    width=250)
combo8.place(x=900,y=230)
combo8.set("english")

def v_v_function():
    def v_v_function1():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            #print("listening.....")
            messagebox.showinfo("listening","say something....")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            #print("Recognizing.....")
            messagebox.showinfo("Please wait","\t\tRecognizing....\nThis may take some time according to the content you have said.")
            query = r.recognize_google(audio, language=input_language)
            #print(f"The User said {query}\n")
        except Exception as e:
            #print("say that again please.....")
            messagebox.showinfo("Error","say that again please....")
            return "None"
        return query


    input_language=combo7.get()
    input_language=lang_code[lang_code.index(input_language)+1]
    # Input from user
    # Make input to lowercase
    query = v_v_function1()
    while (query == "None"):
        query = v_v_function1()



    to_lang = combo8.get()

    to_lang = lang_code[lang_code.index(to_lang)+1]

    # invoking Translator
    translator = Translator()

    # Translating from src to dest
    text_to_translate = translator.translate(query, dest=to_lang)

    text = text_to_translate.text

    # Using Google-Text-to-Speech ie, gTTS() method
    # to speak the translated text into the
    # destination language which is stored in to_lang.
    # Also, we have given 3rd argument as False because
    # by default it speaks very slowly
    speak = gTTS(text=text, lang=to_lang, slow=False)

    # Using save() method to save the translated
    # speech in capture_voice.mp3
    speak.save("recorded_voice.mp3")

    messagebox.showinfo("Finished","Click on Play button to hear the translated voice....")    
    # Using OS module to run the translated voice.
    #playsound('recorded_voice.mp3')
    #os.remove('recorded_voice.mp3')

    # Printing Output
    # print(text)


def play_v_v():
    try:
        playsound('recorded_voice.mp3')
        os.remove('recorded_voice.mp3')
    except Exception as e:
        messagebox.showerror("Error","You haven't recorded any input voice yet") 

b44=customtkinter.CTkButton(cv_v,text="Start Recording",font=("Robot",20),
    fg_color="#28869D",text_color="white",hover_color="blue",bg_color="white",
    border_width=0,height=45,command=v_v_function)
b44.place(x=500,y=350)

b45=customtkinter.CTkButton(cv_v,text="Play",font=("Robot",20),
    fg_color="#28869D",text_color="white",hover_color="blue",bg_color="white",
    border_width=0,height=45,command=play_v_v)
b45.place(x=1150,y=350)


l72=Label(cv_v,text="Want to  translate into text ? click here",bg="#acacac",fg="black",
    font=("Times",20,"italic"))
l72.place(x=620,y=790)

b46=Button(cv_v,image=img14,bg="#acacac",relief="flat",
    command=lambda:[fv_v.place_forget(),fv_t.place(x=0,y=0,width=1920,height=1920)])
b46.place(x=1100,y=770)


################ text to text ################

ct_t=Canvas(ft_t,height=1080,width=1920,background="white",relief="ridge",bg="white")
ct_t.place(x=-1,y=-5)

# vdo2=Label(ct_t,borderwidth=0,border=0,bg="white")
# vdo2.place(x=-28,y=-28)

# player1=tkvideo("ttbgvideo.mp4",vdo2,loop=1,size=(1820,980))

# player1.play()

img29=PhotoImage(file="ttbgpic.png")

l64=Label(ct_t,image=img29,bg="white",border=0)
l64.place(x=-28,y=-28)

def translate():
    try:
        text_=t1.get(1.0,END)
        text_1=Translator()
        trans_text=text_1.translate(text_,src=combo1.get(),dest=combo2.get())
        trans_text=trans_text.text

        t2.delete(1.0,END)
        t2.insert(END,trans_text)
    except Exception as e:

        messagebox.showerror("google trans","please try again")

def reset_tt():
    for widget in ft_t.winfo_children():
        if isinstance(widget,tk.Text):
            widget.delete('1.0','end')

b24=customtkinter.CTkButton(ct_t,text="Home",font=("Times",25,"underline"),border_width=2,
    width=120,hover_color="grey",fg_color="white",text_color="black",border_color="white",corner_radius=20,
    command=lambda:[reset_tt(),ft_t.place_forget(),fmain.place(x=0,y=0,height=1080,width=1920)])
b24.place(x=300,y=80)

l35=Label(ct_t,text=" ",height=1080,width=40,background="#222222")
l35.place(x=0,y=0)

b25=customtkinter.CTkButton(ct_t,text="Help",font=("times",20,"underline"),bg_color="#222222",
    fg_color="#222222",hover_color="black",text_color="white",command=webopen_help)
b25.place(x=80,y=700)

b26=customtkinter.CTkButton(ct_t,text="About",font=("times",20,"underline"),bg_color="#222222",
    fg_color="#222222",hover_color="black",text_color="white",command=webopen_about)
b26.place(x=80,y=750)

l36=Label(ct_t,
    text="\"You never know \nwhen a moment \nand a few sincere words \ncan have an \nimpact on a life\"\n\n— Zig Ziglar",
    font=("Times",19,"italic"),fg="white",background="#222222")
l36.place(x=10,y=350)


l37=Label(ft_t,image=img10,background="#222222")
l37.place(x=80,y=60)

language=googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()

l43=Label(ft_t,text="Input language : ",font="Times 20",fg="black",bg="white")
l43.place(x=660,y=100)

combo1=customtkinter.CTkComboBox(ft_t,values=languageV,font=("Robot",15),
    button_color="#28869D",button_hover_color="cyan",bg_color="white",text_color="black",
    width=250)
combo1.place(x=850,y=105)
combo1.set("English")

t1=Text(ft_t,font="Robot 16",bg="light blue",relief="groove",wrap="word",fg="black")
t1.place(x=585,y=155,height=195,width=605)

scrollbar1=Scrollbar(t1,width=20,cursor="hand2")
scrollbar1.pack(side="right",fill="y")

scrollbar1.configure(command=t1.yview)
t1.configure(yscrollcommand=scrollbar1.set)

l44=Label(ft_t,text="Output language : ",font="Times 20",fg="black",bg="white")
l44.place(x=660,y=465)

combo2=customtkinter.CTkComboBox(ft_t,values=languageV,font=("Robot",15),
    button_color="#28869D",button_hover_color="cyan",bg_color="white",text_color="black",
    width=250)
combo2.place(x=860,y=470)
combo2.set("Select Language")


t2=Text(ft_t,font="Robot 16",bg="light blue",relief="groove",wrap="word",fg="black")
t2.place(x=585,y=555,height=192,width=605)

scrollbar2=Scrollbar(t2,width=20,cursor="hand2")
scrollbar2.pack(side="right",fill="y")

scrollbar2.configure(command=t2.yview)
t2.configure(yscrollcommand=scrollbar2.set)


b27=customtkinter.CTkButton(ft_t,text="Translate",font=("Robot",20),
    fg_color="#28869D",text_color="white",hover_color="light blue",bg_color="white",
    border_width=0,height=45,command=translate,corner_radius=5)
b27.place(x=720,y=400)

b28=customtkinter.CTkButton(ft_t,text="Reset",font=("Robot",20),
    fg_color="#28869D",text_color="white",hover_color="#FFCCCB",bg_color="white",
    border_width=0,height=45,command=reset_tt)
b28.place(x=880,y=400)

l38=Label(ft_t,text="Want to  translate into speech ? click here",bg="white",fg="black",
    font=("Times",20,"italic"))
l38.place(x=620,y=790)

b29=Button(ft_t,image=img14,bg="white",relief="flat",
    command=lambda:[reset_tt(),ft_t.place_forget(),ft_v.place(x=0,y=0,width=1920,height=1920)])
b29.place(x=1100,y=770)


################ text to voice #################

ct_v=Canvas(ft_v,height=1080,width=1920,background="white",relief="ridge")
ct_v.place(x=0,y=0)

# vdo3=Label(ct_v,borderwidth=0,border=0,bg="white")
# vdo3.place(x=-50,y=-70)

# player2=tkvideo("tvbgvideo.mp4",vdo3,loop=1,size=(1820,980))

# player2.play()

img28=PhotoImage(file="tvbgpic.png")

l63=Label(ct_v,image=img28,bg="white",border=0)
l63.place(x=-50,y=-70)

def reset_tv():
    for widget in ft_v.winfo_children():
        if isinstance(widget,tk.Text):
            widget.delete('1.0','end')


b30=customtkinter.CTkButton(ct_v,text="Home",font=("Times",25,"underline"),border_width=2,
    width=120,hover_color="grey",fg_color="white",text_color="black",border_color="white",corner_radius=20,
    command=lambda:[reset_tv(),ft_v.place_forget(),fmain.place(x=0,y=0,height=1080,width=1920)])
b30.place(x=300,y=80)

l49=Label(ct_v,text=" ",height=1080,width=40,background="#222222")
l49.place(x=0,y=0)

b31=customtkinter.CTkButton(ct_v,text="Help",font=("times",20,"underline"),bg_color="#222222",
    fg_color="#222222",hover_color="black",text_color="white",command=webopen_help)
b31.place(x=80,y=700)

b32=customtkinter.CTkButton(ct_v,text="About",font=("times",20,"underline"),bg_color="#222222",
    fg_color="#222222",hover_color="black",text_color="white",command=webopen_about)
b32.place(x=80,y=750)

l50=Label(ct_v,text="\"Communication leads \nto community, that is,\nto understanding,\nintemacy and \nmutual valuing.\"\n\n— Rollo May",
    font=("Times",19,"italic"),fg="white",background="#222222")
l50.place(x=20,y=350)


l51=Label(ft_v,image=img10,background="#222222")
l51.place(x=80,y=60)

l55=Label(ct_v,text="Select your input language : ",font="Times 19",fg="black",bg="white")
l55.place(x=580,y=95)

combo3=customtkinter.CTkComboBox(ct_v,values=lang_list,font=("Robot",15),
    button_color="#28869D",button_hover_color="cyan",bg_color="white",text_color="black",
    width=250)
combo3.place(x=880,y=100)
combo3.set("english")

t3=Text(ft_v,font="Robot 16",bg="light blue",relief="groove",wrap="word")
t3.place(x=540,y=143,height=200,width=660)

scrollbar3=Scrollbar(t3,width=20,cursor="hand2")
scrollbar3.pack(side="right",fill="y")

scrollbar3.configure(command=t3.yview)
t3.configure(yscrollcommand=scrollbar3.set)

l57=Label(ct_v,text="Select your output language : ",font=("Times",19),fg="black",bg="white")
l57.place(x=580,y=495)

combo4=customtkinter.CTkComboBox(ct_v,values=lang_list,font=("Robot",15),
    button_color="#28869D",button_hover_color="cyan",bg_color="white",text_color="black",
    width=250)
combo4.place(x=880,y=500)
combo4.set("english")


b36=customtkinter.CTkButton(ct_v,text="Reset",font=("Robot",20),
    fg_color="#28869D",text_color="white",hover_color="red",
    border_width=0,height=45,command=reset_tv)
b36.place(x=800,y=410)

l59=Label(ct_v,text="Want to  translate into text ? click here",bg="white",
    font=("Times",19,"italic"))
l59.place(x=620,y=780)


def translate1():
    try:
        
        dic = ('afrikaans', 'af', 'albanian', 'sq',
            'amharic', 'am', 'arabic', 'ar',
            'armenian', 'hy', 'azerbaijani', 'az',
            'basque', 'eu', 'belarusian', 'be',
            'bengali', 'bn', 'bosnian', 'bs', 'bulgarian',
            'bg', 'catalan', 'ca', 'cebuano',
            'ceb', 'chichewa', 'ny', 'chinese (simplified)',
            'zh-cn', 'chinese (traditional)',
            'zh-tw', 'corsican', 'co', 'croatian', 'hr',
            'czech', 'cs', 'danish', 'da', 'dutch',
            'nl', 'english', 'en', 'esperanto', 'eo',
            'estonian', 'et', 'filipino', 'tl', 'finnish',
            'fi', 'french', 'fr', 'frisian', 'fy', 'galician',
            'gl', 'georgian', 'ka', 'german',
            'de', 'greek', 'el', 'gujarati', 'gu',
            'haitian creole', 'ht', 'hausa', 'ha',
            'hawaiian', 'haw', 'hebrew', 'he', 'hindi',
            'hi', 'hmong', 'hmn', 'hungarian',
            'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian',
            'id', 'irish', 'ga', 'italian',
            'it', 'japanese', 'ja', 'javanese', 'jw',
            'kannada', 'kn', 'kazakh', 'kk', 'khmer',
            'km', 'korean', 'ko', 'kurdish (kurmanji)',
            'ku', 'kyrgyz', 'ky', 'lao', 'lo',
            'latin', 'la', 'latvian', 'lv', 'lithuanian',
            'lt', 'luxembourgish', 'lb',
            'macedonian', 'mk', 'malagasy', 'mg', 'malay',
            'ms', 'malayalam', 'ml', 'maltese',
            'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian',
            'mn', 'myanmar (burmese)', 'my',
            'nepali', 'ne', 'norwegian', 'no', 'odia', 'or',
            'pashto', 'ps', 'persian', 'fa',
            'polish', 'pl', 'portuguese', 'pt', 'punjabi',
            'pa', 'romanian', 'ro', 'russian',
            'ru', 'samoan', 'sm', 'scots gaelic', 'gd',
            'serbian', 'sr', 'sesotho', 'st',
            'shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si',
            'slovak', 'sk', 'slovenian', 'sl',
            'somali', 'so', 'spanish', 'es', 'sundanese',
            'su', 'swahili', 'sw', 'swedish',
            'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu',
            'te', 'thai', 'th', 'turkish',
            'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur',
            'ug', 'uzbek', 'uz',
            'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
            'yiddish', 'yi', 'yoruba',
            'yo', 'zulu', 'zu')


        inputstring=t3.get(1.0,END)

        inputlang=combo3.get()

        outputlang=combo4.get()


        def translate():
            try:
                text_=inputstring
                text_1=Translator()
                trans_text=text_1.translate(text_,src=inputlang,dest=outputlang)
                trans_text=trans_text.text
                return trans_text
            
            except Exception as e:
                messagebox.showerror("Error in translation","Please try again")
            
        query=translate()
            

        to_lang = dic[dic.index(outputlang)+1]

        translator = Translator()

        text_to_translate = translator.translate(query, dest=to_lang)

        text = text_to_translate.text

        speak = gTTS(text=text, lang=to_lang, slow=False)

        speak.save("captured_voice.mp3")

        playsound('captured_voice.mp3')
        os.remove('captured_voice.mp3')

    except:
        messagebox.showerror("Error","Please try again")


# l60=Label(ct_v,text="Click here to play the translated voice",bg="white",
#     font=("Times",20,"italic"))
# l60.place(x=620,y=700)


img26=PhotoImage(file="playbutton.png")

b38=Button(ct_v,image=img26,bg="white",relief="flat",command=translate1)
b38.place(x=950,y=630)


b37=Button(ct_v,image=img15,bg="white",relief="flat",
    command=lambda:[reset_tv(),ft_v.place_forget(),ft_t.place(x=0,y=0,width=1920,height=1920)])
b37.place(x=1040,y=770)


################ hand #################

chand=Canvas(fhand,height=1080,width=1920,background="white",relief="ridge")
chand.place(x=0,y=0)

img32=PhotoImage(file="handbgpic.png")

l73=Label(chand,image=img32,bg="white",border=0)
l73.place(x=200,y=0)

b33=customtkinter.CTkButton(chand,text="Home",font=("Times",25,"underline"),border_width=2,
    width=120,hover_color="grey",fg_color="#BADCFF",text_color="black",border_color="#BADCFF",
    corner_radius=20,bg_color="#BADCFF",
    command=lambda:[fhand.place_forget(),fmain.place(x=0,y=0,height=1080,width=1920)])
b33.place(x=300,y=80)

l52=Label(chand,text=" ",height=1080,width=40,background="#222222")
l52.place(x=0,y=0)

b34=customtkinter.CTkButton(chand,text="Help",font=("times",20,"underline"),bg_color="#222222",
    fg_color="#222222",hover_color="black",text_color="white",command=webopen_help)
b34.place(x=80,y=700)

b35=customtkinter.CTkButton(chand,text="About",font=("times",20,"underline"),bg_color="#222222",
    fg_color="#222222",hover_color="black",text_color="white",command=webopen_about)
b35.place(x=80,y=750)

l53=Label(chand,text="\"The ability to \nsimplify means to \neliminate the \nunnecessary so that\nthe necessary may\nspeak.\"\n\n— Hans Hofmann",
    font=("Times",19,"italic"),fg="white",background="#222222")
l53.place(x=38,y=350)


l54=Label(chand,image=img10,background="#222222")
l54.place(x=80,y=60)


def opencamera():
    if __name__=="__main__":
        main()

b47=customtkinter.CTkButton(chand,text="Open Camera",font=("times",23,"underline"),bg_color="#BADCFF",
    fg_color="black",hover_color="grey",text_color="white",command=opencamera,width=230,height=50)
b47.place(x=785,y=520)

img33=PhotoImage(file="handchatbox.png")

l74=Label(chand,image=img33,borderwidth=0)

def chatboxappear(e):
    l74.place(x=598,y=375)

def chatboxdisappear(e):
    l74.place_forget()

b47.bind("<Enter>",chatboxappear)

b47.bind("<Leave>",chatboxdisappear)

fstartup.place(x=0,y=0,height=1080,width=1920)

#test_net()

root.mainloop()