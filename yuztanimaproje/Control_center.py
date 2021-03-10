from tkinter import *
from tkinter import messagebox
import os
import shutil
import cv2
from PIL import Image, ImageTk


controlCenter = Tk() #form oluşturduk
controlCenter.title ("Health For My Child") #başlık ismi
controlCenter.configure(bg='#262626')

#ekranıortalaması için kullanılan kod
widthwindow = 1024 #formun boyutu ayarlanıp yükseklikve genişliğe göre ekranda konumu ortalandı
heightwinddow = 720
screenwidht = controlCenter.winfo_screenwidth()
screenheight= controlCenter.winfo_screenheight()
xcoor = (screenwidht/2) - (widthwindow/2)
ycoor = (screenheight/2)- (heightwinddow/2)

controlCenter.geometry("%dx%d+%d+%d" % (widthwindow, heightwinddow,xcoor,ycoor))
controlCenter.resizable(width=False,height=False) #form ekranının boyutunu sabit tutuyor

name = StringVar()
fpath = './images'

#width, height = 640, 480
cap = cv2.VideoCapture(0)
cameraDisplay = Label(controlCenter, highlightthickness=0, bd = 0)
cameraDisplay.place(x=5, y=5)

###############FONKSİYON TANIM BAŞLANGIÇ###############
def show_frame(): #bu kısımda ayrı bir form açılmadan çalıtığımız form üzerinden yüz tanımayı çalıştırmaya çalışmıştım
    #ilerleyen zamanlarda geliştirlecektir
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image2 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image2)
    imgtk = ImageTk.PhotoImage(image=img)
    cameraDisplay.imgtk = imgtk
    cameraDisplay.configure(image=imgtk)
    cameraDisplay.after(10, show_frame)

def save_info(): #bilgilerin kayıt edilmesi için fonksiyonların tutulduğu kısım
    if os.path.isfile(fpath):
        shutil.rmtree('./images')
    adsoyad_info = name.get()
    file = open('Users.txt', 'w')#bu kısımda kullanıcı adı soyadı aldığımız bilgileri user.txt ye yazdırma kısmımız
    file.write (adsoyad_info)
    file.close()
    opennewuser()
    hide_newuser()
    calistirButton.place(x=5, y=680) #buttonun çalışacağı konum fonksiyonu

def hide_newuser():  #aynı form üzerinde tooların görünmesini çalışmasını kontroleden kısım
    L1.place_forget()
    E1.place_forget()
    kisiEkle.place_forget()
    newUserButton.place(x=5, y=638)
    L2.place(x=200, y=638)
    calistirButton.place(x=5, y=680)  # buttonun çalışacağı konum fonksiyonu
def show_newuser():#aynı form üzerinde tooların görünmesini çalışmasını kontroleden kısım
    newUserButton.place_forget()
    L1.place(x=5, y=638)
    E1.place(x=100, y=638)
    kisiEkle.place(x=290, y=638)
    calistirButton.place(x=5, y=680) #buttonun çalışacağı konum fonksiyonu

def opennewuser(): #formda arka planda new userın çalışmasını sağlayan fonk
   exec(open("New_user.py").read())

def face_recognition(): #yüz tanımayı çağıran fonk
    exec(open("Face_recognition.py").read())

def serial(): #yüz tanımayı çağıran fonk
  exec(open("mesafes.py").read())


####################FONKSİYON TANIM BİTİŞ####################



##################CANVAS BAŞLANGIÇ##################
canvaslogo = Canvas(controlCenter, width = 75, height = 90,highlightthickness=0, bg='#262626')
canvaslogo.place(x=948,y=632)
logofile = PhotoImage(file="./png/dpu-logo6.png")
canvaslogo.create_image(0,0, anchor=NW, image=logofile)

canvasline = Canvas(controlCenter, width = 1024, height = 3,highlightthickness=0, bg='#262626')
canvasline.place(y=627)
linefile = PhotoImage(file="./png/side.png")
canvasline.create_image(0,0, anchor=NW, image=linefile)
##################CANVAS BİTİŞ##################

#show_frame()
#toollarımızı tanımladığımız kısım
L1 = Label(controlCenter, text="Adınızı Girin: ",fg="#D9D9D9",font="Helvetica 12 ",highlightthickness=0, bd= 0, bg="#262626")
E1 = Entry(controlCenter,textvariable=name, fg="#262626",font="Helvetica 12 ",highlightthickness=0, bd= 0, bg="#D9D9D9")
kisiEkle = Button(controlCenter, text=" Kişi Ekle ",fg="#D9D9D9",font="Helvetica 12 ",highlightthickness=0, bd= 0, bg="#404040", command=save_info)
L2 = Label(controlCenter, text="Kişi Eklendi ! ",fg="#D9D9D9",font="Helvetica 12 ",highlightthickness=0, bd= 0, bg="#262626")
L2.place_forget()
newUserButton = Button(controlCenter, text = " Yeni Kişi Ekle ",fg="#D9D9D9",font="Helvetica 12 ",highlightthickness=0, bd= 0, bg="#404040",command = show_newuser)
newUserButton.place(x=5, y=638)
calistirButton = Button(controlCenter, text = " Çalıştır ",fg="#D9D9D9",font="Helvetica 12 ",highlightthickness=0, bd= 0, bg="#404040",command = serial)



controlCenter.mainloop()
