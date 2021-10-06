#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 13:25:35 2021

@author: fennieliang
"""

import tkinter as tk
from tkinter import messagebox

def button_event():
    #print(var.get())
    if var.get() == '':
        tk.messagebox.showerror('message', 'Please Give your answer')
    elif var.get() == '10':
        tk.messagebox.showinfo('message', 'Correct')
    else:
        tk.messagebox.showerror('message', 'Wrong')

root = tk.Tk()
root.title('My Python Class')

mylabel = tk.Label(root, text='5+5=')
mylabel.grid(row=0, column=0)

var = tk.StringVar()
myentry = tk.Entry(root, textvariable=var)
myentry.grid(row=0, column=1)

mybutton = tk.Button(root, text='Submit', command=button_event)
mybutton.grid(row=1, column=1)

root.mainloop()