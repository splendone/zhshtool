# -*- coding: utf-8 -*-
from PyQt4 import  QtGui
import json

def setTableFieldsByItem(params):
    with open('fields.json') as data_file:    
        data = json.load(data_file)
        print type(data)
        for k in range(len(data['sql1'])):
            params.horizontalHeaderItem(k).setText(_translate("MainWindow", data['sql1'][k], None))

    # item = params.horizontalHeaderItem(0)
    # item.setText(_translate("MainWindow", "patient_id", None))
    # item = params.horizontalHeaderItem(1)
    # item.setText(_translate("MainWindow", "visit_id", None))
    # item = params.horizontalHeaderItem(2)
    # item.setText(_translate("MainWindow", "mount", None))
    # item = params.horizontalHeaderItem(3)
    # item.setText(_translate("MainWindow", "billing_date_time", None))

def fillTable(tableWidget, data):
    length = len(data)
    for i in range(0, length-1):
        itemi = data[i]
        for j in range(0, len(itemi)-1):
            tableWidget.setItem(i, j, QtGui.QTableWidgetItem(itemi[j]))
            
        # tableWidget.setItem(i, 0, QtGui.QTableWidgetItem(itemi[0]))
        # tableWidget.setItem(i, 1, QtGui.QTableWidgetItem(itemi[1]))
        # tableWidget.setItem(i, 2, QtGui.QTableWidgetItem(itemi[2]))
        # tableWidget.setItem(i, 3, QtGui.QTableWidgetItem(itemi[3]))