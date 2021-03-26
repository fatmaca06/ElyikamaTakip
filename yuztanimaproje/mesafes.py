import serial
import time
with serial.Serial('COM4',9600) as ser:


 while True:
  mesafe = int(ser.readline().decode("utf-8").strip('\n').strip('\r'))
  print(mesafe)

  if (mesafe>30 and mesafe<50): #bu mesafe aralığında kişi oolduğunda

   print("KİŞİ TANINMAKTA")
   exec(open("Face_recognition.py").read())
  else:
   print("İSTENİLEN MESAFEDE KİMSE YOK")

 #ser.close()


