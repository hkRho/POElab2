#include <Servo.h>

Servo yaw;
Servo pitch;
int sensor_pin = A0;
int sensorValue = 0;
int sensorAdd = 0;
int sensorAve = 0;
long baudRate = 9600;
int azimuth = 0;
int elevation = 0;
int x = 0;

void setup(){
    yaw.attach(9);
    pitch.attach(10);
    Serial.begin(baudRate);
}

void loop(){
    for (azimuth = 45; azimuth <= 135; azimuth += 2){
        yaw.write(azimuth);
        delay(15);
        for (elevation = 0; elevation <= 54; elevation += 2) {
            pitch.write(elevation);
            delay(15);
            sensorValue = 0;
            sensorAdd = 0;
            sensorAve = 0;
            for (x = 0; x <= 2; x += 1) {
                sensorValue = analogRead(sensor_pin);
                sensorAdd = sensorAdd + sensorValue;
                delay(50);
            }
            sensorAve = sensorAdd/3;
            Serial.print('\n');
            Serial.print(azimuth);
            Serial.print(',');
            Serial.print(54-elevation);
            Serial.print(',');
            Serial.print(sensorAve);
            delay(500);

        }
    }
}
