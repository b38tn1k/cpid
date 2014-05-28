
const int encoderPinA = 2;
const int encoderPinB = 8;
const int channel_a_enable  = 6;
const int channel_a_input_1 = 4;
const int channel_a_input_2 = 7;
int Pos = 0;
int Vel = 100;
volatile int encoderPos = 0; 

unsigned long lastSend = 0;
unsigned long time;
unsigned long interval = 300;

void setup() {
  Serial.begin(9600);  
  Serial.println("Begun");
  delay(1000);
  pinMode(encoderPinA, INPUT); 
  pinMode(encoderPinB, INPUT); 
  digitalWrite(encoderPinA, HIGH); 
  digitalWrite(encoderPinB, HIGH); 

  pinMode( channel_a_enable, OUTPUT );  // Channel A enable
  pinMode( channel_a_input_1, OUTPUT ); // Channel A input 1
  pinMode( channel_a_input_2, OUTPUT ); // Channel A input 2

  attachInterrupt(1, doEncoder, FALLING); 
  interrupts();
  noInterrupts();
  Serial.println('Finished setup');
  interrupts(); 
}

void loop() {
  uint8_t oldSREG = SREG;
  //cli();
  Pos = encoderPos; 
  SREG = oldSREG; 
  //Serial.println("In loop");
  if ((lastSend + interval) < time){
    noInterrupts();
    Serial.print(Pos);
    Serial.print("\n");
    lastSend = time; //will reset after 50 days
    Serial.flush();
    interrupts();
  }
  
  //Serial.println(1);
  time = millis();
  //Vel = Serial.read();

//  if(Vel < 0){ //this is flipped so encoder output makes sense
//    analogWrite( channel_a_enable, Vel);
//    digitalWrite( channel_a_input_1, HIGH);
//    digitalWrite( channel_a_input_2, LOW);
//  } 
//  else {
//    analogWrite( channel_a_enable, -1*Vel);
//    digitalWrite( channel_a_input_1, LOW);
//    digitalWrite( channel_a_input_2, HIGH);
//  }

  //  if(Pos>1000){ //basic H-Bridge test
  //    Vel = -100;
  //  }
  //  if(Pos<0){
  //    Vel = 100;
  //  }
}

void doEncoder() {
  noInterrupts();
  if (digitalRead(encoderPinA) == digitalRead(encoderPinB))
    encoderPos++; 
  else
    encoderPos--;
  //Serial.println(encoderPos);
  interrupts();
}





















