# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\moorelab\qt\zhshtool\main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from setdb import Ui_Dialog

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSetting = QtGui.QMenu(self.menubar)
        self.menuSetting.setObjectName(_fromUtf8("menuSetting"))
        self.menuStart = QtGui.QMenu(self.menubar)
        self.menuStart.setObjectName(_fromUtf8("menuStart"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionDB = QtGui.QAction(MainWindow)
        self.actionDB.setObjectName(_fromUtf8("actionDB"))
        # print dir(self.actionDB)
        self.actionDB.triggered.connect(self.showDlgDBsetting)
        self.actionWsOne = QtGui.QAction(MainWindow)
        self.actionWsOne.setObjectName(_fromUtf8("actionWsOne"))
        self.menuSetting.addAction(self.actionDB)
        self.menuStart.addAction(self.actionWsOne)
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuStart.menuAction())

        self.retranslateUi(MainWindow)
        #QtCore.QObject.connect(self.actionDB, QtCore.SIGNAL(_fromUtf8("pressed()")), self.showDlgDBsetting)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def showDlgDBsetting(self):
        Dialog = QtGui.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.exec_()


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuSetting.setTitle(_translate("MainWindow", "设置", None))
        self.menuStart.setTitle(_translate("MainWindow", "开始", None))
        self.actionDB.setText(_translate("MainWindow", "DB", None))
        self.actionWsOne.setText(_translate("MainWindow", "第一个", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


