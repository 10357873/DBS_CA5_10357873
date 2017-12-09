#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 15:36:00 2017

@author: ciaran
"""

# program to test the calculator functionality
# unit tests defined, to test each of the calculators 12 defined functions

import unittest
from list_calculator_10357873 import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

	# this tests the add functionality    
    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add([1,2,3,4], [2,3,4,5])
        self.assertEqual([3,5,7,9], result)
        result = self.calc.add([1,0,-3.0],[4.3,4,7])
        self.assertEqual([5.3,4,4.0], result)
        
    # this tests the subtract functionality   
    def test_calculator_subtract_method_returns_correct_result(self):
        result = self.calc.subtract([1,2,3,4], [2,3,4,5])
        self.assertEqual([-1,-1,-1,-1], result)
        result = self.calc.subtract([1,0,-3.0],[4.3,4,7])
        self.assertEqual([-3.3,-4,-10.0], result)
        
    # this tests the multiplication functionality   
    def test_calculator_multiply_method_returns_correct_result(self):
        result = self.calc.multiply([1,2,3,4], [2,3,4,5])
        self.assertEqual([2.0, 6.0, 12.0, 20.0], result)
        result = self.calc.multiply([1,0,-3.0],[4.3,4,7])
        self.assertEqual([4.3, 0.0, -21.0], result)
        
    # this tests the division functionality    
    def test_calculator_divide_method_returns_correct_result(self):
        result = self.calc.divide([1,2,3,4], [2,3,4,5])
        self.assertEqual([0.0, 0.0, 0.0, 0.0], result)
        result = self.calc.divide([1,0,-3.0],[4.3,4,7])
        self.assertEqual([0.23256, 0.0, -0.42857], result)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide([1,2,3],[2,0,1])
        
    # this tests the exponent functionality
    def test_calculator_exponent_method_returns_correct_result(self):
        result = self.calc.exponent([1,2,3,4], [2,3,4,5])
        self.assertEqual([1.0, 8.0, 81.0, 1024.0], result)
        result = self.calc.exponent([1,0,-3.0],[4.3,4,7])
        self.assertEqual([1.0, 0.0, -2187.0], result)

    # this tests the square root functionality
    def test_calculator_square_root_method_returns_correct_result(self):
        result = self.calc.square_root([1,4,25,121])
        self.assertEqual([1,2,5,11], result)
        result = self.calc.square_root([25.0,144.0,5])
        self.assertEqual([5.0, 12.0, 2.23607], result)
        with self.assertRaises(ValueError):
            self.calc.square_root([-2.0,5,4])

    # this tests the square functionality
    def test_calculator_square_method_returns_correct_result(self):
        result = self.calc.square([1,4,25,121])
        self.assertEqual([1.0, 16.0, 625.0, 14641.0], result)
        result = self.calc.square([-25.0,144.0,5])
        self.assertEqual([625.0, 20736.0, 25.0], result)

    # this tests the cube functionality
    def test_calculator_cube_method_returns_correct_result(self):
        result = self.calc.cube([1,4,25,121])
        self.assertEqual([1.0, 64.0, 15625.0, 1771561.0], result)
        result = self.calc.cube([-25.0,144.0,5])
        self.assertEqual([-15625.0, 2985984.0, 125.0], result)
        
    # this tests the sine functionality
    def test_calculator_sine_method_returns_correct_result(self):
        result = self.calc.sine([0,45,90,180])
        self.assertEqual([0.0, 0.70711, 1.0, 0.0], result)

    # this tests the cosine functionality
    def test_calculator_cosine_method_returns_correct_result(self):
        result = self.calc.cosine([0,45,90,180])
        self.assertEqual([1.0, 0.70711, 0.0, -1.0], result)

    # this tests the tangent functionality
    def test_calculator_tangent_method_returns_correct_result(self):
        result = self.calc.tangent([0,45,90,180])
        self.assertEqual([0.0, 1.0, 1.633123935319537e+16, -0.0], result)

    # this tests the inversion functionality
    def test_calculator_inversion_method_returns_correct_result(self):
        result = self.calc.inv([4.0,1,-0.5])  
        self.assertEqual([0.25, 1.0, -2.0], result)
        with self.assertRaises(ZeroDivisionError):
            self.calc.inv([0,2.0])
    
    def test_calculator_returns_error_message_if_one_or_both_list_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, [1,'two',3], [1,2,'three'])
        self.assertRaises(ValueError, self.calc.add, [1,'two',3],  [1,2,3])
        self.assertRaises(ValueError, self.calc.add, [1,2,3], [1,2,'three'])
        self.assertRaises(ValueError, self.calc.subtract, [1,'two',3], [1,2,'three'])
        self.assertRaises(ValueError, self.calc.subtract, [1,'two',3],  [1,2,3])
        self.assertRaises(ValueError, self.calc.subtract, [1,2,3], [1,2,'three'])
        self.assertRaises(ValueError, self.calc.divide, [1,'two',3], [1,2,'three'])
        self.assertRaises(ValueError, self.calc.divide, [1,'two',3],  [1,2,3])
        self.assertRaises(ValueError, self.calc.divide, [1,2,3], [1,2,'three'])
        self.assertRaises(ValueError, self.calc.multiply, [1,'two',3], [1,2,'three'])
        self.assertRaises(ValueError, self.calc.multiply, [1,'two',3],  [1,2,3])
        self.assertRaises(ValueError, self.calc.multiply, [1,2,3], [1,2,'three'])
        self.assertRaises(ValueError, self.calc.exponent, [1,'two',3], [1,2,'three'])
        self.assertRaises(ValueError, self.calc.exponent, [1,'two',3],  [1,2,3])
        self.assertRaises(ValueError, self.calc.exponent, [1,2,3], [1,2,'three'])
        self.assertRaises(ValueError, self.calc.square_root, [1,'two',3])
        self.assertRaises(ValueError, self.calc.square, [1,'two',3])
        self.assertRaises(ValueError, self.calc.cube, [1,'two',3])
        self.assertRaises(ValueError, self.calc.sine, [1,'two',3])        
        self.assertRaises(ValueError, self.calc.cosine, [1,'two',3])        
        self.assertRaises(ValueError, self.calc.tangent, [1,'two',3])    
        self.assertRaises(ValueError, self.calc.inv, [1,'two',3])

if __name__ == '__main__':
    unittest.main()