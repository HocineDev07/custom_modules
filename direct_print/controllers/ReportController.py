# controllers/main.py
from odoo import http
from odoo.http import request


class ReportController(http.Controller):

    @http.route(['/report/pdf/<string:reportname>'], type='http', auth='user', website=True)
    def report_routes(self, reportname, docids=None, converter=None, **data):
        # Get the report model
        report_sudo = request.env['ir.actions.report']._get_report_from_name(reportname)
        print("--------> 00")
        # Generate the PDF content
        pdf_content, _ = report_sudo.with_context(active_ids=docids)._render_qweb_pdf(reportname, docids, data=data)
        print("--------> 10")
        # Create the PDF viewer action
        action = report_sudo.get_pdf_viewer_action(pdf_content)
        print("--------> 11")
        # Return the action to open the PDF viewer wizard
        return request.render(action['view_id'], {'pdf_view': pdf_content})
