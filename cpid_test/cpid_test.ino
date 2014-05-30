
const int channel_a_enable  = 6;
const int channel_a_input_1 = 4;
const int channel_a_input_2 = 7;
const int encoderPinA = 3;
const int encoderPinB = 8;
int Pos, oldPos, Vel, negflag;
int Velocity = 0;
volatile int encoderPos = 0; // variables changed within interrupts are volatile
unsigned long lastMillis;
void setup()

{

  pinMode(encoderPinA, INPUT);
  pinMode(encoderPinB, INPUT);
  digitalWrite(encoderPinA, HIGH);
  digitalWrite(encoderPinB, HIGH);
  pinMode( channel_a_enable, OUTPUT );  // Channel A enable
  pinMode( channel_a_input_1, OUTPUT ); // Channel A input 1
  pinMode( channel_a_input_2, OUTPUT ); // Channel A input 2
  Serial.begin(115200);
  attachInterrupt(1, doEncoder, FALLING); // encoder pin on interrupt 0 (pin 2)
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  lastMillis = millis();
}

void loop()
{
  uint8_t oldSREG = SREG;
  interrupts();
  Pos = encoderPos;


  if (Pos%1000 ==0){ //empty value jitter
    Pos = Pos+1;
  }

  SREG = oldSREG;
  if(millis() > lastMillis+100)
  {
    char a,b;
    a = abs(Pos);
    b = abs(Pos >> 8);
    Serial.write(isNegative(Pos));
    Serial.write(a);
    Serial.write(b);
    Serial.write('/n');
    oldPos = Pos;
    lastMillis = millis();
    if(Serial.available()>=2){
      digitalWrite(13, HIGH);
      negflag = Serial.read();
      Vel = Serial.read();
      Serial.flush();
      Velocity = Vel;
      if(negflag ==2){
        Velocity = -1*Velocity;
      }

    }
    writeMotor(Velocity);
  }

}
/////////////////////
int isNegative(int x){
  if (x<0) return 1;
  else return 0;
}
/////////////////////
void doEncoder()
{
  noInterrupts();
  if (digitalRead(encoderPinA) == digitalRead(encoderPinB))
    encoderPos++; // count up if both encoder pins are the same
  else
    encoderPos--; //count down if pins are different
  interrupts();
}
/////////////////////
void writeMotor(int Vel)
{
  if(Vel < 0){ 
    analogWrite( channel_a_enable, Vel);
    digitalWrite( channel_a_input_1, HIGH);
    digitalWrite( channel_a_input_2, LOW);
  } 
  else {
    analogWrite( channel_a_enable, -1*Vel);
    digitalWrite( channel_a_input_1, LOW);
    digitalWrite( channel_a_input_2, HIGH);
  }
}



