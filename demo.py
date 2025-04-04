import framegrab
from framegrab_web_server import FrameGrabWebServer
import time

# Connect to your camera. Below is an example for connecting to a webcam
# or USB camera. Framegrab also lets you connect other camera types such as RTSP
# Read more about Framegrab here: https://pypi.org/project/framegrab/
config = {
    "input_type": "generic_usb",
}
grabber = framegrab.FrameGrabber.create_grabber(config, warmup_delay=0.0)

# Start the web server
web_server = FrameGrabWebServer("My Image Viewer")

# Open the web server in your browser. The address will be printed to the
# console and will look something like this: http://0.0.0.0:5000

try:
    while True:
        # Capture an image
        frame = grabber.grab()
        
        # Display the image
        web_server.show_image(frame)
        
        time.sleep(0.1)
finally:
    grabber.release()