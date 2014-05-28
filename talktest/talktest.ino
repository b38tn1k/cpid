/*

 RotaryEncoderInterrupt sketch
 
 */

const int encoderPinA = 2;
const int encoderPinB = 8;
int Pos, oldPos;
volatile int encoderPos = 0; // variables changed within interrupts are volatile
unsigned long lastMillis;
void setup()

{

  pinMode(encoderPinA, INPUT);
  pinMode(encoderPinB, INPUT);
  digitalWrite(encoderPinA, HIGH);
  digitalWrite(encoderPinB, HIGH);
  Serial.begin(9600);
  attachInterrupt(0, doEncoder, FALLING); // encoder pin on interrupt 0 (pin 2)
  Serial.println("Setup Complete");
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  Serial.println("yes");
  lastMillis = millis();
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
    oldPos = Pos;
    lastMillis = millis();
  }
  

 // Delay(1000);

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

