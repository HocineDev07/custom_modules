from odoo import http
from odoo.http import request


class VideoUploadController(http.Controller):

    @http.route('/website/form/upload/url', type='http', auth='user', website=True)
    def handle_video_upload(self, **post):
        # Check if a file was uploaded
        if 'video_file' in request.httprequest.files:
            video_file = request.httprequest.files['video_file']
            # Save the uploaded file to a storage location
            file_path = '/videos/' + video_file.filename
            with open(file_path, 'wb') as f:
                f.write(video_file.read())
            # Optionally, you can store the file path or other metadata in your database
            # You might want to associate the uploaded video with a specific record or model in Odoo
            # Example: request.env['your.model'].create({'video_path': file_path})

        # Redirect or return a response as needed
        return request.redirect('/path/to/redirect')
