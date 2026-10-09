
from tkinter import filedialog as fd
from pdf.generator import DocGenerator




def createInvoiceDoc(doc, propsIndex, loadJson):
    path = f"{fd.askdirectory()}/{"test.pdf"}"
    doc = DocGenerator(path=path)
    
    
    doc.add_text(x=100, y=500, text="ДОГОВОР ПОСТАВКИ № _____")
    
createInvoiceDoc()