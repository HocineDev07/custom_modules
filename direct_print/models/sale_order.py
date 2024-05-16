from odoo import models,fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    saved_quotation = fields.Binary(string='Saved Quotation', readonly=True)


class ReportSaleOrder(models.Model):
    _inherit = 'ir.actions.report'

    @api.model
    def render_qweb_pdf(self, docids, data=None):
        res = super(ReportSaleOrder, self).render_qweb_pdf(docids, data=data)

        # Retrieve the sale order
        sale_order = self.env['sale.order'].browse(docids[0])

        # Update the saved_quotation field with the generated PDF
        sale_order.saved_quotation = res[0]

        return res
