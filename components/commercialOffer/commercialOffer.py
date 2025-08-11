from components.num2words.num2words import convertNum2Words
kp_title = [
    'Алапаев Адилет',
    'Умуш Аскар'
]

def createCommercailDoc(doc, data, signPath, propsIndex, loadJson, date, months):
    props = loadJson('data\JSON\kpProps.json')['props'][propsIndex]
    props = props.split("~")
    props.reverse()
    totalPrice = data["totalPrice"].get()
    
    for index, str in enumerate(props):
        text_width = doc.get_string_width(text=str, font='Arial-Thick', font_size=9)
        right_margin = 595
        x = right_margin - text_width - 20
        doc.add_string(x=x, y=720 + index * 15, text=str, font='Arial-Thick', font_size = 9)
    
    doc.add_string(
        x=60, 
        y=670, 
        text=f"Исходный документ №{data["docNum"].get()} от {date["currDay"]} {months[date["currMoth"] - 1]} {date["currYear"]}г.",
        font_size=10
    )
    doc.add_string(x=185, y=620, text="Коммерческое предложение", font="Arial-Thick", font_size = 15)
    doc.add_string(x=120, y=580, text=f"Уважаемый {data["clientName"].get()}, Благодарим за интерес к нашим услугам.", font_size=11)
    doc.add_string(x=90, y=560, text=f"Мы предлагаем рассмотреть наше предложение по реализации {data["offer"].get()}:", font_size=11)
    
    doc.add_string(x=80, y=170, text=f'Итого настоящего коммерческого предложения составило: {totalPrice} сом')
    doc.add_string(x=80, y=150, text=f'{convertNum2Words(totalPrice)} сом')
    doc.add_string(x=90, y=70, text="С уважением", font_size=11)
    doc.add_string(x=90, y=55, text=kp_title[propsIndex], font_size=11)
    
    doc.add_stroke(x=50, y=690, x2=700, y2=690, weight=3)
    
    doc.add_image(path="data\img\emin.png", x=70, y=720, width=140, height=55)
    doc.add_image(path=signPath, x=200, y=0, width=120, height=120)