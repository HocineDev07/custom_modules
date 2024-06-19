# models/report.py
from odoo import models, api, tools
import base64
import logging

_logger = logging.getLogger(__name__)

class Report(models.AbstractModel):
    _inherit = 'ir.actions.report'

    @api.model
    def _render_qweb_pdf(self, report_ref, res_ids=None, data=None):
        # Call the super method to get the original PDF content and content type
        pdf_content, content_type = super(Report, self)._render_qweb_pdf(report_ref, res_ids, data)

        # Here you can customize the behavior, e.g., logging or additional processing
        _logger.info("Custom PDF rendering for report: %s", report_ref)

        # Return the PDF content and content type
        return pdf_content, content_type

    @api.model
    def get_pdf_viewer_action(self, pdf_content):
        # Create a record in pdf.viewer model to store the PDF content
        pdf_viewer = self.env['pdf.viewer'].create({
            'pdf_view': base64.b64encode(pdf_content)
        })
        # Return an action to open the PDF viewer wizard
        return {
            'type': 'ir.actions.act_window',
            'name': 'PDF Viewer',
            'res_model': 'pdf.viewer',
            'view_mode': 'form',
            'view_id': self.env.ref('direct_print.pdf_viewer_view').id,
            'target': 'new',
            'res_id': pdf_viewer.id,
        }
