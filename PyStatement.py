# -*- coding: utf-8 -*-

### PyPDF2 library found in local directory
import PyPDF2 as PyDF

### Imports CSV, Comma-separated values module for writing
import csv

class PyStatement:
    
    def __init__(self, in_file):
        ### Converts the in_file to a PyPDF2 object
        ### Must use mode="rb" for binary read mode
        doc = PyDF.PdfFileReader(open(in_file, mode="rb"))
        
        ### Creates attribute len as a count of the pages in doc
        self.pages = []
        ### Creates attribute pages as a list of all pages in doc
        self.len = doc.getNumPages()
        ### Creates attribute dataList as a list of data
        ### separated in original document by a \n
        self.dataList = []
        
        ### User notification
        print("Converting file " + in_file + " to a PyStatement")
        ### Pulls data from the read document into the list pages
        ### and populates dataList
        for i in range(self.len):
            page = doc.getPage(i)
            self.pages.append(page.extractText())
            
            self.dataList.append([])
            self.dataList[i].append(self.pages[i].split("\n"))
        
        
        ### User notification
        print("File " + in_file + " converted")