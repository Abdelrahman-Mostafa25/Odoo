from odoo import models,fields,api


class Log_user(models.Model):
    _name = 'log.user'
    description = fields.Char(string="Description")
    patient_id = fields.Many2one('patient.patient')


