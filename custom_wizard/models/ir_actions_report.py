from odoo import models

class IrActionsReport(models.Model):
    _inherit = 'ir.actions.report'

    def _render_qweb_pdf(self, report_ref, res_ids=None, data=None):
        context = self.env.context

        # Check if wizard has been confirmed
        if context.get('from_wizard'):
            return super(IrActionsReport, self)._render_qweb_pdf(report_ref, res_ids=res_ids, data=data)
        else:
            # Show the wizard first
            wizard_action = self.env['report.hello.wizard'].action_show_wizard(report_ref, res_ids, data)
            return {
                'type': 'ir.actions.client',
                'tag': 'reload',
                'params': wizard_action
            }
