import time
import RPi.GPIO as GPIO
import gphoto2 as gp

#PIN for Ultrasonic Distance Sensor
TRIG_PIN = 13
ECHO_PIN = 6
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.output(TRIG_PIN,GPIO.LOW)
time.sleep(2)

#PIN for 7 Segment LED

#PIN for Buttons
BLUE_BUTTON = 22
BLACK_BUTTON = 17
GPIO.setup(TRIG_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(ECHO_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
#PIN for Buzzer

#PIN for LEDs
