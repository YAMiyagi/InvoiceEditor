from ui.renderer import RenderUI
from components.form.form import renderCommonForm

docName = ["Счет на оплату", "Коммерческое предложение"]

def renderHome():
    home = RenderUI('DOC RENDER', '400x300')
    frameKey = "button_grid"
    home.add_label_frame(frameKey, "Выберите документ",0,1)
    home.add_button(frameKey,docName[0], lambda: renderCommonForm(docName=docName,docType=0), 0,1)
    home.add_button(frameKey,docName[1], lambda: renderCommonForm(docName=docName,docType=1), 0,2)
    home.update_ui()


