# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:48:49 2020

@author: ucobiz
"""

MD_TAX = 0.06 #this is the constant for TAX rate
subtotal = input("Enter subtotal:")
# convert from string to integer
subtotal = int(subtotal)
tax = subtotal * MD_TAX
total = tax + subtotal
print("Your total is:", int(total))




