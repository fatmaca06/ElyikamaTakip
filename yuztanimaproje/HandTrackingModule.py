import cv2
import mediapipe as mp   #Mediapipe kütüphanesi
import time
class handDetector():
    def __init__(self,mode=False, maxHands = 2, detectionCon = 0.5, trackCon= 0.5 ): #oluşturuduğumuz sınıfın metodu
        self.mode = mode #değişkenlere ve metodlara self olmadan erişemeyiz #oluşan resmin biçimi
        self.maxHands = maxHands # görülecek el sayısı
        self.detectionCon = detectionCon #algılayıcı değer verisi
        self.trackCon = trackCon #izleyici değer verisi
        # el yıkama modülünü oluşturacağız
        self.mpHands = mp.solutions.hands  # mp kütüphanesinin bağlantılarını sağlamakta
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,self.detectionCon, self.trackCon) #mp kütüphanesinin değerleri
        self.mpDraw = mp.solutions.drawing_utils  # 21 farklı el içi noktaların çizimini sağlamakta


    def findHands(self,img, draw = True): #eli görmede kullanacağımız fonkiyn
     imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #rgb renk uzayını kullandık
     self.results = self.hands.process(imgRGB)
    #print(results.multi_hand_landmarks) #eli görüp görmediğini kontrol ettik eli görüce değerleri giriyor
     if self.results.multi_hand_landmarks : #eğer el algılanırsa döngüye sokup elin bilgileri çekmesini sağlayacağız, birden fazla el işareri
          for handLms in self.results.multi_hand_landmarks: #tek el handLms iki el için belirtebiliriz
              if draw:
                 self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS,self.mpDraw.DrawingSpec(color=(80, 22, 10), thickness=2, circle_radius=4),
                                  self.mpDraw.DrawingSpec(color=(80, 44, 121), thickness=2, circle_radius=2)
                                  )
     return img

    def findPosition(self, img, handNo=0, draw=True):

        lmList = []  #landmarks larımızı bu listin içine yazdıracağız bununla çağıracağız
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo] # hangi noktayı istiyoruz
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c = img.shape # düzlemde alacağımız değerler
                cx, cy = int(lm.x * w), int(lm.y * h) # x ve y düzleminde belirli noktalrın olduğu konumu bulma
                # print(id, cx, cy)
                lmList.append([id, cx, cy])  # hangi numaralı noktanın x ve y eksenine olan uzaklığının tutulması
                if draw:
                    cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED) #istenilen noktaların görüntüsü

        return lmList

def main():
    pTime = 0  # önceki zamanı 0a eşitledik kare hızını belirlemek için yani fps
    cTime = 0  # şimdiki zamanıda 0a eşitledik
    time.sleep(2.0)
    cap = cv2.VideoCapture(0)
    detector = handDetector() #yukarıda varsayılan parametreler sahip
    tipIds = [4,8,12,16,20]

    while True:
        success, img = cap.read()  # kameramızı oluşturduk
        img =  detector.findHands(img, draw= True)  #aldığımız görüntüyü yani imgi gönderiyoruz
        lmList = detector.findPosition(img, draw= True) #noktaların konumunu
        fingers = []
        if len(lmList) != 0: #listeleyeceğimiz listenin boyutu 0a eşit değilse ozaman listeleyeceğiz
            if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            for id in range(1,5):
             if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                 fingers.append(1)
             else:
                 fingers.append(0)
             total = fingers.count(1) #kaç tane parmak olduğnu hesaplattırıyoruz
             if total == 0:
                 print("Close")
             elif total == 5:
                 print("Open")

            # if lmList[8][2] < lmList[6][2]:
            #     print("Open")
            # else:
            #     print("Close")

            #print(lmList[4]) #hangi indeksi yani noktayı istiyorsak baş parmak pozisyonları listeleyeceğiz
        #yani burada yaptığımız işlem beliritlen ve istenilen parmağın hangi x,  y koorinatlarında olduğunu listeleyip,
        # ona göre bir hareket belirlemek. İstenilen hareketi konuma göre oluşturacağız
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255),3)  # fpsimiz ekranda belirlediğimiz konumda değerde yazdırdık
        cv2.imshow("Image", img)  # kameramızı çalıştırıdık
        cv2.waitKey(1)

if __name__ == "__main__":
    main()   #modülün  içeri aktarılmasında kullanıyoruz. neler yapacağınız yazıp ona göre çalışmasını sağlayacağız

