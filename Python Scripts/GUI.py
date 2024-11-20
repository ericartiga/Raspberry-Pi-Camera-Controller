# ##
# #GPIO Codes
# ##
# import time
# import RPi.GPIO as GPIO

# # Set up GPIO
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)

# #PIN for Ultrasonic Distance Sensor
# TRIG_PIN = 16
# ECHO_PIN = 21

# GPIO.setup(TRIG_PIN, GPIO.OUT)
# GPIO.setup(ECHO_PIN, GPIO.IN)

# GPIO.output(TRIG_PIN,GPIO.LOW)
# print("waiting for sensor to initialize")
# time.sleep(2)

# #PIN for 7 Segment LED

# #PIN for Buttons
# BLUE_BUTTON = 22
# BLACK_BUTTON = 17
# GPIO.setup(BLUE_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(BLACK_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# #PIN for Buzzer

# #PIN for LEDs

# #Auxilarry functions
# def get_distance(): #cm
	# GPIO.output(TRIG_PIN,GPIO.HIGH)
	# time.sleep(0.00001)
	# GPIO.output(TRIG_PIN,GPIO.LOW)

	# while GPIO.input(ECHO_PIN) == 0:
		# pulse_send = time.time()

	# while GPIO.input(ECHO_PIN) == 1:
		# pulse_received = time.time()

	# distance = ((pulse_received-pulse_send) * 34300) / 2
	# return distance

# num = get_distance()

##
#GUI Codes
##
import tkinter as tk
from PIL import Image, ImageTk
import subprocess
from ImageManip import imageManip
from Camera import Camera

# Main window setup
mainwindow = tk.Tk()
#currentCamera = Camera()

# Create a Frame for the image
imageFrame = tk.Frame(master=mainwindow, relief=tk.RIDGE, borderwidth=10,
                      highlightbackground="white", highlightthickness=10)
imageFrame.grid(row=0, column=0, rowspan=20, columnspan=10)

# Load the original image (for resizing)
currentImage = imageManip("../Image/test.jpg")
initial_width, initial_height = 640, 360
display_image = ImageTk.PhotoImage(currentImage.image_PIL.resize((initial_width, initial_height)))

image_display = tk.Label(master=imageFrame, image=display_image)
image_display.pack()

# Camera Name Label
cameraName = tk.Label(master=mainwindow, text="Camera: Sony A6000")

# Shutter Speed Controls
shutterSpeed = 0
def setShutterSpeed():
    global shutterSpeed
    shutterSpeed = int(shutterSpeedEntry.get())
    currentCamera.set_shutter(shutterSpeed)
    shutterSpeedLabel.config(text="Shutter Speed: " + str(shutterSpeed))

shutterSpeedEntry = tk.Entry(master=mainwindow)
shutterSpeedLabel = tk.Label(master=mainwindow, text="Shutter Speed:")
shutterSpeedSet = tk.Button(master=mainwindow, text="Set", command=setShutterSpeed)

# ISO Controls
iso = 0
def setISO():
    global iso
    iso = int(isoEntry.get())
    currentCamera.set_iso(iso)
    isoLabel.config(text="ISO: " + str(iso))

isoEntry = tk.Entry(master=mainwindow)
isoLabel = tk.Label(master=mainwindow, text="ISO:")
isoSet = tk.Button(master=mainwindow, text="Set", command=setISO)

# Camera Mode Controls
cameraMode = tk.IntVar(value=1)
def setCameraMode():
    if cameraMode.get() == 0:
        cameraModeLabel.config(text="Camera Mode: Auto")
        currentCamera.set_camera_mode("AF-A")
        forgetManual()
    elif cameraMode.get() == 1:
        cameraModeLabel.config(text="Camera Mode: Manual")
        currentCamera.set_camera_mode("Manual")
        packManual()

cameraModeSet = tk.Button(master=mainwindow, text="Set", command=setCameraMode)
autoRadio = tk.Radiobutton(master=mainwindow, text="Auto", variable=cameraMode, value=0)
manualRadio = tk.Radiobutton(master=mainwindow, text="Manual", variable=cameraMode, value=1)
cameraModeLabel = tk.Label(master=mainwindow, text="Camera Mode:")

# Filter Controls
# Function to open the filter window

def update_display_image():
    processed_image = currentImage.image_PIL

    new_width, new_height = 640, 360
    resized_image = processed_image.resize((new_width, new_height))

    new_display_image = ImageTk.PhotoImage(resized_image)

    # Update the image displayed on the Tkinter Label widget
    image_display.config(image=new_display_image)

    # Keep a reference to the image object (important for Tkinter)
    image_display.image = new_display_image
    
    currentImage.save()


def openFilters():
    filterWindow = tk.Tk()
    filterWindow.title("Select Filter")
    
    global filterVar
    filterVar = tk.IntVar() 
    
    def applyFilter():
        print(filterVar.get())
        print("applyFilter() called")
        if(filterVar.get() == 1):
            print("applyMonochrome() called")
            currentImage.applyMonochrome()
        elif(filterVar.get() == 2):
            print("applySepia() called")
            currentImage.applySepia()
        elif(filterVar.get() == 3):
            print("applyBloom() called")
            currentImage.applyBloom()
        else:
            print("No filter function called.")
        
        update_display_image()
        filterWindow.destroy()
        
    def cancel():
        filterWindow.destroy()

    cancelButton = tk.Button(master=filterWindow, text="Cancel", command=cancel)
    applyButton = tk.Button(master=filterWindow, text="Apply", command=applyFilter)

    # Filter options
    monochrome_radio = tk.Radiobutton(filterWindow, text="Monochrome", variable=filterVar, value=1)
    sepia_radio = tk.Radiobutton(filterWindow, text="Sepia", variable=filterVar, value=2)
    bloom_radio = tk.Radiobutton(filterWindow, text="Bloom", variable=filterVar, value=3)

    monochrome_radio.grid(row=1, column=0, columnspan=2, sticky="w")
    sepia_radio.grid(row=2, column=0, columnspan=2, sticky="w")
    bloom_radio.grid(row=3, column=0, columnspan=2, sticky="w")

    cancelButton.grid(row=4, column=0)
    applyButton.grid(row=4, column=1)

    filterWindow.mainloop()

filterButton = tk.Button(master=mainwindow, text="Filter", command=openFilters)

# Reset Controls
def reset():
    global shutterSpeed, iso
    filterVar.set(0)
    cameraMode.set(1)
    shutterSpeed = 0
    iso = 0
    isoLabel.config(text="ISO: ")
    shutterSpeedLabel.config(text="Shutter Speed: ")
    cameraModeLabel.config(text="Camera Mode: ")
    packManual()

resetButton = tk.Button(master=mainwindow, text="Reset", command=reset)

# Show file location
def showFile():
    subprocess.Popen(["open", "/Users/ericartiga/Documents/CMPT_2200/project"])

showFileButton = tk.Button(master=mainwindow, text="Show File Location", command=showFile)

# Timer Controls
timer = 0
def setTimer():
    global timer
    timer = int(timerEntry.get())

timerLabel = tk.Label(master=mainwindow, text="Set Timer: ")
timerEntry = tk.Entry(master=mainwindow)
timerSet = tk.Button(master=mainwindow, text="Set", command=setTimer)

# Photo Distance Controls
photoDistanceMax = 0
photoDistanceMin = 0
def setPhotoDistance():
    global photoDistanceMax, photoDistanceMin
    photoDistanceMin = int(photoDistanceMinEntry.get())
    photoDistanceMax = int(photoDistanceMaxEntry.get())

photoDistanceLabel = tk.Label(master=mainwindow, text="Take Photo After Distance")
photoDistanceLabelMin = tk.Label(master=mainwindow, text="Min: ")
photoDistanceLabelMax = tk.Label(master=mainwindow, text="Max: ")
photoDistanceMaxEntry = tk.Entry(master=mainwindow)
photoDistanceMinEntry = tk.Entry(master=mainwindow)
photoDistanceSet = tk.Button(master=mainwindow, text="Set", command=setPhotoDistance)

# Start Button
def start():
    pass

startButton = tk.Button(master=mainwindow, text="Start", command=start)

# Close Button
def close():
    try:
        filterWindow.destroy()
    except:
        pass
    mainwindow.destroy()

closeButton = tk.Button(master=mainwindow, text="Close", command=close)

# Layout Management

def packMain():
    image_display.pack()

    cameraName.grid(row=0, column=11, columnspan=2)

    shutterSpeedEntry.grid(row=2, column=11, columnspan=2)
    shutterSpeedLabel.grid(row=1, column=11, columnspan=2)
    shutterSpeedSet.grid(row=2, column=13)

    autoRadio.grid(row=6, column=11)
    manualRadio.grid(row=6, column=12)
    cameraModeLabel.grid(row=5, column=11, columnspan=2)
    cameraModeSet.grid(row=6, column=13)

    isoLabel.grid(row=3, column=11, columnspan=2)
    isoEntry.grid(row=4, column=11, columnspan=2)
    isoSet.grid(row=4, column=13)

    imageFrame.grid(row=0, column=0, rowspan=20, columnspan=10)

    filterButton.grid(row=20, column=0)
    resetButton.grid(row=20, column=1)
    showFileButton.grid(row=20, column=2)

    startButton.grid(row=7, column=11)
    closeButton.grid(row=7, column=12)

def packManual():
    timerLabel.grid(row=21, column=1)
    timerEntry.grid(row=21, column=2)
    timerSet.grid(row=21, column=3)

    photoDistanceLabel.grid(row=22, column=0)
    photoDistanceLabelMin.grid(row=22, column=1)
    photoDistanceLabelMax.grid(row=22, column=3)
    photoDistanceMaxEntry.grid(row=22, column=4)
    photoDistanceMinEntry.grid(row=22, column=2)
    photoDistanceSet.grid(row=22, column=5)

def forgetManual():
    timerLabel.grid_forget()
    timerEntry.grid_forget()
    timerSet.grid_forget()
    photoDistanceLabel.grid_forget()
    photoDistanceLabelMin.grid_forget()
    photoDistanceLabelMax.grid_forget()
    photoDistanceMaxEntry.grid_forget()
    photoDistanceMinEntry.grid_forget()
    photoDistanceSet.grid_forget()


# Pack the main window
packMain()

# Run the application
mainwindow.mainloop()

