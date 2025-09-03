from ui.renderer import RenderUI
from components.pdfConf.pdfConf import createPDF
import re


windowSize = "400x700"
requisites = ["ИП Алапаев","Эмин и Ко"]

def renderCommercialForm(form, docType):
    frameKey = "CommercialForm"
    form.add_label_frame(frameKey, docType, 0,1)
    formData = {
        "offer" : form.add_input(frameKey, "Предложение",0,0),
    }
    return formData
    
    
def renderCommonForm(docName, docType):
    frameKey = "formFrame"
    form = RenderUI(docName[docType], windowSize, 10)
    tablesData, invoiceData = form.choose_file()
    form.add_label_frame(frameKey, "Заполните форму", 1,1)
    formData = {
        "docRequisite": form.add_combobox(frameKey,"Реквизит",requisites, 0,0),
        "clientName" : form.add_input(frameKey, "Имя клиента",1,0, text_var=invoiceData["buyer"]),
        "isPrint": form.add_checkbox(frameKey, "Поставить печать", 4, 1, True),
        "docNum": invoiceData["invoice_num"],
    }
    if docType == 1: formData = formData | renderCommercialForm(form, docName[docType])
    form.add_button(frameKey, "СОЗДАТЬ", lambda: createPDF(formData,docName, docType, tablesData, invoiceData), 5,1)
    

    