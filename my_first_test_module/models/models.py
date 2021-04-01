# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class my_first_test_module(models.Model):
#     _name = 'my_first_test_module.my_first_test_module'
#     _description = 'my_first_test_module.my_first_test_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class Course(models.Model):
    _name = 'my.first.test.module.test'
    _description = 'test model'

    name = fields.Char(string="Title", required=True,help="Name of the Course")
    description = fields.Text()

class User(models.Model):
    _name = 'test.profile'
    name = fields.Char(required=True,)

class UserTest(models.Model):
    _name = 'user.test.profile'
    name = fields.Char(required=True,)
