import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")  # 24-hour format
    label.config(text=current_time)
    label.after(1000, update_time)  # Update every 1 second

# Create window
root = tk.Tk()
root.title("🕒 Digital Clock")
root.geometry("400x150")
root.resizable(False, False)

# Clock label
label = tk.Label(root, font=("Arial", 50, "bold"), bg="black", fg="lime")
label.pack(expand=True, fill="both")

# Start the clock
update_time()

root.mainloop()
