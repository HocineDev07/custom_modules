from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.report import ReportController
import logging
import json

_logger = logging.getLogger(__name__)


class CustomReportController(ReportController):
    @http.route([
        '/report/<converter>/<reportname>',
        '/report/<converter>/<reportname>/<docids>',
    ], type='http', auth='user', website=True)
    def report_routes(self, reportname, docids=None, converter=None, **data):
        # Add your custom logic here
        # For example, log the report download
        _logger.info(f"User {request.env.user.name} is downloading the report {reportname}")

        # Create a wizard and open it
        wizard = request.env['print.wizard'].create({})
        return request.render('custom_wizard.view_print_wizard_form', {'wizard': wizard})

        # wizard = request.env['print.wizard'].create({})
        # action = wizard.action_show_message()
        # # Return the response as JSON
        # return request.make_response(
        #     json.dumps(action),
        #     headers={'Content-Type': 'application/json'}
        # )

        # Call the super method to continue the normal flow
        # return super(CustomReportController, self).report_routes(reportname, docids=docids, converter=converter, **data)

    @http.route(['/report/download'], type='http', auth="user")
    def report_download(self, data, context=None, token=None):
        _logger.info("---------> downloading...")
        # Get an instance of your model
        return super(CustomReportController, self).report_download(data, context, token)