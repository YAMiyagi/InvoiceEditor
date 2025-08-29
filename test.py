import pdfplumber 

tablesData = []
textData = ""
with pdfplumber.open(f"naklad.pdf") as pdf:
    for page in pdf.pages:
        tablesData.append(page.extract_table())
        textData += page.extract_text()
        