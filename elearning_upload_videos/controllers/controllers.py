# -*- coding: utf-8 -*-
# from odoo import http


# class ElearningUploadeVideos(http.Controller):
#     @http.route('/elearning_upload_videos/elearning_upload_videos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/elearning_upload_videos/elearning_upload_videos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('elearning_upload_videos.listing', {
#             'root': '/elearning_upload_videos/elearning_upload_videos',
#             'objects': http.request.env['elearning_upload_videos.elearning_upload_videos'].search([]),
#         })

#     @http.route('/elearning_upload_videos/elearning_upload_videos/objects/<model("elearning_upload_videos.elearning_upload_videos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('elearning_upload_videos.object', {
#             'object': obj
#         })
