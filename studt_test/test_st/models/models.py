# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class TestSt(models.Model):# there are a table created in the data base called test_st.test_st
    _name = 'test_st.test_st'
    _description = 'test_st.test_st'
    name = fields.Char(String="Name", required=True)
    email = fields.Char()
    description = fields.Text(readonly=True)
    Boole = fields.Boolean(String="Bool value")
    Integer = fields.Integer(String="Integer value")
    float_num = fields.Float(String="Float value")
    date = fields.Date(String="Date value")
    dateTime_v = fields.Datetime(String="Datetime_value")
    selection = fields.Selection([('1', 'one'), ('2', 'two'), ('3', 'three')], string="Selection") # list of tupple ==> list [] && tupple ()
    upload = fields.Binary(string="Doc")
    html = fields.Html(string="Html")
    m2o= fields.Many2one('test2.test2',string="m2o")
    salary_b = fields.Integer(string="salary Befor")
    salary_buy = fields.Integer(string="salary After")
    win = fields.Integer(string="Money win",compute='compute_win')


    @api.depends('salary_b','salary_buy')
    def compute_win(self):
        for record in self:
            record.win =  record.salary_buy - record.salary_b

    def one_st(self):
        if self.selection==False:
            self.selection='1'
        elif self.selection=='1' :
            self.selection='2'
        elif self.selection=='2':
            self.selection='3'
        elif self.selection=='3':
            self.selection='1'

    @api.model
    def create(self,valu):
        Name = valu['name'].split() #['Mohab','Ahmed']
        valu['email'] = f"{Name[0][0]}{Name[1]}@gmail.com" # MAhmed@gmail.com
        search_email = self.search([('email', '=',  valu['email'])])
        if search_email :
             raise UserError("The value of email is exist")
        return super().create(valu)


    def write(self, vals):
        if 'name' in vals:
            Name = vals['name'].split()  # ['Mohab','Ahmed']
            vals['email'] = f"{Name[0][0]}{Name[1]}@gmail.com"  # MAhmed@gmail.com
        super().write(vals)

    def unlink(self):
        for rec in self:
            if rec.selection == '3':
                raise UserError("You cant delete any person his selection is three")
        super().unlink()



    @api.constrains('Integer')
    def check_in(self):
        if self.Integer > 55:
            raise UserError("The Number is greater than 55")
