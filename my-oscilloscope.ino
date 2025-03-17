const int analogPin1 = A0;
const int analogPin2 = A1;
const int analogPin3 = A2;
 
void setup() {
  //Setup serial connection
  Serial.begin(31250); 
}
 
void loop() {
  delay(1);
  //Read analog pin
  int val1 = analogRead(analogPin1);
  int val2 = analogRead(analogPin2);
  int val3 = analogRead(analogPin3);

  //Write analog value to serial port:
  Serial.write(val1);
  Serial.write(val2);
  Serial.write(val3);
  Serial.println();
}