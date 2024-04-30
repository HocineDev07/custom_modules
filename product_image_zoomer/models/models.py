# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class product_image_zoom(models.Model):
#     _name = 'product_image_zoom.product_image_zoom'
#     _description = 'product_image_zoom.product_image_zoom'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

