import time
import RPi.GPIO as GPIO

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#PIN for Ultrasonic Distance Sensor
TRIG_PIN = 16
ECHO_PIN = 21

GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

GPIO.output(TRIG_PIN,GPIO.LOW)
print("waiting for sensor to initialize")
time.sleep(2)

#PIN for 7 Segment LED

#PIN for Buttons
BLUE_BUTTON = 22
BLACK_BUTTON = 17
GPIO.setup(BLUE_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BLACK_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#PIN for Buzzer

#PIN for LEDs

#Auxilarry functions
def get_distance(): #cm
	GPIO.output(TRIG_PIN,GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(TRIG_PIN,GPIO.LOW)
	
	while GPIO.input(ECHO_PIN) == 0:
		pulse_send = time.time()
	
	while GPIO.input(ECHO_PIN) == 1:
		pulse_received = time.time()
	
	distance = ((pulse_received-pulse_send) * 34300) / 2
	return distance 

num = get_distance()
