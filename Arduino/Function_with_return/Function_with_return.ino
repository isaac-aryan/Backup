int add(int a, int  b){
  int c=a+b;
  return c;
}
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
int sum=add(10,9);
Serial.print(sum);
if(sum<100){
  Serial.println("Sum is less than 100");
}
 if(sum<200){
  Serial.println("Sum is greater than 100 but less than 200");
}
else if(sum<210){
  Serial.println("Sum is greater than 200");
  
}
else{
  Serial.println("Sum is greater than 200");
}
}

void loop() {
  // put your main code here, to run repeatedly:

}
