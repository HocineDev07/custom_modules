from odoo import models

class ReportCustomization(models.AbstractModel):
    _inherit = 'ir.actions.report'

    def _get_report_from_name(self, report_name):
        report = super(ReportCustomization, self)._get_report_from_name(report_name)
        if report.report_type == 'qweb-pdf':
            report.report_type = 'qweb-html'
        return report

    def _render_qweb_pdf(self, report_ref, res_ids=None, data=None):
        # Override to render HTML instead of PDF
        return self._render_qweb_html(report_ref, res_ids=res_ids, data=data)

    def _render_qweb_html(self, report_ref, docids, data=None):
        # Call the super method with correct arguments
        return super(ReportCustomization, self)._render_qweb_html(report_ref, docids, data=data)
