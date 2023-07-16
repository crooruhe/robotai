import cv2
# for camera module libcamera-still or libcamera-vid.
# camera documentation: https://www.raspberrypi.com/documentation/computers/camera_software.html#introducing-the-raspberry-pi-cameras
# to take a picture: libcamera-jpeg -o test.jpg #will need to use subprocess and save to a face picture directory
# camera streaming: libcamera-vid -t 0 --codec libav --libav-format mpegts --libav-audio  -o "udp://<ip-addr>:<port>"
# potential software solution to start detecting faces: https://www.raspberrypi.com/documentation/computers/camera_software.html#libcamera-detect

from picamera2 import Picamera2, Preview


########################################
########################################
#potentially have server or work station do the video/facial recognition processing

# from picamera2.outputs import FileOutput
# import socket
# with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
#   sock.connect(("REMOTEIP", 10001))
#   stream = sock.makefile("wb")
#   output = FileOutput(stream)

########################################
########################################

""" TODO:
sudo apt-get install python-smbus
sudo apt-get install i2c-tools


use this to detect i2c port:
sudo i2cdetect -y 1

*should show the servo hat

need to ensure compatibility w/ circuit python and this regular python app
may need to use subprocess to run thread that contains circuit python code:

sudo pip3 install adafruit-circuitpython-servokit

servo board/hat:
import board
import busio
import adafruit_pca9685
from adafruit_servokit import ServoKit

i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)

documentation for hat: https://circuitpython.readthedocs.io/projects/pca9685/en/latest/api.html

kit = ServoKit(channels=16)

kit.continuous_servo[1].throttle = 1 #full throttle (probably way too fast)
kit.continuous_servo[1].throttle = 0.5 #half throttle
kit.continuous_servo[1].throttle = -1 #reverse

#my servo runs at 50 Hz


"""


import RPi.GPIO as GPIO #will show error on windows machine
#consider gpiozero
# from gpiozero import LED
# from time import sleep

# led = LED(17)

# while True:
#     led.on()
#     sleep(1)
#     led.off()
#     sleep(1)
from time import sleep

def camera_snapshot():
    picam2 = Picamera2()
    camera_config = picam2.create_preview_configuration()
    picam2.configure(camera_config)
    picam2.start_preview(Preview.QTGL) #x windows
    #picam2.start_preview(Preview.DRM) # ms windows (or other)
    picam2.start()
    sleep(2)
    picam2.capture_file("picamera_test_delete_me.jpg")

def picamera_video_capture():
    picam2 = Picamera2()
    picam2.start_and_record_video("test.mp4", duration=5)


###### example
""" GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
print("LED on")
GPIO.output(18,GPIO.HIGH)
sleep(1)
print("LED off")
GPIO.output(18,GPIO.LOW) """
#######

""" face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

video_capture = cv2.VideoCapture(0)

#edit to compare face to face on file or if it finds a new face add it to the collection
def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces

while True:

    result, video_frame = video_capture.read()  # read frames from the video
    if result is False:
        break  # terminate the loop if the frame is not read successfully

    faces = detect_bounding_box(
        video_frame
    )  # apply the function we created to the video frame

    cv2.imshow(
        "My Face Detection Project", video_frame
    )  # display the processed frame in a window named "My Face Detection Project"

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows() """

if __name__ == '__main__':
    pass