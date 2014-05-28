  int Pos = 0;
  unsigned long lastSend = 0;
  unsigned long time;
  unsigned long interval = 1000;

void setup() {
  Serial.begin(9600);  
}

void loop() {
  if ((lastSend + interval) > time){
    Serial.print(Pos);
    Serial.print("\n");
    lastSend = time; //will reset after 50 days
  }
  time = millis();
  Pos +=1;

}









