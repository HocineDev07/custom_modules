# -*- coding: utf-8 -*-
# from odoo import http


# class HDevHospital(http.Controller):
#     @http.route('/dev_hospital/dev_hospital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dev_hospital/dev_hospital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dev_hospital.listing', {
#             'root': '/dev_hospital/dev_hospital',
#             'objects': http.request.env['dev_hospital.dev_hospital'].search([]),
#         })

#     @http.route('/dev_hospital/dev_hospital/objects/<model("dev_hospital.dev_hospital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dev_hospital.object', {
#             'object': obj
#         })
