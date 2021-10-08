#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 15:11:52 2021

@author: fennieliang
"""

import os

class FileOperate:
    

    def create(path, name, string):
        filename = os.path.join(path, name)
        
        # ***** create a new file ************
        file = open(filename, 'w') #the file is open from the current location   
        file.write(string)
        file.close()