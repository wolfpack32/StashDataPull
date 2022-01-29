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
        self.keywords = ["EQUITIES / OPTIONS",
                         "BUY / SELL TRANSACTIONS",
                         "DIVIDENDS AND INTEREST"]
        self.name = in_file.split(".")[0]
        
        
        ### Open in_file to be read as bin_doc, closes when done
        ### Must use mode="rb" for binary read mode
        with open(in_file, mode="rb") as bin_doc:
            
            ### Converts the bin_doc to a PyPDF2 object
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
            self.__compress()
            self.__trim()
            
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
            
            
    ### Pre: self
    ### Post: compresses consecutive single characters into one string
    def __compress(self):
        newList = []
        startCompress = False
        compressed = ""
        ### Selects one page from dataList
        for i in range(self.len):
            for j in range(len(self.dataList[i])):
                ### Selects one word the page
                word = self.dataList[i][j]
                ### Checks if the word is one character long
                if (len(word) == 1):
                    ### If a new compressed word has not been started
                    ### start a new one
                    if (not startCompress):
                        compressed = ""
                        startCompress = True
                    ### Add next character onto word
                    compressed += word
                    
                ### If the next word longer than one character
                else:
                    ### If a compressed word has been made, append it to the list
                    ### and ends the compressed word
                    if startCompress:
                        newList.append(compressed)
                        startCompress = False
                    ### Append the next word to the list
                    newList.append(word)
                    
                ### If the last word on the page is reached adn there is a
                ### compressed word being made, add the word to the list
                if ( (j == len(self.dataList[i]) - 1) and startCompress):
                    newList.append(compressed)
            self.dataList[i] = newList
            newList = []
            
    ### Pre: self
    ### Post: trims irrelevent pages and data from the lists
    def __trim(self):
        ### Removes the first two pages and last five
        self.dataList = self.dataList[2:-5]
        self.len = len(self.dataList)
        
        ### Loops through all words on a page, and checks for keywords
        ### Removes all preceding words from the dataList
        for i in range(self.len):
            while (len(self.dataList[i]) > 0 and not self.dataList[i][0] in self.keywords):
                self.dataList[i].pop(0)
            
        ### Loops through all pages in dataList
        count = 0
        while (count < self.len):
            ### If the page has length 0, page is removed
            ### Statement len decreased by 1
            if(len(self.dataList[count]) == 0):
                self.dataList.pop(count)
                self.len -= 1
            ### If the page has data
            else:
                ### Checks for keyword "continued"
                if(self.dataList[count][1] == "  (continued)"):
                    ### Removes first 2 strings in the list 
                    self.dataList[count] = self.dataList[count][2:]
                else:
                    ### Removes first string in the list
                    self.dataList[count].pop(0)
                count += 1
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            