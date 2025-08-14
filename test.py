from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))

cell = "DSasdjlj aslkjdlksa a skdjalks jdakls  sdasdas ds daccss"

print(pdfmetrics.stringWidth(cell, "Arial", 10))

strArr = cell.split(" ")
text = ""
print(strArr)
textLen = 0

for i, txt in enumerate(strArr):
    textLen += pdfmetrics.stringWidth(txt + " ", "Arial", 10)
    if(textLen > 230): break
    text += txt + " "
print(text)