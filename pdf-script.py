#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()
report = SimpleDocTemplate("pdf/report.pdf")
report_title = Paragraph("A list of fruits I enjoy", styles["h1"])
report.build([report_title])

fruit = {
    "strawberries": 1,
    "kiwis": 1,
    "apples": 2,
    "peaches": 3,
    "bananas": 5,
    "mangos": 8,
    "watermelons": 13
}

