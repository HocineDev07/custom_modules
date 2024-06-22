# controllers/report.py
from odoo import http
from odoo.http import request


class ReportController(http.Controller):

    @http.route(['/report/download'], type='http', auth='user')
    def report_download(self, data, context=None, token=None):
        docids = [int(i) for i in docids.split(',') if i]

        # Add context to show the wizard
        context = dict(request.env.context, show_wizard_instead_of_report=True)
        report = request.env['ir.actions.report'].with_context(context)._get_report_from_name(report_name)

        if report:
            return report._render_qweb_pdf(docids, data=data)[0]
