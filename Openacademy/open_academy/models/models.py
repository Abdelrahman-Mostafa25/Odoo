# -*- coding: utf-8 -*-


from odoo import models, fields, api, exceptions, _
from datetime import timedelta


class open_academy(models.Model):
    _name = 'open_academy.open_academy'
    _description = 'open_academy.open_academy'

    name = fields.Char(string="Course Name", required=True)
    description = fields.Text()
    Levels = fields.Integer()
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True)
    session_id = fields.One2many('openacademy.session', 'course_id', string="Session")

    _sql_constraints = [
        ('name_description_check', 'CHECK(name!=description)', "The title of the course should not be th description"),
        ('name_unique', 'UNIQUE(name)', "The course title must be unique")
    ]


#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
class session(models.Model):
    _name = 'openacademy.session'
    _description = 'open_academy session'

    name = fields.Char(required=True)
    Start_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    active = fields.Boolean(default=True)
    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('open_academy.open_academy', ondelete="cascade", string="course", required=True)
    attendee_ids = fields.Many2many('res.partner', string='Attendees')

    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')
    end_date = fields.Date(string="End Date", store=True, compute='_get_end_date', inverse='_set_end_date')

    attendee_count = fields.Integer(string="Attendees count", compute='_get_attendees_count', store=True)

    @api.depends('Start_date', 'duration')
    def _get_end_date(self):
        for r in self:
            if not (r.Start_date and r.duration):
                r.end_date = r.Start_date
                continue
                duration = timedelta(days=r.duration, seconds=-1)
                r.end_date = r.Start_date + duration

    def _set_end_date(self):
        for r in self:
            if not (r.Start_date and r.end_date):
                continue
                r.duration = (r.end_date - r.Start_date).days + 1

    @api.depends('attendee_ids')
    def _get_attendees_count(self):
        for r in self:
            r.attendee_count = len(r.attendee_ids)

    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats

    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Incorrect 'seats' value ",
                    'message': "The number of available seats may not be negative",
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': _("Too many attendees"),
                    'message': "Increase seats or remove excess attendees",
                },
            }

        @api.constrains('instructor_id', 'attendee_ids')
        def _check_instructor_not_in_attendees(self):
            for rec in self:
                if rec.instructor_id and rec.instructor_id in rec.attendee_ids:
                    raise exceptions.ValidationError("A session's instructor can't be an attendee")

