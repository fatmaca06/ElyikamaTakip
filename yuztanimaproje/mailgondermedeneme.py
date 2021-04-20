import smtplib #gmail serverlarına bu modülü kullanarak göndereceğiz
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
# Gmail email sunucusuna bağlanıyoruz
try: #işlemi kontrol amaçlı bu blok içerisinde yazdım
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()#ben senin üzerinden mail göndereceğim anlamına gelen komut
    mail.starttls() #bilgileri gizleyerek mail servera gönderiyor.
    mail.login("*******@****.com", "******") #gmail servera giriş yapmak gerekiyor

    mesaj = MIMEMultipart()
    mesaj["From"] = "*******@****.com"           # Gönderen hesabın gmail olması gerekli
    mesaj["To"] = " *******@****.com"            # Alıcı
    mesaj["Subject"] = "COVID-19 Pandemi Sürecinde El Yıkama Alışkanlığı Takibi"    # Konusu

    body = """

 Kızınız Eve geldi, Ellerini Yikaması Beklenmektedir.!
    """

    body_text = MIMEText(body, "plain")  #
    mesaj.attach(body_text)

    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string()) #mailgönderme fonksiyonu
    print("Mail başarılı bir şekilde gönderildi.")
    mail.close()
    exec(open("elYikama.py").read()) #bir sonraki aşamaya geçmesi için gerekli fonksiyon

# Eğer mesaj gönderirken hata olursa, hata mesajını konsole yazdırıyorum.
except:
    print("Hata:", sys.exc_info()[0])
