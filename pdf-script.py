#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

# Data to write into PDF
fruit = {
    "strawberries": 1,
    "kiwis": 1,
    "apples": 2,
    "peaches": 3,
    "bananas": 5,
    "mangos": 8,
    "watermelons": 13
}

# Importing styles from the stylesheet to be used in the PDF
styles = getSampleStyleSheet()

# This code is used to create the PDF File
report = SimpleDocTemplate("pdf/report.pdf")

# Setting the title of the PDF report
report_title = Paragraph("A list of fruits I enjoy", styles["h1"])
report.build([report_title])

# Initializing Table for PDF
table_data = []

# Writing data to Table
for k,v in fruit.items():
    table_data.append([k, v])

report_table = Table(data=table_data)
report.build([report_title, report_table])