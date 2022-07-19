import datetime
import re

from odoo import models, fields,api
from odoo.exceptions import UserError
from datetime import date



class HmsPatients(models.Model):# there are a table created in the data base called test_st.test_st
    _name = 'patient.patient'

    name = fields.Char(string="First name")
    lastname = fields.Char(string="Last name")
    email = fields.Char(string="Email")
    bd = fields.Date(string="Birth date")
    history = fields.Html(string="History")
    cr_ratio = fields.Float(string="CR Ratio")
    Blood_type = fields.Selection([('1', 'A'), ('2', 'B'), ('3', 'Z')], string="Blood type") # list of tupple ==> list [] && tupple ()
    pcr = fields.Boolean(string="PCR",default=False)
    upload = fields.Binary(string="Image")
    address = fields.Text(string="Address")
    age = fields.Char(string="Age",compute='clc_age')
    department_id = fields.Many2one('hms.department')
    department_cap = fields.Integer(related="department_id.Capacity")
    states = fields.Selection([('b', ''),('u', 'Undetermined'), ('g', 'Good'), ('f', 'Faie'),('s','Serious')], string="states" ,default="b" )
    doctor_id = fields.Many2many('hms.doctor')
    log=fields.One2many('log.user','patient_id',string="Log")



    @api.depends('bd')
    def clc_age(self):
        for record in self:
            if record.bd:
                if(datetime.datetime.now().year > record.bd.year):
                    record.age = str(datetime.datetime.now().year - record.bd.year)
                else:
                    record.age = 'Please Enter right Date'
            else:
                record.age = 'Please Enter Birth Date'


    def selection(self):
            if self.states is 'b':
                self.states='u'
            elif self.states == 'u':
                self.states='g'
            elif self.states=='g':
                self.states='f'
            elif self.states=='f':
                self.states = 's'
            elif self.states=='s':
                self.states = 'b'

    @api.model
    def create(self,vals):
        Name = vals['name'].split()
        vals['email'] = f"{Name[0][0]}{vals['lastname']}@gmail.com"
        creat_em = self.search([('email','=',vals['email'])])
        if creat_em:
             raise UserError("please change second name")
        return super().create(vals)

    def write(self,vals):
        if 'name' in vals :
           Name = vals['name'].split()
           if 'lastname' in vals:
               vals['email'] = f"{Name[0][0]}{vals['lastname']}@gmail.com"
           else:
               vals['email'] = f"{Name[0][0]}{self.lastname}@gmail.com"
        else:
            if 'lastname' in vals:
                Name = self.name.split()
                vals['email'] = f"{Name[0][0]}{vals['lastname']}@gmail.com"
        super().write(vals)

    @api.constrains('name','lastname')
    def valid(self):
        pattren = "^[A-Za-z_][A-Za-z0-9_]+"
        if re.match(pattren, self.name) is None:
            raise UserError("Not Valid Name")
        elif  re.match(pattren, self.lastname) is None:
            raise UserError("Not Valid Last Name")

    #_sql_constraints =[("Duplicate email","UNIQUE(email)","please change second name")]

    # @api.onchange('age')
    # def _onchange_accepted(self):
    #     self.pcr = False
    #     if self.age < 30 and self.age > 0.00:
    #          self.pcr = True
    #     else:
    #         self.pcr = False
    #     return {
    #         'warning' : {
    #             'title':"Hello",
    #              'message':"The Pcr is become True"
    #         }
    #     }




