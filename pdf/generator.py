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
    
    def add_text(self, x:int, y:int, text_area_width:int, text_align:str="left", text:str="", font:str = "Arial", font_size:int = 13):
        text_x = x
        match text_align:
            case "left":
                text_x += 10
            case "center":
                text_x += text_area_width / 2 - self.get_string_width(text, font, font_size) / 2
            case "rigth":
                text_x += text_area_width - 10
                
        
        self.__canvas.setFont(font, font_size)
        self.__canvas.drawString(text_x, y, text)
    
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
            