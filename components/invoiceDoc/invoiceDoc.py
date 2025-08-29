from components.num2words.num2words import convertNum2Words
from components.productTables.productTables import add_product_tables




def createInvoiceDoc(doc, data, signPath, propsIndex, loadJson, date, months, qty, summ,tablesData):
    props = loadJson('data\JSON\props.json')['props'][propsIndex]
    props = props.split("~")
    props.reverse()
    
    for index, str in enumerate(props):
        doc.add_text(x=150, y=640 + index * 18, text=str, font="Arial-Thick")

    doc.add_text(
        x=60, 
        y=800, 
        text=f'Счет на оплату №{data["docNum"]} от {date["currDay"]} {months[date["currMonth"] - 1]} {date["currYear"]}г.',
        font="Arial-Thick"
    )
    doc.add_text(x=60, y=598, text="Покупатель")
    doc.add_text(x=60, y=623, text="Склад")
    doc.add_text(x=60, y=640, text="Поставщик")
    doc.add_text(x=150, y=598, text=data["clientName"].get(), font="Arial-Thick")
    doc.add_stroke(x=50, y=790, x2=550, y2=790, weight=3)
    
    add_product_tables(doc, tablesData=tablesData, qty=qty, summ=summ)
    
    doc.add_text(x=80, y=170, text=f'Всего наименованний {qty}, на сумму {summ} сом')
    doc.add_text(x=80, y=150, text=f'{convertNum2Words(summ[:-3].replace(" ", ""))} сом')
    doc.add_text(x=80, y=70, text='Руководитель')
    doc.add_text(x=430, y=70, text='Бухгалтер')
    
    doc.add_stroke(x=190, y=65, x2=410, y2=65)
    doc.add_image(path=signPath, x=170, y=0, width=120, height=120)
    
    