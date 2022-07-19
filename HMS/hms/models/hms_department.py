from odoo import models, fields

class HmsPatients(models.Model):# there are a table created in the data base called test_st.test_st
    _name = 'hms.department'

    name = fields.Text(String="Name")
    Capacity = fields.Integer(String="Capacity")
    Is_opened = fields.Boolean(String="Is_opened")
    patient_id = fields.One2many('patient.patient','department_id')