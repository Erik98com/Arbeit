import tkinter as tk

columns = "1"

#zum Setzen der Variable calculation auf die Nutzerauswahl
def callback(selection):
    global columns
    columns = int(selection)

def buildTable():
    global columns
    rows = rowsEntry.get()
    try:
        rows = int(rows)
    except:
        rows = 1
    for i in range(rows):  # Rows
        for j in range(columns):  # Columns
            b = tk.Entry(frameRight, text="")
            b.grid(row=i+2, column=j+2)

windows = tk.Tk()
windows.geometry("1000x700")

frameLeft = tk.Frame(windows)
frameLeft.pack(anchor="n", side="left", padx=10, pady=10)

frameRight = tk.Frame(windows)
frameRight.pack(anchor="n", side="left", padx=10, pady=10)

numberColumns = ["1", "2", "3", "4", "5"]

pasteAsString = tk.StringVar(windows)
pasteAsString.set(numberColumns[0]) # Standardauswahl der Rechenoperation

userSelection = tk.OptionMenu(frameLeft, pasteAsString, *numberColumns, command=callback) #Verweis auf callback()
userSelection.config(font=('Helvetica', 12))
userSelection.grid(row=1, column=1)

label1 = tk.Label(frameLeft, text='Wie viele Zeilen?: ')
label1.grid(row=0, column=0)

label2 = tk.Label(frameLeft, text='Wie viele Spalten?: ')
label2.grid(row=1, column=0)

rowsEntry = tk.Entry(frameLeft)
rowsEntry.grid(row=0, column=1)

btCreateTable = tk.Button(frameLeft, text='Create Table', command=buildTable) # Verweis auf Funktion calculate()
btCreateTable.grid(row=2, column=0)

windows.mainloop()