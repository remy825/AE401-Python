# -*- coding: utf-8 -*-
"""
Created on Sat May 23 11:17:58 2020

@author: remy
"""

import turtle

turtle.shape("circle")
turtle.penup()
#size = 20
for i in range(30):
    turtle.stamp()
    size = size + 3
    turtle.forward(size)
    turtle.right(24)
turtle.done()