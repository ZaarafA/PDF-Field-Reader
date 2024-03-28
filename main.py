from pdfFieldReader import *
import tkinter as tk
from tkinter import ttk
import sv_ttk

# window
window = tk.Tk()
window.title("PDF Field Reader")
window.geometry("800x600")

button = ttk.Button(window, text="Click")
button.pack()

sv_ttk.set_theme("dark")
window.mainloop()