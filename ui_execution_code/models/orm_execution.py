# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class OrmExecution(models.Model):
    _name = "orm.execution"
    _description = "ORM Execution"

    orm_expression = fields.Text(string='ORM Expression')
    result = fields.Text(string='Result')

    @api.depends('orm_expression')
    def compute_result(self):
        for record in self:
            if record.orm_expression:
                try:
                    # Execute the ORM orm_expression dynamically
                    result = eval(record.orm_expression, {'self': self, 'env': self.env})
                    record.result = str(result)
                except Exception as e:
                    record.result = str(e)
            else:
                record.result = 'No orm_expression provided'

    @api.depends('orm_expression')
    def clear_result(self):
        for record in self:
            self.orm_expression = ""
