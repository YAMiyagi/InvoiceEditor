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
                    tablesData.append(page.extract_table())
                    textData += page.extract_text()
            print(tablesData)
            
            
choose_file()