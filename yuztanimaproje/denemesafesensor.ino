const int trigger_pin = 12;
const int echo_pin = 11;

long sure;
int mesafe;

void setup() {
  pinMode(trigger_pin,OUTPUT);
  pinMode(echo_pin,INPUT);
  Serial.begin(9600);
}

void loop() {
digitalWrite(trigger_pin,HIGH);
delayMicroseconds(1000);
digitalWrite(trigger_pin,LOW);

sure = pulseIn(echo_pin,HIGH); // göndeilen kare dalgasının geri dönemsi süresini veriyor
// x= v*t ses hızı* pulse ı 343m/s = 0,0343 cm/ms
//uzaklık =( 0,0343 cm/ms*süre)/2
mesafe  = ((sure/2)/29.1)+2;  //29.1 içinde bulunduğumuz ortamda sıcaklık la birlikte ses dalgasıın kat ettiği yol sıcaklı karttıkça ses dalgasını hozoda artar 

//Serial.print(" cisme olan uzaklık = ");
Serial.println(mesafe);
//Serial.println("cm");
//Serial.println("------------");
delay(500);
}
