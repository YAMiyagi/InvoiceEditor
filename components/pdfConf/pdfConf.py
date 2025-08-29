from tkinter import filedialog as fd
import os
import datetime
import json
import re

from components.invoiceDoc.invoiceDoc import createInvoiceDoc
from components.commercialOffer.createCommercialDoc import createCommercialDoc
from pdf.generator import DocGenerator

months = ['января', 'февраля','марта','апреля','мая','июня','июля','августа','сентября','октября','ноября','декабря']

date = {
    'currDay': str(datetime.date.today().day),
    'currMonth': int(datetime.date.today().month),
    'currYear': str(datetime.date.today().year)
}
signPath = ['data/img/sign_1.png', 'data/img/sign_2.png']

def open_pdf(file_path):
    os.startfile(file_path)

def load_json_file(path):
    with open(path,'r', encoding="utf-8") as file:
        return json.load(file)

def nameFile(data, docName):
    string = f'{docName} {data["docRequisite"].get()} {data["clientName"].get()} {data["docNum"]}'
    cleaned_string = re.sub(r'[/\\"\'!@#$%^&*|+=,.:;?<>\-«»\n]', "", string)
    cleaned_string = cleaned_string.replace(" ", "_")
    return cleaned_string

def createPDF(data,docName, docType, tablesData, textData):
    path = f"{fd.askdirectory()}/{nameFile(data=data, docName=docName[docType])}"
    doc = DocGenerator(path=path)
    propsIndex = int(data["docRequisite"].current())
    total = re.search(r"ИТОГО:\s*([\d\s,]+)", textData).group(1).strip()
    if total:
        qty, summ = total.split(" ", 1)
    common_args={
        "doc":doc,
        "data":data,
        "signPath":signPath[propsIndex],
        "propsIndex":propsIndex,
        "loadJson":load_json_file,
        "date":date,
        "months":months,
        "qty":qty,
        "summ":summ,
        "tablesData":tablesData
    }
    
    if docType == 0:
        createInvoiceDoc(**common_args)
    elif docType == 1:
        createCommercialDoc(**common_args)
    
        
    doc.save_page()
    doc.show_page()
    open_pdf(f"{path}.pdf")
    
    
