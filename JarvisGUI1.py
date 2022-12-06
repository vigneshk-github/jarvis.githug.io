from jarvisUI3 import Ui_JarvisUI
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from PyQt5.uic import loadUiType
import main
import sys


class Mainthraed(QThread):
    def __init__(self):
        super(Mainthraed,self).__init__()

    def run(self):
        main.runJarvis()

startExe = Mainthraed()

class Gui_start(QMainWindow):
    def __init__(self):
        super().__init__()

        self.gui = Ui_JarvisUI()
        self.gui.setupUi(self)

        self.gui.pushButton.clicked.connect(self.startTask)
        # self.gui.pushButton_exit.clicked.connect(self.close)

    def startTask(self):

        self.gui.label1 = QtGui.QMovie("../Downloads/G.U.I Material-20221126T185922Z-001/G.U.I Material/VoiceReg/jarvis_jj.gif")
        self.gui.gif3.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2 = QtGui.QMovie("../../Downloads/G.U.I Material-20221126T185922Z-001/G.U.I Material/B.G/Iron_Template_1.gif")
        self.gui.label.setMovie(self.gui.label2)
        self.gui.label2.start()

        self.gui.label3 = QtGui.QMovie("../../Downloads/G.U.I Material-20221126T185922Z-001/G.U.I Material/ExtraGui/Earth.gif")
        self.gui.label_2.setMovie(self.gui.label3)
        self.gui.label3.start()

        self.gui.label4 = QtGui.QMovie("../../Downloads/G.U.I Material-20221126T185922Z-001/G.U.I Material/ExtraGui/initial.gif")
        self.gui.label_4.setMovie(self.gui.label4)
        self.gui.label4.start()

        self.gui.label5 = QtGui.QMovie("../../Downloads/G.U.I Material-20221126T185922Z-001/G.U.I Material/ExtraGui/Hero_Template.gif")
        self.gui.label_6.setMovie(self.gui.label5)
        self.gui.label5.start()

        # self.gui.label6 = QtGui.QMovie("")
        # self.gui.label.setMovie(self.gui.label6)
        # self.gui.label6.start()

        startExe.start()


GuiApp = QApplication(sys.argv)
jarvis_gui = Gui_start()
jarvis_gui.show()
exit(GuiApp.exec_())