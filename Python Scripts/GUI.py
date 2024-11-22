# ##
# #GPIO Codes
# ##

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG_PIN = 16
ECHO_PIN = 21

GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

GPIO.output(TRIG_PIN,GPIO.LOW)
print("waiting for ultrasonic sensor to initialize")
time.sleep(2)

# #PIN for 7 Segment LED

# #PIN for Buttons
# BLUE_BUTTON = 22
# BLACK_BUTTON = 17
# GPIO.setup(BLUE_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(BLACK_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# #PIN for Buzzer

# #PIN for LEDs


##
#GUI Codes
##
import tkinter as tk
from PIL import Image, ImageTk
import subprocess
from ImageManip import imageManip
from camera import Camera
import sys
import threading

# Main window setup
mainwindow = tk.Tk()
mainwindow.config(bg="#E4A6D5", relief="sunken", borderwidth=2)
mainwindow.resizable(False, False)
mainwindow.geometry("940x728")

currentCamera = Camera()

# Create a Frame for the image
imageFrame = tk.Frame(master=mainwindow, borderwidth=30, 
                      highlightbackground="black", highlightthickness=2, bg = "white", padx=10,pady=10)
controlFrame = tk.Frame(master=mainwindow, highlightbackground="black",  bg = "beige", padx=10,pady=10, highlightthickness=2)
modeFrame = tk.Frame(master=mainwindow, highlightbackground="black",  bg = "beige", padx=25,pady=10, highlightthickness=2)
otherFrame = tk.Frame(master=mainwindow, highlightbackground="black",  bg = "beige", padx=25,pady=10, highlightthickness=2)
infoFrame = tk.Frame(master=mainwindow,  bg = "black", padx=392,pady=10)
manualFrame = tk.Frame(master=mainwindow, highlightbackground="black",  bg = "beige", padx=20,pady=30, highlightthickness=2)
autoFrame = tk.Frame(master=mainwindow, highlightbackground="black",  bg = "beige", padx=25,pady=10, highlightthickness=2)
featureFrame = tk.Frame(master=mainwindow, highlightbackground="black",  bg = "beige", padx=22,pady=15, highlightthickness=2)

# Load the original image (for resizing)
global currentImage
currentImage = imageManip("./__pycache__/temp.jpg")
initial_width, initial_height = 640, 360
display_image = ImageTk.PhotoImage(currentImage.image_PIL.resize((initial_width, initial_height)))

image_display = tk.Label(master=imageFrame, image=display_image)    


#features:
# Timer Controls
def timerIncrement():
    current_value = int(timerEntry.get())  
    if current_value < 9:  
        current_value += 1  
    timerEntry.delete(0, tk.END)  
    timerEntry.insert(0, str(current_value))  
def timerDecrement():
    current_value = int(timerEntry.get()) 
    if current_value > 0:  
        current_value -= 1  
    timerEntry.delete(0, tk.END)  
    timerEntry.insert(0, str(current_value))  
    
timerLabel = tk.Label(master=featureFrame, text="Set Timer: ", bg="beige")
timerEntry = tk.Entry(master=featureFrame, justify='center', width=15)
timerEntry.insert(0, 0)
timerIncreButton = tk.Button(master=featureFrame, text="^", padx=25,pady=2, bg="lightgrey", command = timerIncrement)
timerDecreButton = tk.Button(master=featureFrame, text="v", padx=25,pady=2, bg="lightgrey", command = timerDecrement)


# Camera Name Label
cameraName = tk.Label(master=infoFrame, text=currentCamera.get_camera_name(), bg="black", fg="white")
# ~ cameraName = tk.Label(master=infoFrame, text="Test", bg="black", fg="white")

# Camera Battery Label
def test():
    return

def updateBatteryLabel():
    battery_life = currentCamera.Camera.get_battery_life()
    cameraBattery.config(text=f"Battery: {battery_life}%")
    mainwindow.after(10000, updateBatteryLabel)

cameraBattery = tk.Label(master=infoFrame, text=("Battery: " + currentCamera.get_battery_life()), bg="black", fg="white")
# ~ cameraBattery = tk.Label(master=infoFrame, text=("Battery: "), bg="black", fg="white")

# Aperture Controls
aperture = str(currentCamera.get_aperture())
def setAperture():
    currentCamera.set_aperture(str(apertureEntry.get()))
    aperture = str(currentCamera.get_aperture())
    apertureLabel.config(text="Aperture: " + aperture)
    apertureEntry.delete(0, 'end')
    apertureEntry.insert(0, aperture)

apertureEntry = tk.Entry(master=controlFrame, justify='center')
apertureEntry.insert(0, aperture)
apertureLabel = tk.Label(master=controlFrame, text="Aperture: " + aperture, padx=10,pady=5, bg="beige")
apertureIncrement = tk.Button(master=controlFrame, text=">", padx=25,pady=2, bg="lightgrey", command = test)
apertureDecrement = tk.Button(master=controlFrame, text="<", padx=25,pady=2, bg="lightgrey", command = test)

##Shutterspeed control
shutterSpeed = str(currentCamera.get_shutter())
def setShutterSpeed():
    currentCamera.set_shutter(shutterSpeedEntry.get())
    shutterSpeed = str(currentCamera.get_shutter())
    shutterSpeedLabel.config(text="Shutter Speed: " +shutterSpeed)
    shutterSpeedEntry.delete(0, 'end')
    shutterSpeedEntry.insert(0, shutterSpeed)

shutterSpeedEntry = tk.Entry(master=controlFrame, justify='center')
shutterSpeedEntry.insert(0, shutterSpeed)
shutterSpeedLabel = tk.Label(master=controlFrame, text="Shutter Speed: " + shutterSpeed, padx=10,pady=10, bg="beige")
shutterSpeedIncrement = tk.Button(master=controlFrame, text=">", padx=25,pady=2, bg="lightgrey", command = test)
shutterSpeedDecrement = tk.Button(master=controlFrame, text="<", padx=25,pady=2, bg="lightgrey", command = test)
                          
# ISO Controls
iso = str(currentCamera.get_iso())
def setISO():
    currentCamera.set_iso(str(isoEntry.get()))
    iso = str(currentCamera.get_iso())
    isoLabel.config(text="ISO: " + iso)
    isoEntry.delete(0, 'end')
    isoEntry.insert(0, iso)

isoEntry = tk.Entry(master=controlFrame, justify='center')
isoEntry.insert(0, iso)
isoLabel = tk.Label(master=controlFrame, text="ISO: " + iso, padx=10,pady=5, bg="beige")
isoIncrement = tk.Button(master=controlFrame, text=">", padx=25,pady=2, bg="lightgrey", command = test)
isoDecrement = tk.Button(master=controlFrame, text="<", padx=25,pady=2, bg="lightgrey", command = test)
                          
# Camera Mode Controls

cameraMode = tk.IntVar(value=currentCamera.get_camera_mode())
def convertToStr(num):
    if not num:
        return "Manual"
    else:
        return "AF-A"
def setCameraMode():
    if cameraMode.get() == currentCamera.get_camera_mode():
        print("Already in selected mode")
        return
    if cameraMode.get() == 1:
        cameraModeLabel.config(text="Mode: Auto")
        currentCamera.set_camera_mode("AF-A")
        packAuto()
    elif cameraMode.get() == 0:
        cameraModeLabel.config(text="Mode: Manual")
        currentCamera.set_camera_mode("Manual")
        packManual()
        
        
cameraModeLabel = tk.Label(master=modeFrame, text="Mode: " + convertToStr(cameraMode.get()), padx=10,pady=10, bg="beige")
cameraModeSet = tk.Button(master=modeFrame, text="Set", command=setCameraMode, padx=50, pady=5, bg="#FEB112")
autoRadio = tk.Radiobutton(master=modeFrame, text="Auto", variable=cameraMode, value=1, bg="beige", bd =0, relief="flat", highlightthickness=0, pady=5)
manualRadio = tk.Radiobutton(master=modeFrame, text="Manual", variable=cameraMode, value=0, bg="beige", bd =0, relief="flat", highlightthickness=0, pady=5)


def setControlValues():
    setAperture()
    setISO()
    setShutterSpeed()
controlSet = tk.Button(master=controlFrame, text="Set", command=setControlValues, padx=50,pady=15, bg="#FEB112")

## GUI OPERATION ##
def update_display_image():
    processed_image = currentImage.image_PIL

    new_width, new_height = 640, 360
    resized_image = processed_image.resize((new_width, new_height))

    new_display_image = ImageTk.PhotoImage(resized_image)

    # Update the image displayed on the Tkinter Label widget
    image_display.config(image=new_display_image)

    # Keep a reference to the image object (important for Tkinter)
    image_display.image = new_display_image


# Camera operation
def takePhoto():
    countdown = int(timerEntry.get())
    if countdown != 0:
        for i in range(countdown):
            time.sleep(1)
            print(i)
    currentCamera.take_photo()
    currentImage.updateImage("__pycache__/temp.jpg")
    update_display_image()
        
photoButton = tk.Button(master=mainwindow, text="Snap!", command=takePhoto, padx = 40, pady = 40)

def autofocus():
    currentCamera.focus_camera()

focusButton = tk.Button(master=mainwindow, text="Focus", command=autofocus, padx = 60, pady = 10)

### Camera Processing ###
def openFilters():
    filterWindow = tk.Toplevel(master=mainwindow)
    filterWindow.title("Select Filter")
    
    filterVar = tk.IntVar(value=0) 
    
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
    radio1 = tk.Radiobutton(master=filterWindow, text="Monochrome", variable=filterVar, value=1)
    radio2 = tk.Radiobutton(master=filterWindow, text="Sepia", variable=filterVar, value=2)
    radio3 = tk.Radiobutton(master=filterWindow, text="Bloom", variable=filterVar, value=3)

    radio1.grid(row=1, column=0, columnspan=2, sticky="w")
    radio2.grid(row=2, column=0, columnspan=2, sticky="w")
    radio3.grid(row=3, column=0, columnspan=2, sticky="w")

    cancelButton.grid(row=4, column=0)
    applyButton.grid(row=4, column=1)

    filterWindow.mainloop()

filterButton = tk.Button(master=otherFrame, text="Filter", command=openFilters, padx=10,pady=10,bg="pink")
    
### File manipulation Processing ###
def resetImage():
    currentImage.image_PIL = currentImage.original_image
    update_display_image()
resetButton = tk.Button(master=otherFrame, text="Reset", command=resetImage, padx=10,pady=10,bg="#FEB112")

# Show file location
def savetoFile():
    subprocess.Popen(["open", "../Image/"])

saveFileButton = tk.Button(master=otherFrame, text="Save your Image!", command=savetoFile, padx=10,pady=10,bg="lightgreen")
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
# Photo Distance Controls
def getSubjectDistance():
    print("Getting the subject distance...")
    GPIO.output(TRIG_PIN, GPIO.HIGH)
    time.sleep(0.00001)  
    GPIO.output(TRIG_PIN, GPIO.LOW)

    pulse_send = 0
    pulse_received = 0
    start_time = time.time()  
    timeout = 5  

    while GPIO.input(ECHO_PIN) == 0:
        pulse_send = time.time()
        if time.time() - start_time > timeout:
            print("Timeout: No subject detected.")
            return None  

    while GPIO.input(ECHO_PIN) == 1:
        pulse_received = time.time()
        if time.time() - start_time > timeout:
            print("Timeout: No pulse detected.")
            return None  

    # Calculate the distance
    distance = float(((pulse_received - pulse_send) * 34300) / 2) /100 # Speed of sound is 34300 cm/s
    distance = round(distance, 1)
    SubjectDistanceLabel.config(text="Focus Guideline: " + str(distance) +"m")
    return distance
    
SubjectDistanceLabel = tk.Label(master=manualFrame, text="Focus Guideline: Unknown", bg="beige")
startRangingLabel = tk.Button(master=manualFrame, text="Get the subject distance!", command=getSubjectDistance, padx=10,pady=10)

# Layout Management
# Close Button
def close():
    try:
        filterWindow.destroy()
    except:
        pass
    mainwindow.destroy()
    sys.exit()
closeButton = tk.Button(master=otherFrame, text="Close", command=close,padx=10,pady=10,bg="red")
    
def packMain():
    for i in range(30):
        mainwindow.rowconfigure(i, weight=1, minsize=5)  

    for i in range(18):
        mainwindow.columnconfigure(i, weight=1, minsize=5)  
    
    mainwindow.title("Remote Control Interface: " + currentCamera.get_camera_name())
    # Image packing
    image_display.grid(row=0, column=0, columnspan=11, rowspan=11)
    if(cameraMode.get() == 0):
        packManual()
    else:
        packAuto()
    #Frame
    imageFrame.grid(row=1, column=0, sticky="nsew", columnspan=11, rowspan=11)
    controlFrame.grid(row=1, column=12, columnspan=2, rowspan=2)
    modeFrame.grid(row=6, column=12, columnspan=2, rowspan=5)
    otherFrame.grid(row=14, column = 9, columnspan=2, rowspan=3)
    infoFrame.grid(row = 30, columnspan=18)
    featureFrame.grid(row=14, column = 0, columnspan=1, rowspan=2)
    
    ##timer label
    timerLabel.grid(row=0, column=0, columnspan=2)
    timerEntry.grid(row=1, column=0, columnspan=2)
    timerIncreButton.grid(row=0, column=5)
    timerDecreButton.grid(row=1,column=5)
    # ~ timerSet.grid(row=0, column=4, columnspan=2)
    
    # Camera name and battery labels
    cameraName.grid(row=0, column=0, columnspan=2)
    cameraBattery.grid(row=0, column=2, columnspan=2)

    # Aperture Speed label
    apertureLabel.grid(row=1, column=3, columnspan=2)
    apertureEntry.grid(row=2, column=3, columnspan=2)
    apertureIncrement.grid(row=3, column=4)
    apertureDecrement.grid(row=3, column=3)

    # Shutter Speed label
    shutterSpeedLabel.grid(row=4, column=3, columnspan=2)
    shutterSpeedEntry.grid(row=5, column=3, columnspan=2)
    shutterSpeedIncrement.grid(row=6, column=4)
    shutterSpeedDecrement.grid(row=6, column=3)

    # ISO Label
    isoLabel.grid(row=7, column=3, columnspan=2)
    isoEntry.grid(row=8, column=3, columnspan=2)
    isoIncrement.grid(row=9, column=4)
    isoDecrement.grid(row=9, column=3)

    # Set button
    controlSet.grid(row=10, column=3, columnspan=2)

    # Camera Mode
    cameraModeLabel.grid(row=1, column=3, columnspan=2)
    autoRadio.grid(row=2, column=3)
    manualRadio.grid(row=2, column=4)
    cameraModeSet.grid(row=3, column=3, columnspan=2, rowspan=2)

    # Control Buttons
    filterButton.grid(row=4, column=1, columnspan=1, rowspan=2)
    resetButton.grid(row=4, column=2, columnspan=1, rowspan=2)
    closeButton.grid(row=4, column=3, columnspan=1, rowspan=2)
    saveFileButton.grid(row=9, column=1, columnspan=3)
    
    photoButton.grid(row=15, column = 12, rowspan=3, columnspan=4)
    

def packManual():
    autoFrame.grid_forget()
    focusButton.grid_forget()
    manualFrame.grid(row=14, column = 4, columnspan=1, rowspan=2)
    SubjectDistanceLabel.grid()
    startRangingLabel.grid()

    
def packAuto():
    manualFrame.grid_forget()
    autoFrame.grid(row = 18, column = 3, columnspan=5)
    focusButton.grid(row=19, column = 12, rowspan=3, columnspan=4)

# Pack the main window
packMain()

# Run the application
mainwindow.mainloop()

