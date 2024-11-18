import time
import RPi.GPIO as GPIO
import gphoto2 as gp

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
	
	def change_camera_mode(self, mode):
		config = self.camera.get_config()
		if mode == "manual":
			self.camera.set_config_value("focusmode", "manual")
		if mode == "auto":
			self.camera.set_config_value("focusmode", "auto")
			
	def set_iso(self, value):
		try:
			# Get the camera configuration
			config = self.camera.get_config()

			iso_node = config.get_child_by_name("iso")

			# Check if the ISO node is writable
			if iso_node:
				# Set the ISO value (ensure it's a string)
				iso_node.set_value(str(value))
				self.camera.set_config(config)
				print(f"ISO set to: {value}")
			else:
				print("ISO setting is not available or not writable.")
		
		except gp.GPhoto2Error as ex:
			print(f"Error setting ISO: {ex}")
		
	def get_iso(self):
		config = self.camera.get_config()
		return config.get_child_by_name('iso').get_value()
		
	def set_shutter(self, value):
		try:
			# Get the camera configuration
			config = self.camera.get_config()
			
			shutter_node = config.get_child_by_name("shutterspeed")

			# Check if the shutter node is writable
			if shutter_node:
				shutter_node.set_value(str(value))
				self.camera.set_config(config)
			else:
				print("shutter setting is not available or not writable.")
		
		except gp.GPhoto2Error as ex:
			print(f"Error setting ISO: {ex}")
	
	def get_shutter(self):
		config = self.camera.get_config()
		return config.get_child_by_name('shutterspeed').get_value()
	
	def set_aperture(self, value):
		try:
			# Get the camera configuration
			config = self.camera.get_config()
			
			aperture_node = config.get_child_by_name("f-number")

			# Check if the aperture node is writable
			if aperture_node:
				aperture_node.set_value(str(value))
				self.camera.set_config(config)
			else:
				print("aperture setting is not available or not writable.")
		
		except gp.GPhoto2Error as ex:
			print(f"Error setting ISO: {ex}")
	
	def get_aperture(self):
		config = self.camera.get_config()
		return config.get_child_by_name('f-number').get_value()
	
	def get_battery_life(self):
		config = self.camera.get_config()
		return config.get_child_by_name('batterylevel').get_value()
	

camera = Camera()
print(camera.get_battery_life())
print(camera.get_iso())
camera.set_iso(8000)
camera.set_shutter(320)
camera.set_aperture(1.8)
print(camera.get_iso())
camera.exit()
	

