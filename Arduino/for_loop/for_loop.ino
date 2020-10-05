void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
for(int count=0; count<=10; count+=2){
  Serial.print(count);
}
for(int count=9; count>=0; count--){
  Serial.print(count); 
}
}

void loop() {
  // put your main code here, to run repeatedly:

}
