void LED_light(int anode, int cathode, int state){
  pinMode(anode,OUTPUT);
  pinMode(cathode,OUTPUT);
  digitalWrite(anode,state);
  digitalWrite(cathode,LOW);
 
}
void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:
LED_light(12,11,HIGH);
delay(500);
LED_light(9,8,HIGH);
delay(500);
LED_light(4,3,HIGH);
delay(500);
LED_light(9,8,LOW);
delay(500);
LED_light(4,3,LOW);
delay(500);
LED_light(12,11,LOW);
delay(500);
}
