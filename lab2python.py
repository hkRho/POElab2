import serial
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

def start_serial(com,baud):
    """
    Initialize the serial port to receive arduino data.
    
    Args:
        com: COM port to start the serial communication with
        baud: baud rate
    
    Return:
        serialPort: the opened serial port
    """
    arduinoComPort = com
    baudRate = baud
    serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)
    return serialPort

def live_plot():
    """
    Parse the information in the serial port. Plot the data on an azimuth by elevation graph with depth being the color bar.
    """
    # set the color scheme of the color bar
    cm = plt.cm.get_cmap('RdYlBu')
    
    #start reading from the serial port
    serialPort = start_serial("COM7",9600) 
    time.sleep(2)
    
    fig, ax = plt.subplots()
    ax.axis('equal')
    plt.xlabel('x')
    plt.ylabel('y')

    x_array = []
    y_array = []
    z_array = []

    while serialPort.isOpen() is True:
        lineOfData = serialPort.readline().decode()
        if lineOfData is not '\n': # skip the case when the only output is a new line on the serial port
            # parse the information into plottable data
            point = lineOfData.split(',')
            azimuth = int(point[0])
            elevation = int(point[1])
            sensorAve = int(point[2])       

            x_array.append(azimuth)
            y_array.append(elevation)
            z_array.append(sensorAve)
            
            ax.clear()
            im = ax.scatter(x_array, y_array, c = z_array, cmap = cm, s = 70)
            cb = fig.colorbar(im, ax=ax)
            plt.pause(0.001)
            cb.remove()
    
    plt.show()

live_plot()
