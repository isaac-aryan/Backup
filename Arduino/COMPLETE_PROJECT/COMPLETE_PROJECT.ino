#define PROXPIN 2
void LED_light(int anode, int cathode, int state){
  pinMode(anode, OUTPUT);
  pinMode(cathode, OUTPUT);
  analogWrite(anode, state);
  digitalWrite(cathode, LOW);
  }
void setup() {
  // put your setup code here, to run once:
pinMode(PROXPIN, INPUT);
Serial.begin(9600);
}
int count=0;
void loop() {
  // put your main code here, to run repeatedly:
bool sensor=digitalRead(PROXPIN);
if (sensor==0){
  LED_light(3,4,255);
  LED_light(6,5,0);
  LED_light(11,8,255);

  count=count+1;
  Serial.println(count);
  delay(500);
  while (sensor==0){
    sensor=digitalRead(PROXPIN);
    LED_light(3,4,255);
    LED_light(6,5,0);
    LED_light(11,8,255);
    
  }
  delay(500);
}
else{
  LED_light(6,5,255);
  LED_light(3,4,0);
  LED_light(11,8,0);
}
}
