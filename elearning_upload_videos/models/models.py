# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class elearning_upload_videos(models.Model):
#     _name = 'elearning_upload_videos.elearning_upload_videos'
#     _description = 'elearning_upload_videos.elearning_upload_videos'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
