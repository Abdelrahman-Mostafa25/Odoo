# -*- coding: utf-8 -*-
# from odoo import http


# class TestSt(http.Controller):
#     @http.route('/test_st/test_st/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_st/test_st/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_st.listing', {
#             'root': '/test_st/test_st',
#             'objects': http.request.env['test_st.test_st'].search([]),
#         })

#     @http.route('/test_st/test_st/objects/<model("test_st.test_st"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_st.object', {
#             'object': obj
#         })
