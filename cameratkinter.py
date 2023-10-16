import cv2
import numpy as np
import tkinter
from tkinter import *
import customtkinter

root=tkinter.Tk()
root.state('zoomed')

frame=Frame(root)

canvas=Canvas(frame,height=1080,width=1920,bg="white")
canvas.place(x=0,y=0)

def opencamera():
    cap=cv2.VideoCapture(0)

    cap.set(3,2000)
    cap.set(4,3000)

    while cap.isOpened():
            ret,frame=cap.read()

            #detection
            image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

            #flip on horizontal
            image=cv2.flip(image,1)

            #RGB to BGR
            image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
        
            cv2.imshow('image capturing',image)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

button=customtkinter.CTkButton(canvas,text="click here to open camera",
                               fg_color="blue",text_color="white",bg_color="white",
                               height=50,font=("Times",25),
                               command=opencamera)
button.place(x=680,y=480)

frame.place(x=0,y=0,height=1080,width=1920)

root.mainloop()