import matplotlib.pyplot as plt
import numpy as np


# using the state space representation of the equation of motion
# Only the Sun exerts it's influence on the body.
def f(t, y):
    y0 = y[3]  # velocity on x
    y1 = y[4]  # velocity on y
    y2 = y[5]  # velocity on z
    r = np.sqrt(y[0] ** 2 + y[1] ** 2 + y[2] ** 2)  # norm of the vector r
    y3 = -G * (m_sun + m_object) / (r ** 3) * y[0]  # equation of motion on x
    y4 = -G * (m_sun + m_object) / (r ** 3) * y[1]  # equation of motion on y
    y5 = -G * (m_sun + m_object) / (r ** 3) * y[2]  # equation of motion on z
    return np.array([y0, y1, y2, y3, y4, y5])


def RK4(function, time_vector, initial_conditions, h):
    # Definition of the Runge-Kutta method at the order 4
    results = []
    yin = initial_conditions
    results.append(yin)  # set the first value to the initial conditions
    for t in time_vector:
        k1 = function(t, yin)
        k2 = function(t + h / 2, yin + h / 2 * k1)
        k3 = function(t + h / 2, yin + h / 2 * k2)
        k4 = function(t + h, yin + h * k3)
        yin = yin + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        results.append(yin)  # each value calculated for given t is added to the list
    return np.array(results)


def backward_forward(function, time_vector, initial_conditions, h):
    # allows for error computation. we just need to compute the difference at the starting point
    y_forward = RK4(function, time_vector, initial_conditions, h)  # call RK4 in forward movement
    new_y0 = y_forward[-1]  # new initial conditions
    y_backward = RK4(function, np.flip(time_vector), new_y0, -h)  # call RK4 backwards
    return y_forward, y_backward


# We use our own units : distances in AU, mass in Suns, time in Days

# initial variables
m_sun = 1  # mass of the Sun
m_object = 0  # mass of the object studied
a = 2  # semi-major axis
G = 0.000295824  # gravitation constant expressed in our own system of units
k = np.sqrt(G)

# initial conditions [pos x, pos y, pos z, v x, v y, v z]
init_state = np.array([a, 0, 0, 0, k / np.sqrt(a), 0])

niter = 1000  # number of iterations
tf = 1033  # final time
ti = 0  # starting time
step = 1  # step wanted

time = np.arange(ti, tf, step) # creation of the list containing each value of time

forward, backward = backward_forward(f, time, init_state, step)

# plot of the trajectory
for i in range(len(forward)):
    plt.plot(forward[i][0], forward[i][1], 'o', color='red')
plt.axis('equal')
plt.show()

# computation of the error between forward and backward
err_x = 150e6 * abs(forward[0][0] - backward[-1][0])
err_y = 150e6 * abs(forward[0][1] - backward[-1][1])
print(err_x, err_y)

# TODO: Add automatic step adjustment in function of the error

