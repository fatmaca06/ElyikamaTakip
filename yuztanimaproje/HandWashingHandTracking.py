import cv2 #opencv kütüphanesi
import mediapipe as mp   #Mediapipe kütüphanesi
import time #fps için kullanacağımız
import HandTrackingModule as htm #bu dosyaya yazmış olduğumuz modülü yani sınıfımızı çağırdık  burada el yıkama modülünü oluşturacağız
# bu şekilde modülden çekme sebebim değişkenleri metodlara ve değişkenşlere fazladan tanımlama yapmamak için sınıf kullandık

pTime = 0  # önceki zamanı 0a eşitledik kare hızını belirlemek için yani fps
cTime = 0  # şimdiki zamanıda 0a eşitledik
cap = cv2.VideoCapture(0) #kamradan görüntü alma kodumuz
detector = htm.handDetector()  # yukarıda varsayılan parametreler sahip
while True:
    success, img = cap.read()  # kameramızı oluşturduk
    img = detector.findHands(img,draw=True )  # aldığımız görüntüyü yani imgi gönderiyoruz
    lmList = detector.findPosition(img, draw=True)  # noktaların konumunu istersek çizimleri görünür 7 görünmez yapabiliriz
    if len(lmList) != 0:  # listeleyeceğimiz listenin boyutu 0a eşit değilse ozaman listeleyeceğiz
        print(lmList[0], lmList[4], lmList[8],lmList[12],lmList[16],lmList[20])  # hangi indeksi yani noktayı istiyorsak baş parmak pozisyonları listeleyeceğiz
    # yani burada yaptığımız işlem beliritlen ve istenilen parmağın hangi x,  y koorinatlarında olduğunu listeleyip,
    # ona göre bir hareket belirlemek. İstenilen hareketi konuma göre oluşturacağız
    cTime = time.time() #şimdikizamanı tanımladıkq
    fps = 1 / (cTime - pTime) #burada fps hesabımızı yaptık
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255),
                3)  # fpsimiz ekranda belirlediğimiz konumda değerde yazdırdık
    cv2.imshow("Image", img)  # kameramızı çalıştırıdık
    k = cv2.waitKey(10) & 0xff  # Press 'q' for exiting video
    if k == ord('q'):
        break
