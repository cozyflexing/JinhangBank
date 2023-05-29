// Motor A connections
int enA = 9;
int in1 = 8;
int in2 = 7;

// Motor B connections
int enB = 3;
int in3 = 5;
int in4 = 4;

// Motor C connections
int enC = 10;
int in5 = 11;
int in6 = 12;

void setup()
{
  // Set all the motor control pins to outputs
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(enC, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(in5, OUTPUT);
  pinMode(in6, OUTPUT);

  // Turn off motors - Initial state
  stopMotor(in1, in2);
  stopMotor(in3, in4);
  stopMotor(in5, in6);
}

void loop()
{
  controlMotorA(0); // done
  controlMotorB(0); // done
  controlMotorC(0); // done
}

void controlMotorA(int rotations)
{
  // Set motor to maximum speed
  analogWrite(enA, 245);
  // Turn on motor A
  for (int i = 0; i < rotations; i++)
  {
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    delay(120);
    stopMotor(in1, in2);
    delay(3000);
  }
}

void controlMotorB(int rotations)
{
  // Set motor to maximum speed
  analogWrite(enB, 245);
  // Turn on motor B
  for (int i = 0; i < rotations; i++)
  {
    digitalWrite(in3, HIGH);
    digitalWrite(in4, LOW);
    delay(635);
    stopMotor(in3, in4);
    delay(3000);
  }
}

void controlMotorC(int rotations)
{
  // Set motor to maximum speed
  analogWrite(enC, 245);
  // Turn on motor C
  for (int i = 0; i < rotations; i++)
  {
    digitalWrite(in5, HIGH);
    digitalWrite(in6, LOW);
    delay(120);
    stopMotor(in5, in6);
    delay(3000);
  }
}

void stopMotor(int pin1, int pin2)
{
  // Turn off motor
  digitalWrite(pin1, LOW);
  digitalWrite(pin2, LOW);
}
