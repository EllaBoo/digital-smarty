"""PDF Report Generator"""
import logging
from pathlib import Path
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

logger = logging.getLogger(__name__)

async def generate_pdf_report(output_path: str, analysis: str, diagnostics: str, transcript: str, duration: float, speakers_count: int, language: str = "ru", expertise: dict = None):
    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(output_path, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm, topMargin=20*mm, bottomMargin=20*mm)
    story = []
    
    story.append(Paragraph("Digital Smarty Report", styles["Title"]))
    story.append(Spacer(1, 10*mm))
    
    for line in analysis.split("\n"):
        if line.strip():
            story.append(Paragraph(line, styles["Normal"]))
            story.append(Spacer(1, 2*mm))
    
    doc.build(story)
    logger.info(f"PDF generated: {output_path}")
