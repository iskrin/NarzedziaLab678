import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import main

def browseFile(entry):
    filepath = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, filepath)

def browseDirectory(entry):
    filepath = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, filepath)

root = tk.Tk()
root.title("File Converter")

header1 = tk.Label(root, text="Wybierz plik do konwersji:")
header1.grid(row=0, column=0, sticky="w", padx=10, pady=3)

entry1 = tk.Entry(root, width=50)
entry1.grid(row=1, column=0, padx=10, pady=3)

button1 = tk.Button(root, text="Browse", command=lambda: browseFile(entry1))
button1.grid(row=1, column=1, padx=10)

header2 = tk.Label(root, text="Wybierz ścieżkę wyjściową")
header2.grid(row=2, column=0, sticky="w", padx=10, pady=3)

entry2 = tk.Entry(root, width=50)
entry2.grid(row=3, column=0, padx=10, pady=5)

button2 = tk.Button(root, text="Browse", command=lambda: browseDirectory(entry2))
button2.grid(row=3, column=1, padx=10)

header3 = tk.Label(root, text="Wybierz rozszerzenie wyjściowe:")
header3.grid(row=4, column=0, padx=10, pady=3, columnspan=2)

inputOptions = ttk.Combobox(root, state="readonly") 
inputOptions['values'] = ('json', 'xml', 'yaml') 
inputOptions.grid(column = 0, row = 5, columnspan=2) 


button3 = tk.Button(root, text="Konwertuj", command=lambda: main.convert(entry1.get(), inputOptions.get(), entry2.get()))
button3.grid(row=6, column=0, padx=10, pady=5, columnspan=2)


root.mainloop()
