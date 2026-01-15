import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Hello Tkinter")
window.geometry("300x200")

# Add a label
label = tk.Label(window, text="Hello, VS Code and Tkinter!")
label.pack(pady=20) # Add some padding

# Start the event loop
window.mainloop()
