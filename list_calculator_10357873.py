#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 14:37:26 2017

@author: ciaran
"""
#assumption - all outputs on this calculator are limited to 5 decimal places

    #created 10 extra functions which will work on two lists
        #1. multiplication
        #2. division
        #3. exponent
        #4. square root
        #5. square
        #6. cube
        #7. sine
        #8. cosine
        #9. tan
        #10. inversion
        
#import the math library
import math

class Calculator(object):
    
    #defining addition functionality on calculator -> x + y, where x and y are lists
    
    def add(self,x, y):
            number_types = (int, long, float, complex)
            for i in range (0,len(x)):
                if isinstance(x[i], number_types) and isinstance(y[i], number_types):
                    continue       
                else:
                    raise ValueError
            result = [x[i] + y[i] for i in range(len(x))]
            return result
    
    #defining subtraction functionality on calculator -> x - y, where x and y are lists
    def subtract(self,x, y):
            number_types = (int, long, float, complex)
            for i in range (0,len(x)):
                if isinstance(x[i], number_types) and isinstance(y[i], number_types):
                    continue       
                else:
                    raise ValueError
            result = [x[i] - y[i] for i in range(len(x))]
            return result
    
    #defining multiplication functionality on calculator -> x * y, where x and y are lists
    def multiply(self,x, y):
            number_types = (int, long, float, complex)
            for i in range (0,len(x)):
                if isinstance(x[i], number_types) and isinstance(y[i], number_types):
                    continue       
                else:
                    raise ValueError
            result = [round(x[i] * y[i],5) for i in range(len(x))]
            return result
        
    #defining division functionality on calculator -> x / y, where x and y are lists
    def divide(self,x, y):
            number_types = (int, long, float, complex)
            for i in range (0,len(x)):
                if isinstance(x[i], number_types) and isinstance(y[i], number_types):
                    continue       
                else:
                    raise ValueError
            result = [round(x[i] / y[i],5) for i in range(len(x))]
            return result
    
    #defining exponential functionality on calculator -> x ^ y, where x and y are lists
    def exponent(self,x, y):
            number_types = (int, long, float, complex)
            for i in range (0,len(x)):
                if isinstance(x[i], number_types) and isinstance(y[i], number_types):
                    continue       
                else:
                    raise ValueError
            result = [round(x[i] ** y[i],5) for i in range(len(x))]
            return result

    #defining square root functionality on calculator -> sqrt(x), where x is a list
    def square_root(self,x):
            number_types = (int, long, float, complex)
            for i in range (0,len(x)):
                if isinstance(x[i], number_types):
                    continue       
                else:
                    raise ValueError
            result = [round(math.sqrt(x[i]), 5) for i in range(len(x))]
            return result

    #defining square functionality on calculator -> x * x, where x is a list
    def square(self,x):
            number_types = (int, long, float, complex)
            for i in range (0,len(x)):
                if isinstance(x[i], number_types):
                    continue       
                else:
                    raise ValueError
            result = [round(x[i] * x[i], 5) for i in range(len(x))]
            return result      
        
    #defining cube functionality on calculator -> x * x * x, where x is a list
    def cube(self,x):
            number_types = (int, long, float, complex)
            for i in range (0,len(x)):
                if isinstance(x[i], number_types):
                    continue       
                else:
                    raise ValueError
            result = [round(x[i] * x[i] * x[i], 5) for i in range(len(x))]
            return result   
        
    #defining sin functionality on calculator -> sin(x), where x is a list
    def sine(self,x):
            number_types = (int, long, float, complex)
            for i in range (0,len(x)):
                if isinstance(x[i], number_types):
                    continue       
                else:
                    raise ValueError
            result = [round(math.sin(math.radians(x[i])), 5) for i in range(len(x))]
            return result
        
    #defining cos functionality on calculator -> cos(x), where x is a list
    def cosine(self,x):
            number_types = (int, long, float, complex)
            for i in range (0,len(x)):
                if isinstance(x[i], number_types):
                    continue       
                else:
                    raise ValueError
            result = [round(math.cos(math.radians(x[i])), 5) for i in range(len(x))]
            return result

    #defining tan functionality on calculator -> tan(x), where x is a list
    def tangent(self,x):
            number_types = (int, long, float, complex)
            for i in range (0,len(x)):
                if isinstance(x[i], number_types):
                    continue       
                else:
                    raise ValueError
            result = [round(math.tan(math.radians(x[i])), 5) for i in range(len(x))]
            return result
        
    #defining inversion functionality on calculator -> 1 / x, where x is a list
    def inv(self,x):
            number_types = (int, long, float, complex)
            for i in range (0,len(x)):
                if isinstance(x[i], number_types):
                    continue       
                else:
                    raise ValueError
            result = [round(1 /x[i], 5) for i in range(len(x))]
            return result


