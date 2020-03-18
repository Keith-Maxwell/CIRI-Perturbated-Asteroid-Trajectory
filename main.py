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
t = 0  # start time
tf = 1000  # stop time
h = 10  # step

yout_f = init_state
results_forward = []
for i in range(t, tf, h):
    yout_f = RK4(f, t, yout_f)  # at each step we integrate using RK4 method
    plt.plot(yout_f[0], yout_f[1], '.')  # at each step we plot one point on the graph
    results_forward.append(yout_f)
plt.axis('equal')
plt.show()

# forward and backward test to adjust the step size

yout_b = yout_f
results_backward = []
for i in range(tf, t, -h):
    yout_b = RK4(f, t, yout_b)
    results_backward.append(yout_b)
err_x = abs(results_forward[0][0] - results_backward[-1][0])
err_y = abs(results_forward[0][1] - results_backward[-1][1])
print(err_x, err_y)

# step = 10     0.15767095259326092 0.9085819291869152
# step = 3      0.14244108281397927 0.7785828277686659
# step = 2      0.16122427607983747 0.8113732533872091
# step = 1      0.16133521348074753 0.79921188284136
