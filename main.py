from pdfFieldReader import *
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import sv_ttk

def openFile():
    filepath = filedialog.askopenfilename()
    intro_text.delete('1.0', tk.END)
    intro_text.insert(tk.END, filepath)

# window
window = tk.Tk()
window.title("PDF Field Reader")
window.geometry("800x600")

# Widgets
button = ttk.Button(window, text="Click")
intro_text = tk.Text(window)
select_button = ttk.Button(text="SELECT PDF", command=openFile)
saveTXT_button = ttk.Button(text="SAVE TO TXT")
saveCSV_button = ttk.Button(text="SAVE TO CSV")
saveJSON_button = ttk.Button(text="SAVE TO JSON")

select_button.pack()
intro_text.pack()
intro_text.insert(tk.END, "Hello, World!")

# window init
sv_ttk.set_theme("dark")
window.mainloop()