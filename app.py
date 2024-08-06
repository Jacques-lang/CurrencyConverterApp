import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk


def get_currency():
    api_key = "6daebde0b3bf91d00a779fd9"
    try:
        amount = float(amount_sum.get())
        if amount < 0:
            messagebox.showerror("Amount must be positive")
            return
    except ValueError:
        messagebox.showerror("Amount must be a number")
        return

    base_country_currency_code = base_currency.get()
    converted_rate = converted_currency.get()
    try:
        api_request = requests.get(f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_country_currency_code}")
        if api_request.status_code == 200:
            converted_unit = api_request.json()['conversion_rates'][converted_rate]
            converted_amount = (converted_unit * amount)
            currency_info = (
                f"{amount} {base_country_currency_code} converted to {converted_rate} is {converted_amount:.2f}")
            currency_label.config(text=currency_info)
        else:
            messagebox.showerror("Invalid currency!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Currency App")

#Image
image_path = "appPic.png"
image = Image.open(image_path)
image_resize = image.resize((400, 200))
photo = ImageTk.PhotoImage(image_resize)
image_label = tk.Label(root, image=photo)
image_label.pack(pady=5)

#Textfields
tk.Label(root, text="Enter the cash amount").pack(pady=5)
amount_sum = tk.Entry(root)
amount_sum.pack(pady=5)

tk.Label(root, text="Enter the base currency").pack(pady=5)
base_currency = tk.Entry(root)
base_currency.pack(pady=5)

tk.Label(root, text="Enter the preferred conversion currency").pack(pady=5)
converted_currency = tk.Entry(root)
converted_currency.pack(pady=5)

#Button
tk.Button(root, text="Get converted amount", command=get_currency).pack(pady=5)
currency_label = tk.Label(root, text="")
currency_label.pack(pady=5)

root.mainloop()
