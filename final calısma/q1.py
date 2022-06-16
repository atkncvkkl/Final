# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 15:05:57 2022

@author: atknc
"""

import employees

def main():
    
    my_employee = employees.employees("atakan", "çevikkol")
    my_employee.print_employee()
    
    my_comm_employee = employees.commissionEmployee("atakan", "cevikkol", 10000, 0.6)
    my_comm_employee.print_employee()
    my_comm_employee.calculate_earnings()
    
    my_base_comm_employee = employees.basepluscommissionemployee("ato", "baba", 5000, 0.4 ,300)
    my_base_comm_employee.print_employee()
    my_base_comm_employee.earnings()
    
    
    
main()