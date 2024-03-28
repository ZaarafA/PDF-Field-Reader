from pdfFieldReader import *
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import sv_ttk

filepath = ''

# opens a file dialog and stores the selected file path
def openFile():
    global filepath
    filepath = filedialog.askopenfilename()
    print(filepath)

# window
window = tk.Tk()
window.title("PDF Field Reader")
window.geometry("800x600")
window.resizable(False, False)

# Widgets
intro_label = tk.Label(window, width=300, height=50,wraplength=200,
                        text="This tool reads the fields in a pdf and allows you to export it into a file")
display_text = tk.Text(window)
select_button = ttk.Button(text="SELECT PDF", command=openFile)
saveTXT_button = ttk.Button(text="SAVE TO TXT")
saveCSV_button = ttk.Button(text="SAVE TO CSV")
saveJSON_button = ttk.Button(text="SAVE TO JSON")

# Layout
intro_label.place(x=25,y=10,width=350,height=50)
display_text.place(width=390,height=550,x=390,y=10)
select_button.place(width=350,height=50,x=15,y=70)
saveTXT_button.place(width=250,x=65,y=135)
saveCSV_button.place(width=250,x=65,y=175)
saveJSON_button.place(width=250,x=65,y=215)


# window init
sv_ttk.set_theme("dark")
window.mainloop()