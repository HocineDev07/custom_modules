# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SlideSlide(models.Model):
    _inherit = "slide.slide"

    upload_video = fields.Binary(string="Upload Video", attachment=True)
    is_local = fields.Boolean(string="Is Local", default=False)

    # Method to handle saving the uploaded video as attachment
    def save_video_as_attachment(self):
        for record in self:
            if record.upload_video:
                # Create an attachment record
                attachment_vals = {
                    'name': 'Video Attachment',  # Name of the attachment
                    'res_id': record.id,  # ID of the record associated with the attachment
                    'res_model': 'custom.slide',  # Model name of the record associated with the attachment
                    'datas': record.upload_video,  # Binary data of the uploaded video
                }
                self.env['ir.attachment'].create(attachment_vals)
