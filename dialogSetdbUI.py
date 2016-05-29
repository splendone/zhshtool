# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\moorelab\qt\zhshtool\dialogSetdbUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import cx_Oracle as oracle
import decimal

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def __init__(self, ui_main):
        self.ui_main = ui_main
        
    def setupUi(self, Dialog):
        self.dlg = Dialog
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayoutWidget = QtGui.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 221))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_ip = QtGui.QLabel(self.formLayoutWidget)
        self.label_ip.setObjectName(_fromUtf8("label_ip"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_ip)
        self.lineEdit_ip = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_ip.setObjectName(_fromUtf8("lineEdit_ip"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_ip)
        self.label_port = QtGui.QLabel(self.formLayoutWidget)
        self.label_port.setObjectName(_fromUtf8("label_port"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_port)
        self.lineEdit_port = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_port.setObjectName(_fromUtf8("lineEdit_port"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_port)
        self.label_username = QtGui.QLabel(self.formLayoutWidget)
        self.label_username.setObjectName(_fromUtf8("label_username"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_username)
        self.lineEdit_username = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_username.setObjectName(_fromUtf8("lineEdit_username"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_username)
        self.label_password = QtGui.QLabel(self.formLayoutWidget)
        self.label_password.setObjectName(_fromUtf8("label_password"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_password)
        self.lineEdit_password = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_password.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_password.setObjectName(_fromUtf8("lineEdit_password"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_password)
        self.label_database = QtGui.QLabel(self.formLayoutWidget)
        self.label_database.setObjectName(_fromUtf8("label_database"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_database)
        self.lineEdit_database = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_database.setObjectName(_fromUtf8("lineEdit_database"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_database)
        self.label_result = QtGui.QLabel(self.formLayoutWidget)
        self.label_result.setText(_fromUtf8(""))
        self.label_result.setObjectName(_fromUtf8("label_result"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.label_result)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.saveCursor)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def saveCursor(self):
        if not self.ui_main.db:
            dsn = oracle.makedsn(self.lineEdit_ip.text(),self.lineEdit_port.text(),self.lineEdit_database.text())
            self.ui_main.db = oracle.connect('%s'%self.lineEdit_username.text(),'%s'%self.lineEdit_password.text(),dsn)
            self.ui_main.cursor = self.ui_main.db.cursor()
        
        self.dlg.accept()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_ip.setText(_translate("Dialog", "IP", None))
        self.lineEdit_ip.setText(_translate("Dialog", "132.147.200.16", None))
        self.label_port.setText(_translate("Dialog", "Port", None))
        self.lineEdit_port.setText(_translate("Dialog", "1521", None))
        self.label_username.setText(_translate("Dialog", "User Name", None))
        self.lineEdit_username.setText(_translate("Dialog", "xhf", None))
        self.label_password.setText(_translate("Dialog", "Password", None))
        self.lineEdit_password.setText(_translate("Dialog", "asdw", None))
        self.label_database.setText(_translate("Dialog", "Database", None))
        self.lineEdit_database.setText(_translate("Dialog", "orcl", None))

