from ui.renderer import RenderUI
from components.form.form import renderCommonForm

docName = ["Счет на оплату", "Коммерческое предложение"]

def renderHome():
    home = RenderUI('DOC RENDER', '400x300')
    frameName = "button_grid"
    home.add_label_frame(frameName, "Выберите документ",0,1)
    home.add_button(frameName,docName[0], lambda: renderCommonForm(docName=docName,docType=0), 0,1)
    home.add_button(frameName,docName[1], lambda: renderCommonForm(docName=docName,docType=1), 0,2)
    home.update_ui()


