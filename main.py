import tkinter as tk
#import mysql.connector
from tkinter import filedialog
from tkinter.filedialog import askopenfile

import PIL.ImageOps
from PIL import ImageTk, Image, ImageFilter
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Sejal Modi\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
root=tk.Tk()
root.title("THROUGH IMAGE TEXT EXTRACT")
#connection=mysql.connector.connect(host="localhost",user="root",port='3306',database='image')
root.geometry('1000x700+200+50')
root.configure(bg="#123123")
lbl1=tk.Label(root,text="UPLOAD IMAGE IN LOCALDISK",font=("bold",40),fg="pink",background="grey")
lbl1.grid(padx=100,pady=15,row=0,column=2)

def upload():
    global img
    f_types=[('jpg Files',"*.jpg"),('png Files',"*.png"),('jpeg Files',"*.jpeg")]
    name=filedialog.askopenfilename(filetypes=f_types)
    if name:
        img=Image.open(name)
        #FILTER
        img = img.filter(ImageFilter.Kernel((3, 3),(-1, -1, -1, -1, 9, -1, -1, -1, -1), 1, 0))
        #gray image
        img=PIL.ImageOps.grayscale(img)

        img=img.resize((400,400))
        tex = pytesseract.pytesseract.image_to_string(img)
        #FOR LINK TO TK WINDOW
        img=ImageTk.PhotoImage(img)

        #b2 = tk.Button(root, image=img)  # using Button
        #b2.grid(row=3, column=1)


        t=tk.Text(root,height=30,width=75,padx=15,pady=15)
        t.insert(1.0,tex)

        t.grid(column=2,row=4)


btn=tk.Button(root,text="UPLOAD FILE",font=("arial",15),fg="white",bg="purple",command=lambda :upload())
btn.grid(padx=5,pady=5,row=1,column=2)

root.mainloop()