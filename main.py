from pdfFieldReader import extract_pdf_fields
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import sv_ttk
import csv
import json

# global variables
filepath = ''
fields_dict = {}

##### MAIN LOGIC #####
# opens a file dialog and stores the selected file path
def openFile():
    global filepath
    filepath = filedialog.askopenfilename()
    global fields_dict
    fields_dict = extract_pdf_fields(filepath)
    displayField(fields_dict)

    print(filepath)
    saveTXT_button.config(state="normal") # enable buttons
    saveCSV_button.config(state="normal")
    saveJSON_button.config(state="normal")
# loads PDF fields into text display widget
def displayField(dict):
    if not dict:
        display_text.delete('1.0',tk.END)
        display_text.insert(tk.END, "No Fields Found")
    for field_name, field_value in dict.items():
        display_text.insert(tk.END, f"Field: {field_name}, Value: {field_value}\n")

### Save to File Functions ###
# saves field and values into a text file
def saveToText():
    file = filedialog.asksaveasfile(defaultextension='.txt', initialdir=filepath, filetypes=[('Text file', '.txt')])
    if file is None:
        return
    filetext = ''
    for field_name, field_value in fields_dict.items():
        filetext += f"{field_name}: {field_value}\n"
    file.write(filetext)
    file.close()
# saves field and values into a csv file
def saveToCSV():
    file = filedialog.asksaveasfile(defaultextension='.txt', initialdir=filepath, filetypes=[('CSV file', '.csv')])
    if file is None:
        return
    with open(file.name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for field_name, field_value in fields_dict.items():
            writer.writerow([field_name,field_value])
    csv_file.close()
# save field and values into a JSON file
def saveToJSON():
    file = filedialog.asksaveasfile(defaultextension='.json', initialdir=filepath, filetypes=[('JSON file', '.json')])
    if file is None:
        return
    with open(file.name, 'w') as json_file:
        json.dump(fields_dict, json_file, indent=4)
    json_file.close()


##### TKINTER SETUP #####
# Window Setup
window = tk.Tk()
window.title("PDF Field Extractor")
window.geometry("800x600")
window.resizable(False, False)

# Widgets
intro_label = tk.Label(window, width=300, height=50,wraplength=200,
                        text="This tool reads the fields in a pdf and allows you to export it into a file")
display_text = tk.Text(window)
select_button = ttk.Button(text="SELECT PDF", command=openFile)
saveTXT_button = ttk.Button(text="SAVE TO TXT", command=saveToText, state=tk.DISABLED)
saveCSV_button = ttk.Button(text="SAVE TO CSV", command=saveToCSV, state=tk.DISABLED)
saveJSON_button = ttk.Button(text="SAVE TO JSON", command=saveToJSON, state=tk.DISABLED)

# Layout
intro_label.place(x=25,y=10,width=350,height=50)
display_text.place(width=390,height=550,x=390,y=10)
select_button.place(width=350,height=50,x=15,y=70)
saveTXT_button.place(width=250,x=65,y=135)
saveCSV_button.place(width=250,x=65,y=175)
saveJSON_button.place(width=250,x=65,y=215)

# Window init
sv_ttk.set_theme("dark")
window.mainloop()