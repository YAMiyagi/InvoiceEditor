import pdfplumber 
import re
import os
from pdf.generator import DocGenerator 

textData = ""
tablesData = []
with pdfplumber.open("naklad.pdf") as pdf:
    for page in pdf.pages:
        print(page.extract_table())
        tablesData.append(page.extract_table())
        textData += page.extract_text()
invoice_num = re.search(r'НАКЛАДНАЯ №(\d+)', textData).group(1)
buyer = re.search(r'ПОКУПАТЕЛЬ\s*(.+?)\s*________________', textData).group(1).strip()
total = re.search(r"ИТОГО:\s*([\d\s,]+)", textData).group(1).strip()

if total:
    qty, summ = total.split(" ", 1)
    
    
tablesData = sum(tablesData, [])
def open_pdf(file_path):
    os.startfile(file_path)

def createPDF():
    path = "pdfgenerated"
    doc = DocGenerator(path=path)
    doc.add_table(data=[["№", "КАТЕГОРИЯ","ПАРАМЕТРЫ","КОЛ","ЦЕНА","СУММА"]],
                  x=50,
                  y=568,
                  col_widths=[30, 100, 200, 30, 70, 70],
                  rect_height=13,
                  font="Arial-Thick",
                  font_size=10)
    doc.add_table(data=tablesData,
                  x=50,
                  y=550,
                  col_widths=[30, 100, 200, 30, 70, 70],
                  rect_height=11,
                  font_size=8)
    
    
    doc.save_page()
    doc.show_page()
    os.startfile(path + ".pdf")
    
createPDF()
    
    
