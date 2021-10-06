#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 13:11:16 2021

@author: fennieliang
"""
import tkinter as tk

main = tk.Tk() #declare a main window

main.title("My Phthon Window")


#  add button to the window
button = tk.Button(main, #widget
                   text = "hello", 
                   width = 20)

button.pack()#every widget needs to be packed in the main window

main.mainloop()#mainloop is for the window to active
