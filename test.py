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
                for page in pdf.pages:
                    table = page.extract_table()
                    tablesData.append(table)
                    textData += page.extract_text()
            tablesData[0][0][-1] = "Сумма"
            tablesData[0][0][-2] = "Цена"
            total = tablesData[len(tablesData) -1][-1]
            del tablesData[0][-1]
            buyer = re.search(r"Покупатель:\s*(.+)", textData).group(1).strip()
            invoiceData = {
                "invoice_num": re.search(r'\*(\d+)', textData).group(1),
                "buyer": buyer if buyer[0] != "№" else " ",
                "qty": total[2],
                "sum": total[4],
            }
            