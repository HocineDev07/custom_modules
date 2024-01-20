# -*- coding: utf-8 -*-

from odoo import models, fields, api


class dev_hospital_patient(models.Model):
    _name = 'dev_hospital.patient'
    _description = 'Dev Hospital Patient'

    name = fields.Char(string='Name')
    reference = fields.Char(string='Reference Order', readonly=True, copy=False)
    responsible_id = fields.Many2one('res.users', string='Responsible',tracking=True)
    age = fields.Integer(string='Age')
    appointment_count = fields.Integer(string='Appointment Count', readonly=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ],tracking=True, required=True, default='male')



    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
