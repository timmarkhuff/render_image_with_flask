import framegrab
from framegrab_web_server import FrameGrabWebServer
import time

# Connect to your camera. Below is an example for connecting to a web cam
config = {
    "input_type": "generic_usb",
}
grabber = framegrab.FrameGrabber.create_grabber(config, warmup_delay=0.0)

# Start the web server
web_server = FrameGrabWebServer("My Demo Image Viewer")

# Open the web server in your browser. The address will be printed to the
# console and will look something like this: http://0.0.0.0:5000

while True:
    # Handle user input
    user_input = input(
        "Enter 'q' to quit.  "
        "Press Enter to grab a frame and display it in the web server:  "
        ).lower().strip()
    
    if user_input == 'q':
        break
    
    # Capture an image
    frame = grabber.grab()
    
    # Display the image
    web_server.show_image(frame)
    
    time.sleep(0.1)

grabber.release()