# -*- coding: utf-8 -*-
"""
Created on Sat May 30 12:05:23 2020

@author: remy
"""


import random

ans = random.randint(1,20)
counter = 0

while counter<5:
    guess = input('Please guess a number between 1 ~ 20:(只能猜五次): ')
    guess = int(guess)
    
    if guess>20 or guess<0:
        print('輸入錯誤，請重新輸入!!!')
        counter = counter +1
    else:
        if guess > ans:
            if counter == 4:
                print("抱歉，你已經猜五次了")
                break
            else:
                print('小一點')
                counter =counter+ 1
        elif guess < ans:
            if counter == 4:
                print("抱歉，你已經猜五次了")
                break
            else:
                print('大一點')
                counter =counter+ 1
        else:
            print('Bingo!!!')
            counter =counter+ 1
            print('你猜了'+str(counter)+'次就答對了')
            break
        