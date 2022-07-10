# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 12:04:23 2022

@author: samhe
"""
import numpy

x = float(input("Enter number x: "))
y = float(input("Enter number y: "))

Power = x**y
Log = numpy.log2(x)

print("x**y = ", Power)
print("log(x) = ", Log)
