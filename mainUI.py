# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\moorelab\qt\zhshtool\main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from dialogSetdbUI import Ui_Dialog as Ui_Dialog_Setdb
from dialogSetItemUI import Ui_Dialog as Ui_Dialog_SetItem
from sqlsFormate import sqlByItem
from optResultFields import fillTable
import json

DB = None
CURSOR = None


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
    def __init__(self):
        self.db = None
        self.cursor = None
        self.data = None
        
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(890, 550)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 320, 510))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_items = QtGui.QWidget()
        self.tab_items.setObjectName(_fromUtf8("tab_items"))
        self.formLayoutWidget = QtGui.QWidget(self.tab_items)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 304, 471))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_from = QtGui.QLabel(self.formLayoutWidget)
        self.label_from.setObjectName(_fromUtf8("label_from"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_from)
        self.label_to = QtGui.QLabel(self.formLayoutWidget)
        self.label_to.setObjectName(_fromUtf8("label_to"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_to)
        self.label_item = QtGui.QLabel(self.formLayoutWidget)
        self.label_item.setObjectName(_fromUtf8("label_item"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_item)
        self.comboBox_item = QtGui.QComboBox(self.formLayoutWidget)
        self.comboBox_item.setObjectName(_fromUtf8("comboBox_item"))
        self.setItemCode()
        # self.comboBox_item.addItem(_fromUtf8("120400001"))
        # self.comboBox_item.addItem(_fromUtf8("120400001A"))
        # self.comboBox_item.addItem(_fromUtf8("120400002"))
        # self.comboBox_item.addItem(_fromUtf8("120400002A"))
        # self.comboBox_item.addItem(_fromUtf8("120400002B"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.comboBox_item)
        self.label_mount = QtGui.QLabel(self.formLayoutWidget)
        self.label_mount.setObjectName(_fromUtf8("label_mount"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_mount)
        self.spinBox_mount = QtGui.QSpinBox(self.formLayoutWidget)
        self.spinBox_mount.setValue(6)
        self.spinBox_mount.setObjectName(_fromUtf8("spinBox_mount"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.spinBox_mount)
        self.pushButton = QtGui.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.pushButton)
        self.calendarWidget_from = QtGui.QCalendarWidget(self.formLayoutWidget)
        self.calendarWidget_from.setSelectedDate(QtCore.QDate(2015, 5, 28))
        self.calendarWidget_from.setObjectName(_fromUtf8("calendarWidget_from"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.calendarWidget_from)
        self.calendarWidget_to = QtGui.QCalendarWidget(self.formLayoutWidget)
        self.calendarWidget_to.setObjectName(_fromUtf8("calendarWidget_to"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.calendarWidget_to)
        self.tabWidget.addTab(self.tab_items, _fromUtf8(""))
        self.tab_others = QtGui.QWidget()
        self.tab_others.setObjectName(_fromUtf8("tab_others"))
        self.tabWidget.addTab(self.tab_others, _fromUtf8(""))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(340, 30, 540, 490))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.setdb = QtGui.QAction(QtCore.QString("SetDB"),self.toolBar) 
        self.toolBar.addAction(self.setdb)
        self.setItem = QtGui.QAction(QtCore.QString("SetItem"),self.toolBar) 
        self.toolBar.addAction(self.setItem)
        self.saveCsv = QtGui.QAction(QtCore.QString("SaveCSV"),self.toolBar) 
        self.saveCsv.setEnabled(False)
        self.toolBar.addAction(self.saveCsv)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.setdb, QtCore.SIGNAL(_fromUtf8("triggered ()")), self.showDlgSetdb)
        QtCore.QObject.connect(self.setItem, QtCore.SIGNAL(_fromUtf8("triggered ()")), self.showDlgSetItem)
        QtCore.QObject.connect(self.saveCsv, QtCore.SIGNAL(_fromUtf8("triggered ()")), self.saveFileCsv)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("pressed ()")), self.searchByItem)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
    def setItemCode(self):
        with open('itemcode.json') as data_file:    
            data = json.load(data_file)
            print type(data)
            for k in range(len(data)):
                print data[k]
                self.comboBox_item.addItem(_fromUtf8(data[k]))
        
        
    def saveFileCsv(self):
        pass
        # dlg=QFileDialog()
        # dlg.setacceptMode(QFileDialog.AcceptSave)
        # dlg.setFileMode(QFileDialog.AnyFile) 
        # dlg.setFilter("Text files (*.txt)") 
        # filenames=QStringList() 
        # if dlg.exec_(): 
        #     filenames=dlg.selectedFiles() 
        #     f = open(filenames[0], 'r') 
        #     with f: 
        #         data = f.read() 
        #         self.contents.setText(data)

    def searchByItem(self):
        if not self.cursor:
            self.showDlgSetdb()
        params = {}
        params['itemCode'] = str(self.comboBox_item.itemText(self.comboBox_item.currentIndex()))
        params['from'] = str(self.calendarWidget_from.selectedDate().toString('yyyy-MM-dd'))
        params['to'] = str(self.calendarWidget_to.selectedDate().toString('yyyy-MM-dd'))
        params['mount'] = self.spinBox_mount.value()
        print params
        sql = sqlByItem(params)
        print sql
        r= self.cursor.execute(sql)
        self.data = r.fetchall()
        
        
        length = len(self.data)
        self.tableWidget.setRowCount(length)
        if length > 0:
            self.saveCsv.setEnabled(True)
            
            
        fillTable(self.tabWidget, self.data)
        
        
        # for i in range(0, length-1):
        #     itemi = self.data[i]
        #     print itemi
            
        #     self.tableWidget.setItem(i, 0, QtGui.QTableWidgetItem(itemi[0]))
        #     self.tableWidget.setItem(i, 1, QtGui.QTableWidgetItem(str(itemi[1])))
        #     self.tableWidget.setItem(i, 2, QtGui.QTableWidgetItem(str(itemi[2])))
        #     self.tableWidget.setItem(i, 3, QtGui.QTableWidgetItem(itemi[3]).strftime("%Y-%m-%d"))
        
        
    
    
    def showDlgSetdb(self):
        Dialog = QtGui.QDialog()
        ui = Ui_Dialog_Setdb(self)
        ui.setupUi(Dialog)
        Dialog.exec_()
        print 'dlg set db closed...'
        CURSOR = self.cursor
        DB = self.db
        
    def showDlgSetItem(self):
        Dialog = QtGui.QDialog()
        ui = Ui_Dialog_SetItem()
        ui.setupUi(Dialog)
        Dialog.exec_()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_from.setText(_translate("MainWindow", "From", None))
        self.label_to.setText(_translate("MainWindow", "To", None))
        self.label_item.setText(_translate("MainWindow", "Item", None))
        # self.comboBox_item.setItemText(0, _translate("MainWindow", "120400001", None))
        # self.comboBox_item.setItemText(1, _translate("MainWindow", "120400002", None))
        self.label_mount.setText(_translate("MainWindow", "Mount > ", None))
        self.pushButton.setText(_translate("MainWindow", "Search", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_items), _translate("MainWindow", "Items", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_others), _translate("MainWindow", "Others", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "patient_id", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "visit_id", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "mount", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "billing_date_time", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
    

class MyWindow(QtGui.QMainWindow):
    
    def closeEvent(self,event):
        if CURSOR:
            CURSOR.close()
        if DB:
            DB.close()
        print 'close db/cursor ...'
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = MyWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())
    # ui.closeDBConnect()

