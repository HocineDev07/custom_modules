# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HospitalPatient(models.Model):
    _inherit = "hospital.patient"

    confirm_user_id = fields.Many2one('res.users', string="Confirmed User")

