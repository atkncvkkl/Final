# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 13:58:10 2022

@author: musta
"""
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLineEdit, QTextEdit,QComboBox, QStatusBar
from PyQt5.QtGui import QIntValidator
import sys
import numpy as np
class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi("interface.ui",self)
        self.run_button=self.findChild(QPushButton,"pushButton")
        self.run_button.clicked.connect(self.calculate_primes)
        self.lineEdit = self.findChild(QLineEdit,"lineEdit")
        #self.lineEdit.setValidator(QIntValidator())
        self.text=self.findChild(QTextEdit,"textEdit")
        self.combo=self.findChild(QComboBox,"comboBox")
        self.status=self.findChild(QStatusBar,"statusbar")
        self.show()
    def calculate_primes(self):
        a=list()
        self.text_combo = str(self.combo.currentText())
        a.append(2)
        userinput = self.lineEdit.text()
        print("User input",userinput)
        self.check_user_input(userinput)
        try:
            for num in range(int(userinput) + 1):
               # all prime numbers are greater than 1
               if num > 1:
                   for i in range(2, num):
                       if (num % i) == 0:
                           break
                       else:
                           a.append(num)
            uniq=np.unique(a)
            print(uniq)
            print(str(self.text_combo))
            if self.text_combo=="Print the text box":
                self.text.append(str(np.unique(a)))
            elif self.text_combo=="Write the file":
                np.savetxt('test.txt',uniq,fmt='%.2e')
        except:
            self.status.showMessage("An error occured")
    def check_user_input(self,userinput):
        try:
            # Convert it into integer
            val = int(userinput)
            print("Input is an integer number. Number = ", val)
            self.status.showMessage("Input is an integer number")
        except ValueError:
            try:
                # Convert it into float
                val = float(userinput)
                print("Input is a float  number. Number = ", val)
                self.status.showMessage("Input is a float  number.")
            except ValueError:
                print("No.. input is not a number. It's a string")
                self.status.showMessage("No.. input is not a number. It's a string")
app=QApplication(sys.argv)
UIWindow=UI()
app.exec_()