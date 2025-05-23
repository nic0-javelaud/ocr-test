# importing modules
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import B6

w, h = B6

# initializing variables with values
fileName = 'sample.pdf'
documentTitle = 'sample'
title = 'PAYMENT DUE'
subTitle = 'The largest thing now!!'
textLines = [
    'Technology makes us aware of',
    'the world around us.',
]
image = '../../../assets/images/signature.png'

supplier = {
    "name": 'TechNova',
    "address" : [
        '1912 Harvest Lane',
        'New York, NY 12210'
    ]
}
invoice = {
    "id": 'US-006',
    "date": '26/02/2025',
    "due_date": '18/03/2025',
    "amount": '154.06',
    "tax": '9.06'
}

# creating a pdf object
pdf = canvas.Canvas(fileName, pagesize=B6)

# setting the title of the document
pdf.setTitle(f"{invoice['id']}.pdf")

# registering a external font in python
# pdfmetrics.registerFont(
#     TTFont('abc', 'SakBunderan.ttf')
# # )˜

# creating the title by setting it's font 
# and putting it on the canvas
# pdf.setFont('abc', 36)
y_z = 64
pdf.setFont("Helvetica-Bold", 24)
pdf.drawCentredString(w /2 , h - y_z, f"INVOICE # {invoice['id']}")

# creating the subtitle by setting it's font, 
# colour and putting it on the canvas
y_z = y_z + 36
pdf.setFont("Helvetica-Bold", 14)
pdf.drawCentredString(w /2 , h - y_z, supplier['name'])

y_z = y_z + 20
pdf.setFont("Helvetica", 12)
pdf.drawCentredString(w /2 , h - y_z, supplier['address'][0])
y_z = y_z + 16
pdf.drawCentredString(w /2 , h - y_z, supplier['address'][1])

y_z = y_z + 20 
pdf.line(24, h - y_z, w - 24, h - y_z)

y_z = y_z + 24
pdf.setFont("Helvetica-Bold", 12)
pdf.drawString(24, h - y_z, 'QTY')
pdf.drawString(60, h - y_z, 'DESCRIPTION')
pdf.drawRightString(w - 88, h - y_z, 'UNIT PRICE')
pdf.drawRightString(w-24, h - y_z, 'AMOUNT')

y_z = y_z + 24
pdf.setFont("Helvetica", 12)
pdf.drawString(24, h - y_z, '2')
pdf.drawString(60, h - y_z, 'Front and rear brake cables')
pdf.drawRightString(w - 88, h - y_z, '60.00')
pdf.drawRightString(w-24, h - y_z, '120.00')

y_z = y_z + 24
pdf.setFont("Helvetica", 12)
pdf.drawString(24, h - y_z, '2')
pdf.drawString(60, h - y_z, 'Front and rear brake cables')
pdf.drawRightString(w - 88, h - y_z, '60.00')
pdf.drawRightString(w-24, h - y_z, '120.00')

y_z = y_z + 24
pdf.setFont("Helvetica", 12)
pdf.drawString(24, h - y_z, '2')
pdf.drawString(60, h - y_z, 'Front and rear brake cables')
pdf.drawRightString(w - 88, h - y_z, '60.00')
pdf.drawRightString(w-24, h - y_z, '120.00')

y_z = y_z + 32
pdf.drawRightString(w - 88, h - y_z, 'Subtotal')
pdf.drawRightString(w - 24, h - y_z, '292.00')

y_z = y_z + 24
pdf.drawRightString(w - 88, h - y_z, 'Sales tax (6.25%)')
pdf.drawRightString(w - 24, h - y_z, '18.25')

y_z = y_z + 20 
pdf.line(24, h - y_z, w - 24, h - y_z)

y_z = y_z + 24
pdf.setFont("Helvetica-Bold", 18)
pdf.drawString(24, h - y_z, 'Total Amount')
pdf.drawRightString(w - 24, h - y_z, "$310.25")

y_z = y_z + 32
pdf.setFont("Helvetica", 12)
pdf.drawCentredString(w /2 , h - y_z, f"Date: {invoice['date']}")
y_z = y_z + 16
pdf.drawCentredString(w /2 , h - y_z, f"Due Date: {invoice['due_date']}")

pdf.setFont("Helvetica-Bold", 14)
pdf.drawCentredString(w /2 , 48, f"Thank you")
pdf.drawCentredString(w /2 , 24, f"your business with {supplier['name']}")


# saving the pdf
pdf.save()