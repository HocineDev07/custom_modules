# -*- coding: utf-8 -*-

from odoo import models, fields, api


class dev_hospital_patient(models.Model):
    _name = 'dev_hospital.patient'
    _description = 'Dev Hospital Patient'

    name = fields.Char(string='Name')
    reference = fields.Char(string='Reference Order', copy=False)
    responsible_id = fields.Many2one('res.users', string='Responsible',tracking=True)
    age = fields.Integer(string='Age')
    appointment_count = fields.Integer(string='Appointment Count', readonly=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ],tracking=True, required=True, default='male')
    note = fields.Text(string='Description')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'done'),
        ('cancel', 'Cancel'),
    ], tracking=True, default='draft')
    image = fields.Binary(string='Patient Image')



    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
