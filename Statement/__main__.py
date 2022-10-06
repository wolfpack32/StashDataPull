# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 20:20:03 2022

@author: Ryan Tilgner
        Reece Tilgner
"""

### Statement object, see PyStatement/formatting.py
import PyStatement as Statement

### GUI for file uploads and data viewing
import Interface as SC

import sqlite3
from sqlite3 import Error


"""
try:
    con = sqlite3.connect(":memory:")
    print("Connected to database\n")

except Error:
    print(Error)
    
finally:
    con.close()

"""

gui = SC.Screen()

try:
    #June = Statement.PyStatement("JuneDoc.pdf")
    #June.toFile("CSV")
    pass
    
except PermissionError:
    print("Error in conversion, please close any open files and try again.")
    
    
