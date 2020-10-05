void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:
pinMode(7, OUTPUT);
pinMode(6, OUTPUT);
digitalWrite(7, HIGH);
digitalWrite(6, LOW);
delay(50);
digitalWrite(7, LOW);
digitalWrite(6, LOW);
delay(50);
}
