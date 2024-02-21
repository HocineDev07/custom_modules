from datetime import date
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from dateutil import relativedelta


class PatientTag(models.Model):
    _name = "patient.tag"
    _description = "Patient Tag"
    _order = "id desc, name asc"

    name = fields.Char(string="Name", required=True)
    active = fields.Boolean(string="Active", default=True)
    color = fields.Integer(string="Color")
    color_2 = fields.Char(string="Color 2")
    sequence = fields.Integer(string="Sequence", default=1)
    age = fields.Integer(string="Age", compute="calculate_age", inverse="inverse_calculate_age")
    date_of_birth = fields.Date(string="Date of birth")
    reference_field = fields.Reference([('hospital.patient','Patients'), ('hospital.appointment','Appointment')], string="Reference")



    def click(self):
        cancel_day = self.env['ir.config_parameter'].get_param('om_hospital.cancel_day')
        allowed_date = self.date_of_birth - relativedelta.relativedelta(days=int(cancel_day))
        if allowed_date <= date.today():
            raise ValidationError(_("You can not cancel this tag!"))
        else:
            raise ValidationError(_("You can cancel this tag"))

    @api.depends('date_of_birth')
    def calculate_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1

    @api.depends('age')
    def inverse_calculate_age(self):
        today = date.today()
        for rec in self:
            if rec.age > 0:
                rec.date_of_birth = today - relativedelta.relativedelta(years=rec.age)
            else:
                rec.date_of_birth = today - relativedelta.relativedelta(years=1)

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        default = {}
        if 'name' not in default:
            default['name'] = _("%s (copy)") % (self.name)
        return super(PatientTag, self).copy(default=default)

    def unlink(self):
        if self.name == "VIP.":
            raise ValidationError(_("Not allowed to delete: "+ self.name))
        return super(PatientTag, self).unlink()

    _sql_constraints = [
        ('unique_tag_name', 'unique(name)', 'Name must be unique!'),
        ('check_sequence', 'CHECK(sequence > 0)', 'Sequence must be greater than 0!')
    ]
