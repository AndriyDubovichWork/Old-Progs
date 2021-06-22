# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_run(object):
    def setupUi(self, run):
        run.setObjectName("run")
        run.resize(412, 303)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        run.setFont(font)
        run.setStyleSheet("QDialog{\n"
"    background-color:#514E4F;\n"
"}\n"
"QPushButton{\n"
"    background-color:#A69FA2;\n"
"}\n"
"QGraphicsView{\n"
"    background-color:#514E4F;\n"
"}\n"
"QSlider{\n"
"    background-color:#514E4F;\n"
"}")
        run.setSizeGripEnabled(True)
        self.save = QtWidgets.QPushButton(run)
        self.save.setGeometry(QtCore.QRect(334, 262, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.save.setFont(font)
        self.save.setObjectName("save")
        self.km_runed = QtWidgets.QGraphicsView(run)
        self.km_runed.setGeometry(QtCore.QRect(10, 10, 391, 231))
        self.km_runed.setObjectName("km_runed")
        self.save_2 = QtWidgets.QPushButton(run)
        self.save_2.setGeometry(QtCore.QRect(10, 260, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.save_2.setFont(font)
        self.save_2.setObjectName("save_2")
        self.save_3 = QtWidgets.QPushButton(run)
        self.save_3.setGeometry(QtCore.QRect(80, 260, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.save_3.setFont(font)
        self.save_3.setObjectName("save_3")
        self.checkBox = QtWidgets.QCheckBox(run)
        self.checkBox.setGeometry(QtCore.QRect(190, 266, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(run)
        QtCore.QMetaObject.connectSlotsByName(run)

    def retranslateUi(self, run):
        _translate = QtCore.QCoreApplication.translate
        run.setWindowTitle(_translate("run", "Dialog"))
        self.save.setText(_translate("run", "save"))
        self.save_2.setText(_translate("run", "add"))
        self.save_3.setText(_translate("run", "add user"))
        self.checkBox.setText(_translate("run", "Calendar/graph"))



