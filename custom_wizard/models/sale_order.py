from odoo import models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'Sale order inherited'

    def open_wizard(self):
        wizard = self.env['print.wizard'].create({})
        return wizard.action_show_message()
