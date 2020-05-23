# -*- coding: utf-8 -*-
"""
Created on Sat May 16 11:30:14 2020

@author: remy
"""


math = input("score")
eng = input("score")
math = int(math)
eng = int(eng)


if (math >= 90 and eng >=90):
    print('get gift')
    
elif (math <60 and eng <60):
    print('fail')

elif (math < 60 or eng <60):
    print('keep going')
    
else:
    print('pass')
    

    