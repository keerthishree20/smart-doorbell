// Define constants for pin numbers
const int inputPin = 8;
const int outputPin = 9;

void setup()
{
    // Initialize the input and output pins
    pinMode(inputPin, INPUT);
    pinMode(outputPin, OUTPUT);
}

void loop()
{
    // Read the state of the input pin
    int inputState = digitalRead(inputPin);

    // Check if the input state is LOW (e.g., button pressed)
    if (inputState == LOW)
    {
        // Set the output pin HIGH (turn on LED)
        digitalWrite(outputPin, HIGH);
    }
    else
    {
        // Set the output pin LOW (turn off LED)
        digitalWrite(outputPin, LOW);
    }

    // Add a short delay to debounce the input signal
    delay(50);
}
