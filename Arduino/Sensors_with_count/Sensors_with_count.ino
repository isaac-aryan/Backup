#define PROXPIN 2
void LED_light(int anode, int cathode, int state) {
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
int c = 0;
void loop() {
  // put your main code here, to run repeatedly:
  bool sensor = digitalRead(PROXPIN);
  //Serial.println(sensor);
  if (sensor == 0) {
    //Serial.println("There is no obstacle");
    LED_light(4, 3, LOW);
    LED_light(6, 5, 127);
  

    c = c + 1;
    Serial.println(c);
    delay(500);
    while (sensor == 0) {
      sensor = digitalRead(PROXPIN);
        LED_light(11, 8, LOW);

    }
    delay(500);
  }
  else {
    //Serial.println("There is an obstacle in the way");
    LED_light(6, 5, 10);
    LED_light(4, 3, HIGH);
    LED_light(11, 8, HIGH);

  }

}
