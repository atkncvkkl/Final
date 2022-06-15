# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 13:56:12 2022

@author: musta
"""

from PyQt5 import uic

with open('interfaceUI.py','w',encoding="utf-8") as fout:
          uic.compileUi('interface.ui', fout)