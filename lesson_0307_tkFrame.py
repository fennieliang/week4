#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 10:04:49 2021

@author: fennieliang
"""

import tkinter as tk
# tkinter has three ways of deploying widget 
# pack:pack(side='right');side can be on 'top','down','left,'right'
# pack(side='left', ipadx=20, padx=30, ipady=5, pady=10)
# padx and pady are between widgets
# ipadx and ipady are inside widgets
# pack(fill='x');pack(fill='y');pack(fill='both')
# pack(fill='both', expand=1);1: auto expand, 0 not expand

# grid(column=0, row=0, ipadx=5, pady=5)

# place(x=0, y=0); place widget at an absolute place
main = tk.Tk() #declare a main window

main.title("My Phthon Window")

#  add labels in a frame to the window
frame1 = tk.Label(main, bg='#6C0CE5')
frame1.pack()
tk.Label(frame1, text='Full Name').grid(row=0, column=0, padx=5, pady= 5)
#use padx and pady to give space between each label and entry
tk.Label(frame1, text='Email').grid(row=1, column=0)
tk.Label(frame1, text='Password').grid(row=2, column=0)
#name_Tf = tk.Entry(frame1)
#name_Tf.grid(row=0, column=1)
tk.Entry(frame1).grid(row=0, column=1)
tk.Entry(frame1).grid(row=1, column=1)
tk.Entry(frame1, show="*").grid(row=2, column=1)

main.mainloop()#mainloop is for window to active