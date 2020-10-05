#include <SoftwareSerial.h>
SoftwareSerial myserial(11, 10); //11 is RX and 10 is TX
void setup() {
  Serial.begin(115200);
  myserial.begin(115200);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  digitalWrite(8, LOW);
}

void loop() {
  if (myserial.available()) {
    String data = myserial.readString();
    Serial.println(data);

    if (data == "on") {
      digitalWrite(9, HIGH);

    }
    else {
      digitalWrite(9, LOW);
    }
  }


}
