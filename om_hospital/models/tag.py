from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class PatientTag(models.Model):
    _name = "patient.tag"
    _description = "Patient Tag"

    name = fields.Char(string="Name", required=True)
    active = fields.Boolean(string="Active", default=True)
    color = fields.Integer(string="Color")
    color_2 = fields.Char(string="Color 2")
    sequence = fields.Integer(string="Sequence", default=1)
    age = fields.Integer(string="Age", compute="calculate_age")

    def click(self):
        return

    def calculate_age(self):
        for rec in self:
            rec.age = rec.sequence + 10

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        default = {}
        if 'name' not in default:
            default['name'] = _("%s (copy)") % (self.name)
        return super(PatientTag, self).copy(default=default)

    def unlink(self):
        if self.name == "VIP":
            raise ValidationError(_("Not allowed to delete: "+ self.name))
        return super(PatientTag, self).unlink()

    _sql_constraints = [
        ('unique_tag_name', 'unique(name)', 'Name must be unique!'),
        ('check_sequence', 'CHECK(sequence > 0)', 'Sequence must be greater than 0!')
    ]
