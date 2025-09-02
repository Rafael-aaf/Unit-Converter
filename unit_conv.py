import tkinter as tk

conversion_rates = {
    "Pounds": [0.4536, "kg"],
    "Inches": [2.54, "cm"],
    "Feet": [0.3048, "m"],
    "Kg": [2.2046, "lb"],
    "Cm": [0.3937, "in"],
    "Meters": [3.2808, "ft"]
}

def convert(x):
    value = x * conversion_rates.get(var.get())[0]
    return value

#GUI
root = tk.Tk()
root.geometry("300x200")
root.title("Unit Converter")
root.configure(bg="#B5FFF6")

#User Input
entry = tk.Entry(root, font = 8, borderwidth = 5)
entry.grid(row=0, column=0, padx=5, pady=(40, 5))
entry.configure(bg="white")

#Dropdown
var = tk.StringVar()
var.set("Units")
drop = tk.OptionMenu(root, var, "Pounds",  "Inches", "Feet", "Kg", "Cm", "Meters")
drop.grid(row=0, column=1, padx=5, pady=(40, 5))
drop.configure(bg="white", width=6)

#Button
def button_action():
    num = float(entry.get())
    value = convert(num)
    myLabel.config(text = f"{value} {conversion_rates.get(var.get())[1]}")

Button = tk.Button(root, text = "Convert", command = button_action)
Button.grid(row=1, column=0, columnspan=2, pady=20)
Button.configure(bg="white")

#Label
myLabel = tk.Label(root, text="")
myLabel.grid(row=2, column=0, columnspan=2, pady=5)
myLabel.configure(bg="#B5FFF6")

root.mainloop()