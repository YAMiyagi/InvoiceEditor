import pdfplumber 
import re
tablesData = []
textData = ""
with pdfplumber.open(f"naklad.pdf") as pdf:
    for page in pdf.pages:
        tablesData.append(page.extract_table())
        textData += page.extract_text()
if len(tablesData) > 1:
        tablesData = sum(tablesData, [])         
else: 
    pattern = r"^\s*(\d+)\s+(\S+)\s+(.+?)\s+(\d+)\s+(\d+)\s+(\d+)\s*$"
    matches = re.findall(pattern, textData, re.MULTILINE)
    print(matches)
    # tablesData = [list(matches[0])]
tablesData.insert(0,["№","КАТЕГОРИЯ","ПАРАМЕТРЫ","КОЛ","ЦЕНА","СУММА"])
print(tablesData)