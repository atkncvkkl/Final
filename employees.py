# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 11:05:39 2022

@author: musta
"""

class Employee:
    def __init__(self,firstName,lastName):
        super().__init__()
        self.__firstName=firstName
        self.__lastName=lastName
        
    def setfirst(self,firstName):
        self.__firstName=firstName
        
    def setlast(self,lastName):
        self.__lastName=lastName 
        
    def getfirst(self):
        return self.__firstName
    
    def getlast(self):
        return self.__lastName
    
    def print_employee(self):
        print("First Name: ",self.__firstName)
        print("Last Name: ",self.__lastName)

class CommissionEmployee(Employee):
    def __init__(self,firstName,lastName,commission_rate,gross_sales):
        Employee.__init__(self,firstName,lastName)
        self.__gross_sales=gross_sales
        self.__commission_rate=commission_rate
        self.earn=0
    def setgross_sales(self,gross_sales):
        self.__gross_sales=gross_sales
        
    def setcommission_rate(self,commission_rate):
        self.__commission_rate=commission_rate 
        
    def getgross_sales(self):
        return self.__gross_sales
    
    def getcommission_rate(self):
        return self.__commission_rate
    
    def earnings(self):
        self.earn+=self.getcommission_rate()*self.getgross_sales()
        print("Earnings:",self.earn)
    
    def print_employee(self):
        print("")
        Employee.print_employee(self)
        print("Commission Rate: ",self.getcommission_rate())
        print("Gross Sales: ",self.getgross_sales())
    
class BasePlusCommissionEmployee(CommissionEmployee):
    def __init__(self,firstName,lastName,commission_rate,gross_sales,base_salary):
       CommissionEmployee.__init__(self,firstName,lastName,commission_rate,gross_sales)
       self.__base_salary=base_salary

    def setbase_salary(self,base_salary):
       self.__base_salary=base_salary
    
    def getbase_salary(self):
        return self.__base_salary
    def earnings(self):
        self.earn+=self.getbase_salary()
        print("Base Salary: ",self.getbase_salary())
        CommissionEmployee.earnings(self)
        