import tkinter as tk
from PIL import Image, ImageTk

# Create the main Tkinter window
mainwindow = tk.Tk()

# Set window title and size
mainwindow.title("Image Resizer Example")
mainwindow.geometry("800x600")  # Set the window size to 800x600

# Load the image using Pillow (PIL)
image_path = "../Image/test.jpg"  # Replace with your image path
original_image = Image.open(image_path)

# Resize the image (e.g., resizing it to 400x300)
resized_image = original_image.resize((400, 300))

# Convert the resized image to a format Tkinter can use
display_image = ImageTk.PhotoImage(resized_image)

# Create a Label widget to display the image
image_label = tk.Label(master=mainwindow, image=display_image)
image_label.pack()

# Run the Tkinter event loop
mainwindow.mainloop()
