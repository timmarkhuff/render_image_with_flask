# flask_server.py
from flask import Flask, send_file, render_template_string
import threading
import io
import cv2
import logging

class FrameGrabWebServer:
    def __init__(self, name: str = "FrameGrab Image Viewer", host="0.0.0.0", port=5000, refresh_interval=100):
        self.name = name
        self.host = host
        self.port = port
        self.refresh_interval = refresh_interval
        self.image_bytes = None
        
        logging.getLogger('werkzeug').setLevel(logging.ERROR)

        self.app = Flask(__name__)
        self._setup_routes()

        threading.Thread(target=self._run, daemon=True).start()
        self._thread_started = True
        print(f"FrameGrab webserver running at http://{self.host}:{self.port}")

    def _setup_routes(self):
        TEMPLATE = f'''
        <html>
          <head><title>{self.name}</title></head>
          <link rel="icon" type="image/x-icon" href="/static/groundlight_favicon.ico">
          <body>
            <img src="/image" width="640">
            <script>
              setInterval(() => {{
                document.querySelector("img").src = "/image?" + new Date().getTime();
              }}, {self.refresh_interval});
            </script>
          </body>
        </html>
        '''

        @self.app.route('/')
        def index():
            return render_template_string(TEMPLATE)

        @self.app.route('/image')
        def image():
            if self.image_bytes is None:
                return 'No image available', 404
            return send_file(io.BytesIO(self.image_bytes), mimetype='image/jpeg')

    def _run(self):
        self.app.run(host=self.host, port=self.port, debug=False, use_reloader=False)

    def show_image(self, frame):
        _, jpeg = cv2.imencode('.jpg', frame)
        self.image_bytes = jpeg.tobytes()
