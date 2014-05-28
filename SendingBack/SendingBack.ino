/*

 RotaryEncoderInterrupt sketch
 
 */

const int encoderPinA = 12;

const int encoderPinB = 8;

const int channel_a_enable  = 6;
const int channel_a_input_1 = 4;
const int channel_a_input_2 = 7;

int Pos, oldPos, Vel;

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

  Serial.begin(9600);

  attachInterrupt(1, doEncoder, FALLING); // encoder pin on interrupt 0 (pin 2)

  Serial.println("Setup Complete");
  digitalWrite(13, HIGH);
  delay(3000);
  digitalWrite(13, LOW);
  lastMillis = millis(); //resets after 50 days
}

void loop()

{
  uint8_t oldSREG = SREG;
  cli();
  Pos = encoderPos;
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
    Serial.flush();
    Vel = 100; //serial read Vel
    writeMotor(Vel);
    oldPos = Pos;
    lastMillis = millis();
  }
}

int isNegative(int x){
  if (x<0) return 1;
  else return 0;
}

void doEncoder()
{
  if (digitalRead(encoderPinA) == digitalRead(encoderPinB))
    encoderPos++; // count up if both encoder pins are the same
  else
    encoderPos--; //count down if pins are different
}

void writeMotor(int Vel){
  if(Vel < 0){ //this is flipped so encoder output makes sense
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


