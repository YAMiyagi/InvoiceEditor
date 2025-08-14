import math

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import black

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Arial-Thick', "data/fonts/G_ari_bd.TTF"))
pdfmetrics.registerFont(TTFont('Arial', 'data/fonts/arial.ttf'))

class DocGenerator():
    def __init__(self, path:str):
        self.__canvas = canvas.Canvas(f"{path}.pdf", pagesize=A4)
    
    def add_text(self, x:int, y:int, text_area_width:int, text_align:str="left", padding:int = 10, text_gap:int = 15, text:str="", font:str = "Arial", font_size:int = 13):
        text_x = x
        self.__canvas.setFont(font, font_size)
        # match text_align:
        #     case "left":
        #         text_x += padding
        #     case "center":
        #         text_x += text_area_width / 2 - self.get_string_width(text, font, font_size) / 2
        #     case "rigth":
        #         text_x += text_area_width - padding
                
        words = text.split()
        line = 0
        current_line = ""

        for word in words:
            test_line = (current_line + " " + word).strip() if current_line else word
            if pdfmetrics.stringWidth(test_line, font, font_size) > text_area_width:
                if current_line:
                    print(f"Drawing text: {current_line} at position ({text_x}, {y * line})")
                    self.__canvas.drawString(text_x, y - text_gap * line, current_line)
                    line += 1
                current_line = word
            else:
                current_line = test_line
        if current_line:
            self.__canvas.drawString(text_x, y - text_gap * line, current_line)

    
    def add_image(self, path:str, x:int, y:int, width:int=200, height:int=150):
        self.__canvas.drawImage(path, x, y, width, height, mask="auto")
    
    def add_stroke(self, x:int, y:int, x2:int, y2:int, weight:int = 1):
        self.__canvas.setStrokeColor(black)
        self.__canvas.setLineWidth(weight)
        self.__canvas.line(x, y, x2, y2)
        
    def add_table(self, data:list, x:int, y:int, col_widths:list = None):
        if col_widths is None:
            col_widths = [100] * len(data[0])
        for i, row in enumerate(data):
            height = 15 * math.ceil(pdfmetrics.stringWidth(row[2], 'Arial', 10) / col_widths[2])
            for j, cell in enumerate(row):
                
                self.__canvas.rect(x + sum(col_widths[:j]), y - i * 15, col_widths[j], height)
                self.add_text(
                    x + sum(col_widths[:j]),
                    y - i * 15 + 5,
                    text_area_width= col_widths[j],
                    text_align= "center",
                    text= cell, 
                    font_size=10)
    
    def get_string_width(self, text:str, font:str = "Arial", font_size:int = 13):
        return self.__canvas.stringWidth(text, font, font_size)
    
    def save_page(self):
        self.__canvas.save()
        
    def show_page(self):
        self.__canvas.showPage()
            