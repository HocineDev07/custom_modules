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

        # Fetch the report details
        report_sudo = self._get_report(report_ref)
        print("------> ", report_sudo.model)
        # Check if the model is 'sale.order' to show the wizard
        if report_sudo.model == 'sale.order':
            pdf_viewer = self.env['pdf.viewer'].create({
                'pdf_view': base64.b64encode(pdf_content)
            })
            print("--------------> ", pdf_viewer)
            return {
                'type': 'ir.actions.act_window',
                'name': 'PDF Viewer',
                'res_model': 'pdf.viewer',
                'view_mode': 'form',
                'view_id': self.env.ref('direct_print.pdf_viewer_view', raise_if_not_found=False).id,
                'target': 'new',
                # 'res_id': pdf_viewer.id,
            }

        return pdf_content, content_type
