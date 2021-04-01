from odoo import fields, models

class ContactProfile(models.Model):
    _name = 'contact.profile'

    name = fields.Char(string='Person name')
    email = fields.Char(string='Email')
    phone = fields.Char('phone')
    person_image = fields.Image(string="Upload Image", max_width=100, max_height=100,
     verify_resolution=False)