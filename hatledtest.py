import board
import busio
import adafruit_pca9685
from time import sleep
from adafruit_servokit import ServoKit

i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)

hat.frequency = 60

led_channel = hat.channels[0]

while True:
#	led_channel.duty_cycle = 0xffff
    led_channel.duty_cycle = 0
    break
