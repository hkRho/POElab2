import serial
import numpy as np
import matplotlib.pyplot as plt
import time

def start_serial(com,baud):
    arduinoComPort = com
    baudRate = baud
    serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)
    return serialPort


def sph_to_cart(azimuth, elevation, r):
    rcos_theta = r * np.cos(elevation)
    x = rcos_theta * np.cos(azimuth)
    y = rcos_theta * np.sin(azimuth)
    z = r * np.sin(elevation)
    return x, y, z

def live_plot():
    serialPort = start_serial("COM7",9600)
    time.sleep(2)
    plt.axis([-100,100,-100,100])
    while serialPort.isOpen() is True:
        lineOfData = serialPort.readline().decode()
        print(lineOfData)
        if lineOfData is not '\n':
            point = lineOfData.split(',')
            azimuth = int(point[0])
            elevation = int(point[1])
            sensorAve = int(point[2])       
            [x, y, z] = sph_to_cart(azimuth,elevation,sensorAve)
            print(x,y,z)


live_plot()