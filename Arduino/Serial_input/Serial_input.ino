void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    String received_data = Serial.readString();
   Serial.println("The received data is:"+received_data);
   int num=received_data.toInt();
   if(num%2==0)
   Serial.println("The number is even.");
   else
   Serial.println("The number is odd");
  }
}
