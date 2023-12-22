import tkinter as tk
import tkinter.messagebox



def close_window():
    root.destroy()

root = tk.Tk()
root.attributes('-fullscreen', True)
root.title("Emergency System")
root.geometry("400x300")
root.config(bg='lightblue')

def open_window(): 
  tk.messagebox.showinfo("Open window", "Emergency Request sent")
  

def open_contacts():
   contact=tk.Tk()
   l1=tk.Label(contact,text="Phone No. - 987654321\nemail - kgfsj@gmail.com")
   l1.pack()
   
def open_about():
   about=tk.Tk()
   l2=tk.Label(about,text="we are here to provide our service to you")
   l2.pack()

def open_feedback():
   feedback=tk.Tk()
   l3=tk.Label(feedback,text="please give a positive feedback or else no one will come to save you:")
   l3.pack()
   feedback_text=tk.Entry(feedback,width=100)
   feedback_text.pack()
   feed_btn=tk.Button(feedback,text="sumbit",command=feedback.destroy)
   feed_btn.pack()


# Nav bar
navbar_frame = tk.Frame(root, bg="lightgrey", height=40)
navbar_frame.pack(side="top", fill="x")

# Bell icon and "REVIVE" text
bell_icon = tk.Label(navbar_frame, text="🔔", font=("Arial", 12), bg="beige")
bell_icon.pack(side="left", padx=10)
revive_label = tk.Label(navbar_frame, text="REVIVE", font=("Arial", 10, "bold"), bg="beige")
revive_label.pack(side="left")

# Search bar
search_bar = tk.Entry(root, width=50).place(x=680, y=50)
search_bar_text = tk.Label(search_bar, text="Search", font=("Arial", 10, "bold") )
search_btn=tk.Button(root,text="search")
search_btn.place(x=1000,y=50)
# Navigation buttons

contact_btn = tk.Button(navbar_frame, font=("Arial", 10), bg="beige",command=open_contacts,text="contact us")
contact_btn.pack(side="left", padx=20)


about_btn = tk.Button(navbar_frame, text="about us",font=("Arial", 10), bg="beige",command=open_about)
about_btn.pack(side="left", padx=20)


feedback_btn = tk.Button(navbar_frame,text="feedback" ,font=("Arial", 10), bg="beige",command=open_feedback)
feedback_btn.pack(side="left", padx=20)


# Emergency Button
emergency_button = tk.Button(root, text="Emergency", font=("Arial", 20, "bold"), bg="lightgreen", width=15,command=open_window)
emergency_button.place(relx=0.5, rely=0.4, anchor="center")

# Exit Button
exit_button = tk.Button(root, text="Exit", font=("Arial", 12), bg="lightgrey", fg="black", width=10, command=close_window)
exit_button.place(relx=0.5, rely=0.9, anchor="s")   

root.mainloop()
