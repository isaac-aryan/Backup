void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
int c= 0;
while(c<=10)
{
  Serial.println(c);
  c=c+1;
}
}

void loop() {
  // put your main code here, to run repeatedly:

}
