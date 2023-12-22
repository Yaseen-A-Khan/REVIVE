import tkinter as tk

def close_window():
    root.destroy()

root = tk.Tk()
root.attributes('-fullscreen', True)
root.title("Emergency System")
root.geometry("400x300")

# Nav bar
navbar_frame = tk.Frame(root, bg="lightblue", height=40)
navbar_frame.pack(side="top", fill="x")

# Bell icon and "REVIVE" text
bell_icon = tk.Label(navbar_frame, text="🔔", font=("Arial", 12), bg="lightblue")
bell_icon.pack(side="left", padx=10)
revive_label = tk.Label(navbar_frame, text="REVIVE", font=("Arial", 10, "bold"), bg="lightblue")
revive_label.pack(side="left")

# Search bar
search_bar = tk.Entry(navbar_frame, width=20)
search_bar.pack(side="top", padx=10)

# Navigation buttons
nav_buttons = ["Home", "About Us", "Feedback"]
for nav_button in nav_buttons:
    btn = tk.Button(navbar_frame, text=nav_button, font=("Arial", 10), bg="lightblue")
    btn.pack(side="left", padx=20)

# Emergency Button
emergency_button = tk.Button(root, text="Emergency", font=("Arial", 12, "bold"), bg="lightgreen", width=15)
emergency_button.place(relx=0.5, rely=0.4, anchor="center")

# Exit Button
exit_button = tk.Button(root, text="Exit", font=("Arial", 10), bg="grey", fg="red", width=10, command=close_window)
exit_button.place(relx=0.5, rely=0.9, anchor="s")

root.mainloop()
