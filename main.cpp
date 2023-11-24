#include <Arduino.h>
#include <Wire.h>
#include <VL6180X.h>

VL6180X sensor;
const int window = 4;
int data[window] = {0};
int T = 100;

void setup() 
{
  Serial.begin(9600);
  Wire.begin();
  
  sensor.init();
  sensor.configureDefault();
  sensor.setTimeout(500);

  for(int i=0; i<window; i++){
    data[i] = sensor.readRangeSingleMillimeters();
    delay(T);
  }
}

void loop() 
{ 
  for(int i=0; i<window; i++){
    data[i] = sensor.readRangeSingleMillimeters();
    int val = 0;
    for(int j=0; j<window; j++)
    {
      val += data[j];
    }
    Serial.println(val/window);
    delay(T);
  }
}