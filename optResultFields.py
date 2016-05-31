# -*- coding: utf-8 -*-
from PyQt4 import  QtGui
import json



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