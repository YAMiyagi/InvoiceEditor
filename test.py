import PyPDF2

# Укажите путь к вашему PDF-файлу
pdf_path = 'naklad.pdf'  # Замените на реальный путь

# Открываем файл в бинарном режиме
with open(pdf_path, 'rb') as file:
    # Создаём объект PdfReader
    reader = PyPDF2.PdfReader(file)
    
    # Проходим по всем страницам
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text = page.extract_text()  # Извлекаем текст с страницы
        
        # Выводим текст (или сохраняем в файл/базу данных)
        print(f"Страница {page_num + 1}:\n{text}\n{'-'*50}")