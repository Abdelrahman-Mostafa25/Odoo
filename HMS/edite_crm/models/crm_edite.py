from odoo import models,fields,api
from odoo.exceptions import UserError

class Crm_Edite(models.Model):
    _inherit = 'res.partner'

    related_patient_id = fields.Many2one('patient.patient')

    def unlink(self):
        for rec in self:
            if rec.related_patient_id :
                raise UserError("Sorry canit delete this record becase is has a patienet id ")
        super().unlink()


    @api.model
    def create(self, vals):
        creat_em = self.env['patient.patient'].search([('email', '=', vals['email'])])
        if creat_em:
            raise UserError("please change your email")
        return super().create(vals)