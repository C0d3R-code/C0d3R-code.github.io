#include <SevSeg.h>

SevSeg display;

const int redPin = 2;
const int yellowPin = 3;
const int greenPin = 4;

int timer = 9; 

void setup() {
  // Define the display parameters.
  byte numDigits = 1; // Use 1 digit for the timer
  byte digitPins[] = {5}; 
  byte segmentPins[] = {6, 7, 8, 9, 10, 11, 12}; 

  // Initialize the display.
  display.begin(COMMON_ANODE, numDigits, digitPins, segmentPins);

  // Set the brightness (optional).
  display.setBrightness(90); 

  pinMode(redPin, OUTPUT);
  pinMode(yellowPin, OUTPUT);
  pinMode(greenPin, OUTPUT);

  Serial.begin(9600); 
}

void loop() {
  // Green light for 30 seconds
  digitalWrite(greenPin, HIGH);
  digitalWrite(redPin, LOW);
  digitalWrite(yellowPin, LOW);
  timer = 9; 
  displayTimer(); 
  delay(30000); 

  // Yellow light for 5 seconds
  digitalWrite(greenPin, LOW);
  digitalWrite(redPin, LOW);
  digitalWrite(yellowPin, HIGH);
  timer = 5; 
  displayTimer(); 
  delay(5000);

  // Red light for 30 seconds
  digitalWrite(greenPin, LOW);
  digitalWrite(redPin, HIGH);
  digitalWrite(yellowPin, LOW);
  timer = 9; 
  displayTimer(); 
  delay(30000); 
}

void displayTimer() {
  display.clear(); 
  display.print(timer); 
  display.refresh(); 
  timer--; 
  delay(1000); // Update timer every second
}