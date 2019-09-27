import serial
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

def start_serial(com,baud):
    arduinoComPort = com
    baudRate = baud
    serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)
    return serialPort


def sph_to_cart(azimuth, elevation, r=5):
    rcos_theta = r * np.cos(np.deg2rad(elevation))
    rsin_theta = r * np.sin(np.deg2rad(elevation))
    x = rsin_theta * np.cos(np.deg2rad(azimuth))
    y = rsin_theta * np.sin(np.deg2rad(azimuth))
    z = rcos_theta
    return x, y, z

def live_plot():
    cm = plt.cm.get_cmap('RdYlBu')
    serialPort = start_serial("COM7",9600)
    time.sleep(2)
    fig, ax = plt.subplots()
    plt.xlabel('x')
    plt.ylabel('y')
    x_array = []
    y_array = []
    z_array = []
    while serialPort.isOpen() is True:
        lineOfData = serialPort.readline().decode()
        if lineOfData is not '\n':
            point = lineOfData.split(',')
            azimuth = int(point[0])
            elevation = int(point[1])
            sensorAve = int(point[2])       
            # [x, y, z] = sph_to_cart(azimuth,elevation)
            x_array.append(azimuth)
            y_array.append(elevation)
            z_array.append(sensorAve)
            im = ax.scatter(x_array,y_array,c = z_array, cmap = cm)
            cb = fig.colorbar(im, ax=ax)
            plt.pause(0.5)
            cb.remove()
    
    plt.show()

def live_plot_3d():
    serialPort = start_serial("COM7",9600)
    time.sleep(2)
    fig = plt.figure()
    ax = Axes3D(fig)
    plt.xlabel('x')
    plt.ylabel('y')
    x_array = []
    y_array = []
    z_array = []
    while serialPort.isOpen() is True:
        lineOfData = serialPort.readline().decode()
        if lineOfData is not '\n':
            point = lineOfData.split(',')
            azimuth = int(point[0])
            elevation = int(point[1])
            sensorAve = int(point[2])       
            [x, y, z] = sph_to_cart(azimuth,elevation,sensorAve)
            x_array.append(x)
            y_array.append(y)
            z_array.append(z)
            ax.scatter(x_array,y_array,z_array)
            plt.pause(0.5)
    
    plt.show()




live_plot()