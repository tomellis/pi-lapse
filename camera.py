from picamera import PiCamera
from time import sleep
from datetime import datetime 

image_folder = '/home/pi/pi-lapse/images'
timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

camera = PiCamera()
sleep(5)
camera.rotation = 180
camera.capture(image_folder + 'image-' + timestamp + '.png')
