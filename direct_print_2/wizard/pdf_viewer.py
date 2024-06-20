from odoo import models, fields


class PdfViewer(models.TransientModel):
    _name = 'pdf.viewer'
    _description = 'Pdf Viewer'

    pdf_view = fields.Binary('PDF View')
    name = fields.Char('File Name', readonly=True)
