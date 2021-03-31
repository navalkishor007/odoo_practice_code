from odoo import fields, models

class ContactProfile(models.Model):
    _name = 'contact.profile'

    name = fields.Char(string='Person name')
    email = fields.Char(string='Email')
    phone = fields.Char('phone')