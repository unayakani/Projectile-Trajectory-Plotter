import matplotlib.pyplot as plot
import math

t = 0.01
g = -9.8
theta = math.pi / 3
vel = 80
vx = vel * math.cos(theta)
vy = vel * math.sin(theta)
x = [0.00]
y = [0.00]
x_counter = 0.00
y_counter = 0.00

while y[-1] >= 0:
    x2 = float(vx * t)
    x_counter += x2
    x.append(x_counter)
    y2 = float(vy * t + 0.5 * g * t**2)
    y_counter += y2
    y.append(y_counter)
    vy = vy + g * t

plot.plot(x, y)
plot.xlim(0, max(x))
plot.ylim(0, max(y)*1.2)
plot.show()
