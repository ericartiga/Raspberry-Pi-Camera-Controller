import tkinter as tk
from PIL import Image, ImageTk
import subprocess

mainwindow = tk.Tk()

imageFrame = tk.Frame(master = mainwindow, relief = tk.RIDGE, borderwidth = 10,\
                        highlightbackground = "white", highlightthickness = 10)
DisplayImage = ImageTk.PhotoImage(Image.open("1145263.jpeg").resize((640, 360)))
imageDisplay = tk.Label(master = imageFrame, image = DisplayImage)

cameraName = tk.Label(master = mainwindow, text = "Camera: Placeholder")

shutterSpeed = 0
def setShutterSpeed():
    shutterSpeedLabel.config(text = "Shutter Speed: " + str(shutterSpeedEntry.get()))
    shutterSpeed = int(shutterSpeedEntry.get())
shutterSpeedEntry = tk.Entry(master = mainwindow)
shutterSpeedLabel = tk.Label(master = mainwindow, text = "Shutter Speed:")
shutterSpeedSet = tk.Button(master = mainwindow, text = "Set", command = setShutterSpeed)

iso = 0
def setISO():
    isoLabel.config(text = "ISO: " + str(isoEntry.get()))
    iso = int(isoEntry.get())
isoEntry = tk.Entry(master = mainwindow)
isoLabel = tk.Label(master = mainwindow, text = "ISO:")
isoSet = tk.Button(master = mainwindow, text = "Set", command = setISO)

cameraMode = tk.IntVar(value = 1)
def setCameraMode():
    if cameraMode.get() == 0:
        cameraModeLabel.config(text = "Camera Mode: Auto")
        forgetManual()
    elif cameraMode.get() == 1:
        cameraModeLabel.config(text = "Camera Mode: Manual")
        packManual()
cameraModeSet = tk.Button(master = mainwindow, text = "Set", command = setCameraMode)
autoRadio = tk.Radiobutton(master = mainwindow, text = "Auto", variable = cameraMode, value = 0)
manualRadio = tk.Radiobutton(master = mainwindow, text = "Manual", variable = cameraMode, value = 1)
cameraModeLabel = tk.Label(master = mainwindow, text = "Camera Mode:")

filterVar = tk.IntVar(value = 0)
def openFilters():
    filterWindow = tk.Tk()
    def cancel():
        filterWindow.destroy()
    def apply():
        pass
    cancelButton = tk.Button(master = filterWindow, text = "Cancel", command = cancel)
    applyButton = tk.Button(master = filterWindow, text = "Apply", command = apply)
    noneRadio = tk.Radiobutton(master = filterWindow, text = "None", variable = filterVar, value = 0)
    f1 = tk.Radiobutton(master = filterWindow, text = "f1", variable = filterVar, value = 1)
    f2 = tk.Radiobutton(master = filterWindow, text = "f2", variable = filterVar, value = 2)
    f3 = tk.Radiobutton(master = filterWindow, text = "f3", variable = filterVar, value = 3)
    noneRadio.grid(row = 0, column = 0, columnspan = 2, sticky = "w")
    f1.grid(row = 1, column = 0, columnspan = 2, sticky = "w")
    f2.grid(row = 2, column = 0, columnspan = 2, sticky = "w")
    f3.grid(row = 3, column = 0, columnspan = 2, sticky = "w")
    cancelButton.grid(row = 4, column = 0)
    applyButton.grid(row = 4, column = 1)
    filterWindow.mainloop()
filterButton = tk.Button(master = mainwindow, text = "Filter", command = openFilters)

def reset():
    filterVar.set(0)
    cameraMode.set(1)
    shutterSpeed = 0
    iso = 0
    isoLabel.config(text = "ISO: ")
    shutterSpeedLabel.config(text = "Shutter Speed: ")
    cameraModeLabel.config(text = "Camera Mode: ")
    packManual()
resetButton = tk.Button(master = mainwindow, text = "Reset", command = reset)

def showFile():
    subprocess.Popen(["open","/Users/ericartiga/Documents/CMPT_2200/project"])
showFileButton = tk.Button(master = mainwindow, text = "Show File Location", command = showFile)

timer = 0
def setTimer():
    timer = int(timerEntry.get())
timerLabel = tk.Label(master = mainwindow, text = "Set Timer: ")
timerEntry = tk.Entry(master = mainwindow)
timerSet = tk.Button(master = mainwindow, text = "Set", command = setTimer)

photoDistanceMax = 0
photoDistanceMin = 0
def setPhotoDistance():
    photoDistanceMin = photoDistanceMinEntry.get()
    hotoDistanceMax = photoDistanceMaxEntry.get()
photoDistanceLabel = tk.Label(master = mainwindow, text = "Take Photo After Distance")
photoDistanceLabelMin = tk.Label(master = mainwindow, text = "Min: ")
photoDistanceLabelMax = tk.Label(master = mainwindow, text = "Max: ")
photoDistanceMaxEntry = tk.Entry(master = mainwindow)
photoDistanceMinEntry = tk.Entry(master = mainwindow)
photoDistanceSet = tk.Button(master = mainwindow, text = "Set", command = setPhotoDistance)

def start():
    pass
startButton = tk.Button(master = mainwindow, text = "Start", command = start)

def close():
    try:
        filterWindow.destroy()
    except:
        pass
    mainwindow.destroy()
closeButton = tk.Button(master = mainwindow, text = "Close", command = close)

def packMain():
    imageDisplay.pack()

    cameraName.grid(row = 0, column = 11, columnspan = 2)

    shutterSpeedEntry.grid(row = 2, column = 11, columnspan = 2)
    shutterSpeedLabel.grid(row = 1, column = 11, columnspan = 2)
    shutterSpeedSet.grid(row = 2, column = 13)

    autoRadio.grid(row = 6, column = 11)
    manualRadio.grid(row = 6, column = 12)
    cameraModeLabel.grid(row = 5, column = 11, columnspan = 2)
    cameraModeSet.grid(row = 6, column = 13)

    isoLabel.grid(row = 3, column = 11, columnspan = 2)
    isoEntry.grid(row = 4, column = 11, columnspan = 2)
    isoSet.grid(row = 4, column = 13)

    imageFrame.grid(row = 0, column = 0, rowspan = 20, columnspan = 10)

    filterButton.grid(row = 20, column = 0)
    resetButton.grid(row = 20, column = 1)
    showFileButton.grid(row = 20, column = 2)

    startButton.grid(row = 7, column = 11)
    closeButton.grid(row = 7, column = 12)

def packManual():
    timerLabel.grid(row = 21, column = 1)
    timerEntry.grid(row = 21, column = 2)
    timerSet.grid(row = 21, column = 3)
    photoDistanceLabel.grid(row = 22, column = 0)
    photoDistanceLabelMin.grid(row = 22, column = 1)
    photoDistanceLabelMax.grid(row = 22, column = 3)
    photoDistanceMaxEntry.grid(row = 22, column = 4)
    photoDistanceMinEntry.grid(row = 22, column = 2)
    photoDistanceSet.grid(row = 22, column = 5)

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
    
packMain()
packManual()

mainwindow.mainloop()
