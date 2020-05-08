import matplotlib.pyplot as plt
import numpy as np
import time as chrono


class planet(object):
    def __init__(self, m, a, i, e, Omega, omega, M0):
        self.m = m
        self.a = a
        self.i = np.radians(i)
        self.e = e
        self.Omega = np.radians(Omega)
        self.omega = np.radians(omega)
        self.M0 = np.radians(M0)
        self.T = np.sqrt((4 * np.pi ** 2) / (G * (m_sun + self.m)) * self.a ** 3)
        self.w = 2 * np.pi / self.T

    def orbitalparam2vector(self, t):
        self.x = self.a * np.cos(self.w * t)
        self.y = self.a * np.sin(self.w * t)
        self.z = 0
        return [self.x, self.y, self.z]

    def orbitalparam2vectorList(self, timevector):
        self.posList = [self.completeOrbitalElem2Vector(t) for t in timevector]
        return np.array(self.posList)

    def completeOrbitalElem2Vector(self, t):
        self.n = k / np.sqrt(self.a ** 3)
        self.M = self.M0 + self.n * (t)
        self.E = self.newton(self.keplerEquation, self.M0)
        self.bigX = self.a * (np.cos(self.E) - self.e)
        self.bigY = self.a * np.sqrt(1 - self.e ** 2) * np.sin(self.E)
        self.bigXdot = - self.n * self.a ** 2 / \
            (self.a * (1 - self.e * np.cos(self.E))) * np.sin(self.E)
        self.bigYdot = self.n * self.a ** 2 / \
            (self.a * (1 - self.e * np.cos(self.E))) * np.sqrt(1 - self.e ** 2) * np.cos(self.E)
        self.position = np.dot(np.dot(np.dot(self.rotation3(-self.Omega),
                                             self.rotation1(-self.i)),
                                      self.rotation3(-self.omega)),
                               np.array([[self.bigX], [self.bigY], [0]]))
        self.velocity = np.dot(np.dot(np.dot(self.rotation3(-self.Omega),
                                             self.rotation1(-self.i)),
                                      self.rotation3(-self.omega)),
                               np.array([[self.bigXdot], [self.bigYdot], [0]]))
        return [self.position[0, 0], self.position[1, 0], self.position[2, 0],
                self.velocity[0, 0], self.velocity[1, 0], self.velocity[2, 0]]

    def rotation1(self, theta):
        return np.array([[1, 0, 0],
                         [0, np.cos(theta), np.sin(theta)],
                         [0, -np.sin(theta), np.cos(theta)]])

    def rotation3(self, theta):
        return np.array([[np.cos(theta), np.sin(theta), 0],
                         [-np.sin(theta), np.cos(theta), 0],
                         [0, 0, 1]])

    def newton(self, f, E0, h=1e-4):
        E = E0
        for _ in range(5):
            diff = (f(E + h) - f(E)) / h
            E -= f(E) / diff
        return E

    def keplerEquation(self, E):
        return E - self.e * np.sin(E) - self.M


class MultiBody():
    ''' This class groups together 3 functions :
        - the Equation of Motion, which is the core of the program
        - The Ruunge Kutta 4 integrator
        - The Forward Backward method'''

    @classmethod
    def func(cls, t, y, planets):
        ''' State space representation of the Equation of Perturbated Motion
            Takes into account every selected planet.'''

        y0 = y[3]  # velocity on x
        y1 = y[4]  # velocity on y
        y2 = y[5]  # velocity on z
        r = np.sqrt(y[0] ** 2 + y[1] ** 2 + y[2] ** 2)  # norm of the vector r
        y3 = -G * (m_sun + float(asteroid.m)) / (r ** 3) * y[0]
        y4 = -G * (m_sun + float(asteroid.m)) / (r ** 3) * y[1]
        y5 = -G * (m_sun + float(asteroid.m)) / (r ** 3) * y[2]
        for planet in planets:
            pos = planet.completeOrbitalElem2Vector(t)
            # delta is the difference between 'r' and 'pos', it is the distance between asteroid & planet
            delta = np.sqrt((y[0] - pos[0]) ** 2 + (y[1] - pos[1])
                            ** 2 + (y[2] - pos[2]) ** 2)
            # equation of motion on x
            y3 += - G * planet.m * ((y[0] - pos[0]) / (delta ** 3) + pos[0] / np.linalg.norm(pos) ** 3)
            # equation of motion on y
            y4 += - G * planet.m * ((y[1] - pos[1]) / (delta ** 3) + pos[1] / np.linalg.norm(pos) ** 3)
            # equation of motion on z
            y5 += - G * planet.m * ((y[2] - pos[2]) / (delta ** 3) + pos[2] / np.linalg.norm(pos) ** 3)
        return np.array([y0, y1, y2, y3, y4, y5])

    @classmethod
    def RK4(cls, time_vector, initial_conditions, h, planets):
        ''' Runge kutta 4 integrator :
            takes a time vector, an initial conditions vector, a step and a list of planets
            as an input, and outputs the list of positions and accelerations'''

        results = []
        yin = initial_conditions
        results.append(yin)  # set the first value to the initial conditions
        for t in time_vector[1:]:
            k1 = cls.func(t, yin, planets)
            k2 = cls.func(t + h / 2, yin + h / 2 * k1, planets)
            k3 = cls.func(t + h / 2, yin + h / 2 * k2, planets)
            k4 = cls.func(t + h, yin + h * k3, planets)
            yin = yin + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            # each value calculated for given t is added to the list
            results.append(yin)
        return np.array(results)

    @classmethod
    def forward_backward(cls, time_vector, initial_conditions, h, planets):
        ''' Calls the RK4 integrator a first time from the initial condition,
            and a second time from the results, thus going back to the very
            first starting point. By computing the difference between the results
            and the initital conditions at the starting point, we obtain the
            errors due to the integration'''

        y_forward = cls.RK4(time_vector, initial_conditions, h, planets)  # call RK4 forwards
        new_y0 = y_forward[-1]  # new initial conditions
        y_backward = cls.RK4(np.flip(time_vector), new_y0, - h, planets)  # call RK4 backwards

        return y_forward, y_backward


def extract_vectors(results):
    '''takes the list of outputs from RK4 and extracts a list of position and velocity vectors'''

    r_list = [[results[i][j] for j in range(0, 3)] for i in range(len(results))]
    r_dot_list = [[results[i][j + 3] for j in range(0, 3)] for i in range(len(results))]
    return r_list, r_dot_list


def vector2orbitalparam(r, rdot):
    # takes two vectors : pos(x,y,z) and v(x,y,z) and computes the orbital parameters at this point
    semi_major_axis = (2 / np.linalg.norm(r) - np.linalg.norm(rdot) ** 2 / mu) ** (-1)
    eccentricity = np.linalg.norm(np.cross(rdot, np.cross(r, rdot)) / mu - r / np.linalg.norm(r))
    k_vector = np.cross(r, rdot) / (np.linalg.norm(r) * np.linalg.norm(rdot))
    inclination = np.arccos(np.around(k_vector[2], 4))  # np.around rounds the value of k_vectors so it stays in [-1,1]
    return semi_major_axis, eccentricity, inclination


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


def plotOrbitalVariation(a, e, i, t):
    # Plots the orbital parameters in order to visualise their variations over time
    plt.subplot(3, 1, 1)
    plt.plot(t, a)
    plt.title('Variations of Semi-major axis [a]')
    plt.subplot(3, 1, 2)
    plt.plot(t, e)
    plt.title('Variations of Eccentricity [e]')
    plt.subplot(3, 1, 3)
    plt.plot(t, i)
    plt.title('Variations of Inclination [i]')
    plt.show()


# =============================================================================================
# Definition of the initial parameters
# =============================================================================================

# We use our own units : distances in AU, mass in Suns, time in Days

# initial variables
m_sun = 1  # mass of the Sun
G = 0.000295824  # gravitation constant expressed in our own system of units
k = np.sqrt(G)
mu = G * m_sun

# Creation of the each planet from their orbital parameters at J2000
# mercury=planet(m_sun / 6023622.047, 0.38709893, 7.00487, 0.20563069, 48.33167, 77.45645, 126.464)
# venus=planet(m_sun / 408544.7263,  0.72333199, 3.39471, 0.00677323, 76.68069, 131.53298, -26.23394)
# earth=planet(m_sun / 332965.0462, 1, 0.00005, 0.01671022, 348.73936, 102.94719, -351.2222)
# mars=planet(m_sun / 3098854.873, 1.52366231,  1.85061,  0.09341233, 49.57854, 336.04084, -30.16606)
jupiter = planet(m_sun / 1047.348625, 5.202603, 1.303, 0.048498, 100.46, -86.13, 20.0)
# saturn=planet(m_sun / 3498.926925, 9.5370703, 2.484, 0.054151, 113.72, 92.43, -156.2)
# uranus=planet(m_sun / 22906.30182, 19.19126393, 0.76986, 0.04716771, 74.22988, 170.96424, 68.0392)
# neptune=planet(, m_sun / 19418.13922, 30.06896348, 1.76917, 0.00858587,  131.72169, 44.97135, 128.19)

# integration parameters
tf = 50000  # Number of days
ti = 5055.5  # starting time (Epoch)
step = 1  # step wanted

# creation of the list containing each value of time
time = np.arange(ti, tf + step + ti, step)

# initial conditions of the asteroid [pos x, pos y, pos z, v x, v y, v z]
asteroid = planet(0, 5.454, 108.358, 0.3896, 276.509, 226.107, 146.88)
init_state = np.array(asteroid.completeOrbitalElem2Vector(ti))

# =============================================================================================
# Start of the computation for 3 body problem
# =============================================================================================
start_time = chrono.time()
forward2, backward2 = MultiBody.forward_backward(time, init_state, step, [jupiter])

# computation of the error between forward and backward
err_x = 150e6 * abs(forward2[0][0] - backward2[-1][0]) / 2
err_y = 150e6 * abs(forward2[0][1] - backward2[-1][1]) / 2
err_z = 150e6 * abs(forward2[0][2] - backward2[-1][2]) / 2
print(' Error on x : ', err_x, ' km\n', 'Error on y : ', err_y, ' km\n', 'Error on z : ', err_z, ' km')

# plot of the trajectory
jup_param = jupiter.orbitalparam2vectorList(time)
plt.plot(forward2[:, 0], forward2[:, 1], 'o', color='red', markersize=1, label='Asteroid')  # plot of the asteroid
plt.plot(jup_param[:, 0], jup_param[:, 1], 'o', color='green', markersize=1, label='Jupiter')  # plot of Jupiter
plt.axis('equal')
plt.title('perturbed trajectory around the sun')
plt.legend()
plt.show()

# get the position and velocity from previous results
r_list, rdot_list = extract_vectors(forward2)

# calculate the orbital parameters from the position and velocity
a_list, e_list, i_list = orbital_parameters_list(r_list, rdot_list)

# plot the orbital parameters
plotOrbitalVariation(a_list, e_list, i_list, time)

stop_time = chrono.time()
print("Computation time = ", stop_time - start_time, " seconds")
