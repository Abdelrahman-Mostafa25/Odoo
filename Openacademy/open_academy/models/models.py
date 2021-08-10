# -*- coding: utf-8 -*-

from odoo import models, fields, api


class open_academy(models.Model):
    _name = 'open_academy.open_academy'
    _description = 'open_academy.open_academy'

    name = fields.Char(string="Course Name", required=True)
    description = fields.Text()
    Levels = fields.Text()

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
