# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 490)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setAcceptDrops(False)
        MainWindow.setToolTipDuration(0)
        MainWindow.setStyleSheet("")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(500, 40, 51, 41))
        self.toolButton.setWhatsThis("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource/1200178.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setObjectName("toolButton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(490, 90, 81, 21))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(690, 200, 51, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resource/1200191.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_3.setGeometry(QtCore.QRect(690, 40, 51, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resource/swipe_down_89.474060822898px_1200188_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_4.setGeometry(QtCore.QRect(600, 40, 51, 41))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resource/like_77.762004175365px_1200177_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon3)
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_5 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_5.setGeometry(QtCore.QRect(690, 120, 51, 41))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resource/1200169.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon4)
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_6 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_6.setGeometry(QtCore.QRect(600, 120, 51, 41))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("resource/zoom_in_98.436090225564px_1200197_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_6.setIcon(icon5)
        self.toolButton_6.setObjectName("toolButton_6")
        self.toolButton_7 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_7.setGeometry(QtCore.QRect(500, 120, 51, 41))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("resource/wave_99.585365853659px_1200195_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_7.setIcon(icon6)
        self.toolButton_7.setObjectName("toolButton_7")
        self.toolButton_8 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_8.setGeometry(QtCore.QRect(500, 270, 51, 41))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("resource/1200173.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_8.setIcon(icon7)
        self.toolButton_8.setObjectName("toolButton_8")
        self.toolButton_9 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_9.setGeometry(QtCore.QRect(600, 200, 51, 41))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("resource/1200174.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_9.setIcon(icon8)
        self.toolButton_9.setObjectName("toolButton_9")
        self.toolButton_10 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_10.setGeometry(QtCore.QRect(500, 200, 51, 41))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("resource/1200171.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_10.setIcon(icon9)
        self.toolButton_10.setObjectName("toolButton_10")
        self.toolButton_11 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_11.setGeometry(QtCore.QRect(600, 270, 51, 41))
        self.toolButton_11.setIcon(icon1)
        self.toolButton_11.setObjectName("toolButton_11")
        self.toolButton_12 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_12.setGeometry(QtCore.QRect(690, 270, 51, 41))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("resource/1200184.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_12.setIcon(icon10)
        self.toolButton_12.setObjectName("toolButton_12")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(580, 90, 81, 21))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_3 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_3.setGeometry(QtCore.QRect(680, 90, 81, 21))
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName("progressBar_3")
        self.progressBar_4 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_4.setGeometry(QtCore.QRect(680, 170, 81, 21))
        self.progressBar_4.setProperty("value", 24)
        self.progressBar_4.setObjectName("progressBar_4")
        self.progressBar_5 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_5.setGeometry(QtCore.QRect(490, 170, 81, 21))
        self.progressBar_5.setProperty("value", 24)
        self.progressBar_5.setObjectName("progressBar_5")
        self.progressBar_6 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_6.setGeometry(QtCore.QRect(580, 170, 81, 21))
        self.progressBar_6.setProperty("value", 24)
        self.progressBar_6.setObjectName("progressBar_6")
        self.progressBar_7 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_7.setGeometry(QtCore.QRect(490, 250, 81, 21))
        self.progressBar_7.setProperty("value", 24)
        self.progressBar_7.setObjectName("progressBar_7")
        self.progressBar_8 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_8.setGeometry(QtCore.QRect(680, 250, 81, 21))
        self.progressBar_8.setProperty("value", 24)
        self.progressBar_8.setObjectName("progressBar_8")
        self.progressBar_9 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_9.setGeometry(QtCore.QRect(580, 250, 81, 21))
        self.progressBar_9.setProperty("value", 24)
        self.progressBar_9.setObjectName("progressBar_9")
        self.progressBar_10 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_10.setGeometry(QtCore.QRect(490, 320, 81, 21))
        self.progressBar_10.setProperty("value", 24)
        self.progressBar_10.setObjectName("progressBar_10")
        self.progressBar_11 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_11.setGeometry(QtCore.QRect(680, 320, 81, 21))
        self.progressBar_11.setProperty("value", 24)
        self.progressBar_11.setObjectName("progressBar_11")
        self.progressBar_12 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_12.setGeometry(QtCore.QRect(580, 320, 81, 21))
        self.progressBar_12.setProperty("value", 24)
        self.progressBar_12.setObjectName("progressBar_12")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(110, 360, 281, 51))
        self.textEdit.setStyleSheet("")
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 50, 361, 271))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 370, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 370, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 65, 91, 31))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.toolButton_3.setText(_translate("MainWindow", "..."))
        self.toolButton_4.setText(_translate("MainWindow", "..."))
        self.toolButton_5.setText(_translate("MainWindow", "..."))
        self.toolButton_6.setText(_translate("MainWindow", "..."))
        self.toolButton_7.setText(_translate("MainWindow", "..."))
        self.toolButton_8.setText(_translate("MainWindow", "..."))
        self.toolButton_9.setText(_translate("MainWindow", "..."))
        self.toolButton_10.setText(_translate("MainWindow", "..."))
        self.toolButton_11.setText(_translate("MainWindow", "..."))
        self.toolButton_12.setText(_translate("MainWindow", "..."))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#0080ff;\">thumb up</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton_2.setText(_translate("MainWindow", "End"))

