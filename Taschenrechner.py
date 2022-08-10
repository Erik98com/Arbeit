import tkinter as tk

columns = "Addition"
val1 = 0

#zum Setzen der Variable calculation auf die Nutzerauswahl
def callback(selection):
    global columns
    calculation = selection

def calculate():
    global columns
    val1 = input1.get()
    val2 = input2.get()

    # prüfen, ob Eingabe leer ist, bei leerer Eingabe Wert = 0
    if not val1 == "":
        val1 = float(input1.get())
    else:
        val1 = 0

    if not val2 == "":
        val2 = float(input2.get())
    else:
        val2 = 0

    if calculation == "Addition":
        output.config(text=val1+val2)
    elif calculation == "Subtraktion":
        output.config(text=val1-val2)
    elif calculation == "Multiplikation":
        output.config(text=val1*val2)
    else:#Test, ob Eingabe2 == 0
        try:
            output.config(text=val1/val2)
        except ZeroDivisionError:
            output.config(text="Division durch 0 nicht möglich!")


windows = tk.Tk()
windows.geometry("1000x700")

arithmeticOperations = ["Addition", "Subtraktion", "Multiplikation", "Division"]

pasteAsString = tk.StringVar(windows)
pasteAsString.set(arithmeticOperations[0]) # Standardauswahl der Rechenoperation

userSelection = tk.OptionMenu(windows, pasteAsString, *arithmeticOperations, command=callback) #Verweis auf callback()
userSelection.config(font=('Helvetica', 12))
userSelection.grid(row=0, column=2)

label1 = tk.Label(windows, text='Zahl 1:  ')
label1.grid(row=0, column=0)

label2 = tk.Label(windows, text='Zahl 2:  ')
label2.grid(row=1, column=0)

input1 = tk.Entry(windows)
input1.grid(row=0, column=1)

input2 = tk.Entry(windows)
input2.grid(row=1, column=1)

btShowResult = tk.Button(windows, text='Ergebnis', command=calculate) # Verweis auf Funktion calculate()
btShowResult.grid(row=2, column=1)

output = tk.Label(windows)
output.grid(row=2, column=2)

windows.mainloop()
