import tkinter as tk
from tkinter import ttk
import requests

root = tk.Tk()
root.geometry("360x200")
root.title("Euro-in-Fr calculator")
eurodesk = 'https://api.exchangerate-api.com/v4/latest/Eur'
price = tk.StringVar()


def calc_euro_price():
    try:
        response = requests.get(eurodesk)
        response_dict = response.json()
        current_Fr_price_euro = response_dict["rates"]["CHF"]
        calc_price_Fr = float(Euro_entry.get()) * current_Fr_price_euro
        price.set(calc_price_Fr)
    except ValueError:
        price.set("Bitte geben sie eine gültige Zahl ein! ")


Euro_Label = ttk.Label(root, text="Anzahl Euro:", font=("Arial", 10))
Euro_Label.pack(side="top", fill="x", padx=5, pady=2)

Euro_entry = ttk.Entry(root, font=("Arial", 15))
Euro_entry.pack(side="top", fill="x", padx=5, pady=2)

FR_Label = ttk.Label(root, text="Preis in Fr:", font=("Arial", 10))
FR_Label.pack(side="top", fill="x", padx=5, pady=2)

Fr_display = ttk.Label(root, textvariable=price, font=("Arial", 10))
Fr_display.pack(side="top", fill="x", padx=5, pady=2)

calc_button = ttk.Button(root, text="Berechnung durchführen", command=calc_euro_price)
calc_button.pack(side="bottom", fill="x", padx=10, pady=10)


root.mainloop()
