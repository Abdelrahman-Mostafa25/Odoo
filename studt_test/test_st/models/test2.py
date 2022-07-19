

from odoo import models, fields, api


class Test2(models.Model):
    _name = 'test2.test2'  # there are a table created in the data base called test_st.test_st
    _description = 'test22'

    name = fields.Char(string="Name", required=True)
    Start_date = fields.Date()
    Duration = fields.Float(digits=(7, 3))
    Seats = fields.Integer(string="Seats")
    o2m =fields.One2many('test_st.test_st','m2o')
