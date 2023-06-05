import tkinter as tk

def compress_image():
    # Add your compression logic here
    pass

# Create the main window
window = tk.Tk()
window.title("Image Compression Website")
window.geometry("400x300")
window.configure(bg="light blue")

# Username and history widget
username_label = tk.Label(window, text="Username", bg="light blue")
username_label.place(x=10, y=10)

history_label = tk.Label(window, text="History", bg="light blue")
history_label.place(x=10, y=40)

# Square box containing the "+" symbol and upload button
box_size = 200
box_frame = tk.Frame(window, width=box_size, height=box_size, bg="white")
box_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

plus_label = tk.Label(box_frame, text="+", font=("Arial", 30), bg="white")
plus_label.pack(pady=20)

upload_button = tk.Button(box_frame, text="Upload", width=10)
upload_button.pack(pady=10)

# Compression settings and compress buttons
settings_button = tk.Button(window, text="Compression Settings", width=15)
settings_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

compress_button = tk.Button(window, text="Compress", width=10, command=compress_image)
compress_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

window.mainloop()
