#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 15:13:34 2021

@author: fennieliang
"""
import os


class FileOperate:
    def append(path, name, string):
        filename = os.path.join(path, name)
        
        # ***** write to an existing file ************
        file = open(filename, 'a')
        file.write(string)
        file.close()