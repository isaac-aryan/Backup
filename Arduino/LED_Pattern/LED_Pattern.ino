void LED1_light(){
pinMode(7, OUTPUT);
pinMode(6, OUTPUT);
digitalWrite(7, HIGH);
digitalWrite(6, LOW);
delay(500);

digitalWrite(7, LOW);
digitalWrite(6, LOW);
delay(500);
}

void LED2_light(){
  pinMode(3, OUTPUT);
  pinMode(2, OUTPUT);
  digitalWrite(3,HIGH);
  digitalWrite(2,LOW);
  delay(500);
  digitalWrite(3,LOW);
  digitalWrite(2,LOW);
  delay(500);
}
void LED3_light(){
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  digitalWrite(11,HIGH);
  digitalWrite(10,LOW);
  delay(500);
  digitalWrite(11,LOW);
  digitalWrite(10,LOW);
  delay(500);
}
void setup() {
  // put your setup code here, to run once:
LED1_light();
LED2_light();
LED3_light();
LED2_light();
LED3_light();     
LED1_light();
LED1_light();
}

void loop() {
  // put your main code here, to run repeatedly:

}
