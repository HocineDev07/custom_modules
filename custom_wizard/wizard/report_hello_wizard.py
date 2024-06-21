from odoo import models, fields, api

class ReportHelloWizard(models.TransientModel):
    _name = 'report.hello.wizard'
    _description = 'Report Hello Wizard'

    message = fields.Char(string='Message', default='Hello!')

    def action_confirm(self):
        report_ref = self.env.context.get('report_ref')
        res_ids = self.env.context.get('res_ids')
        data = self.env.context.get('data')

        # Return the action to download the report
        return {
            'type': 'ir.actions.report',
            'report_name': report_ref,
            'report_type': 'qweb-pdf',
            'report_file': f'{report_ref}.pdf',
            'context': dict(self.env.context, from_wizard=True, res_ids=res_ids, data=data),
        }

    @api.model
    def action_show_wizard(self, report_ref, res_ids, data):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'report.hello.wizard',
            'view_mode': 'form',
            'view_id': self.env.ref('custom_wizard.view_report_hello_wizard_form').id,
            'target': 'new',
            'context': {
                'default_message': 'Hello!',
                'report_ref': report_ref,
                'res_ids': res_ids,
                'data': data,
            },
        }
