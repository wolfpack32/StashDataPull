# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 20:20:03 2022

@author: Ryan Tilgner
        Reece Tilgner
"""
#Hello RYAN LOOK HEREEEEEE
#Seen
import PyPDF2 as PyDF

### Opens a file, important to use mode='rb' for binary read mode
### 
in_file = open("JuneDoc.pdf", mode="rb")

### Converts the in_file to a PyPDF2 object
doc = PyDF.PdfFileReader(in_file)

### Creates a list of individual pages
pages = []
for i in range(doc.getNumPages()):
    pages.append(doc.getPage(i))
    