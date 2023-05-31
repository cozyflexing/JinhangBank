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

    // Start the serial communication
    Serial.begin(9600);
}

void loop()
{
    parseSerialInput();
    // controlMotorA(0); // Motor A rotates 2 times
    // delay(2000); // wait for 2 seconds
    // controlMotorB(0); // Motor B rotates 2 times
    // delay(2000); // wait for 2 seconds
    // controlMotorC(0); // Motor C rotates 2 times
    // delay(2000); // wait for 2 seconds
}

void parseSerialInput()
{
    if (Serial.available() > 0)
    {
        String incomingMessage = Serial.readString();
        incomingMessage = incomingMessage.substring(1, incomingMessage.length() - 1);
        int commaIndex = incomingMessage.indexOf(",");
        while (commaIndex != -1)
        {
            String numStr = incomingMessage.substring(0, commaIndex);
            int num = numStr.toInt();
            controlMotor(num);
            incomingMessage = incomingMessage.substring(commaIndex + 2);
            commaIndex = incomingMessage.indexOf(",");
        }
        int num = incomingMessage.toInt();
        controlMotor(num);
    }
}

void controlMotor(int num)
{
    switch (num)
    {
    case 10:
        controlMotorA(1); // Motor A for 10
        break;
    case 20:
        controlMotorB(1); // Motor B for 20
        break;
    case 50:
        controlMotorC(1); // Motor C for 50
        break;
    }
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
        delay(130);
        stopMotor(in3, in4);
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
        delay(200);
        stopMotor(in5, in6);
    }
}

void stopMotor(int pin1, int pin2)
{
    // Turn off motor
    digitalWrite(pin1, LOW);
    digitalWrite(pin2, LOW);
}
