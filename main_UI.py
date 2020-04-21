# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_v2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1114, 851)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ------------------------------------------------------------------------
        self.groupIntegrationParam = QtWidgets.QGroupBox(self.centralwidget)
        self.groupIntegrationParam.setGeometry(QtCore.QRect(210, 10, 241, 241))
        self.groupIntegrationParam.setObjectName("groupIntegrationParam")

        self.inputFinalTime = QtWidgets.QLineEdit(self.groupIntegrationParam)
        self.inputFinalTime.setGeometry(QtCore.QRect(120, 40, 113, 22))
        self.inputFinalTime.setObjectName("inputFinalTime")

        self.label_2 = QtWidgets.QLabel(self.groupIntegrationParam)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 111, 16))
        self.label_2.setObjectName("label_2")

        self.inputStep = QtWidgets.QLineEdit(self.groupIntegrationParam)
        self.inputStep.setGeometry(QtCore.QRect(120, 70, 113, 22))
        self.inputStep.setObjectName("inputStep")

        self.label_4 = QtWidgets.QLabel(self.groupIntegrationParam)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 111, 16))
        self.label_4.setObjectName("label_4")

        self.methodBox = QtWidgets.QComboBox(self.groupIntegrationParam)
        self.methodBox.setGeometry(QtCore.QRect(20, 110, 211, 22))
        self.methodBox.setObjectName("methodBox")
        self.methodBox.addItem("")

        self.forwBackCheckBox = QtWidgets.QCheckBox(self.groupIntegrationParam)
        self.forwBackCheckBox.setGeometry(QtCore.QRect(20, 150, 211, 20))
        self.forwBackCheckBox.setObjectName("forwBackCheckBox")

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

        self.figure1 = Figure()
        self.trajectory_canvas = FigureCanvas(self.figure1)
        self.figure2 = Figure()
        self.orbitVar_canvas = FigureCanvas(self.figure2)

        # ------------------------------------------------------------------------
        self.groupPerturbPlanets = QtWidgets.QGroupBox(self.centralwidget)
        self.groupPerturbPlanets.setGeometry(QtCore.QRect(10, 10, 191, 241))
        self.groupPerturbPlanets.setObjectName("groupPerturbPlanets")

        self.layoutWidget = QtWidgets.QWidget(self.groupPerturbPlanets)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 26, 171, 191))
        self.layoutWidget.setObjectName("layoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.mercuryCheckBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.mercuryCheckBox.setEnabled(False) # TODO : implement Mercury
        self.mercuryCheckBox.setTristate(False)
        self.mercuryCheckBox.setObjectName("mercuryCheckBox")
        self.gridLayout.addWidget(self.mercuryCheckBox, 0, 0, 1, 1)
        self.jupiterCheckBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.jupiterCheckBox.setObjectName("jupiterCheckBox")
        self.gridLayout.addWidget(self.jupiterCheckBox, 0, 1, 1, 1)
        self.venusCheckBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.venusCheckBox.setEnabled(False) # TODO : implement Venus
        self.venusCheckBox.setTristate(False)
        self.venusCheckBox.setObjectName("venusCheckBox")
        self.gridLayout.addWidget(self.venusCheckBox, 1, 0, 1, 1)
        self.saturnCheckBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.saturnCheckBox.setEnabled(False) # TODO : implement Saturn
        self.saturnCheckBox.setTristate(False)
        self.saturnCheckBox.setObjectName("saturnCheckBox")
        self.gridLayout.addWidget(self.saturnCheckBox, 1, 1, 1, 1)
        self.earthCheckBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.earthCheckBox.setEnabled(False) # TODO : implement Earth
        self.earthCheckBox.setTristate(False)
        self.earthCheckBox.setObjectName("earthCheckBox")
        self.gridLayout.addWidget(self.earthCheckBox, 2, 0, 1, 1)
        self.uranusCheckBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.uranusCheckBox.setEnabled(False)  # TODO : implement Urnanus
        self.uranusCheckBox.setTristate(False)
        self.uranusCheckBox.setObjectName("uranusCheckBox")
        self.gridLayout.addWidget(self.uranusCheckBox, 2, 1, 1, 1)
        self.marsCheckBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.marsCheckBox.setEnabled(False)  # TODO : implement Mars
        self.marsCheckBox.setTristate(False)
        self.marsCheckBox.setObjectName("marsCheckBox")
        self.gridLayout.addWidget(self.marsCheckBox, 3, 0, 1, 1)
        self.neptuneCheckBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.neptuneCheckBox.setEnabled(False)  # TODO : implement Neptune
        self.neptuneCheckBox.setTristate(False)
        self.neptuneCheckBox.setObjectName("neptuneCheckBox")
        self.gridLayout.addWidget(self.neptuneCheckBox, 3, 1, 1, 1)

        # ------------------------------------------------------------------------
        self.groupAsteroidParam = QtWidgets.QGroupBox(self.centralwidget)
        self.groupAsteroidParam.setGeometry(QtCore.QRect(630, 10, 471, 244))
        self.groupAsteroidParam.setObjectName("groupAsteroidParam")

        self.label_5 = QtWidgets.QLabel(self.groupAsteroidParam)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 101, 16))
        self.label_5.setObjectName("label_5")

        self.inputAsteroidMass = QtWidgets.QLineEdit(self.groupAsteroidParam)
        self.inputAsteroidMass.setGeometry(QtCore.QRect(120, 30, 101, 22))
        self.inputAsteroidMass.setObjectName("inputAsteroidMass")

        self.label_14 = QtWidgets.QLabel(self.groupAsteroidParam)
        self.label_14.setGeometry(QtCore.QRect(10, 60, 101, 16))
        self.label_14.setObjectName("label_14")

        self.inputAsteroidSMaxis = QtWidgets.QLineEdit(self.groupAsteroidParam)
        self.inputAsteroidSMaxis.setGeometry(QtCore.QRect(120, 60, 101, 22))
        self.inputAsteroidSMaxis.setObjectName("inputAsteroidSMaxis")

        self.tabWidget = QtWidgets.QTabWidget(self.groupAsteroidParam)
        self.tabWidget.setGeometry(QtCore.QRect(250, 10, 211, 228))
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.hide()

        self.xyzTab = QtWidgets.QWidget()
        self.xyzTab.setObjectName("xyzTab")

        self.layoutWidget1 = QtWidgets.QWidget(self.xyzTab)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 191, 181))
        self.layoutWidget1.setObjectName("layoutWidget1")

        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget1)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)

        self.inputPosX = QtWidgets.QLineEdit(self.layoutWidget1)
        self.inputPosX.setObjectName("inputPosX")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inputPosX)

        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)

        self.inputPosY = QtWidgets.QLineEdit(self.layoutWidget1)
        self.inputPosY.setObjectName("inputPosY")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.inputPosY)

        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)

        self.inputPosZ = QtWidgets.QLineEdit(self.layoutWidget1)
        self.inputPosZ.setObjectName("inputPosZ")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.inputPosZ)

        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_10)

        self.inputVelX = QtWidgets.QLineEdit(self.layoutWidget1)
        self.inputVelX.setObjectName("inputVelX")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.inputVelX)

        self.label_11 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_11)

        self.inputVelY = QtWidgets.QLineEdit(self.layoutWidget1)
        self.inputVelY.setObjectName("inputVelY")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.inputVelY)

        self.label_12 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_12)

        self.inputVelZ = QtWidgets.QLineEdit(self.layoutWidget1)
        self.inputVelZ.setObjectName("inputVelZ")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.inputVelZ)

        # ------------------------------------------------------------------------

        self.label_5 = QtWidgets.QLabel(self.groupAsteroidParam)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 101, 16))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.groupAsteroidParam)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 121, 16))
        self.label_6.setObjectName("label_6")

        self.inputAsteroidMass = QtWidgets.QLineEdit(self.groupAsteroidParam)
        self.inputAsteroidMass.setGeometry(QtCore.QRect(120, 30, 101, 22))
        self.inputAsteroidMass.setObjectName("inputAsteroidMass")

        self.inputAsteroidSmAxis = QtWidgets.QLineEdit(self.groupAsteroidParam)
        self.inputAsteroidSmAxis.setGeometry(QtCore.QRect(120, 60, 101, 22))
        self.inputAsteroidSmAxis.setObjectName("inputAsteroidSmAxis")

        self.circularCheckBox = QtWidgets.QCheckBox(self.groupAsteroidParam)
        self.circularCheckBox.setGeometry(QtCore.QRect(120, 90, 101, 22))
        self.circularCheckBox.setTristate(False)
        self.circularCheckBox.setObjectName("circularCheckBox")
        self.circularCheckBox.setChecked(True)
        self.circularCheckBox.stateChanged.connect(self.hide_show_InitialCond)

        self.tabWidget.addTab(self.xyzTab, "")
        self.orbitTab = QtWidgets.QWidget()
        self.orbitTab.setObjectName("orbitTab")

        self.widget = QtWidgets.QWidget(self.orbitTab)
        self.widget.setGeometry(QtCore.QRect(20, 6, 181, 181))
        self.widget.setObjectName("widget")

        self.formLayout_2 = QtWidgets.QFormLayout(self.widget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")

        self.label_18 = QtWidgets.QLabel(self.widget)
        self.label_18.setObjectName("label_18")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_18)

        self.inputEcc = QtWidgets.QLineEdit(self.widget)
        self.inputEcc.setObjectName("inputEcc")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inputEcc)

        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setObjectName("label_17")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_17)

        self.inputInc = QtWidgets.QLineEdit(self.widget)
        self.inputInc.setObjectName("inputInc")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.inputInc)

        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_13)

        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_15)

        self.inputAop = QtWidgets.QLineEdit(self.widget)
        self.inputAop.setObjectName("inputAop")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.inputAop)

        self.label_19 = QtWidgets.QLabel(self.widget)
        self.label_19.setObjectName("label_19")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_19)

        self.inputM = QtWidgets.QLineEdit(self.widget)
        self.inputM.setObjectName("inputM")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.inputM)

        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_16)

        self.inputEpoch = QtWidgets.QLineEdit(self.widget)
        self.inputEpoch.setObjectName("inputEpoch")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.inputEpoch)

        self.inputLan = QtWidgets.QLineEdit(self.widget)
        self.inputLan.setObjectName("inputLan")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.inputLan)

        self.tabWidget.addTab(self.orbitTab, "")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget) #TODO : improve implementation inside code
        self.progressBar.setGeometry(QtCore.QRect(800, 280, 301, 16))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")

        # ------------------------------------------------------------------------
        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(670, 260, 121, 51))
        self.StartButton.setObjectName("StartButton")

        self.warningLabel = QtWidgets.QLabel(self.centralwidget)
        self.warningLabel.setGeometry(QtCore.QRect(40, 260, 491, 61))
        self.warningLabel.setObjectName("warningLabel")
        self.fwbwOutputLabel = QtWidgets.QLabel(self.centralwidget)
        self.fwbwOutputLabel.setGeometry(QtCore.QRect(470, 20, 141, 231))
        self.fwbwOutputLabel.setWordWrap(True)
        self.fwbwOutputLabel.setObjectName("fwbwOutputLabel")

        self.StartButton.clicked.connect(self.Start)

        # ------------------------------------------------------------------------
        self.groupPerturbPlanets.raise_()
        self.groupPlots.raise_()
        self.groupIntegrationParam.raise_()
        self.groupAsteroidParam.raise_()
        self.progressBar.raise_()
        self.StartButton.raise_()
        self.warningLabel.raise_()
        self.fwbwOutputLabel.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        # ------------------------------------------------------------------------
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1114, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # ------------------------------------------------------------------------
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # ------------------------------------------------------------------------
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Asteroid Trajectory"))
        self.groupIntegrationParam.setTitle(_translate("MainWindow", "Integration parameters"))
        self.label_2.setText(_translate("MainWindow", "Number of days :"))
        self.label_4.setText(_translate("MainWindow", "Step :"))
        self.methodBox.setItemText(0, _translate("MainWindow", "RungeKutta4"))
        self.forwBackCheckBox.setText(_translate("MainWindow", "Forward-Backward integration"))
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
        self.label_5.setText(_translate("MainWindow", "Mass (in Suns):"))
        self.circularCheckBox.setText(_translate("MainWindow", "Circular orbit"))
        self.label_14.setText(_translate("MainWindow", "Semi-Major axis"))
        self.label_7.setText(_translate("MainWindow", "Position x :"))
        self.label_8.setText(_translate("MainWindow", "Position y :"))
        self.label_9.setText(_translate("MainWindow", "Position z :"))
        self.label_10.setText(_translate("MainWindow", "Velocity x :"))
        self.label_11.setText(_translate("MainWindow", "Velocity y :"))
        self.label_12.setText(_translate("MainWindow", "Velocity z :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.xyzTab), _translate("MainWindow", "Pos/Vel"))
        self.label_18.setText(_translate("MainWindow", "E : "))
        self.label_17.setText(_translate("MainWindow", "INC :"))
        self.label_13.setText(_translate("MainWindow", "LAN :"))
        self.label_15.setText(_translate("MainWindow", "AOP :"))
        self.label_19.setText(_translate("MainWindow", "M :"))
        self.label_16.setText(_translate("MainWindow", "Epoch :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.orbitTab), _translate("MainWindow", "Orbit param"))
        self.StartButton.setText(_translate("MainWindow", "Start !"))
        self.warningLabel.setText(_translate("MainWindow", " ")) #TODO : connect to error output
        self.fwbwOutputLabel.setText(_translate("MainWindow", " ")) # TODO : connect to Forward Backward output

    def Start(self):
        if self.jupiterCheckBox.checkState():  # TODO : implement other planets
            self.progressBar.setValue(0)

            jupiter = planet(m_sun / 1047.348625, 5.2, 0, 0)
            jupiter.orbital_period()

            self.progressBar.setValue(5)

            self.get_init_state()

            self.time = np.arange(0, int(self.inputFinalTime.text()) + int(self.inputStep.text()),
                                  int(self.inputStep.text()))  # creation of the list containing each value of time

            self.progressBar.setValue(10)

            self.results = threeBody.RK4(self.time, self.init_state, int(self.inputStep.text()), jupiter)

            self.progressBar.setValue(50)

            self.PlotTrajectory(jupiter)  # plot of the results + jupiter

            self.r_list, self.rdot_list = extract_vectors(self.results)
            self.a_list, self.e_list, self.i_list = orbital_parameters_list(self.r_list, self.rdot_list)
            self.PlotOrbitVar(self.a_list, self.e_list, self.i_list, self.time[1:])

            self.progressBar.setValue(85)

            self.plotTrajectory.setPixmap(QtGui.QPixmap("Plots/trajectory.png"))
            self.plotOrbitVar.setPixmap(QtGui.QPixmap("Plots/orbitVar.png"))

            self.progressBar.setValue(100)

        else:  # No Jupiter
            self.get_init_state()
            self.time = np.arange(0, int(self.inputFinalTime.text()) + int(self.inputStep.text()),
                                  int(self.inputStep.text()))  # creation of the list containing each value of time
            self.results = twoBody.RK4(self.time, self.init_state, int(self.inputStep.text()))
            self.PlotTrajectory()
            self.plotTrajectory.setPixmap(QtGui.QPixmap("Plots/trajectory.png"))
            self.progressBar.setValue(100)

    def hide_show_InitialCond(self):
        if self.circularCheckBox.checkState():
            self.tabWidget.hide()
        else:
            self.tabWidget.show()

    def get_init_state(self): #TODO : choose between xyz position or orbital parameters in function of the tab selected
        if self.circularCheckBox.checkState():  # Circular initial orbit
            self.init_state = np.array(
                [float(self.inputAsteroidSmAxis.text()), 0, 0,
                 0, k / np.sqrt(float(self.inputAsteroidSmAxis.text())), 0])
        else:  # User defined initial parameters # TODO : Verify the type of the input and make it foolproof
            self.init_state = np.array(
                [float(self.inputPosX.text()), float(self.inputPosY.text()), float(self.inputPosZ.text()),
                 float(self.inputVelX.text()), float(self.inputVelY.text()), float(self.inputVelZ.text())])

    def PlotTrajectory(self, planet=None): #TODO : set axis equal
        self.figure1.clear()
        self.ax = self.figure1.add_subplot(111)
        self.ax.plot(self.results[:, 0],
                self.results[:, 1],
                'o', color='red', markersize=1, label='Asteroid')  # plot of the asteroid
        if planet:
            self.ax.plot(planet.orbitalparam2vectorList(self.time)[:, 0],
                    planet.orbitalparam2vectorList(self.time)[:, 1],
                    'o', color='green', markersize=1, label='planet')  # plot of the planet
        self.ax.set_facecolor(plot_background_color)
        self.ax.tick_params(colors='white')
        self.figure1.patch.set_facecolor((39/255, 42/255, 49/255))
        self.trajectory_canvas.draw()
        self.trajectory_canvas.print_png('Plots/trajectory.png') #TODO : find a better solution than printing and calling

    def PlotOrbitVar(self, val1, val2, val3, time):
        self.figure2.clear()
        self.ax1 = self.figure2.add_subplot(311)
        self.ax1.plot(time, val1)
        self.ax1.set_facecolor(plot_background_color)
        self.ax1.tick_params(colors='white')
        self.ax1.legend('a') # Variations of the Semi-major axis [a]
        self.ax2 = self.figure2.add_subplot(312)
        self.ax2.plot(time, val2)
        self.ax2.set_facecolor(plot_background_color)
        self.ax2.tick_params(colors='white')
        # self.ax2.set_title('Variations of the Eccentricity [e]')
        self.ax2.legend('e')
        self.ax3 = self.figure2.add_subplot(313)
        self.ax3.plot(time, val3)
        self.ax3.set_facecolor(plot_background_color)
        self.ax3.tick_params(colors='white')
        # self.ax3.set_title('Variations of the Inclination [i]')
        self.ax3.legend('i')

        self.figure2.patch.set_facecolor((39/255, 42/255, 49/255))
        self.orbitVar_canvas.draw()
        self.orbitVar_canvas.print_png('Plots/orbitVar.png')


class planet(object): #TODO implement changes from master branch
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
        return np.array(self.posList)


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

    app.setStyle("Fusion")
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QtGui.QColor(51, 54, 63))
    dark_palette.setColor(QPalette.WindowText, QtGui.QColor(250, 250, 250))
    dark_palette.setColor(QPalette.Base, QtGui.QColor(39, 42, 49))
    dark_palette.setColor(QPalette.AlternateBase, QtGui.QColor(51, 54, 63))
    dark_palette.setColor(QPalette.ToolTipBase, QtGui.QColor(250, 250, 250))
    dark_palette.setColor(QPalette.ToolTipText, QtGui.QColor(250, 250, 250))
    dark_palette.setColor(QPalette.Text, QtGui.QColor(250, 250, 250))
    dark_palette.setColor(QPalette.Button, QtGui.QColor(51, 54, 63))
    dark_palette.setColor(QPalette.ButtonText, QtGui.QColor(250, 250, 250))
    dark_palette.setColor(QPalette.BrightText, QtGui.QColor(255, 0, 0))
    dark_palette.setColor(QPalette.Link, QtGui.QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QtGui.QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, QtGui.QColor(0, 0, 0))
    app.setPalette(dark_palette)
    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
    plot_background_color = (0.12, 0.13, 0.15)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
