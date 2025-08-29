from components.num2words.num2words import convertNum2Words
from components.productTables.productTables import add_product_tables
from reportlab.pdfbase import pdfmetrics
kp_title = [
    'Алапаев Адилет',
    'Умуш Аскар'
]

def createCommercialDoc(doc, data, signPath, propsIndex, loadJson, date, months, qty, summ,tablesData):
    props = loadJson('data/JSON/kpProps.json')['props'][propsIndex]
    props = props.split("~")
    props.reverse()
    
    for index, str in enumerate(props):
        text_width = doc.get_string_width(text=str, font='Arial-Thick', font_size=9)
        right_margin = 595
        x = right_margin - text_width - 20
        doc.add_text(x, y=720 + index * 15, text=str, font='Arial-Thick', font_size = 9)
    
    doc.add_text(
        x=60, 
        y=670, 
        text=f"Исходный документ №{data['docNum']} от {date['currDay']} {months[date['currMonth'] - 1]} {date['currYear']}г.",
        font_size=10
    )
    doc.add_text(x=185, y=620, text="Коммерческое предложение", font="Arial-Thick", font_size = 15)
    doc.add_text(x=120, y=580, text_area_width = 400, text=f'Уважаемый {data["clientName"].get()}, Благодарим за интерес к нашим услугам.', font_size=11)
    doc.add_text(x=90, y=560, text_area_width = 400, text=f'Мы предлагаем рассмотреть наше предложение по реализации {data["offer"].get()}:', font_size=11)
    doc.add_image(path="data\img\emin.png", x=70, y=720, width=140, height=55)
    doc.add_stroke(x=50, y=690, x2=700, y2=690, weight=3)
    
    add_product_tables(doc, y=500, tablesData=tablesData, qty=qty, summ=summ)
    
    doc.add_text(x=80, y=170, text=f'Итого настоящего коммерческого предложения составило: {summ} сом')
    doc.add_text(x=80, y=150, text=f'{convertNum2Words(summ[:-3].replace(" ", ""))} сом')
    doc.add_text(x=90, y=70, text="С уважением", font_size=11)
    doc.add_text(x=90, y=55, text=kp_title[propsIndex], font_size=11)
    
    
    doc.add_image(path=signPath, x=200, y=0, width=120, height=120)