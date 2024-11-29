import gphoto2 as gp
import time
from threading import Thread

#Camera Class
class Camera:
	def __init__(self):
		self.camera = None
		self.initialize_camera()
		
	def initialize_camera(self):
		while True:
			try:
				print("Please set your camera to PC-remote.")
				print("Please plug in your sony A-6000")
				self.camera = gp.Camera()
				self.camera.init()
				print("Camera initialized successfully.")
				break
			except gp.GPhoto2Error as e:
				if e.code == gp.GP_ERROR_MODEL_NOT_FOUND:
					print("Camera not found. Retrying to connection in 2 seconds.")
					time.sleep(2)
					continue
				raise
	
	def get_battery_life(self):
		try:
			config = self.camera.get_config()
			return config.get_child_by_name('batterylevel').get_value()
		except gp.GPhoto2Error as e:
			print(f"Error getting camera battery life: {e}")
			
	def get_camera_name(self):
		try:
			config = self.camera.get_config()
			return str(config.get_child_by_name('cameramodel').get_value())
		except gp.GPhoto2Error as e:
			print(f"Error getting camera battery name: {e}")
	
	def get_camera_manufacturer(self):
		try:
			
			config = self.camera.get_config()
			return str(config.get_child_by_name('manufacturer').get_value())
		except gp.GPhoto2Error as e:
			print(f"Error getting camera manufacturer: {e}")
	
	def take_photo(self):
		try:
			file_path = self.camera.capture(gp.GP_CAPTURE_IMAGE)
			target = "./__pycache__/temp.jpg"
			self.camera.file_get(file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL).save(target)
			self.exit()
			self.initialize_camera()
		except gp.GPhoto2Error as e:
			print(f"Error taking photo: {e}")
			raise
		
	def focus_camera(self):
		try:
			
			print("Focusing camera")
			config = self.camera.get_config()
			if(config.get_child_by_name('focusmode').get_value() == "Manual"):
				print("Unable to autofocus. Camera is in manual mode.")
				return 
			autofocus_node = config.get_child_by_name("autofocus")
		
			if autofocus_node:
				autofocus_node.set_value(0)
				self.camera.set_config(config)
				autofocus_node.set_value(1)
				self.camera.set_config(config)
				time.sleep(1)
				autofocus_node.set_value(0)
				self.camera.set_config(config)
		except gp.GPhoto2Error as e:
			print(f"Error trying to focus camera: {e}")
			
		
	def exit(self):
		try:
			if self.camera:
				print("Exiting camera")
				self.camera.exit()
				self.camera = None
		except gp.GPhoto2Error as e:
			print(f"Error exiting camera: {e}")

	def get_camera_mode(self):
		try:
			config = self.camera.get_config()
			autofocus_node = config.get_child_by_name("autofocus")
			focus_mode = config.get_child_by_name("focusmode").get_value()
			if focus_mode == "Manual":
				return 0
			else:
				return 1
		except gp.GPhoto2Error as e:
			print(f"Error getting camera mode: {e}")
			
	def set_camera_mode(self, mode): #"AF-S" or "Manual". other are "AF-A" or "AF-C"
		try:
			# Get the camera configuration
			config = self.camera.get_config()

			focus_node = config.get_child_by_name("focusmode")

			if focus_node:
				focus_node.set_value(mode)
				self.camera.set_config(config)
				print(f"Camera Mode set to: {mode}")
			else:
				print("Camera Mode setting is not available or not writable.")
		
		except gp.GPhoto2Error as e:
			print(f"Error setting Camera Mode: {e}")
			
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
		
		except gp.GPhoto2Error as e:
			print(f"Error setting ISO: {e}")
		
	def get_iso(self):
		try:
			config = self.camera.get_config()
			return config.get_child_by_name('iso').get_value()
		except gp.GPhoto2Error as e:
			print(f"Error getting ISO: {e}")
		
	def set_shutter(self, value): #input must be in string format Example: "1/200", "1/300"
		try:
			# Get the camera configuration
			config = self.camera.get_config()
			
			shutter_node = config.get_child_by_name("shutterspeed")

			# Check if the shutter node is writable
			if shutter_node:
				shutter_node.set_value(value)
				self.camera.set_config(config)
			else:
				print("shutter setting is not available or not writable.")
		
		except gp.GPhoto2Error as e:
			print(f"Error setting SHUTTER: {e}")
	
	def get_shutter(self):
		try:
			config = self.camera.get_config()
			return config.get_child_by_name('shutterspeed').get_value()
		except gp.GPhoto2Error as e:
			print(f"Error getting camera manufacturer: {e}")
	
	def set_aperture(self, value):
		try:
			# Get the camera configuration
			config = self.camera.get_config()
			
			aperture_node = config.get_child_by_name("f-number")

			# Check if the aperture node is working properly
			if aperture_node:
				aperture_node.set_value(str(value))
				self.camera.set_config(config)
			else:
				print("aperture setting is not available or not writable.")
		except gp.GPhoto2Error as e:
			print(f"Error setting APERTURE: {e}")
	
	def get_aperture(self):
		try:
			config = self.camera.get_config()
			return config.get_child_by_name('f-number').get_value()
		except gp.GPhoto2Error as e:
			print(f"Error getting APERTURE: {e}")
	
	def set_white_balance(self):
		try:
			config = self.camera.get_config()
			white_balance_node = config.get_child_by_name("")
			
			if white_balance_node:
				white_balance_node.set_value(str(value))
				self.camera.set_config(config)
			else:
				print("White balance setting is not available or not writable.")
		
		except gp.GPhoto2Error as ex:
			print(f"Error setting WHITE BALANCE: {ex}")
			
	def get_white_balance(self):
		try:
			config = self.camera.get_config()
		except gp.GPhoto2Error as e:
			print(f"Error getting WHITE BALANCE: {e}")


