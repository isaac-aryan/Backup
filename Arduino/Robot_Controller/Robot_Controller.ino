void forward(){
  digitalWrite(9,LOW);
  digitalWrite(10,HIGH);
  digitalWrite(6,LOW);
  digitalWrite(5,HIGH);
}
void backward(){
  digitalWrite(9,HIGH);
  digitalWrite(10,LOW);
  digitalWrite(6,HIGH);
  digitalWrite(5,LOW);
  
}
void spot_right(){
  digitalWrite(9,LOW);
  digitalWrite(10,HIGH);
  digitalWrite(6,HIGH);
  digitalWrite(5,LOW);
}
void spot_left(){
  digitalWrite(9,HIGH);
  digitalWrite(10,LOW);
  digitalWrite(6,LOW);
  digitalWrite(5,HIGH);
  
}
void right(){
  digitalWrite(9,LOW);
  digitalWrite(10,HIGH);
  digitalWrite(6,LOW);
  digitalWrite(5,LOW);
}
void left(){
  digitalWrite(9,LOW);
  digitalWrite(10,LOW);
  digitalWrite(6,LOW);
  digitalWrite(5,HIGH);
}
void stp(){
  digitalWrite(9,LOW);
  digitalWrite(10,LOW);
  digitalWrite(6,LOW);
  digitalWrite(5,LOW);
}
void brake(){
  digitalWrite(9,HIGH);
  digitalWrite(10,HIGH);
  digitalWrite(6,HIGH);
  digitalWrite(5,HIGH);
}
void setup() {
  pinMode(10,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(5,OUTPUT);

}

void loop() {
  forward();
  delay(1000);
  left();
  delay(750);
  
  
}
