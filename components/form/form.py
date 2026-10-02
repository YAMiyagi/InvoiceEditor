from ui.renderer import RenderUI
from components.pdfConf.pdfConf import createPDF
from tkinter import filedialog
import pdfplumber 
import re


windowSize = "500x700"
requisites = ["ИП Алапаев","Эмин и Ко"]

def renderCommercialForm(form, docType):
    frameKey = "CommercialForm"
    form.add_label_frame(frameKey, docType, 0,1)
    formData = {
        "offer" : form.add_input(frameKey, "Предложение по реализации",0,0),
    }
    return formData

def choose_file():
        file_path = ""
        file_path = filedialog.askopenfilename(
            title="Выберите файл",
            filetypes=[("PDF файлы", "*.pdf")]
        )
        if file_path == "":
            return None, None
        if file_path != "":
            tablesData = []
            textData = ""
            with pdfplumber.open(f"{file_path}") as pdf:
                for page in pdf.pages:
                    table = page.extract_table()
                    tablesData.append(table)
                    textData += page.extract_text()
            tablesData[0][0][-1] = "Сумма"
            tablesData[0][0][-2] = "Цена"
            total = tablesData[len(tablesData) -1][-1]
            del tablesData[0][-1]
            buyer = re.search(r"Покупатель:\s*(.+)", textData).group(1).strip()
            invoiceData = {
                "invoice_num": re.search(r'\*(\d+)', textData).group(1),
                "buyer": buyer.replace("+996", "") if buyer[0] != "№" else " ",
                "qty": total[2],
                "sum": total[4],
            }
            return tablesData, invoiceData
    
def renderCommonForm(docName, docType):
    tablesData, invoiceData = choose_file()
    if tablesData is None or invoiceData is None:
        return
    frameKey = "formFrame"
    form = RenderUI(docName[docType], windowSize, 10)
    
    form.add_label_frame(frameKey, "Заполните форму", 1,1)
    formData = {
        "docRequisite": form.add_combobox(frameKey,"Реквизит",requisites, 0,0),
        "clientName" : form.add_input(frameKey, "Имя клиента",1,0, text_var=invoiceData["buyer"]),
        "isPrint": form.add_checkbox(frameKey, "Поставить печать", 5, 1, True),
        "docNum": invoiceData["invoice_num"],
    }
    if docType == 1: formData = formData | renderCommercialForm(form, docName[docType])
    form.add_button(frameKey, "СОЗДАТЬ", lambda: createPDF(formData,docName, docType, tablesData, invoiceData), 6,1)
    

    