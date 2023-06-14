#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab_platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

report = SimpleDocTemplate("pdf/report.pdf")
styles = getSampleStyleSheet()

fruit = {
    "elderberries": 1,
    "figs": 1,
    "apples": 2,
    "peaches": 3,
    "bananas": 5,
    "mangos": 8,
    "watermelons": 13
}

