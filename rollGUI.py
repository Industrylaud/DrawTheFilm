# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\mrfro\Desktop\rollGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap, QIcon
import home, time
import urllib
import sys


class Ui_MainWindow(object):
    fw = ''
    randomedFilm = ''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(697, 444)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 19, 151, 173))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.loginField = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.loginField.setObjectName("loginField")
        self.verticalLayout.addWidget(self.loginField)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.passwordField = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordField.setObjectName("passwordField")
        self.verticalLayout.addWidget(self.passwordField)
        self.loginButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout.addWidget(self.loginButton)
        self.logoutButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.logoutButton.setObjectName("logoutButton")
        self.verticalLayout.addWidget(self.logoutButton)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 200, 151, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rollButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.rollButton.setObjectName("rollButton")
        self.verticalLayout_2.addWidget(self.rollButton)

        self.posterView = QtWidgets.QLabel(self.centralwidget)
        self.posterView.setGeometry(QtCore.QRect(306, 12, 341, 271))
        self.posterView.setFrameShape(QtWidgets.QFrame.Box)
        self.posterView.setText('')
        self.posterView.setObjectName("posterView")

        self.titleView = QtWidgets.QLineEdit(self.centralwidget)
        self.titleView.setGeometry(QtCore.QRect(306, 290, 341, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.titleView.sizePolicy().hasHeightForWidth())

        self.titleView.setSizePolicy(sizePolicy)
        self.titleView.setBaseSize(QtCore.QSize(0, 29))
        #self.titleView.setFrameShape(QtWidgets.QFrame.NoFrame)
        #self.titleView.setFrameShadow(QtWidgets.QFrame.Sunken)
        #self.titleView.setLineWrapMode(QtWidgets.QTextEdit.FixedColumnWidth)
        self.titleView.setObjectName("titleView")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 697, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.loginButton.clicked.connect(lambda: self.logIn())
        self.rollButton.clicked.connect(lambda: self.roll())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Login"))
        self.label_2.setText(_translate("MainWindow", "Hasło"))
        self.loginButton.setText(_translate("MainWindow", "zaloguj"))
        self.logoutButton.setText(_translate("MainWindow", "wyloguj"))
        self.rollButton.setText(_translate("MainWindow", "losuj"))

    def setImage(self):
        data = urllib.urlopen(home.getPoster(self.randomedFilm)).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        scene = QtWidgets.QGraphicsView(self)
        scene.addItem(pixmap)
        self.posterView.setScene(scene)

    def setTitle(self):
        self.titleView.clear()
        self.titleView.setText(home.getName(self.randomedFilm))

    def logIn(self):
        try:
            self.fw = home.logIn(self.loginField.text(), self.passwordField.text())
            self.loginField.clear()
            self.passwordField.clear()
        except:
            self.passwordField.clear()
            print('dupa')

    def roll(self):
        self.randomedFilm = home.rollFilm(self.fw)
        self.setTitle()

def mainFunc():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    mainFunc()
