import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pdfplumber 
import re
class RenderUI():
    def __init__(self, title: str, geometry: str, gap:int = 5):
        self.__root = tk.Tk()
        self.__geometry = geometry
        self.__title = title
        self.__frames = {}
        self.__gap = gap
        self.render_window()
    
    def render_window(self):
        self.__root.title(self.__title)
        self.__root.geometry(self.__geometry)
        
    def update_ui(self):
        self.__root.mainloop()
    
    def add_label_frame(self, name:str, text:str, row:int, column:int):
        lf = ttk.LabelFrame(self.__root, text=text)
        lf.grid(row=row, column=column, padx=self.__gap, pady=self.__gap, sticky="nsew")
        self.__root.grid_columnconfigure(1, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__frames[name] = lf

    def add_button(self,frameKey:str, text:str, onClick, row: int, col: int):
        self._check_frame_key(frameKey)
        btn = ttk.Button(self.__frames[frameKey], text=text, command=onClick)
        btn.grid(row=row, column=col, padx=self.__gap, pady=self.__gap)
        
    def add_input(self, frameKey:str, text:str, row:int, col:int, isNum: bool = False, text_var = None):
        
        self._check_frame_key(frameKey)
        self.add_label(frameKey, text, row, col)
        entry = ttk.Entry(self.__frames[frameKey])
        entry.insert(0, text_var if text_var else "")
        entry.bind("<Key>", self._on_key_release)
        entry.grid(row=row, column=col + 1, padx=self.__gap, pady=self.__gap, sticky="ew")
        
        if isNum:
            self._validate_numeric_input(entry)
        return entry
        
    def add_combobox(self,frameKey:str, text:str, props, row:int, col:int):
        self._check_frame_key(frameKey)
        self.add_label(frameKey, text, row, col)
        combo = ttk.Combobox(self.__frames[frameKey], values = props, state="readonly")
        combo.grid(row=row, column=col + 1, padx=self.__gap, pady=self.__gap)
        return combo
    
    def add_checkbox(self, framekey: str, text:str, row:int, col: int, default=False):
        self._check_frame_key(framekey)
        var = tk.IntVar(value=1 if default else 0)
        checkbox = ttk.Checkbutton(self.__frames[framekey], text=text, variable=var)
        checkbox.grid(row=row, column=col, padx=self.__gap, pady=self.__gap)
        return var
        
    def add_label(self, frameKey: str, text: str, row: int, col: int):
        ttk.Label(self.__frames[frameKey], text=text).grid(row=row, column=col, sticky="e", padx=self.__gap, pady=self.__gap)

    def choose_file(self):
        file_path = ""
        file_path = filedialog.askopenfilename(
            title="Выберите файл",
            filetypes=[("PDF файлы", "*.pdf")]
        )
        if file_path != "":
            tablesData = []
            textData = ""
            with pdfplumber.open(f"{file_path}") as pdf:
                for page in pdf.pages:
                    tablesData.append(page.extract_table())
                    textData += page.extract_text()
            if len(tablesData[0]) > 1:
                tablesData = sum(tablesData, [])         
            else: 
                pattern = r"^\s*(\d+)\s+(\S+)\s+(.+?)\s+(\d+)\s+(\d+)\s+(\d+)\s*$"
                matches = re.findall(pattern, textData, re.MULTILINE)
                tablesData = [list(matches[0])]
                
            tablesData.insert(0,["№","КАТЕГОРИЯ","ПАРАМЕТРЫ","КОЛ","ЦЕНА","СУММА"])
            return tablesData, textData
        

    
    def _check_frame_key(self, framekey:str):
        if framekey not in self.__frames:
            raise ValueError(f"Frame '{framekey}' not found")
        
    def _validate_numeric_input(self, entry_widget):
        def validate(new_value):
            return new_value.isdigit() or new_value == ""
        validate_cmd = self.__root.register(validate)
        entry_widget.configure(
            validate="key",
            validatecommand=(validate_cmd, '%P')
        )
    
    @staticmethod
    def _on_key_release(event):
        ctrl  = (event.state & 0x4) != 0
        if event.keycode==88 and  ctrl and event.keysym.lower() != "x": 
            event.widget.event_generate("<<Cut>>")

        if event.keycode==86 and  ctrl and event.keysym.lower() != "v": 
            event.widget.event_generate("<<Paste>>")

        if event.keycode==67 and  ctrl and event.keysym.lower() != "c":
            event.widget.event_generate("<<Copy>>")
        
        
        
        
    
        