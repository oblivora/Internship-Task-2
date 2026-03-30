import numpy as np
import matplotlib.pyplot as plt

# Constants
mass = 1.5
gravity = 9.81
dt = 0.1
time = np.arange(0, 20, dt)

# PID constants (to tune)
Kp = 3.0
Ki = 0.5
Kd = 9.0

target_height = 10

velocity = 0
height = 0
integral = 0
prev_error = 0

heights = []

for t in time:
    error = target_height - height
    integral += error * dt
    derivative = (error - prev_error) / dt

    thrust = Kp*error + Ki*integral + Kd*derivative + (mass * gravity)

    acceleration = (thrust - mass * gravity) / mass
    velocity += acceleration * dt
    height += velocity * dt

    heights.append(height)
    prev_error = error

plt.plot(time, heights)
plt.axhline(target_height, linestyle='--')
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("PID Controlled UAV Altitude")
plt.show()