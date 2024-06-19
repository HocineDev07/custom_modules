# controllers/main.py
from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)


class ReportController(http.Controller):

    @http.route(['/report/pdf/<string:reportname>/<string:docids>'], type='http', auth='user', website=True)
    def report_routes(self, reportname, docids=None, **data):
        _logger.info("Custom ReportController triggered.")

        # Parse the docids from the URL
        if docids:
            docids = [int(i) for i in docids.split(',') if i.isdigit()]
            _logger.info(f"Document IDs: {docids}")
        else:
            docids = []
            _logger.info("No document IDs provided.")

        # Get the report model
        report_sudo = request.env['ir.actions.report']._get_report_from_name(reportname)
        _logger.info(f"Report Model: {report_sudo}")

        # Generate the PDF content
        pdf_content, _ = report_sudo.with_context(active_ids=docids)._render_qweb_pdf(reportname, docids, data=data)
        _logger.info("PDF content generated.")

        # Create the PDF viewer action
        action = report_sudo.get_pdf_viewer_action(pdf_content)
        _logger.info(f"PDF viewer action: {action}")

        # Return the action to open the PDF viewer wizard
        action_window = request.env['ir.actions.act_window'].search(
            [('res_model', '=', 'pdf.viewer'), ('res_id', '=', action['res_id'])]).read()[0]
        _logger.info(f"Action window: {action_window}")
        return action_window
