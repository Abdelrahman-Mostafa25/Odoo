# -*- coding: utf-8 -*-

from odoo import models, fields


class it_courses(models.Model):
    _name = 'it_courses.it_courses'
    _description = 'it_courses.it_courses'

    name = fields.Char(string="Titel", required=True)
    description = fields.Text()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
