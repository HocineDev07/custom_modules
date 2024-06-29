# models/print_wizard.py
from odoo import models, fields


class PrintWizard(models.TransientModel):
    _name = 'print.wizard'
    _description = 'Print Wizard'

    message = fields.Char(string='Message', default='Hello')

    def action_show_message(self):
        return {
            'name': 'Message Wizard',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'print.wizard',
            'target': 'new',
            'res_id': self.id,
        }
