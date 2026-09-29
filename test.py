import re
from tkinter import filedialog
import pdfplumber
    
def choose_file():
        file_path = ""
        file_path = filedialog.askopenfilename(
            title="Выберите файл",
            filetypes=[("PDF файлы", "*.pdf")]
        )
        if file_path == "":
            return None, None
        if file_path != "":
            tablesData = []
            textData = ""
            with pdfplumber.open(f"{file_path}") as pdf:
                for i, page in enumerate(pdf.pages):
                    table = page.extract_table()
                    tablesData.append(table)
                    for row in tablesData[i]:
                        value, rest = row[2].split(" ", 1)
                        row[3] = value
                        row[2] = rest
                    textData += page.extract_text()
            total = re.search(r"ИТОГО:\s*([\d\s,]+)", textData).group(1).strip()

            invoiceData = {
                "invoice_num": re.search(r'\*(\d+)', textData).group(1),
                "buyer": re.search(r'ПОКУПАТЕЛЬ\s*(.+?)\s*________________', textData).group(1).strip(),
                "qty": total.split(" ", 1)[0],
                "summ": total.split(" ", 1)[1], 
            }
            
            print(tablesData)
            print(invoiceData)
            
choose_file()