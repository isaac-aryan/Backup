
void setup() {
  // put your setup code here, to run once:
pinMode(8, INPUT);
Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
bool sensor=digitalRead(8);
//Serial.println(sensor);
if (sensor==1){
    digitalWrite(7,LOW);
  } 
  else{
    //Serial.println("There is an obstacle in the way");
    digitalWrite(7,HIGH);
    delay(
    
  }

}
