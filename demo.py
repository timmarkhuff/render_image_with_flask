import framegrab
from framegrab_web_server import FrameGrabWebServer

config = {
    "input_type": "generic_usb",
}
grabber = framegrab.FrameGrabber.create_grabber(config, warmup_delay=0.0)

web_server = FrameGrabWebServer("My Demo Image Viewer")

while True:
    frame = grabber.grab()
    web_server.show_image(frame)
    # time.sleep(0.1)

grabber.release()