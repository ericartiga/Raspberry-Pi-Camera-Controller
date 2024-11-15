import time
import RPi.GPIO as GPIO
import gphoto2 as gp

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#PIN for Ultrasonic Distance Sensor
TRIG_PIN = 20
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

#Camera Class
class Camera:
	def __init__(self):
		self.camera = None
		self.initalize_camera()
		
	def initalize_camera(self):
		while True:
			try:
				print("Please set your camera to PC-remote.")
				print("Please plug in your sony A-6000")
				self.camera = gp.Camera()
				self.camera.init()
				print("Camera initialized successfully.")
				break
			except gp.GPhoto2Error as ex:
				if ex.code == gp.GP_ERROR_MODEL_NOT_FOUND:
					print("Camera not found. Retrying to connection in 2 seconds.")
					time.sleep(2)
					continue
				raise
	
	def take_photo(self):
		print("Taking photo")
		file_path = self.camera.capture(gp.GP_CAPTURE_IMAGE)
		target = f"./{file_path.name}"
		self.camera.file_get(file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL).save(target)
		
	def exit(self):
		if self.camera:
			self.camera.exit()
	
	def change_camera_mode():
		return
	
	def set_exposure():
		return
		
	def set_shutter():
		return

#gphoto2 --list-config
	

camera = Camera()
camera.set_focus(get_distance())
camera.take_photo()
camera.exit()
	
