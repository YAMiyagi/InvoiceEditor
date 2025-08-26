import math
from reportlab.pdfbase import pdfmetrics
import re



def add_product_tables(doc, x:int=50, y:int=550, col_widths:list=None, rect_height:int=11, font_size:int=8, tablesData:list=None, qty:str=None, summ:str=None):
        thick_font = "Arial-Thick"
        font = "Arial"
        col_widths=[30, 100, 200, 30, 70, 70]
        y_offset = 0
        height = 0
        print("table")
        if col_widths is None:
            col_widths = [100] * len(tablesData[0])
        for row in tablesData:
            height = rect_height * math.ceil(pdfmetrics.stringWidth(row[2], font, font_size) / (col_widths[2] - font_size))
            if y - y_offset - height < 40: doc.current_page += 1; doc.show_page(); y_offset = 0; y = 800
            for j, cell in enumerate(row):
                doc.add_table(
                    x + sum(col_widths[:j]),
                    y - y_offset,
                    width=col_widths[j],
                    height=height,
                    text=cell,
                    font=font,
                    font_size=font_size,
                )
            y_offset += height
        doc.add_table(
            x + sum(col_widths[:3]),
            y - y_offset,
            width=col_widths[3],
            text=qty,
            font=thick_font,
            font_size=font_size
        )
        doc.add_table(
            x + sum(col_widths[:-1]),
            y - y_offset,
            width=col_widths[-1],
            text=summ,
            font=thick_font,
            font_size=font_size,
        )
        doc.add_text(
            x + sum(col_widths[:2]) - 30,
            y - y_offset - 10,
            text_area_width= col_widths[2],
            text_align= "rigth",
            text= "ИТОГО:" ,
            font=thick_font,
            font_size=font_size,
        )
