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
        self.current_page = 1
    
    def add_text(self, x:int, y:int, text_area_width:int = 500, text_align:str="left", paddingX:int = 10, text_gap:int = 15, text:str="", font:str = "Arial", font_size:int = 13):
        self.__canvas.setFont(font, font_size)       
        words = text.split()
        line = 0
        current_line = ""
        for word in words:
            test_line = (current_line + " " + word).strip() if current_line else word
            if self.get_string_width(test_line, font, font_size) > text_area_width:
                if current_line:
                    text_x = self.align_text(x, current_line, text_area_width, text_align, font, font_size, paddingX)
                    self.__canvas.drawString(text_x, y- text_gap * line, current_line)
                    line += 1
                current_line = word
            else:
                current_line = test_line
        if current_line:
            text_x = self.align_text(x, current_line, text_area_width, text_align, font, font_size, paddingX)
            self.__canvas.drawString(text_x, y- text_gap * line, current_line)

    
    def add_image(self, path:str, x:int, y:int, width:int=200, height:int=150):
        self.__canvas.drawImage(path, x, y, width, height, mask="auto")
    
    def add_stroke(self, x:int, y:int, x2:int, y2:int, weight:int = 1):
        self.__canvas.setStrokeColor(black)
        self.__canvas.setLineWidth(weight)
        self.__canvas.line(x, y, x2, y2)
    
    def align_text(self,x:int, text:str, width:int,text_align:str = "left", font:str = "Arial", font_size:int = 10, padding:int = 10):
        match text_align:
            case "left":
                x += padding
            case "center":
                x += width / 2 - self.get_string_width(text, font, font_size) / 2
            case "rigth":
                x += width - padding
        return x

    def add_table(self, x:int, y:int, width:int, height:int = 15, text:str="", font:str = "Arial", font_size:int = 10, text_gap:int = 10, text_align:str = "center"):
        self.__canvas.setLineWidth(1)
        self.__canvas.rect(x, y - height, width, height)
        self.add_text(
                    x,
                    y - font_size,
                    text_area_width= width,
                    text_align= text_align,
                    text= text, 
                    font=font,
                    font_size=font_size,
                    text_gap= text_gap)
    def get_string_width(self, text:str, font:str = "Arial", font_size:int = 10):
        return pdfmetrics.stringWidth(text, font, font_size)
    def save_page(self):
        self.__canvas.save()
        
    def show_page(self):
        self.__canvas.showPage()
            