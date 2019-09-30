import matplotlib.pyplot as plt
import numpy as np
from sympy import S, symbols
import sympy

# calibration data recorded
distances = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12]
sensor_readings = [3, 157, 323, 330, 365, 384, 407, 503, 551, 561, 558, 538, 524, 510, 500, 486, 475, 463, 450, 436, 421, 405, 390, 379, 368]

# error data recorded
error_distance = [0.25, 1.25, 2.25, 3.25, 4.25, 5.25, 6.25, 7.25, 8.25, 9.25, 10.25, 11.25]
error_sensor_readings = [234, 432, 372, 454, 561, 555, 531, 510, 583, 558, 425, 395]

# creating a list for the annotations
n = [0,1,2,3,4,5,6,7,8,9,10,11]

# fitting an equation to the calibration data
p = np.polyfit(distances, sensor_readings, 10)
f = np.poly1d(p)

# calculating points using the equation found
distances_new = np.linspace(distances[0], distances[-1], 200)
sensor_readings_new = f(distances_new)

# ??
x = symbols("x")
poly = sum(S("{:6.2f}".format(v))*x**i for i, v in enumerate(p[::-1]))
eq_latex = sympy.printing.latex(poly)

fig,ax = plt.subplots()
# ax.scatter(distances, sensor_readings)
ax.scatter(error_distance, error_sensor_readings, color = 'purple')
ax.plot(distances_new,sensor_readings_new, label="${}$".format(eq_latex))

# calculates error (the difference between the new points not used for calibration and the calibration curve)
for x in range(0,12):
    sensor = error_sensor_readings[x]
    n[x] = np.round(sensor - f(error_distance[x]))
    if n[x] > 0:
        n[x] = '+' + str(n[x])

# displays the value of the error at each point not used for calibration
for i, txt in enumerate(n):
    ax.annotate(txt, (error_distance[i], error_sensor_readings[i]))

plt.legend(fontsize="small")
plt.xlabel("Distance From The Sensor (inches)")
plt.ylabel("Sensor Reading")
plt.title("Error Plot For The Sensor")
plt.show()
