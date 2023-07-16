# i think a lot of this is old picamera 1 so it needs to be updated to 2 which is what the picamera 3 uses

import time
import picamera
import picamera.array
import cv2

camera = picamera.PiCamera()

camera.resolution = (640, 480)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to perform face detection on an image
def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

try:
    # Start the video stream
    with picamera.array.PiRGBArray(camera) as stream:
        while True:
            # Capture a frame from the video stream
            camera.capture(stream, format='bgr')
            image = stream.array

            # Perform face detection on the captured image
            faces = detect_faces(image)

            if len(faces) > 0:
                print("Face detected!")

            # Clear the stream in preparation for the next capture
            stream.truncate(0)

            # Wait for 1.2 seconds before capturing the next image
            time.sleep(1.2)

except KeyboardInterrupt:
    pass

finally:
    # Release resources
    camera.close()
