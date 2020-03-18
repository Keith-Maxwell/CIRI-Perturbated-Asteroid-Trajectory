import matplotlib.pyplot as plt
import numpy as np


def f(t, y):  # using the state space representation
    y0 = y[3]  # velocity on x
    y1 = y[4]  # velocity on y
    y2 = y[5]  # velocity on z
    r = np.sqrt(y[0] ** 2 + y[1] ** 2 + y[2] ** 2)  # norm of the vector r
    y3 = -G * (m_sun + m_object) / (r ** 3) * y[0]  # equation of motion on x
    y4 = -G * (m_sun + m_object) / (r ** 3) * y[1]  # equation of motion on x
    y5 = -G * (m_sun + m_object) / (r ** 3) * y[2]  # equation of motion on x
    return np.array([y0, y1, y2, y3, y4, y5])


def RK4(fonction, t, yin):
    # Definition of the Runge-Kutta method at the order 4
    k1 = fonction(t, yin)
    k2 = fonction(t + h / 2, yin + h / 2 * k1)
    k3 = fonction(t + h / 2, yin + h / 2 * k2)
    k4 = fonction(t + h, yin + h * k3)
    yout = yin + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return yout


# We use our own units : distances in AU, mass in Suns, time in Days

# initial variables
m_sun = 1  # mass of the Sun
m_object = 0  # mass of the object studied
a = 2  # semi-major axis
G = 0.000295824  # gravitation constant expressed in our own system of units
k = np.sqrt(G)

# initial conditions [pos x, pos y, pos z, v x, v y, v z]
state_vector = np.array([a, 0, 0, 0, k / np.sqrt(a), 0])

# integration parameters (in number of days)
h = 1  # step
n = 1000  # number of iterations
t = 0  # start time

yout = state_vector
for i in range(t, n, h):
    yout = RK4(f, t, yout)  # at each step we integrate using RK4 method
    plt.plot(yout[0], yout[1], '.')  # at each step we plot one point on the graph
plt.axis('equal')
plt.show()
