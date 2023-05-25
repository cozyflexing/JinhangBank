#include <Keypad.h>

// Define the keypad layout
const byte ROWS = 4;
const byte COLS = 2;
char keys[ROWS][COLS] = {
    {'1', '2'},
    {'4', '5'},
    {'7', '8'},
    {' ', '0'}};
byte rowPins[ROWS] = {9, 8, 7, 6}; // Connect row pins to these Arduino pins
byte colPins[COLS] = {3, 2};       // Connect column pins to these Arduino pins

// Create the Keypad object
Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

void setup()
{
    Serial.begin(9600);
}

void loop()
{
    // Check for key press
    char key = keypad.getKey();

    // Process the pressed key
    if (key)
    {
        Serial.println(key);
    }
}
