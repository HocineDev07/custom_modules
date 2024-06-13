from odoo import models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def open_wizard_action(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'PDF Viewer',
            'res_model': 'pdf.viewer',
            'view_mode': 'form',
            'view_id': self.env.ref('direct_print.pdf_viewer_view').id,
            'target': 'new',
            # 'res_id': pdf_viewer.id,
        }
