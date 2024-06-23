# models/report_action_override.py
from odoo import models

class ReportActionOverride(models.AbstractModel):
    _inherit = 'ir.actions.report'

    def _render_qweb_pdf(self, res_ids=None, data=None):

        if self.env.context.get('show_wizard_instead_of_report', False):
            wizard = self.env['print.wizard'].create({})
            return wizard.action_show_message()
        else:
            return super(ReportActionOverride, self)._render_qweb_pdf(res_ids, data)

    def _get_report_from_name(self, report_name):
        report = super(ReportActionOverride, self)._get_report_from_name(report_name)
        if report:
            report._render_qweb_pdf = self._render_qweb_pdf
        return report
