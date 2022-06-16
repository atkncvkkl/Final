# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 15:00:50 2022

@author: atknc
"""

class employees:
    
    def __init__(self,e_name,e_surname):
        
        self.__e_name = e_name
        self.__e_surname = e_surname
        
    def set_name(self,e_name):
        
        self.__e_name = e_name
        
    def set_surname(self,e_surname):
        
        self.__e_surname = e_surname
        
    def get_name(self):
        
        return self.__e_name
    
    def get_surname(self):
        
        return self.__e_surname
    
    def print_employee(self):
        
        print(self.__e_name,self.__e_surname)



class commissionEmployee(employees):
    
    def __init__(self, e_name, e_surname,commission_rate,gross_sales):
        
        employees.__init__(self, e_name, e_surname)
        
        self.__commission_rate = commission_rate
        self.__gross_sales = gross_sales
        
    
    def set_commissionrate(self,commission_rate):
        
        self.__commission_rate = commission_rate
        
    def set_grosssales(self,gross_sales):
        
        self.__gross_sales = gross_sales
        
    def get_commissionrate(self):
        
        return self.__commission_rate
    
    def get_grosssales(self):
        
        return self.__gross_sales
    
        
    def print_employee(self):
        
        employees.print_employee(self)
        print(self.__commission_rate,self.__gross_sales)
        
    def calculate_earnings(self):
        
        earnings = self.__commission_rate*self.__gross_sales
        print(earnings)
        
class basepluscommissionemployee(commissionEmployee):
    
    def __init__(self, e_name, e_surname, commission_rate, gross_sales,base_salary):
        
        commissionEmployee.__init__(self, e_name, e_surname, commission_rate, gross_sales)
        
        self.__base_salary = base_salary
        
    def set_base_salary(self,base_salary):
        
        self.__base_salary = base_salary
        
    def get_base_salary(self):
        
        return self.__base_salary
    
    def print_employee(self):
        
        commissionEmployee.print_employee(self)
        print(self.__base_salary)
        
    def earnings(self):
        
        earnings = self.__base_salary+(commissionEmployee.get_commissionrate(self)*commissionEmployee.get_grosssales(self))
        print(earnings)