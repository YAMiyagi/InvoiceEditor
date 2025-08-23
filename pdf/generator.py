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
    
    def add_text(self, x:int, y:int, text_area_width:int, text_align:str="left", padding:int = 10, text_gap:int = 15, text:str="", font:str = "Arial", font_size:int = 13):
        self.__canvas.setFont(font, font_size)       
        words = text.split()
        line = 0
        current_line = ""
        for word in words:
            test_line = (current_line + " " + word).strip() if current_line else word
            if pdfmetrics.stringWidth(test_line, font, font_size) > text_area_width:
                if current_line:
                    text_x = self.align_text(x, current_line, text_area_width, text_align, font, font_size, padding)
                    self.__canvas.drawString(text_x, y - text_gap * line, current_line)
                    line += 1
                current_line = word
            else:
                current_line = test_line
        if current_line:
            text_x = self.align_text(x, current_line, text_area_width, text_align, font, font_size, padding)
            self.__canvas.drawString(text_x, y - text_gap * line, current_line)

    
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
                x += width / 2 - pdfmetrics.stringWidth(text, font, font_size) / 2
            case "rigth":
                x += width - padding
        return x
        
    def add_product_table(self, data:list, x:int, y:int, col_widths:list = None,rect_height:int = 15, font:str = "Arial", font_size:int = 10, summ:str = "", qty:str = ""):
        thick_font = "Arial-Thick"
        y_offset = 0
        height = 0
        if col_widths is None:
            col_widths = [100] * len(data[0])
        for row in data:
            height = rect_height * math.ceil(pdfmetrics.stringWidth(row[2], font, font_size) / (col_widths[2] - font_size))
            if y - y_offset - height < 40: self.current_page += 1; self.__canvas.showPage(); y_offset = 0; y = 800
            for j, cell in enumerate(row):
                self.add_table(
                    x + sum(col_widths[:j]),
                    y - y_offset,
                    width=col_widths[j],
                    height=height,
                    text=cell,
                    font=font,
                    font_size=font_size,
                )
            y_offset += height
        self.add_table(
            x + sum(col_widths[:3]),
            y - y_offset,
            width=col_widths[3],
            text=qty,
            font=thick_font,
            font_size=font_size
        )
        self.add_table(
            x + sum(col_widths[:-1]),
            y - y_offset,
            width=col_widths[-1],
            text=summ,
            font=thick_font,
            font_size=font_size,
        )
        self.add_text(
            x + sum(col_widths[:2]) - 30,
            y - y_offset - 10,
            text_area_width= col_widths[2],
            text_align= "rigth",
            text= "ИТОГО:" ,
            font=thick_font,
            font_size=font_size,
        )

    def add_table(self, x:int, y:int, width:int, height:int = 15, text:str="", font:str = "Arial", font_size:int = 10):
        self.__canvas.rect(x, y - height, width, height)
        self.add_text(
                    x,
                    y - font_size,
                    text_area_width= width,
                    text_align= "center",
                    text= text, 
                    font=font,
                    font_size=font_size,
                    text_gap= 10)
    def save_page(self):
        self.__canvas.save()
        
    def show_page(self):
        self.__canvas.showPage()
            