from odoo import models,fields

class EditeHr(models.Model):
    _inherit ='hr.employee'

    army_cir = fields.Binary()