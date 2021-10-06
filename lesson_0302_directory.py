#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 15:14:52 2021

@author: fennieliang
"""

import os

print (os.getcwd())#get current directory

'''
os.chdir('/Users/fennieliang/Documents/GitHub/python/') #change directory


print (os.listdir())# list without a path 


# ***** list files in a directory ****************
path = os.getcwd()
with os.scandir(path) as entries:
    for entry in entries:
        print(entry.name)
'''