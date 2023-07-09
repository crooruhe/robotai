import cv2
# for camera module libcamera-still or libcamera-vid.
# camera documentation: https://www.raspberrypi.com/documentation/computers/camera_software.html#introducing-the-raspberry-pi-cameras
# to take a picture: libcamera-jpeg -o test.jpg #will need to use subprocess and save to a face picture directory
# camera streaming: libcamera-vid -t 0 --codec libav --libav-format mpegts --libav-audio  -o "udp://<ip-addr>:<port>"
# potential software solution to start detecting faces: https://www.raspberrypi.com/documentation/computers/camera_software.html#libcamera-detect
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

###### example
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
print("LED on")
GPIO.output(18,GPIO.HIGH)
sleep(1)
print("LED off")
GPIO.output(18,GPIO.LOW)
#######

face_classifier = cv2.CascadeClassifier(
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
cv2.destroyAllWindows()