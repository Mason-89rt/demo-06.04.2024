# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(426, 406)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 3, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.page)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.page)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(382, 231, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 4, 0, 1, 2)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_3.addWidget(self.lineEdit_4, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_3.addWidget(self.lineEdit_5, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_3.addWidget(self.lineEdit_6, 2, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(379, 231, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 4, 0, 1, 2)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Зарегистрироваться"))
        self.label_3.setText(_translate("Dialog", "Email"))
        self.label.setText(_translate("Dialog", "Login"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.label_5.setText(_translate("Dialog", "Login"))
        self.label_4.setText(_translate("Dialog", "Password"))
        self.label_6.setText(_translate("Dialog", "Email"))
        self.pushButton_2.setText(_translate("Dialog", "Войти"))
