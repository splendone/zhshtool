# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\moorelab\qt\zhshtool\setdb.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtSql import QSqlDatabase, QSqlQuery

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

class MyListWidget(QtGui.QListWidget): 
    # def Clicked(self,item):
    pass

class Ui_Dialog(object):
    def __init__(self):
        self.db = None

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(450, 339)
        self.frameDbConn = QtGui.QFrame(Dialog)
        self.frameDbConn.setGeometry(QtCore.QRect(10, 10, 431, 121))
        self.frameDbConn.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameDbConn.setFrameShadow(QtGui.QFrame.Raised)
        self.frameDbConn.setObjectName(_fromUtf8("frameDbConn"))
        self.labelIp = QtGui.QLabel(self.frameDbConn)
        self.labelIp.setGeometry(QtCore.QRect(0, 0, 61, 21))
        self.labelIp.setAlignment(QtCore.Qt.AlignCenter)
        self.labelIp.setObjectName(_fromUtf8("labelIp"))
        self.labelUserName = QtGui.QLabel(self.frameDbConn)
        self.labelUserName.setGeometry(QtCore.QRect(0, 30, 61, 21))
        self.labelUserName.setAlignment(QtCore.Qt.AlignCenter)
        self.labelUserName.setObjectName(_fromUtf8("labelUserName"))
        self.labelPassword = QtGui.QLabel(self.frameDbConn)
        self.labelPassword.setGeometry(QtCore.QRect(0, 60, 61, 21))
        self.labelPassword.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPassword.setObjectName(_fromUtf8("labelPassword"))
        self.pushButtonConnect = QtGui.QPushButton(self.frameDbConn)
        self.pushButtonConnect.setGeometry(QtCore.QRect(250, 60, 75, 21))
        self.pushButtonConnect.setObjectName(_fromUtf8("pushButtonConnect"))
        self.labelDatabase = QtGui.QLabel(self.frameDbConn)
        self.labelDatabase.setGeometry(QtCore.QRect(0, 90, 61, 20))
        self.labelDatabase.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDatabase.setObjectName(_fromUtf8("labelDatabase"))
        self.lineEdit_Ip = QtGui.QLineEdit(self.frameDbConn)
        self.lineEdit_Ip.setGeometry(QtCore.QRect(60, 0, 113, 20))
        self.lineEdit_Ip.setObjectName(_fromUtf8("lineEdit_Ip"))
        self.lineEditUserName = QtGui.QLineEdit(self.frameDbConn)
        self.lineEditUserName.setGeometry(QtCore.QRect(60, 30, 113, 20))
        self.lineEditUserName.setObjectName(_fromUtf8("lineEditUserName"))
        self.lineEditPassword = QtGui.QLineEdit(self.frameDbConn)
        self.lineEditPassword.setGeometry(QtCore.QRect(60, 60, 113, 20))
        self.lineEditPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditPassword.setObjectName(_fromUtf8("lineEditPassword"))
        self.lineEditDatabase = QtGui.QLineEdit(self.frameDbConn)
        self.lineEditDatabase.setGeometry(QtCore.QRect(60, 90, 113, 20))
        self.lineEditDatabase.setEchoMode(QtGui.QLineEdit.Normal)
        self.lineEditDatabase.setObjectName(_fromUtf8("lineEditDatabase"))
        self.labelPort = QtGui.QLabel(self.frameDbConn)
        self.labelPort.setGeometry(QtCore.QRect(180, 0, 61, 21))
        self.labelPort.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPort.setObjectName(_fromUtf8("labelPort"))
        self.lineEditPort = QtGui.QLineEdit(self.frameDbConn)
        self.lineEditPort.setGeometry(QtCore.QRect(250, 0, 113, 20))
        self.lineEditPort.setObjectName(_fromUtf8("lineEditPort"))
        self.frameTableFeild = QtGui.QFrame(Dialog)
        self.frameTableFeild.setGeometry(QtCore.QRect(10, 140, 431, 191))
        self.frameTableFeild.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameTableFeild.setFrameShadow(QtGui.QFrame.Raised)
        self.frameTableFeild.setObjectName(_fromUtf8("frameTableFeild"))
        self.listWidgetTables = MyListWidget(self.frameTableFeild)
        self.listWidgetTables.setGeometry(QtCore.QRect(0, 0, 201, 191))
        self.listWidgetTables.setObjectName(_fromUtf8("listWidgetTables"))
        self.listWidgetFeilds = MyListWidget(self.frameTableFeild)
        self.listWidgetFeilds.setGeometry(QtCore.QRect(230, 0, 201, 191))
        self.listWidgetFeilds.setObjectName(_fromUtf8("listWidgetFeilds"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButtonConnect, QtCore.SIGNAL(_fromUtf8("pressed()")), self.showTables)
        # QtCore.QObject.connect(self.pushButtonConnect, QtCore.SIGNAL(_fromUtf8("pressed()")), self.showTables)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def showTables(self):
        if not self.db:
            print 'init self.db'
            self.db = QSqlDatabase.addDatabase("QMYSQL")
            self.db.setHostName (self.lineEdit_Ip.text())
            self.db.setUserName (self.lineEditUserName.text())
            self.db.setPassword (self.lineEditPassword.text())
            self.db.setDatabaseName (self.lineEditDatabase.text())
            self.db.setPort (int(self.lineEditPort.text()))
            self.db.setConnectOptions("CLIENT_SSL=1;CLIENT_IGNORE_SPACE=1")
            self.db.open()

            self.listWidgetTables.pressed.connect(self.showFeilds) 
        else:
            print 'change self.db'
            self.db.close()
            self.db.removeDatabase(self.db.connectionName())

            self.db = QSqlDatabase.addDatabase("QMYSQL")
            self.db.setHostName (self.lineEdit_Ip.text())
            self.db.setUserName (self.lineEditUserName.text())
            self.db.setPassword (self.lineEditPassword.text())
            self.db.setDatabaseName (self.lineEditDatabase.text())
            self.db.setPort (int(self.lineEditPort.text()))
            self.db.setConnectOptions("CLIENT_SSL=1;CLIENT_IGNORE_SPACE=1")
            self.db.open()

            self.listWidgetTables.clear()
        print 'i'
        # defaultDB = QSqlDatabase.database()
        query = QSqlQuery("show tables")
        qe = query.exec_()
        if qe:
            while query.next():
                self.listWidgetTables.addItem(query.value(0).toString())

        self.listWidgetTables.show()
        


    def showFeilds(self):
        defaultDB = QSqlDatabase.database()
        query = QSqlQuery("desc {}".format(self.listWidgetTables.currentItem().text()))
        qe = query.exec_()
        if qe:
            self.listWidgetFeilds.clear()
            while query.next():
                self.listWidgetFeilds.addItem(query.value(0).toString())



    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.labelIp.setText(_translate("Dialog", "IP", None))
        self.labelUserName.setText(_translate("Dialog", "USERNAME", None))
        self.labelPassword.setText(_translate("Dialog", "PASSWORD", None))
        self.pushButtonConnect.setText(_translate("Dialog", "CONNECT", None))
        self.labelDatabase.setText(_translate("Dialog", "DATABASE", None))
        self.lineEdit_Ip.setText(_translate("Dialog", "127.0.0.1", None))
        self.lineEditUserName.setText(_translate("Dialog", "root", None))
        self.lineEditPassword.setText(_translate("Dialog", "123123", None))
        self.lineEditDatabase.setText(_translate("Dialog", "testtest", None))
        self.labelPort.setText(_translate("Dialog", "PORT", None))
        self.lineEditPort.setText(_translate("Dialog", "3306", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

