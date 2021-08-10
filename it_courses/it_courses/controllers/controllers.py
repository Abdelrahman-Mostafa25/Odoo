# -*- coding: utf-8 -*-
# from odoo import http


# class ItCourses(http.Controller):
#     @http.route('/it_courses/it_courses/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/it_courses/it_courses/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('it_courses.listing', {
#             'root': '/it_courses/it_courses',
#             'objects': http.request.env['it_courses.it_courses'].search([]),
#         })

#     @http.route('/it_courses/it_courses/objects/<model("it_courses.it_courses"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('it_courses.object', {
#             'object': obj
#         })
