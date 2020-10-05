void light(){
pinMode(7, OUTPUT);
pinMode(6, OUTPUT);
digitalWrite(7, HIGH);
digitalWrite(6, LOW);
delay(2000);
}
void light_off(){
  pinMode(7, OUTPUT);
pinMode(6, OUTPUT);
digitalWrite(7, LOW);
digitalWrite(6, LOW);
}
void setup() {
  // put your setup code here, to run once:
light();
light_off();
}

void loop() {
  // put your main code here, to run repeatedly:

}
