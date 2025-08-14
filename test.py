from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import math

pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))

cell = "DSasdjlj aslkjdlksa a skdjalks jdakls  sdasdas ds daccss adjklasjd lkasj ldk jalsj djaslkjdlksjakdj aslkd jlkasj dlkajs lkdjaslk jdlkjas lkdj laskjdlkasj d"

max_width = 230
font_name = "Arial"
font_size = 10


print(math.ceil(pdfmetrics.stringWidth(cell, font_name, font_size) / max_width))
# words = cell.split()
# lines = []
# current_line = ""

# for word in words:
#     test_line = (current_line + " " + word).strip() if current_line else word
#     if pdfmetrics.stringWidth(test_line, font_name, font_size) > max_width:
#         if current_line:
#             lines.append(current_line)
#         current_line = word
#     else:
#         current_line = test_line
# if current_line:
#     lines.append(current_line)

# print(lines)