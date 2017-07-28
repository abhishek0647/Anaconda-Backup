# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 00:03:19 2016

@author: abhishek
"""

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

# Open a PDF document.
fp = open('/Users/abhishek/Downloads/Table of Schedule for sales 11.03.2016.pdf', 'rb')
parser = PDFParser(fp)
document = PDFDocument(parser)

# Get the outlines of the document.
try:
    outlines = document.get_outlines()
    for (level,title,dest,a,se) in outlines:
        print (level, title)
except PDFNoOutlines:
    pass
