# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 20:29:58 2022

@author: atknc
"""

import sys
from PyQt5.QtWidgets import (QPushButton, QSpinBox,QComboBox,QTextEdit, QFormLayout, QGroupBox, QVBoxLayout,QWidget,QLabel,QLineEdit,QApplication)
import numpy as np


class example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.createFormGroupBox()
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        self.setLayout(mainLayout)
        self.show()
        
        
    def createFormGroupBox(self):
        
        
        self.formGroupBox = QGroupBox("Form layout")
        
        self.label_2 = QLabel("status")
        self.linedit = QLineEdit()
        self.textedit = QTextEdit()
        self.combo_box = QComboBox()
        combo_items = ["print to text box", "print to file"]
        self.combo_box.addItems(combo_items)

        
        self.b_run = QPushButton("run")
        self.b_run.clicked.connect(self.operation)
        
        layout = QFormLayout()
        layout.addRow(self.textedit)
        layout.addRow(QLabel("enter number:"), self.linedit)
        layout.addRow(self.combo_box,self.b_run)
        layout.addRow(self.label_2)

        self.formGroupBox.setLayout(layout)
        
        
        
    def operation(self):
        
        self.my_list = []
        try:
            x = int(self.linedit.text())

            
            for n in range(1,x + 1):
               if n > 1:
                   for i in range(2,n):
                       if (n % i) == 0:
                           break
                   else:
                       self.my_list.append(n)
        
        except ValueError:
            self.label_2.setText("WRONG FORMAT")
        

        
        if self.combo_box.currentText() == "print to text box":
            self.print_text_box()
        else:
            self.print_to_file()
          
    
        
    def print_text_box(self):
        
        self.textedit.setText(str(self.my_list))
        
        
    def print_to_file(self):
        
        np.savetxt("deneme.txt", self.my_list, fmt='%.4f')
        
        
        
        
        
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = example()
    sys.exit(app.exec_())