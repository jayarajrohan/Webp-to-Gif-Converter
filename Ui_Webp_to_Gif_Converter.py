# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Projects\Python\Webp to Gif Converter\Webp to Gif Converter.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PIL import Image
import tkinter
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
from tkinter import filedialog
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import webbrowser


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(341, 270)
        MainWindow.setMaximumSize(QtCore.QSize(341, 270))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("e:\\Projects\\Python\\Webp to Gif Converter\\wtog.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(52, 82, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(110, 10, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Button1.setFont(font)
        self.Button1.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.Button1.setObjectName("Button1")
        self.Button2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button2.setGeometry(QtCore.QRect(110, 90, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Button2.setFont(font)
        self.Button2.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.Button2.setObjectName("Button2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(30, 160, 291, 23))
        self.progressBar.setStyleSheet("color: rgb(255, 255, 255);")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(80, 190, 191, 16))
        self.label1.setStyleSheet("color: rgb(255, 255, 255);")
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        self.Button3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button3.setGeometry(QtCore.QRect(50, 210, 75, 23))
        self.Button3.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.Button3.setObjectName("Button3")
        self.Button4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button4.setGeometry(QtCore.QRect(200, 210, 75, 23))
        self.Button4.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.Button4.setObjectName("Button4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Webp to Gif Converter"))
        self.Button1.setText(_translate("MainWindow", "Select Files"))
        self.Button2.setText(_translate("MainWindow", "Convert"))
        self.label1.setText(_translate("MainWindow", "This software is created by M.J.Rohan"))
        self.Button3.setText(_translate("MainWindow", "My LinkedIn"))
        self.Button4.setText(_translate("MainWindow", "My Github"))

        files = []

        def select_file():
            root = tkinter.Tk()
            root.wm_attributes('-topmost', 1)
            root.withdraw()

            filename = askopenfilenames(filetypes=[("Webp files", ".webp")])

            if filename == '':
                filename = []
            global files
            files = filename

        self.Button1.clicked.connect(select_file)

        def convert():
            global files
            try:
                files2 = files
            except:
                files2 = []
            if files2 != []:
                root = tkinter.Tk()
                root.wm_attributes('-topmost', 1)
                root.withdraw()

                dir_name = filedialog.askdirectory()

            
                if dir_name != '':
                    length = len(files2)
                    pro_cnt = 100 / length
                    count = 0
                    count2 = 1
                    for i in files2:
                        head_tail = os.path.split(i)
                        wo_exe = head_tail[1].rstrip(".webp")
                        im = Image.open(i)
                        im.info.pop('background', None)
                        im.save(dir_name + "/" + wo_exe + ".gif", 'gif', save_all=True)
                        count += pro_cnt
                        if count2 == length and count <= 100:
                            self.progressBar.setValue(100)
                        else:
                            self.progressBar.setValue(count)
                        count2 += 1
                    files = []
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("File conversion completed")
                    msg.setWindowTitle("Successful")
                    msg.exec()
                    self.progressBar.setValue(0)
                        
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("You have to select some files before trying to convert")
                msg.setWindowTitle("Select file")
                msg.exec()
        
        self.Button2.clicked.connect(convert)

        def linkedin():
            webbrowser.open('https://www.linkedin.com/in/jayarajrohan/')

        self.Button3.clicked.connect(linkedin)

        def github():
            webbrowser.open('https://github.com/jayarajrohan')

        self.Button4.clicked.connect(github)
