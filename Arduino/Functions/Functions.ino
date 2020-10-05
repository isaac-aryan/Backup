int c=100;
void add(){
  int a= 10;
  int b=20;
  Serial.println(a+b);
}
void add2(int a, int b){
  Serial.println((a+b)*c);
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println(c);
  add();
  add2(45,63);

}

void loop() {
  // put your main code here, to run repeatedly:

}
