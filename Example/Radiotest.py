import tkinter as tk

def display_selection():
    # Display the selected value of filterVar
    selection = filterVar.get()
    label.config(text=f"Selected value: {selection}")

# Create the main window
root = tk.Tk()
root.title("Radio Button Test")

# Create the IntVar to hold the selected filter value
filterVar = tk.IntVar(value=0)  # Default value is 0 (no selection)

# Create the radio buttons for testing
radio1 = tk.Radiobutton(root, text="Option 1", variable=filterVar, value=1)
radio2 = tk.Radiobutton(root, text="Option 2", variable=filterVar, value=2)
radio3 = tk.Radiobutton(root, text="Option 3", variable=filterVar, value=3)

# Pack the radio buttons into the window
radio1.pack()
radio2.pack()
radio3.pack()

# Add a button to display the selected radio button's value
button = tk.Button(root, text="Show Selection", command=display_selection)
button.pack()

# Label to display the current selection
label = tk.Label(root, text="Selected value: 0")
label.pack()

# Start the Tkinter main loop
root.mainloop()
