from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    cancel_days = fields.Integer(string="Cancel days", config_parameter='om_hospital.cancel_day')
