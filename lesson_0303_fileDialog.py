#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 09:25:23 2021

@author: fennieliang
"""

# ***** select a file from the file dialogue ************

import tkinter as tk

from tkinter import filedialog as fd

#from lesson_03_class import FileOperate as fo


root = tk.Tk() #assign a tkinter window
root.withdraw()

file = fd.askopenfilename()
print (file)


#string = ('I am Fennie.\n')
#fo.createFile(file, string)
#lines = fo.readFile(file)
#print (lines)



 