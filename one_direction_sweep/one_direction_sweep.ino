#include <Servo.h>

Servo yaw;
Servo pitch;
// pin connected to the distance sensor
int sensor_pin = A0;

// variable to get the output value of the distance sensor
int sensorValue = 0;

// variable to add all analogRead output at each location
int sensorAdd = 0;

// variable to get the average analogRead value per yaw&pitch
int sensorAve = 0;
long baudRate = 9600;

// variable to change the azimuth/yaw
int azimuth = 0;

// variable to change the elevation/pitch
int elevation = 0;

// variable to control the number of analogRead outputs to be taken at each yaw&pitch
int x = 0;

void setup(){
    yaw.attach(9);
    pitch.attach(10);
    Serial.begin(baudRate);
}

void loop(){
        yaw.write(105); // fixes the azimuth/yaw at a constant location
        delay(15);
        
        for (elevation = 30; elevation <= 140; elevation += 2) {  // sweep through the elevation by incrementing 2 degrees each time
            pitch.write(elevation);
            delay(15);
            sensorValue = 0;
            sensorAdd = 0;
            sensorAve = 0;
            
            for (x = 0; x <= 2; x += 1) { // take 3 analogRead output at each location and add it put to sensorAdd
                sensorValue = analogRead(sensor_pin);
                sensorAdd = sensorAdd + sensorValue;
                delay(50);
            }
            
            sensorAve = sensorAdd/3;  // take the average of the analogRead values at each location
            // output formatting for python script
            Serial.print('\n');
            Serial.print(azimuth);
            Serial.print(',');
            Serial.print(elevation);
            Serial.print(',');
            Serial.print(sensorAve);
            delay(500);
    }
    Serial.close();
}
