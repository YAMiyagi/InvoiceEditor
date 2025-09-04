import PyPDF2
import re

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
match = re.search(r"1\s+([A-Z0-9\- ]+[\s\S]*?)\d+\s+\d+", text)
if match:
    product_name = match.group(1).strip()
    print(product_name)