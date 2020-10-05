void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    String received_data = Serial.readString();
    if (received_data == "hello") {
      Serial.println("Hi!");
    }
    else if (received_data == "my name is Aryan") {
      Serial.println("My name is Arduino Uno");
    }
     else if (received_data =="who is the best footballer in the world") {
      Serial.println("Harry Kane, obviously");
    }
    else if (received_data == "bye") {
      Serial.println("Goodbye!");
    }
    else{
      Serial.println("I did not understand.");
    }
  }
}
