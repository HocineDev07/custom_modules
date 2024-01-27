from odoo import http
from odoo.http import request


class VideoController(http.Controller):

    @http.route('/upload_video', type='http', auth="public", website=True)
    def upload_video(self, **kwargs):
        # Handle video upload logic
        # Retrieve the uploaded video file
        uploaded_video = request.httprequest.files.get('video_file')

        if uploaded_video:
            video_data = uploaded_video.read()

            # Get the name of the uploaded video file
            video_name = uploaded_video.filename
            # Remove the path from the filename if it exists
            video_name = os.path.basename(video_name)

            # Save the video data as an attachment to the model
            request.env['hospital.patient'].create({
                'name': video_name,
                'video': video_data,
            })

        return "Video uploaded successfully!"
