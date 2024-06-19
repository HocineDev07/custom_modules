from odoo import models, fields, api
import base64


class DirectPrintWizard(models.TransientModel):
    _name = 'direct.print.wizard'
    _description = 'Direct Print Wizard'

    pdf_view = fields.Binary(string='PDF View')
    report_name = fields.Char(string='Report Name')

    @api.model
    def default_get(self, fields):
        res = super(DirectPrintWizard, self).default_get(fields)
        # Add logic to get the report content
        report_name = self.env.context.get('report_name')
        report = self.env['ir.actions.report']._get_report_from_name(report_name)
        if report:
            pdf = report._render_qweb_pdf([self.env.context.get('active_id')])[0]
            res['pdf_view'] = base64.b64encode(pdf)
            res['report_name'] = report_name
        return res
