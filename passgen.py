# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 09:24:26 2020

@author: samga
"""


import  random

uCase = "QWERTYUIOPASDFGHJKLZXCVBNM"
lCase = "qwertyuiopasdfghjklzxcvbnm"
numbers = "0123456789"
symbols = "\|?/>.<`~!@#$%^&*()_+;,"

all = uCase + lCase + numbers + symbols

length = 16 
password = "".join(random.sample(all, length))

print(password)