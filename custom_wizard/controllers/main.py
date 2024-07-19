# custom_report/controllers/main.py
from odoo import http
from odoo.http import request
import json
import base64


class CustomReportController(http.Controller):

    @http.route(['/report/open_wizard'], type='json', auth="user")
    def report_open_wizard(self, data, token=None):
        print("--------- /report/open_wizard Called")
        data = json.loads(data)
        url, report_type = data
        report = request.env['ir.actions.report']._get_report_from_name(report_name)
        docids = request.context.get('active_ids')
        pdf = report.with_context(request.context)._render_qweb_pdf(docids)[0]
        pdf_base64 = base64.b64encode(pdf)

        wizard = request.env['print.wizard'].create({
            'report_data': pdf_base64,
            'report_name': report.name
        })

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'print.wizard',
            'view_mode': 'form',
            'res_id': wizard.id,
            'target': 'new'
        }
