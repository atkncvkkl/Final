# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 11:45:32 2022

@author: musta
"""

import employees

def main():
    my_employee=employees.Employee("John", "Smith")
    my_employee.print_employee()
    
    my_comm_employee=employees.CommissionEmployee("Sue","Jones",10000,0.6)
    my_comm_employee.print_employee()
    my_comm_employee.earnings()
    
    my_base_comm_employee=employees.BasePlusCommissionEmployee("Bob", "Lewis", 5000, 0.4, 300)
    my_base_comm_employee.print_employee()
    my_base_comm_employee.earnings()
main()