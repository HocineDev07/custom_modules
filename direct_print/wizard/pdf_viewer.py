from odoo import models, fields, api


class PdfViewer(models.TransientModel):
    _name = 'pdf.viewer'
    _description = 'PDF Viewer'

    pdf_view = fields.Binary(string="PDF View")


