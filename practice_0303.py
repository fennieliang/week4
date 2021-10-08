#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 15:17:53 2021

@author: fennieliang
"""
import os

class FileOperate:
    
    def read(path, name):
        filename = os.path.join(path, name)
    
        # ***** read a file ************
        file = open (filename, 'r')
        lines = file.readlines()
        file.close() 
        return lines