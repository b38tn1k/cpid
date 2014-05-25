
const int encoderPinA = 2;
const int encoderPinB = 8;
const int channel_a_enable  = 6;
const int channel_a_input_1 = 4;
const int channel_a_input_2 = 7;
int Pos, oldPos;
int velocity = 100;
volatile int encoderPos = 0; 

void setup() {
  Serial.begin(9600);  
  delay(1000);
  pinMode(encoderPinA, INPUT); 
  pinMode(encoderPinB, INPUT); 
  digitalWrite(encoderPinA, HIGH); 
  digitalWrite(encoderPinB, HIGH); 

  pinMode( channel_a_enable, OUTPUT );  // Channel A enable
  pinMode( channel_a_input_1, OUTPUT ); // Channel A input 1
  pinMode( channel_a_input_2, OUTPUT ); // Channel A input 2

  attachInterrupt(0, doEncoder, FALLING); 
  Serial.write("Setup Complete\n");
}

void loop() {
  uint8_t oldSREG = SREG;
  cli();
  Pos = encoderPos; 
  SREG = oldSREG; 
  if(Pos != oldPos) {
    Serial.println(Pos,DEC); 
    oldPos = Pos;
  } 
  if(velocity < 0){ //this is flipped so encoder output makes sense
    analogWrite( channel_a_enable, velocity);
    digitalWrite( channel_a_input_1, HIGH);
    digitalWrite( channel_a_input_2, LOW);
  } 
  else {
    analogWrite( channel_a_enable, -1*velocity);
    digitalWrite( channel_a_input_1, LOW);
    digitalWrite( channel_a_input_2, HIGH);
  }

//  if(Pos > 500){
//    velocity = -100;
//  }
//  if(Pos < 0){
//    velocity = 100;
//  }

}

void doEncoder() {
  noInterrupts();
  if (digitalRead(encoderPinA) == digitalRead(encoderPinB))
    encoderPos++; 
  else
    encoderPos--; 
  interrupts();
}












