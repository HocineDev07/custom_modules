from odoo import models, api, _
from odoo.exceptions import UserError
import base64


class ReportCustomization(models.AbstractModel):
    _inherit = 'ir.actions.report'

    def _get_report_from_name(self, report_name):
        report = super(ReportCustomization, self)._get_report_from_name(report_name)
        # Force all reports to use qweb-html
        report.report_type = 'qweb-html'
        return report

    def _render_qweb_pdf(self, report_ref, docids, data=None):
        # Render the report
        html = self._render_qweb_html(report_ref, docids, data=data)
        return self._convert_to_pdf(html)

    def _convert_to_pdf(self, html):
        # You can use any HTML to PDF conversion library, e.g., wkhtmltopdf
        # Here we'll just encode the HTML for simplicity
        pdf_content = base64.b64encode(html[0]).decode('utf-8')
        return pdf_content

    @api.model
    def _create_pdf_viewer(self, report_name, docids, data=None):
        report = self._get_report_from_name(action['report_name'])
        pdf_content = self._render_qweb_pdf(report, docids)
        print('pdf_content', pdf_content)
        wizard = self.env['pdf.viewer'].create({
            'pdf_view': pdf_content,
            'name': 'report.pdf'
        })
        return {
            'name': _('PDF Viewer'),
            'type': 'ir.actions.act_window',
            'res_model': 'pdf.viewer',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': wizard.id,
            'target': 'new',
        }

    def _render_qweb_html(self, report_ref, docids, data=None):
        # Call the super method with correct arguments
        return super(ReportCustomization, self)._render_qweb_html(report_ref, docids, data)

    def _render(self, report_ref, docids, data=None):
        action = self.env.context.get('params', {}).get('action', {})
        return self._create_pdf_viewer(action['report_name'], docids, data)

    # def _get_report_from_name(self, report_name):
    #     # Override to get the report
    #     report = super(ReportCustomization, self)._get_report_from_name(report_name)
    #     print("report type-----> " + report.report_type)
    #     if report.report_type == 'qweb-pdf':
    #         report.report_type = 'qweb-html'
    #     return report
    #
    # def _render_qweb_pdf(self, report_ref, res_ids=None, data=None):
    #     # This method should now return HTML
    #     return self._render_qweb_html(report_ref, res_ids=res_ids, data=data)
    #
    # def _render_qweb_html(self, report_ref, res_ids=None, data=None):
    #     # Call the super method
    #     return super(ReportCustomization, self)._render_qweb_html(report_ref, res_ids, data=data)


