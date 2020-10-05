void setup() {
  // put your setup code here, to run on
  Serial.begin(9600);
  pinMode(A0,INPUT);
  pinMode(10,OUTPUT);
  pinMode(9,OUTPUT);
  digitalWrite(10,LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
int ldr=analogRead(A0);
Serial.println(ldr);
delay (100);
int ambiant_light=840;
if(ldr>ambiant_light){
  digitalWrite(9,HIGH);
}
else{
  digitalWrite(9,LOW);
}

}
