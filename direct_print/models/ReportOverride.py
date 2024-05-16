from odoo import models, api

class ReportOverride(models.Model):
    _inherit = 'ir.actions.report'

    @api.model
    def render_qweb_pdf(self, res_ids=None, data=None):
        # Call the original render_qweb_pdf method
        pdf_content, _ = super(ReportOverride, self).render_qweb_pdf(res_ids=res_ids, data=data)

        # Open your custom wizard action and pass the PDF content
        action = self.env.ref('direct_print.action_pdf_viewer_view').read()[0]
        action['context'] = {'default_pdf_view': pdf_content}
        return action
