from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)


class CustomReportController(http.Controller):
    @http.route('/custom_wizard/trigger_wizard', type='json', auth='user')
    def trigger_wizard(self):
        wizard = request.env['print.wizard'].create({})
        return wizard.action_show_message()
