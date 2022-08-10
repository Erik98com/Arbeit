import tkinter as tk

goods = {'Schrauben': 0.07, 'Muttern': 0.04, 'Unterlegscheiben': 0.02}
valuesGoods = list(goods.values())


def hornbach():
    val1 = input1.get()
    val2 = input2.get()
    val3 = input3.get()
    valList = (val1, val2, val3)
    price = 0
    count = 0

    for actLoopValue in valList:
        if not actLoopValue == "":
            var = int(actLoopValue) # filtert Texteingaben nicht raus
        else:
            var = 0
        price = var * valuesGoods[count] + price
        count += 1

    result.config(text=price)


window = tk.Tk()
window.geometry("1000x700")

label1 = tk.Label(window, text='Anzahl Schrauben:  ')
label1.grid(row=0, column=0)

label2 = tk.Label(window, text='Anzahl Muttern:  ')
label2.grid(row=1, column=0)

label3 = tk.Label(window, text='Anzahl Unterlegscheiben:  ')
label3.grid(row=2, column=0)

input1 = tk.Entry(window)
input1.grid(row=0, column=1)

input2 = tk.Entry(window)
input2.grid(row=1, column=1)

input3 = tk.Entry(window)
input3.grid(row=2, column=1)

btShowResult = tk.Button(window, text='Ergebnis', command=hornbach) # Verweis auf Funktion calculate()
btShowResult.grid(row=3, column=1)

result = tk.Label(window)
result.grid(row=3, column=2)

window.mainloop()
