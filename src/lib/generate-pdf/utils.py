# importing modules
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors

w, h = letter

# initializing variables with values
fileName = 'sample.pdf'
documentTitle = 'sample'
title = 'PAYMENT DUE'
subTitle = 'The largest thing now!!'
textLines = [
    'Technology makes us aware of',
    'the world around us.',
]
image = './signature.png'

supplier = {
    "name": 'TechNova',
    "address" : [
        '1912 Harvest Lane',
        'New York, NY 12210'
    ]
}
invoice = {
    "id": 'US-002',
    "date": '26/02/2025',
    "due_date": '18/03/2025',
    "amount": '154.06',
    "tax": '9.06'
}

# creating a pdf object
pdf = canvas.Canvas(fileName, pagesize=letter)

# setting the title of the document
pdf.setTitle(documentTitle)

# registering a external font in python
# pdfmetrics.registerFont(
#     TTFont('abc', 'SakBunderan.ttf')
# # )˜

# creating the title by setting it's font 
# and putting it on the canvas
# pdf.setFont('abc', 36)
pdf.setFont("Helvetica-Bold", 24)
pdf.drawRightString(w - 64, h - 128, title)

# # creating the subtitle by setting it's font, 
# # colour and putting it on the canvas
# pdf.setFillColorRGB(0, 0, 255)
pdf.setFont("Helvetica-Bold", 18)
pdf.drawString(64, h - 128, supplier['name'])

# # creating a multiline text using 
# # textline and for loop
text = pdf.beginText(72, h - 148)
text.setFont("Helvetica", 12)
for line in supplier['address']:
    text.textLine(line)
pdf.drawText(text)

pdf.setFont("Helvetica-Bold", 14)
pdf.drawString(64, h - 220, 'BILL TO')
pdf.drawString(w - 248, h - 220, 'INVOICE #')
pdf.drawString(w - 248, h - 244, 'DATE')
pdf.drawString(w - 248, h - 268, 'DUE DATE')

pdf.setFont("Helvetica", 12)
pdf.drawString(72, h - 236, 'Jonh Smith')
pdf.drawString(72, h - 252, '2 Court Square')
pdf.drawString(72, h - 268, 'New York, NY 12210')

pdf.drawRightString(w - 64, h - 220, "US-002")
pdf.drawRightString(w - 64, h - 244, "18/02/2025")
pdf.drawRightString(w - 64, h - 268, "14/03/2025")

# drawing a line
y_z = 290
pdf.line(64, h - y_z, w - 64, h - y_z)

y_z = y_z + 24 + 12
pdf.setFont("Helvetica-Bold", 26)
pdf.drawString(64, h - y_z, 'Total Amount')
pdf.drawRightString(w - 64, h - y_z, "$154.06")

y_z = y_z + 18
pdf.line(64, h - y_z, w - 64, h - y_z)

y_z = y_z + 36
pdf.setFont("Helvetica-Bold", 14)
pdf.drawString(64, h - y_z, 'QTY')
pdf.drawString(112, h - y_z, 'DESCRIPTION')
pdf.drawRightString(w - 148, h - y_z, 'UNIT PRICE')
pdf.drawRightString(w-64, h - y_z, 'AMOUNT')

y_z = y_z + 22
pdf.setFont("Helvetica", 12)
pdf.drawString(64, h - y_z, '2')
pdf.drawString(112, h - y_z, 'Front and rear brake cables')
pdf.drawRightString(w - 148, h - y_z, '60.00')
pdf.drawRightString(w-64, h - y_z, '120.00')

y_z = y_z + 16
pdf.drawString(64, h - y_z, '5')
pdf.drawString(112, h - y_z, 'New set of pedals')
pdf.drawRightString(w-148, h - y_z, '15.00')
pdf.drawRightString(w-64, h - y_z, '60.00')

y_z = y_z + 16
pdf.drawString(64, h - y_z, '1')
pdf.drawString(112, h - y_z, 'Frame')
pdf.drawRightString(w - 148, h - y_z, '112.00')
pdf.drawRightString(w - 64, h - y_z, '112.00')

y_z = y_z + 32
pdf.drawRightString(w - 148, h - y_z, 'Subtotal')
pdf.drawRightString(w - 64, h - y_z, '292.00')
y_z = y_z + 16
pdf.drawRightString(w - 148, h - y_z, 'Sales tax (6.25%)')
pdf.drawRightString(w - 64, h - y_z, '18.25')
# # drawing a image at the 
# # specified (x.y) position
y_z = y_z + 124
pdf.drawInlineImage(image, w - 196, h - y_z)

# saving the pdf
pdf.save()