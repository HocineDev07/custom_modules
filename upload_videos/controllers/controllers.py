# -*- coding: utf-8 -*-
# from odoo import http


# class UploadVideos(http.Controller):
#     @http.route('/upload_videos/upload_videos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/upload_videos/upload_videos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('upload_videos.listing', {
#             'root': '/upload_videos/upload_videos',
#             'objects': http.request.env['upload_videos.upload_videos'].search([]),
#         })

#     @http.route('/upload_videos/upload_videos/objects/<model("upload_videos.upload_videos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('upload_videos.object', {
#             'object': obj
#         })
