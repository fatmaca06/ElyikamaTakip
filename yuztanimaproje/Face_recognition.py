import cv2,os
import numpy as np
import pickle
id = 0
with open('Users.txt', encoding='utf8') as adsoyad:  #control centerdan alınan ismi burda da çektik
    for line in adsoyad:
        nameinfo = line.strip()
adsoyad.close()
names = ['None', nameinfo, 'X', 'A', 'B', 'C']
with open('labels', 'rb') as f:
	dicti = pickle.load(f)
	f.close()
#kendi görüntümüzü okuyarak kameradan görüntü alıyoruz
camera = cv2.VideoCapture(0)
camera.set(3,640)
camera.set(4,480)
minW = 0.1*camera.get(3)
minH = 0.1*camera.get(4)
path = os.path.dirname(os.path.abspath(__file__))  #dosya verilerinin yolunu elirledik
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml") #eğitme kısmında kaydettiğimiz verileri burda okuyoruz
font = cv2.FONT_HERSHEY_SIMPLEX
while True:#kameradan alınan görüntü doğru olduğu sürece
    ret, im =camera.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) #kameradan okunan görüntüyü gri tona çevir
    #yukarıdaoluşturduğumuz değişkeni
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100),flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces: #belirtiğimiz kordintattan yüzler içerinde tarama yapsın
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 2) #resmin üzerinde diktörtgen oluşturduk
#tarama yaptığı yüzlerden kişiyi tahminettrdiğimiz kısım
        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
        if (confidence < 100):
#tahmin edlien kişi id bilgisinden çektiği verilerle karşılaştırma yapıp kıyaslamadaki doğruluk oranına göre
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
            exec(open("mailgondermedeneme.py").read())

        else:
#doğruluk oranına göre tahn edilen kişinin eşleşip eşleşmediğini kontrol eder ve değeri yazdırır
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))

        cv2.putText(im, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        cv2.putText(im, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)
        #çercevenin alt kısmında değeri yazrdırdık

    cv2.imshow("Kisi Onizleme.", im)
    k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
camera.release()
cv2.destroyAllWindows()