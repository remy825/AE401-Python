# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:11:36 2020

@author: remy
"""
"""
fo = open('fuck2.txt', 'w')
fo.write('thisis a test')

fo = open('fuck2.txt')
myletter = fo.read()
print(myletter)
"""

fo = open('fuck2.txt', 'a')
fo.write('and i')
fo.close()

fo = open('fuck2.txt', 'r')
myletter = fo.read()
print(myletter)
fo.close()


import os.path

if os.path.isfile('fuck2.txt'):
    print('yes')
else:
    print('no')