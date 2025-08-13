import pdfplumber
import re
import os
from pdf.generator import DocGenerator 

textData = ""
tablesData = []
with pdfplumber.open("naklad.pdf") as pdf:
    for page in pdf.pages:
        tablesData.append(page.extract_table())
        textData += page.extract_text()
invoice_num = re.search(r'НАКЛАДНАЯ №(\d+)', textData).group(1)
buyer = re.search(r'ПОКУПАТЕЛЬ\s*(.+?)\s*________________', textData).group(1).strip()

def open_pdf(file_path):
    os.startfile(file_path)

def createPDF():
    path = "pdfgenerated"
    doc = DocGenerator(path=path)
    doc.add_table(data=tablesData[0], x=50, y=750, col_widths=[30, 100, 200, 30, 70, 70])
    
    
    doc.save_page()
    doc.show_page()
    os.startfile(path + ".pdf")
    
createPDF()
    
    
