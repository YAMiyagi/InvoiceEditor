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
    
    def add_string(self, x:int, y:int, text:str, font:str = "Arial", font_size:int = 13):
        self.__canvas.setFont(font, font_size)
        self.__canvas.drawString(x, y, text)
    
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
            for j, cell in enumerate(row):
                self.__canvas.rect(x + sum(col_widths[:j]), y - i * 15, col_widths[j], 15)
                self.add_string(x + sum(col_widths[:j]) + col_widths[j] / 2 - pdfmetrics.stringWidth(cell, 'Arial', 10) / 2, y - i * 15 + 5, cell, font="Arial", font_size=10)
    
    def get_string_width(self, text:str, font:str = "Arial", font_size:int = 13):
        return self.__canvas.stringWidth(text, font, font_size)
    
    def save_page(self):
        self.__canvas.save()
        
    def show_page(self):
        self.__canvas.showPage()
            