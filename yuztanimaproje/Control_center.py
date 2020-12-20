from tkinter import *
from tkinter import messagebox
import os
import shutil


def save_info():
    shutil.rmtree('./images')
    adsoyad_info = name.get()
    file = open('Users.txt', 'w')
    file.write (adsoyad_info)
    file.close()
    opennewuser()
    hide_newuser()

def hide_newuser():
    L1.grid_remove()
    E1.grid_remove()
    kisiEkle.grid_remove()
def show_newuser():

    L1.grid(padx=780, pady=60)
    E1.grid(padx=780, pady=50)
    kisiEkle.grid(padx=780, pady=40)

def opennewuser():
   exec(open("New_user.py").read())
   # var = messagebox.showinfo("Uyarı", "www.yazilimbilisim")

controlCenter = Tk()
controlCenter.title ("Health For My Child")
#ekranıortalaması için kullanılan kod
widthwindow = 1024
heightwinddow = 720
screenwidht = controlCenter.winfo_screenwidth()
screenheight= controlCenter.winfo_screenheight()
xcoor = (screenwidht/2) - (widthwindow/2)
ycoor = (screenheight/2)- (heightwinddow/2)
controlCenter.geometry("%dx%d+%d+%d" % (widthwindow, heightwinddow,xcoor,ycoor))
controlCenter.resizable(width=False,height=False) #boyutunu değiştirmesin kimse

mainapp = Frame(controlCenter)
mainapp.grid()
name = StringVar()

L1 = Label(mainapp, text="Adınızı Girin",font="Helvetica 22 bold",fg="#52344c",bg ="#e0d9de")
E1 = Entry(mainapp,textvariable=name, bd=2,bg='#e0d9de',font="Helvetica 15",fg="#4f3149")
kisiEkle = Button(mainapp, text="Kişi Ekle",bd='20', command=save_info,bg="#c1b5be",font ="Helvetica 18 bold ",fg="#52344c")

newUserButton = Button( mainapp, text = " Yeni Kişi Ekle",bd='20',fg="#52344c",font="Helvetica 19 bold",bg="#c1b5be",command = show_newuser)
newUserButton.grid(padx=780, pady=20)
controlCenter.mainloop()
