from PIL import Image, ImageFilter
import cv2
import numpy as np


def applyBloom(ImageLocation):
	# read image
	img = cv2.imread(ImageLocation)

	# set arguments
	thresh_value = 245  # threshold to find white
	blur_value = 50     # bloom smoothness
	gain = 6            # bloom gain in intensity

	# convert image to hsv colorspace as floats
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(np.float64)
	h, s, v = cv2.split(hsv)

	# Desire low saturation and high brightness for white
	# So invert saturation and multiply with brightness
	sv = ((255-s) * v / 255).clip(0,255).astype(np.uint8)

	# threshold
	thresh = cv2.threshold(sv, thresh_value, 255, cv2.THRESH_BINARY)[1]

	# blur and make 3 channels
	blur = cv2.GaussianBlur(thresh, (0,0), sigmaX=blur_value, sigmaY=blur_value)
	blur = cv2.cvtColor(blur, cv2.COLOR_GRAY2BGR)

	# blend blur and image using gain on blur
	result = cv2.addWeighted(img, 1, blur, gain, 0)

	# save output image
	cv2.imwrite('barn_bloom.jpg', result)

def applyMonochrome(ImageLocation):
	return

def applySepia(image_path:str)->Image:
    img = Image.open(image_path)
    width, height = img.size

    pixels = img.load() # create the pixel map

    for py in range(height):
        for px in range(width):
            r, g, b = img.getpixel((px, py))

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

    return img
