import serial
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

## function that starts communicating with the arduino by receiving output data from the script
## parameters com, baud is used to vary the COMPORT and the baud rate
def start_serial(com,baud):
    arduinoComPort = com
    baudRate = baud
    serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)
    return serialPort

## function that plots the data received from the arduino script into a 2D intensity/color map
## 2D scatter plot where the color of the points are determined by the distance
def live_plot():
    cm = plt.cm.get_cmap('RdYlBu') # instantiate a color map
    serialPort = start_serial("COM7",9600) # start communicating with arduino
    time.sleep(2)
    fig, ax = plt.subplots()
    ax.axis('equal')
    plt.xlabel('x')
    plt.ylabel('y')

    x_array = []
    y_array = []
    z_array = []

    while serialPort.isOpen() is True:  # while the arduino script is sending data
        lineOfData = serialPort.readline().decode()
        if lineOfData is not '\n':  # make sure we are getting outputs composed of numbers
            # format of arduino output is [azimuth, elevation, sensorAve]
            point = lineOfData.split(',')
            azimuth = int(point[0])
            elevation = int(point[1])
            sensorAve = int(point[2])       

            x_array.append(azimuth)
            y_array.append(elevation)
            z_array.append(sensorAve)

            im = ax.scatter(x_array, y_array, c = z_array, cmap = cm, s = 70) # 2D scatter plot with colors changing depending on distance
            cb = fig.colorbar(im, ax=ax)
            plt.pause(0.001)
            cb.remove()
    
    plt.show()

live_plot()