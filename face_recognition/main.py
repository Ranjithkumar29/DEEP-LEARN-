import tkinter as tk
from tkinter import*
from PIL import ImageTk, Image
import recognition
import registration
import showcsv
import sys

def login():
    # Create a Tkinter window
    root = tk.Tk()
    root.title(" Attendance System ")
    
    
    # Load the background image
    bg_image = Image.open("assets/ChatGPT Image Aug 25, 2025, 08_54_20 PM.png")
    bg_image = ImageTk.PhotoImage(bg_image)
    
    # Create a label for the background image
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    # Create Image objects for the images
    image1 = Image.open("assets/recognize.png").resize((100, 100))
    image2 = Image.open("assets/registration.png").resize((100, 100))
    image3 = Image.open("assets/attendance.jpg").resize((100, 100))
    image4 = Image.open("assets/database.jpg").resize((100, 100))
    image5 = Image.open("assets/exit.png").resize((100, 100))
    
    # Convert Image objects to PhotoImage objects
    image1 = ImageTk.PhotoImage(image1)
    image2 = ImageTk.PhotoImage(image2)
    image3 = ImageTk.PhotoImage(image3)
    image4 = ImageTk.PhotoImage(image4)
    image5 = ImageTk.PhotoImage(image5)
    
    # Create image buttons using the PhotoImage objects
    button1 = tk.Button(root, image=image1,command=lambda: recognition.recognize())
    button2 = tk.Button(root, image=image2,command=lambda: registration.register())
    button3 = tk.Button(root, image=image3,command=lambda: showcsv.display("Attendance.csv",'Attendance'))
    button4 = tk.Button(root, image=image4,command=lambda: showcsv.display("Database.csv",'Student Details'))
    button5 = tk.Button(root, image=image5,command=lambda: exit())
    
    button1.place(x=185, y=350)
    button2.place(x=560, y=350)
    button3.place(x=935, y=350)
    button4.place(x=185, y=560)
    button5.place(x=800, y=620)
    
    def exit():
        print ("exiting")
        sys.exit()
        
    # Start the Tkinter event loop
    root.mainloop()

