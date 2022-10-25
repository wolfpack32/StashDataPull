# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 13:01:12 2022

@author: rtilgner
"""

### Statement object, see PyStatement/formatting.py
import PyStatement as Statement

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

class Screen:
    global file_names = ""
    def __init__(self):
        root = tk.Tk()
        self.populate(root)
        
    def populate(self, root):
        root.title("Stash Investment Viewer")
        
        files = tk.Label(root,
                     text="Please choose a file")
        
        open_button = ttk.Button(
            root,
            text="Select Files",
            command= lambda: self.select_files(files))
        
        
        files.pack()
        open_button.pack()
        root.geometry('500x500')
        
        root.mainloop()
        
    def select_files(self, label):
        filetypes = [("pdf file", "*.pdf")]
        filenames = fd.askopenfilenames(
            title="Open Files",
            initialdir="/",
            filetypes = filetypes)
        label.config(text=filenames)
        file_names = filenames