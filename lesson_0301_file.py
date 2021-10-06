# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 9:46:42 2021

@author: fennieliang
"""

import os

#from lesson_03_class import FileOperate as fo


# ***** create a new file ************
file = open('file_list.txt', 'w') #the file is open from the current location   
file.write("Add a new line to the file.\n")
file.close()
'''
# ***** write to an existing file ************
file = open('file_list.txt', 'a')
file.write("Add a second line to the file.\n")
file.close()
    

# ***** read a file ************
file = open ('file_list.txt', 'r')
print (file.read(5))
#print (file.read())
#print (file.readline())
#print (file.readlines())
file.close()


path = '/Users/fennieliang/Documents/GitHub/python/lesson03/' 
name = 'file_list.txt'

filename = fo.filePath(path, name)

string = 'Add a third line to this file.\n'

file = fo.createFile(filename, string)
string1 = 'Append a new line.\n'
file = fo.appendString(filename, string1)
lines = fo.readFile(filename)

print (lines)
'''

'''
practice 
0301 create a class FileOperate and a function called filePath
0302 add a function createFile to create a new file
0303 add a function appendString for appending text to an existing file
0304 add a function readFile for reading text from a file
'''
