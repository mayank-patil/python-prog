import tkinter as tk
from tkinter import ttk
import webbrowser

def dorebell(event):
    print("Someone?? Rang!! the Door bell!!")
def open_g(event):
    webbrowser.open_new_tab("https://google.co.in")

window = tk.Tk()
window.geometry("300x200")

alabel = ttk.Label(text="Banana")
alabel.grid(column=0,row=0)

blabel = ttk.Label(text="Apple")
blabel.grid(column=1,row=0)

button = tk.Button(window,text="Doorbell")
button.grid(column=0)

button2 = tk.Button(window,text="10")
button2.grid(column=1, row=1)

button.bind("<Button-1>", dorebell)
button2.bind("<Button-1>", open_g)

window.mainloop()
