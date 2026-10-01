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
                    textData += page.extract_text()
            total = tablesData[0][-1]
            del tablesData[0][-1]
            invoiceData = {
                "invoice_num": re.search(r'\*(\d+)', textData).group(1),
                "buyer": re.search(r"Покупатель:\s*(.+)", textData).group(1).strip(),
                "qty": total[2],
                "summ": total[4],
            }
            print(tablesData)
            print(invoiceData)
            
a = "51 850.00"
print(a[:-3].replace(" ",""))