from components.num2words.num2words import convertNum2Words





def createInvoiceDoc(doc, data, signPath, propsIndex, loadJson, date, months):
    props = loadJson('data\JSON\props.json')['props'][propsIndex]
    props = props.split("~")
    props.reverse()
    
    totalPrice = data["totalPrice"].get()
    
    for index, str in enumerate(props):
        doc.add_string(x=150, y=640 + index * 18, text=str, font="Arial-Thick")

    doc.add_string(
        x=60, 
        y=800, 
        text=f"Счет на оплату №{data["docNum"].get()} от {date["currDay"]} {months[date["currMoth"] - 1]} {date["currYear"]}г.",
        font="Arial-Thick"
    )
    doc.add_string(x=60, y=598, text="Покупатель")
    doc.add_string(x=60, y=623, text="Склад")
    doc.add_string(x=60, y=640, text="Поставщик")
    doc.add_string(x=150, y=598, text=data["clientName"].get(), font="Arial-Thick")
    doc.add_string(x=80, y=170, text=f'Всего наименованний {data["itemsAmount"].get()}, на сумму {totalPrice} сом')
    doc.add_string(x=80, y=150, text=f'{convertNum2Words(totalPrice)} сом')
    doc.add_string(x=80, y=70, text='Руководитель')
    doc.add_string(x=430, y=70, text='Бухгалтер')
    
    doc.add_stroke(x=50, y=790, x2=550, y2=790, weight=3)
    doc.add_stroke(x=190, y=65, x2=410, y2=65)
    doc.add_image(path=signPath, x=170, y=0, width=120, height=120)
    
    