# models/print_wizard.py
from odoo import models, fields, api


class PrintWizard(models.TransientModel):
    _name = 'print.wizard'
    _description = 'Print Wizard'

    message = fields.Char(string='Message', default='Hello')

    @api.model
    def action_show_message(self):
        print('--------------')
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'print.wizard',
            'view_mode': 'form',
            'view_id': self.env.ref('custom_wizard.view_print_wizard_form').id,
            'target': 'new',
            'res_id': self.id,
        }
