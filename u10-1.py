# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 11:30:12 2020

@author: remy
"""

letters='abcdefghijklmnopqrst'
print(letters[5])
print(letters[-2])
print(letters[1:6])
print(letters[10:])

letters='a duck goes into a bar'
print(letters.capitalize())
print(letters.title())
print(letters.upper())
print(letters.swapcase())

string = 'this is string example...'
print(string.split())
print(string.split('i'))
print(string.split('i',1))