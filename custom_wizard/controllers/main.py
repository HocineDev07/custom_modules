# custom_report/controllers/main.py
from odoo import http
from odoo.http import content_disposition, request
import json
import base64
import logging
import werkzeug.exceptions
from werkzeug.urls import url_parse

from odoo.tools.misc import html_escape


_logger = logging.getLogger(__name__)


class CustomReportController(http.Controller):
    @http.route('/report/open_wizard', type='json', auth='user')
    def open_wizard(self, data, context=None):
        print("context-------------------> ", context)
        request_content = json.loads(data)
        url, report_type = request_content[0], request_content[1]
        report = request.env['ir.actions.report']
        # context = dict(request.env.context)
        pattern = '/report/pdf/' if report_type == 'qweb-pdf' else '/report/text/'
        reportname = url.split(pattern)[1].split('?')[0]

        # Extract the docids if available
        docids = None
        if '/' in reportname:
            reportname, docids = reportname.split('/')
            docids = [int(i) for i in docids.split(',') if i.isdigit()]

        # Load the report context if provided
        # if context:
        #     context = json.loads(context)

        if not docids:
            print("not docids")
            # Particular report:
            data = url_parse(url).decode_query(cls=dict)  # decoding the args represented in JSON
            if 'context' in data:
                print("context in data")
                context, data_context = json.loads(context or '{}'), json.loads(data.pop('context'))
                context = json.dumps({**context, **data_context})


        # Determine the converter type and generate the report content
        if report_type == 'qweb-pdf':
            # pdf_content = report.with_context(context)._render_qweb_pdf(reportname, docids)[0]
            pdf_content = report.with_context(context)._render_qweb_pdf(reportname, docids, data=data)[0]
            report_binary = base64.b64encode(pdf_content)
            extension = 'pdf'
        elif report_type == 'qweb-html':
            html_content = report.with_context(context)._render_qweb_html(reportname, docids)[0]
            report_binary = base64.b64encode(html_content.encode())
            extension = 'html'
        elif report_type == 'qweb-text':
            text_content = report.with_context(context)._render_qweb_text(reportname, docids)[0]
            report_binary = base64.b64encode(text_content.encode())
            extension = 'txt'
        else:
            return {'success': False, 'message': f'Unsupported report type: {report_type}'}

        # Create the wizard record
        wizard = request.env['print.wizard'].create({
            'report_data': report_binary,
            'report_name': f'report.{extension}',
        })

        # Return a response indicating success and the wizard ID
        return {
            'success': True,
            'message': 'Wizard opened successfully',
            'wizard_id': wizard.id,
        }
























# class CustomReportController(http.Controller):
#
#     @http.route(['/report/open_wizard'], type='json', auth="user")
#     def report_open_wizard(self, data, context=None, token=None):
#         print("--------- /report/open_wizard Called")
#         try:
#             # Ensure data is parsed correctly
#             request_content = json.loads(data)
#             url, report_type = request_content[0], request_content[1]
#             report_name = '???'
#             print("--------- report_type ", report_type)
#
#             # Ensure context is a dictionary
#             if context:
#                 print("--------- context loaded ")
#                 context = json.loads(context)
#             else:
#                 context = {}
#
#             # Determine the report pattern based on type
#             if report_type == 'qweb-pdf':
#                 pattern = '/report/pdf/'
#             elif report_type == 'qweb-text':
#                 pattern = '/report/text/'
#             else:
#                 raise ValueError("Unsupported report type: {}".format(report_type))
#
#             # Extract report name from the URL
#             if pattern in url:
#                 try:
#                     report_name = url.split(pattern)[1].split('?')[0]
#                     print("report name: ", report_name)
#                 except IndexError:
#                     raise ValueError("URL format is incorrect or pattern not found: {}".format(url))
#             else:
#                 raise ValueError("Pattern not found in URL: {}".format(url))
#
#             # Split docids if present
#             docids = None
#             if '/' in report_name:
#                 report_name, docids = report_name.split('/')
#                 if docids:
#                     docids = [int(x) for x in docids.split(",") if x.isdigit()]
#
#             # Ensure report_name is a string
#             if isinstance(report_name, list):
#                 report_name = report_name[0]  # Extract the first element if it's a list
#
#             # Search for the report using the correct method
#             report = request.env['ir.actions.report']._get_report_from_name(report_name)
#             print("report: ", report)
#
#             # Ensure context is passed correctly
#             if not isinstance(context, dict):
#                 raise ValueError("Context must be a dictionary")
#
#             pdf = report.with_context(context)._render_qweb_pdf(docids or [])[0]
#             pdf_base64 = base64.b64encode(pdf).decode('utf-8')
#
#             wizard = request.env['print.wizard'].create({
#                 'report_data': pdf_base64,
#                 'report_name': report.name
#             })
#
#             return {
#                 'type': 'ir.actions.act_window',
#                 'res_model': 'print.wizard',
#                 'view_mode': 'form',
#                 'res_id': wizard.id,
#                 'target': 'new'
#             }
#         except Exception as e:
#             _logger.warning("Error while generating report for wizard", exc_info=True)
#             return {'error': str(e)}
