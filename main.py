# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 20:20:03 2022

@author: rmdti
"""

import PyPDF2

test_pdf = open('JuneDoc.pdf', mode='rb')
pdfdoc = PyPDF2.PdfFileReader(test_pdf)

print(pdfdoc.documentInfo)