from odoo import http
from odoo.http import request


class DirectPrintController(http.Controller):

    @http.route('/direct_print_2/open_report_wizard', type='http', auth='user')
    def open_report_wizard(self, **kw):
        report_name = kw.get('report_name')
        active_id = kw.get('active_id')

        # Your logic to open the report wizard here
        # Example:
        # return request.render('direct_print_2.report_wizard_template', {
        #     'report_name': report_name,
        #     'active_id': active_id,
        # })

        return request.make_response("Report Wizard Opened Successfully")
