#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

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
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
table_data = []

# Initializing pie & variables
report_pie = Pie(width=3*1, height=3*1)
report_pie.data = []
report_pie.labels = []

# Drawing pie chart
for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)

report_chart = Drawing()
report_chart.add(report_pie)

# Writing data to Table
for k,v in fruit.items():
    table_data.append([k, v])

report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
report.build([report_title, report_table, report_chart])