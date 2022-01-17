# -*- coding: utf-8 -*-

### PyPDF2 library found in local directory
import PyPDF2 as PyDF

### Imports CSV, Comma-separated values module for writing
import csv

"""
Atributes:
    name - name of file
    len - number of pages in file
    pages - list of plaintext pulled from pages of the document
    dataList - 2D List of plaintext separated by \n
"""
class PyStatement:
    
    ### Pre: Initialization
    ### Post: Converts file in_file to parseable data and sets atributes
    def __init__(self, in_file):
        self.name = in_file.split(".")[0]
        
        ### Open file to be read, closes when done
        ### Must use mode="rb" for binary read mode
        with open(in_file, mode="rb") as bin_doc:
            
            ### Converts the in_file to a PyPDF2 object
            doc = PyDF.PdfFileReader(bin_doc)
            
            
            ### Creates attribute len as the number of the pages in doc
            self.len = doc.getNumPages()
            ### Creates attribute pages as a list of all pages in doc
            self.pages = []
            ### Creates attribute dataList as a list of data
            ### separated in original document by a \n
            self.dataList = []
            
            ### User notification
            print("Converting file " + in_file + " to a PyStatement")
            
            ### Pulls data from the read document into the list pages
            ### and populates dataList
            for i in range(self.len):
                page = doc.getPage(i)
                
                ### Raw page data
                self.pages.append(page.extractText())
                
                ### Raw line data
                ### pages[i].split() returns a list of \n separated values
                self.dataList.append(self.pages[i].split("\n"))
            
            ### User notification
            print("File " + self.name + " converted\n")
            
            
    ### Pre: CSV or TSV as string for file type
    ### Post: Writes a CSV or TSV file with the data from read document
    def toFile(self, file_type):
        ### Raises exception if the file type is not a CSV or TSV
        if(file_type != "CSV" and file_type != "TSV"):
            raise Exception("Unsupported file type")
            
        ### Opens the file in correct format to be written to as out_file,
        ### closes when done
        with open(self.name + "_converted." + file_type.lower(), "w", newline="") as out_file:
            if(file_type == "CSV"):
                print("File " + self.name + " being written to CSV")
                writer = csv.writer(out_file)
            elif(file_type == "TSV"):
                print("File " + self.name + " being written to TSV")
                writer = csv.writer(out_file, delimiter="\t")
                
            ### Writes data in dataList to the new file
            writer.writerows(self.dataList)
            print("File written as a " + file_type +"\n")
            