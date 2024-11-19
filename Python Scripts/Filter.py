from PIL import Image, ImageFilter
import cv2
import numpy as np

class imageManip:
	def __init__(self, image_path: str):
		self.image_PIL = Image.open(image_path)
		self.image_CV = np.array(self.image_PIL)
		self.original_image = self.image_PIL.copy()
		self.original_image_CV = self.image_CV.copy() 
		
	#format of function PIL
	# Do the image processing for PIL
	# Update image cv using copy
	
	#Format of function CV
	# Do the image processing for CV
	# Update image pil using copy
		
	def applyMonochrome(self):
		self.image_PIL = self.image_PIL.convert('L')
		self.image_CV = self.image_PIL.copy()
		
	def applySepia(self):
		width, height = self.image_PIL.size
		pixels = self.image_PIL.load()

		for py in range(height):
			for px in range(width):
				r, g, b = self.image_PIL.getpixel((px, py))

				tr = int(0.393 * r + 0.769 * g + 0.189 * b)
				tg = int(0.349 * r + 0.686 * g + 0.168 * b)
				tb = int(0.272 * r + 0.534 * g + 0.131 * b)

				if tr > 255:
					tr = 255

				if tg > 255:
					tg = 255

				if tb > 255:
					tb = 255

				pixels[px, py] = (tr,tg,tb)
				
		self.image_CV = np.array(self.image_PIL)
	
	def applyBloom(self, thresh_value=245, blur_value=50, gain=6):

		# Convert image to hsv colorspace as floats
		hsv = cv2.cvtColor(self.image_CV, cv2.COLOR_BGR2HSV).astype(np.float64)
		h, s, v = cv2.split(hsv)

		# Desired low saturation and high brightness for white
		# So invert saturation and multiply with brightness
		sv = ((255 - s) * v / 255).clip(0, 255).astype(np.uint8)

		# Apply threshold
		thresh = cv2.threshold(sv, thresh_value, 255, cv2.THRESH_BINARY)[1]

		# Apply Gaussian blur
		blur = cv2.GaussianBlur(thresh, (0, 0), sigmaX=blur_value, sigmaY=blur_value)
		blur = cv2.cvtColor(blur, cv2.COLOR_GRAY2BGR)

		# Blend the blur with the original image using the gain
		result = cv2.addWeighted(self.image_CV, 1, blur, gain, 0)

		# Save the output image
		self.image_PIL = Image.fromarray(result)
		self.image_CV = result
	
	def save(self):
		self.image_PIL.save("../Image/testoutput.jpg")

image = imageManip("/home/admin/Desktop/Raspberry-Pi-Camera-Controller/Image/test.jpg")
image.applyBloom()
image.save()




