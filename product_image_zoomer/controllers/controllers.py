# -*- coding: utf-8 -*-
# from odoo import http


# class ProductImageZoom(http.Controller):
#     @http.route('/product_image_zoom/product_image_zoom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_image_zoom/product_image_zoom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_image_zoom.listing', {
#             'root': '/product_image_zoom/product_image_zoom',
#             'objects': http.request.env['product_image_zoom.product_image_zoom'].search([]),
#         })

#     @http.route('/product_image_zoom/product_image_zoom/objects/<model("product_image_zoom.product_image_zoom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_image_zoom.object', {
#             'object': obj
#         })

