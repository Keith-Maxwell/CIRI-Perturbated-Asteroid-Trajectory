import matplotlib.pyplot as plt
import numpy as np


# using the state space representation of the equation of motion
# Only the Sun exerts it's influence on the body.
def f2body(t, y):
    y0 = y[3]  # velocity on x
    y1 = y[4]  # velocity on y
    y2 = y[5]  # velocity on z
    r = np.sqrt(y[0] ** 2 + y[1] ** 2 + y[2] ** 2)  # norm of the vector r
    y3 = -G * (m_sun + m_object) / (r ** 3) * y[0]  # equation of motion on x
    y4 = -G * (m_sun + m_object) / (r ** 3) * y[1]  # equation of motion on y
    y5 = -G * (m_sun + m_object) / (r ** 3) * y[2]  # equation of motion on z
    return np.array([y0, y1, y2, y3, y4, y5])


# TODO : Influence of Jupiter
def f3body(t, y, position_Jupiter):
    y0 = y[3]  # velocity on x
    y1 = y[4]  # velocity on y
    y2 = y[5]  # velocity on z
    r = np.sqrt(y[0] ** 2 + y[1] ** 2 + y[2] ** 2)  # norm of the vector r
    # delta is the difference between r and position_Jupiter (distance between the asteroid and jupiter)
    delta = np.sqrt(
        (y[0] - position_Jupiter[0]) ** 2 + (y[1] - position_Jupiter[1]) ** 2 + (y[2] - position_Jupiter[2]) ** 2)
    # equation of motion on x
    y3 = -G * (m_sun + m_object) / (r ** 3) * y[0] \
         - G * m_jup * ((y[0] - position_Jupiter[0]) / (delta ** 3)
                        + position_Jupiter[0] / np.linalg.norm(position_Jupiter) ** 3)
    # equation of motion on y
    y4 = -G * (m_sun + m_object) / (r ** 3) * y[1] \
         - G * m_jup * ((y[1] - position_Jupiter[1]) / (delta ** 3)
                        + position_Jupiter[1] / np.linalg.norm(position_Jupiter) ** 3)
    # equation of motion on z
    y5 = -G * (m_sun + m_object) / (r ** 3) * y[2] \
         - G * m_jup * ((y[2] - position_Jupiter[2]) / (delta ** 3)
                        + position_Jupiter[2] / np.linalg.norm(position_Jupiter) ** 3)
    return np.array([y0, y1, y2, y3, y4, y5])


# TODO : variable step ?
def RK4(function, time_vector, initial_conditions, h):
    # Definition of the Runge-Kutta method at the order 4
    results = []
    yin = initial_conditions
    results.append(yin)  # set the first value to the initial conditions
    for t in time_vector[1:]:
        k1 = function(t, yin)
        k2 = function(t + h / 2, yin + h / 2 * k1)
        k3 = function(t + h / 2, yin + h / 2 * k2)
        k4 = function(t + h, yin + h * k3)
        yin = yin + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        results.append(yin)  # each value calculated for given t is added to the list
    return np.array(results)


def forward_backward(function, time_vector, initial_conditions, h):
    # allows for error computation. we just need to compute the difference at the starting point
    y_forward = RK4(function, time_vector, initial_conditions, h)  # call RK4 in forward movement
    new_y0 = y_forward[-1]  # new initial conditions
    y_backward = RK4(function, np.flip(time_vector), new_y0, -h)  # call RK4 backwards
    return y_forward, y_backward


def extract_vectors(results):
    # takes the list of outputs from RK4 and extracts a list of position and velocity vectors
    r_list = []
    r_dot_list = []
    for i in range(len(results)):
        r = []
        r_dot = []
        for j in range(0, 3):
            r.append(results[i][j])
            r_dot.append(results[i][j + 3])
        r_list.append(r)
        r_dot_list.append(r_dot)
    return r_list, r_dot_list


def vector2orbitalparam(r, rdot):
    # takes two vectors : pos(x,y,z) and v(x,y,z) and computes the orbital parameters at this point
    semi_major_axis = (2 / np.linalg.norm(r) - np.linalg.norm(rdot) ** 2 / mu) ** (-1)
    eccentricity = np.linalg.norm(np.cross(rdot, np.cross(r, rdot)) / mu - r / np.linalg.norm(r))
    k_vector = np.cross(r, rdot) / (np.linalg.norm(r) * np.linalg.norm(rdot))
    inclination = np.arccos(np.around(k_vector[2], 4))  # np.around rounds the value of k_vectors so it stays in [-1,1]
    return semi_major_axis, eccentricity, inclination


# TODO : conversion of orbital elements to position and velocity vectors (for Jupiter)
def orbitalparam2vector(a, t):
    x_jup = a * np.cos(w_jup * t)
    y_jup = a * np.sin(w_jup * t)
    z_jup = 0
    return np.array([x_jup, y_jup, z_jup])


def orbital_parameters_list(r, rdot):
    # takes the list of position vectors and velocity vectors and computes the corresponding
    # orbital parameters at each point. Returns individual lists of those parameters
    a_list = []
    e_list = []
    i_list = []
    for iii in range(len(r)):
        a, e, i = vector2orbitalparam(r[iii], rdot[iii])
        a_list.append(a)
        e_list.append(e)
        i_list.append(i)
    return a_list, e_list, i_list


def orbit_plot_var(a, e, i, t):
    # Plots the orbital parameters in order to visualise their variations over time
    plt.subplot(3, 1, 1)
    plt.plot(t, a)
    plt.title('Semi-major axis [a]')
    plt.subplot(3, 1, 2)
    plt.plot(t, e)
    plt.title('Eccentricity [e]')
    plt.subplot(3, 1, 3)
    plt.plot(t, i)
    plt.title('Inclination [i]')
    plt.show()


# =============================================================================================
# Definition of the initial parameters
# =============================================================================================

# We use our own units : distances in AU, mass in Suns, time in Days

# initial variables
m_sun = 1  # mass of the Sun
m_object = 0  # mass of the object studied
a = 2  # semi-major axis
G = 0.000295824  # gravitation constant expressed in our own system of units
k = np.sqrt(G)
mu = G * m_sun

# definition of Jupiter orbital parameters
m_jup = m_sun / 1047.348625
a_jup = 5.2
i_jup = 0
e_jup = 0
T_jup = np.sqrt((4 * np.pi ** 2) / (G * (m_sun + m_jup)) * a ** 3)  # orbital period of Jupiter in days
w_jup = 2 * np.pi / T_jup  # Angular velocity of Jupiter in radians per day

# initial conditions of the asteroid [pos x, pos y, pos z, v x, v y, v z]
init_state = np.array([a, 0, 0, 0, k / np.sqrt(a), 0])

# integration parameters
niter = 1000  # number of iterations (useless for now, it is auto-determined by np.arange)
tf = 1033  # final time
ti = 0  # starting time
step = 1  # step wanted

time = np.arange(ti, tf + step, step)  # creation of the list containing each value of time

# =============================================================================================
# Start of the computation for 2 body problem
# =============================================================================================

forward, backward = forward_backward(f2body, time, init_state, step)

# computation of the error between forward and backward
err_x = 150e6 * abs(forward[0][0] - backward[-1][0])
err_y = 150e6 * abs(forward[0][1] - backward[-1][1])
print(' Error on x : ', err_x, ' km\n', 'Error on y : ', err_y, ' km')

# TODO: Add automatic step adjustment in function of the error ?

# plot of the trajectory
for i in range(len(forward)):
    plt.plot(forward[i][0], forward[i][1], 'o', color='red', markersize=1)
plt.axis('equal')
plt.title('Unperturbed trajectory around the sun')
plt.show()

# get the position and velocity from previous results
r_list, rdot_list = extract_vectors(forward)

# calculate the orbital parameters from the position and velocity
a_list, e_list, i_list = orbital_parameters_list(r_list, rdot_list)

# plot the orbital parameters
orbit_plot_var(a_list, e_list, i_list, time)


# =============================================================================================
# Start of the computation for 3 body problem
# =============================================================================================


