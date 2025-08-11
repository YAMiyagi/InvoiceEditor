from ui.renderer import RenderUI
from components.pdfConf.pdfConf import createPDF

windowSize = "400x700"
requisites = ["ИП Алапаев","Эмин и Ко"]

def renderInvoiceForm(form, docType):
    frameKey = "invoiceFrame"
    form.add_label_frame(frameKey, docType, 0,1)
    formData = {
        "itemsAmount" : form.add_input(frameKey, "Количество товаров",1,0, isNum=True)
    }
    return formData

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
    secondaryFormData = renderInvoiceForm(form, docName[docType]) if docType == 0 else renderCommercialForm(form, docName[docType])
    form.add_label_frame(frameKey, "Заполните форму", 1,1)
    formData = {
        "docRequisite": form.add_combobox(frameKey,"Реквизит",requisites, 0,0),
        "clientName" : form.add_input(frameKey, "Имя клиента",1,0),
        "docNum": form.add_input(frameKey, "Номер накладной",2,0, True),
        "totalPrice": form.add_input(frameKey, "Конечная стоимость",3,0, True),
        "isPrint": form.add_checkbox(frameKey, "Поставить печать", 4, 1, True)
    }
    formData = formData | secondaryFormData
    
    form.add_button(frameKey, "СОЗДАТЬ", lambda: createPDF(formData,docName, docType), 5,1)
    

    