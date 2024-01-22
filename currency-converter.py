import requests
import tkinter as tk
from tkinter import ttk

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        # Variables
        self.base_currency_var = tk.StringVar()
        self.target_currency_var = tk.StringVar()
        self.amount_var = tk.DoubleVar()
        self.result_var = tk.StringVar()

        # Entry widgets
        ttk.Label(root, text="Base Currency:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        ttk.Entry(root, textvariable=self.base_currency_var).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(root, text="Target Currency:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        ttk.Entry(root, textvariable=self.target_currency_var).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(root, text="Amount:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        ttk.Entry(root, textvariable=self.amount_var).grid(row=2, column=1, padx=5, pady=5)

        # Result label
        ttk.Label(root, text="Result:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        ttk.Label(root, textvariable=self.result_var).grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # Convert button
        ttk.Button(root, text="Convert", command=self.convert_currency).grid(row=4, column=0, columnspan=2, pady=10)

    def get_exchange_rate(self):
        base_currency = self.base_currency_var.get().upper()
        target_currency = self.target_currency_var.get().upper()

        api_url = f'https://open.er-api.com/v6/latest/{base_currency}'
        response = requests.get(api_url)

        if response.status_code == 200:
            exchange_rates = response.json().get('rates')
            if target_currency in exchange_rates:
                return exchange_rates[target_currency]
            else:
                return None
        else:
            return None

    def convert_currency(self):
        exchange_rate = self.get_exchange_rate()

        if exchange_rate is not None:
            amount = self.amount_var.get()
            converted_amount = amount * exchange_rate
            self.result_var.set(f"{amount} {self.base_currency_var.get()} is equal to {converted_amount:.2f} {self.target_currency_var.get()}")
        else:
            self.result_var.set("Error: Unable to fetch exchange rates.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
