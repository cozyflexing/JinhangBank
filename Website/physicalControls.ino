#include <Keypad.h>

// Define the keypad layout
const byte ROWS = 4;
const byte COLS = 4;
char keys[ROWS][COLS] = {
    {'1', '2', '3', 'd'},
    {'4', '5', '6', 'c'},
    {'7', '8', '9', ' '},
    {' ', '0', ' ', 'e'}};
byte rowPins[ROWS] = {9, 8, 7, 6}; // Connect row pins to these Arduino pins
byte colPins[COLS] = {2, 3, 4, 5}; // Connect column pins to these Arduino pins

// Create the Keypad object
Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

// Define the button pins
const int navPins[8] = {2, 3, 4, 5, 6, 7, 8, 9};

void setup()
{
    // Start the serial communication
    Serial.begin(9600);

    // Configure the button pins as input and enable the internal pull-up resistors
    for (int i = 0; i < 8; i++)
    {
        pinMode(navPins[i], INPUT_PULLUP);
    }
}

void checkNavButtons()
{
    // Check the state of each button
    for (int i = 0; i < 8; i++)
    {
        int buttonState = digitalRead(navPins[i]);
        // If the button is pressed (the pin is LOW because the buttons connect the pin to GND when pressed)
        if (buttonState == LOW)
        {
            // Print the corresponding letter. Start from 'z' and subtract i
            Serial.println((char)('z' - i));
            // Debouncing: Wait a bit before the next read to avoid reading multiple presses if the button bounces
            delay(20);
            // Wait for the button to be released to avoid repeating the digit while the button is pressed
            while (digitalRead(navPins[i]) == LOW)
            {
                delay(20);
            }
        }
    }
}

void loop()
{
    checkNavButtons();
}
