# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_v1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 845)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ------------------------------------------------------------------------
        self.groupIntegrationParam = QtWidgets.QGroupBox(self.centralwidget)
        self.groupIntegrationParam.setGeometry(QtCore.QRect(320, 10, 281, 241))
        self.groupIntegrationParam.setObjectName("groupIntegrationParam")

        self.inputFinalTime = QtWidgets.QLineEdit(self.groupIntegrationParam)
        self.inputFinalTime.setGeometry(QtCore.QRect(150, 40, 113, 22))
        self.inputFinalTime.setObjectName("inputFinalTime")

        self.label_2 = QtWidgets.QLabel(self.groupIntegrationParam)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 111, 16))
        self.label_2.setObjectName("label_2")

        self.inputStep = QtWidgets.QLineEdit(self.groupIntegrationParam)
        self.inputStep.setGeometry(QtCore.QRect(150, 70, 113, 22))
        self.inputStep.setObjectName("inputStep")

        self.label_4 = QtWidgets.QLabel(self.groupIntegrationParam)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 111, 16))
        self.label_4.setObjectName("label_4")

        # ------------------------------------------------------------------------
        self.groupPlots = QtWidgets.QGroupBox(self.centralwidget)
        self.groupPlots.setGeometry(QtCore.QRect(40, 320, 1031, 501))
        self.groupPlots.setAlignment(QtCore.Qt.AlignCenter)
        self.groupPlots.setObjectName("groupPlots")

        self.label_3 = QtWidgets.QLabel(self.groupPlots)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 501, 21))
        self.label_3.setObjectName("label_3")

        self.label = QtWidgets.QLabel(self.groupPlots)
        self.label.setGeometry(QtCore.QRect(580, 10, 501, 21))
        self.label.setObjectName("label")

        self.plotTrajectory = QtWidgets.QLabel(self.groupPlots)
        self.plotTrajectory.setEnabled(True)
        self.plotTrajectory.setGeometry(QtCore.QRect(20, 40, 441, 441))
        self.plotTrajectory.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.plotTrajectory.setText("")
        self.plotTrajectory.setPixmap(QtGui.QPixmap("Plots/Robert.png"))
        self.plotTrajectory.setScaledContents(True)
        self.plotTrajectory.setObjectName("plotTrajectory")

        self.plotOrbitVar = QtWidgets.QLabel(self.groupPlots)
        self.plotOrbitVar.setGeometry(QtCore.QRect(580, 40, 441, 441))
        self.plotOrbitVar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.plotOrbitVar.setText("")
        self.plotOrbitVar.setPixmap(QtGui.QPixmap("Plots/Robert.png"))
        self.plotOrbitVar.setScaledContents(True)
        self.plotOrbitVar.setObjectName("plotOrbitVar")

        self.trajectory_canvas = FigureCanvasQTAgg(Figure(figsize=(5, 5)))
        self.orbitVar_canvas = FigureCanvasQTAgg(Figure(figsize=(5, 5)))

        # ------------------------------------------------------------------------
        self.groupPerturbPlanets = QtWidgets.QGroupBox(self.centralwidget)
        self.groupPerturbPlanets.setGeometry(QtCore.QRect(10, 10, 281, 241))
        self.groupPerturbPlanets.setObjectName("groupPerturbPlanets")

        self.widget = QtWidgets.QWidget(self.groupPerturbPlanets)
        self.widget.setGeometry(QtCore.QRect(10, 26, 261, 191))
        self.widget.setObjectName("widget")

        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.mercuryCheckBox = QtWidgets.QCheckBox(self.widget)
        self.mercuryCheckBox.setEnabled(False) # TODO : implement Mercury
        self.mercuryCheckBox.setTristate(False)
        self.mercuryCheckBox.setObjectName("mercuryCheckBox")
        self.gridLayout.addWidget(self.mercuryCheckBox, 0, 0, 1, 1)
        self.jupiterCheckBox = QtWidgets.QCheckBox(self.widget)
        self.jupiterCheckBox.setEnabled(True)
        self.jupiterCheckBox.setTristate(False)
        self.jupiterCheckBox.setObjectName("jupiterCheckBox")
        self.gridLayout.addWidget(self.jupiterCheckBox, 0, 1, 1, 1)
        self.venusCheckBox = QtWidgets.QCheckBox(self.widget)
        self.venusCheckBox.setEnabled(False)  # TODO : implement Venus
        self.venusCheckBox.setTristate(False)
        self.venusCheckBox.setObjectName("venusCheckBox")
        self.gridLayout.addWidget(self.venusCheckBox, 1, 0, 1, 1)
        self.saturnCheckBox = QtWidgets.QCheckBox(self.widget)
        self.saturnCheckBox.setEnabled(False)  # TODO : implement Saturn
        self.saturnCheckBox.setTristate(False)
        self.saturnCheckBox.setObjectName("saturnCheckBox")
        self.gridLayout.addWidget(self.saturnCheckBox, 1, 1, 1, 1)
        self.earthCheckBox = QtWidgets.QCheckBox(self.widget)
        self.earthCheckBox.setEnabled(False)  # TODO : implement Earth
        self.earthCheckBox.setTristate(False)
        self.earthCheckBox.setObjectName("earthCheckBox")
        self.gridLayout.addWidget(self.earthCheckBox, 2, 0, 1, 1)
        self.uranusCheckBox = QtWidgets.QCheckBox(self.widget)
        self.uranusCheckBox.setEnabled(False)  # TODO : implement Urnanus
        self.uranusCheckBox.setTristate(False)
        self.uranusCheckBox.setObjectName("uranusCheckBox")
        self.gridLayout.addWidget(self.uranusCheckBox, 2, 1, 1, 1)
        self.marsCheckBox = QtWidgets.QCheckBox(self.widget)
        self.marsCheckBox.setEnabled(False)  # TODO : implement Mars
        self.marsCheckBox.setTristate(False)
        self.marsCheckBox.setObjectName("marsCheckBox")
        self.gridLayout.addWidget(self.marsCheckBox, 3, 0, 1, 1)
        self.neptuneCheckBox = QtWidgets.QCheckBox(self.widget)
        self.neptuneCheckBox.setEnabled(False)  # TODO : implement Neptune
        self.neptuneCheckBox.setTristate(False)
        self.neptuneCheckBox.setObjectName("neptuneCheckBox")
        self.gridLayout.addWidget(self.neptuneCheckBox, 3, 1, 1, 1)

        # ------------------------------------------------------------------------
        self.groupAsteroidParam = QtWidgets.QGroupBox(self.centralwidget)
        self.groupAsteroidParam.setGeometry(QtCore.QRect(630, 10, 471, 241))
        self.groupAsteroidParam.setObjectName("groupAsteroidParam")

        self.groupInitialConditions = QtWidgets.QGroupBox(self.groupAsteroidParam)
        self.groupInitialConditions.setGeometry(QtCore.QRect(250, 20, 211, 211))
        self.groupInitialConditions.setObjectName("groupInitialConditions")
        self.groupInitialConditions.hide()

        self.widget1 = QtWidgets.QWidget(self.groupInitialConditions)
        self.widget1.setGeometry(QtCore.QRect(10, 20, 191, 191))
        self.widget1.setObjectName("widget1")
        self.formLayout = QtWidgets.QFormLayout(self.widget1)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.label_7 = QtWidgets.QLabel(self.widget1)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)

        self.inputPosX = QtWidgets.QLineEdit(self.widget1)
        self.inputPosX.setObjectName("inputPosX")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inputPosX)

        self.label_8 = QtWidgets.QLabel(self.widget1)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)

        self.inputPosY = QtWidgets.QLineEdit(self.widget1)
        self.inputPosY.setObjectName("inputPosY")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.inputPosY)

        self.label_9 = QtWidgets.QLabel(self.widget1)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)

        self.inputPosZ = QtWidgets.QLineEdit(self.widget1)
        self.inputPosZ.setObjectName("inputPosZ")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.inputPosZ)

        self.label_10 = QtWidgets.QLabel(self.widget1)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_10)

        self.inputVelX = QtWidgets.QLineEdit(self.widget1)
        self.inputVelX.setObjectName("inputVelX")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.inputVelX)

        self.label_11 = QtWidgets.QLabel(self.widget1)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_11)

        self.inputVelY = QtWidgets.QLineEdit(self.widget1)
        self.inputVelY.setObjectName("inputVelY")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.inputVelY)

        self.label_12 = QtWidgets.QLabel(self.widget1)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_12)

        self.inputVelZ = QtWidgets.QLineEdit(self.widget1)
        self.inputVelZ.setObjectName("inputVelZ")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.inputVelZ)

        # ------------------------------------------------------------------------
        self.groupOrbitalParameters = QtWidgets.QGroupBox(self.groupAsteroidParam)
        self.groupOrbitalParameters.setGeometry(QtCore.QRect(10, 20, 231, 211))

        self.groupOrbitalParameters.setObjectName("groupOrbitalParameters")
        self.label_5 = QtWidgets.QLabel(self.groupOrbitalParameters)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 101, 16))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.groupOrbitalParameters)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 121, 16))
        self.label_6.setObjectName("label_6")

        self.inputAsteroidMass = QtWidgets.QLineEdit(self.groupOrbitalParameters)
        self.inputAsteroidMass.setGeometry(QtCore.QRect(120, 30, 101, 22))
        self.inputAsteroidMass.setObjectName("inputAsteroidMass")

        self.inputAsteroidSmAxis = QtWidgets.QLineEdit(self.groupOrbitalParameters)
        self.inputAsteroidSmAxis.setGeometry(QtCore.QRect(120, 60, 101, 22))
        self.inputAsteroidSmAxis.setObjectName("inputAsteroidSmAxis")

        self.circularCheckBox = QtWidgets.QCheckBox(self.groupOrbitalParameters)
        self.circularCheckBox.setGeometry(QtCore.QRect(120, 90, 101, 22))
        self.circularCheckBox.setTristate(False)
        self.circularCheckBox.setObjectName("circularCheckBox")
        self.circularCheckBox.setChecked(True)
        self.circularCheckBox.stateChanged.connect(self.hide_show_InitialCond)

        # ------------------------------------------------------------------------
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(250, 300, 631, 16))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")

        # ------------------------------------------------------------------------
        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(510, 260, 93, 28))
        self.StartButton.setObjectName("StartButton")

        self.StartButton.clicked.connect(self.Start)

        # ------------------------------------------------------------------------
        self.groupPerturbPlanets.raise_()
        self.groupPlots.raise_()
        self.groupIntegrationParam.raise_()
        self.groupAsteroidParam.raise_()
        self.progressBar.raise_()
        self.StartButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        # ------------------------------------------------------------------------
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # ------------------------------------------------------------------------
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # ------------------------------------------------------------------------
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Asteroid Trajectory"))
        self.groupIntegrationParam.setTitle(_translate("MainWindow", "Integration parameters"))
        self.label_2.setText(_translate("MainWindow", "Number of days :"))
        self.label_4.setText(_translate("MainWindow", "Step :"))
        self.groupPlots.setTitle(_translate("MainWindow", "Plots"))
        self.label_3.setText(_translate("MainWindow", "Trajectory of the asteroid"))
        self.label.setText(_translate("MainWindow", "Variations of the orbital parameters"))
        self.groupPerturbPlanets.setTitle(_translate("MainWindow", "Include perturbations from"))
        self.mercuryCheckBox.setText(_translate("MainWindow", "Mercury"))
        self.jupiterCheckBox.setText(_translate("MainWindow", "Jupiter"))
        self.venusCheckBox.setText(_translate("MainWindow", "Venus"))
        self.saturnCheckBox.setText(_translate("MainWindow", "Saturn"))
        self.earthCheckBox.setText(_translate("MainWindow", "Earth"))
        self.uranusCheckBox.setText(_translate("MainWindow", "Uranus"))
        self.marsCheckBox.setText(_translate("MainWindow", "Mars"))
        self.neptuneCheckBox.setText(_translate("MainWindow", "Neptune"))
        self.groupAsteroidParam.setTitle(_translate("MainWindow", "Asteroid parameters"))
        self.groupInitialConditions.setTitle(_translate("MainWindow", "Initial conditions"))
        self.label_7.setText(_translate("MainWindow", "Position x :"))
        self.label_8.setText(_translate("MainWindow", "Position y :"))
        self.label_9.setText(_translate("MainWindow", "Position z :"))
        self.label_10.setText(_translate("MainWindow", "Velocity x :"))
        self.label_11.setText(_translate("MainWindow", "Velocity y :"))
        self.label_12.setText(_translate("MainWindow", "Velocity z :"))
        self.groupOrbitalParameters.setTitle(_translate("MainWindow", "Orbital parameters"))
        self.label_5.setText(_translate("MainWindow", "Mass (in Suns):"))
        self.label_6.setText(_translate("MainWindow", "Semi-major axis :"))
        self.circularCheckBox.setText(_translate("MainWindow", "Circular orbit"))
        self.StartButton.setText(_translate("MainWindow", "Start !"))

    def Start(self):  # TODO : clean all this shit with functions
        if self.jupiterCheckBox.checkState():  # TODO : implement other planets
            jupiter = planet(m_sun / 1047.348625, 5.2, 0, 0)
            jupiter.orbital_period()

            if self.circularCheckBox.checkState():
                self.init_state = np.array(
                    [float(self.inputAsteroidSmAxis.text()), 0, 0,
                     0, k / np.sqrt(float(self.inputAsteroidSmAxis.text())), 0])
            else:  # TODO : Verify the type of the input and make it foolproof
                self.init_state = np.array(
                    [float(self.inputPosX.text()), float(self.inputPosY.text()), float(self.inputPosZ.text()),
                     float(self.inputVelX.text()), float(self.inputVelY.text()), float(self.inputVelZ.text())])

            self.time = np.arange(0, int(self.inputFinalTime.text()) + int(self.inputStep.text()),
                             int(self.inputStep.text()))  # creation of the list containing each value of time

            self.results = threeBody.RK4(self.time, self.init_state, int(self.inputStep.text()), jupiter)

            self.progress = 0
            self.trajectory_ax = self.trajectory_canvas.figure.subplots()
            for i in range(len(self.results)):
                self.progressBar.setValue(self.progress)
                self.progress += 100 / len(self.results)
                self.trajectory_ax.plot(self.results[i][0], self.results[i][1], 'o', color='red',
                                        markersize=1)  # plot of the asteroid
                self.trajectory_ax.plot(jupiter.orbitalparam2vectorList(self.time)[i][0],
                                        jupiter.orbitalparam2vectorList(self.time)[i][1], 'o',
                                        color='green', markersize=1)  # plot of Jupiter
            self.trajectory_canvas.print_png('Plots/trajectory.png')

            self.r_list, self.rdot_list = extract_vectors(self.results)
            # calculate the orbital parameters from the position and velocity
            self.a_list, self.e_list, self.i_list = orbital_parameters_list(self.r_list, self.rdot_list)
            # plot the orbital parameters
            self.plotOrbitalVariation(self.a_list, self.e_list, self.i_list, self.time[1:])

            self.progressBar.setValue(100)

            self.plotTrajectory.setPixmap(QtGui.QPixmap("Plots/trajectory.png"))
            self.plotOrbitVar.setPixmap(QtGui.QPixmap("Plots/orbitVar.png"))
        else:  # TODO : No Jupiter
            pass

    def hide_show_InitialCond(self):
        if self.circularCheckBox.checkState():
            self.groupInitialConditions.hide()
        else:
            self.groupInitialConditions.show()

    def plotOrbitalVariation(self, a, e, i, t):
        # Plots the orbital parameters in order to visualise their variations over time
        self.orbitVar_ax1 = self.orbitVar_canvas.figure.subplots()
        self.orbitVar_ax1.plot(t, a)
        '''#self.orbitVar_ax1.title('Variations of Semi-major axis [a]')
        self.orbitVar_ax2 = self.orbitVar_canvas.figure.subplots(312)
        self.orbitVar_ax2.plot(t, e)
        #self.orbitVar_ax2.title('Variations of Eccentricity [e]')
        self.orbitVar_ax3 = self.orbitVar_canvas.figure.subplots(313)
        self.orbitVar_ax2.plot(t, e)
        #self.orbitVar_ax2.title('Variations of Inclination [i]')'''

        self.orbitVar_canvas.print_png('Plots/orbitVar.png')


class planet(object):
    def __init__(self, m, a, i, e):
        self.m = m
        self.a = a
        self.i = i
        self.e = e

    def orbital_period(self):
        self.T = np.sqrt((4 * np.pi ** 2) / (G * (m_sun + self.m)) * self.a ** 3)
        self.w = 2 * np.pi / self.T

    def orbitalparam2vector(self, t):
        x = self.a * np.cos(self.w * t)
        y = self.a * np.sin(self.w * t)
        z = 0
        return [x, y, z]

    def orbitalparam2vectorList(self, timevector):
        self.posList = [self.orbitalparam2vector(t) for t in timevector]
        return self.posList


class twoBody():  # Only the Sun exerts it's influence on the body.
    @classmethod
    def func(cls, t, y):  # using the state space representation of the equation of motion
        y0 = y[3]  # velocity on x
        y1 = y[4]  # velocity on y
        y2 = y[5]  # velocity on z
        r = np.sqrt(y[0] ** 2 + y[1] ** 2 + y[2] ** 2)  # norm of the vector r
        y3 = -G * (m_sun + float(ui.inputAsteroidMass.text())) / (r ** 3) * y[0]  # equation of motion on x
        y4 = -G * (m_sun + float(ui.inputAsteroidMass.text())) / (r ** 3) * y[1]  # equation of motion on y
        y5 = -G * (m_sun + float(ui.inputAsteroidMass.text())) / (r ** 3) * y[2]  # equation of motion on z
        return np.array([y0, y1, y2, y3, y4, y5])

    # TODO : variable step ?
    @classmethod
    def RK4(cls, time_vector, initial_conditions, h):
        # Definition of the Runge-Kutta method at the order 4
        results = []
        yin = initial_conditions
        results.append(yin)  # set the first value to the initial conditions
        for t in time_vector[1:]:
            k1 = cls.func(t, yin)
            k2 = cls.func(t + h / 2, yin + h / 2 * k1)
            k3 = cls.func(t + h / 2, yin + h / 2 * k2)
            k4 = cls.func(t + h, yin + h * k3)
            yin = yin + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            results.append(yin)  # each value calculated for given t is added to the list
        return np.array(results)

    @classmethod
    def forward_backward(cls, time_vector, initial_conditions, h):
        # allows for error computation. we just need to compute the difference at the starting point
        y_forward = cls.RK4(time_vector, initial_conditions, h)  # call RK4 in forward movement
        new_y0 = y_forward[-1]  # new initial conditions
        y_backward = cls.RK4(np.flip(time_vector), new_y0, -h)  # call RK4 backwards
        return y_forward, y_backward


class threeBody():
    @classmethod
    def func(cls, t, y, planet):
        y0 = y[3]  # velocity on x
        y1 = y[4]  # velocity on y
        y2 = y[5]  # velocity on z
        r = np.sqrt(y[0] ** 2 + y[1] ** 2 + y[2] ** 2)  # norm of the vector r
        # delta is the difference between r and position_Jupiter (distance between the asteroid and jupiter)
        delta = np.sqrt(
            (y[0] - planet.orbitalparam2vector(t)[0]) ** 2 + (y[1] - planet.orbitalparam2vector(t)[1]) ** 2 + (
                    y[2] - planet.orbitalparam2vector(t)[2]) ** 2)
        # equation of motion on x
        y3 = -G * (m_sun + float(ui.inputAsteroidMass.text())) / (r ** 3) * y[0] \
             - G * planet.m * ((y[0] - planet.orbitalparam2vector(t)[0]) / (delta ** 3)
                               + planet.orbitalparam2vector(t)[0] / np.linalg.norm(planet.orbitalparam2vector(t)) ** 3)
        # equation of motion on y
        y4 = -G * (m_sun + float(ui.inputAsteroidMass.text())) / (r ** 3) * y[1] \
             - G * planet.m * ((y[1] - planet.orbitalparam2vector(t)[1]) / (delta ** 3)
                               + planet.orbitalparam2vector(t)[1] / np.linalg.norm(planet.orbitalparam2vector(t)) ** 3)
        # equation of motion on z
        y5 = -G * (m_sun + float(ui.inputAsteroidMass.text())) / (r ** 3) * y[2] \
             - G * planet.m * ((y[2] - planet.orbitalparam2vector(t)[2]) / (delta ** 3)
                               + planet.orbitalparam2vector(t)[2] / np.linalg.norm(planet.orbitalparam2vector(t)) ** 3)
        return np.array([y0, y1, y2, y3, y4, y5])

    @classmethod
    def RK4(cls, time_vector, initial_conditions, h, planet):
        # Definition of the Runge-Kutta method at the order 4
        results = []
        yin = initial_conditions
        results.append(yin)  # set the first value to the initial conditions
        for i in range(1, len(time_vector[1:])):
            k1 = cls.func(time_vector[i], yin, planet)
            k2 = cls.func(time_vector[i] + h / 2, yin + h / 2 * k1, planet)
            k3 = cls.func(time_vector[i] + h / 2, yin + h / 2 * k2, planet)
            k4 = cls.func(time_vector[i] + h, yin + h * k3, planet)
            yin = yin + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            results.append(yin)  # each value calculated for given t is added to the list
        return np.array(results)


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





if __name__ == "__main__":
    m_sun = 1  # mass of the Sun
    G = 0.000295824  # gravitation constant expressed in our own system of units
    k = np.sqrt(G)
    mu = G * m_sun

    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
