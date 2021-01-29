import tkinter as tk

from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

def greet():
    print(f"Hello, {user_name.get() or 'World' } ! ")

    
root = tk.Tk()
root.title("Hey!")

root.columnconfigure(0, weight = 1)
user_name = tk.StringVar()

input_frame = ttk.Frame(root, padding = (20, 10, 20, 0))
input_frame.grid(row = 0, column = 0, sticky = "EW") # not really necessary "row = 0, column = 0"

name_label = ttk.Label(input_frame, text="Name :")
name_label.grid(row = 0, column = 0,padx=(0,10))
name_entry = ttk.Entry(input_frame, width = 15, textvariable = user_name)
name_entry.grid(row = 0, column = 1)
name_entry.focus()

buttons = ttk.Frame(root, padding = (20, 10))
buttons.grid(row = 1, column = 0, sticky = "EW")

buttons.columnconfigure(0, weight = 1)
buttons.columnconfigure(1, weight = 1)

greet_button = ttk.Button(buttons, text = "Greet", command = greet)
greet_button.grid(row = 0, column = 0, sticky = "EW")  

quit_button = ttk.Button(buttons, text = "Quit", command = root.destroy)
quit_button.grid(row = 0, column = 1, sticky = "EW")

root.mainloop()

'''
side = "left" or "right" or "top" or "bottom
--> side = "top" is default

fill = "x" or "y" or "both"
---> comes with the property to fill the extra space in that dimension

Also let's say if side = "left" and fill = "x"
--> it doesnt work. Because of the reserved space

expand = True
---> expands the size of the button along with the screen

'''
