from odoo import models, fields

class HmsPatients(models.Model):# there are a table created in the data base called test_st.test_st
    _name = 'hms.doctor'

    name = fields.Text(required=True,String="First name")
    lastname = fields.Text(required=True,String="Last name")
    upload = fields.Binary(string="Image")