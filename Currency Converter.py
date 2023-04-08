import tkinter as tk
import requests
from tkinter import *

def convertr():
    # global symbol
    app_id = 'f4e494322ec44941b20f1d08c31490f6'

    # Make a request to the latest exchange rates API endpoint
    response = requests.get(f'https://openexchangerates.org/api/latest.json?app_id={app_id}')

    # Check if the request was successful
    if response.status_code == 200:

        # Parse the JSON response and extract the exchange rates data
        exchange_rates = response.json()['rates']  # is a dictionary that contains the exchange rates of different
        # currencies with respect to a base currency.
       # print(exchange_rates)
        currency_1 = list1.get()  # here we get the option from list 1
        currency_2 = list2.get()  # here i get the option from list 2
        amount = float(p.get())  # here the value user will give
        rate_1 = exchange_rates[currency_1]
        rate_2 = exchange_rates[currency_2]
        converted_amount = round(amount / rate_1 * rate_2,2)  # The result is rounded to two decimal places using the round()
        formated = '{:,.2f}'.format(converted_amount)
        lblp2['text'] = formated
        print(converted_amount, formated)

    else:
        print(f'Request failed with status code {response.status_code}')
        
def reset():  # this function resets all the values
    p.delete(0, END)
    list1.set('')
    list2.set('')
    lblp2['text']

window = tk.Tk()
window.geometry("500x500")
window.title("$ THE CURRENCY CONVERTER $")
window.resizable(height = False, width = False)

heading=Label(window,text="Currency converter",font=(25))
heading.pack()

lblp = Label (window, text = "Enter Amount" , fg='black',font=(11))
lblp.pack()
p = Entry(window)
p.pack()
lblp = Label(window, text="From", bg= 'blue', fg='white',font=(5))
lblp.pack()

list1 = tk.StringVar()
cur = tk.OptionMenu(window, list1, 'USD', 'PKR', 'INR', 'QR')
cur.pack()

lblp1 = Label(window, text="To", bg= 'blue', fg='white',font=(5))
lblp1.pack()

list2 = tk.StringVar()
cur2 = tk.OptionMenu(window, list2, 'USD', 'PKR', 'INR', 'QR')
cur2.pack()

button = tk.Button(window, text="Convert",command=convertr,font=(3))
button.pack()

lblp2 = Label (window, text = "Converted Amount:" , fg='black',font=(3))
lblp2.pack()

reset_button = Button(window, text="Reset", width=7, padx=5, height=1, bg="red", fg='white',
                      font=("Ivy 10 bold"), command=reset)
reset_button.pack()

window.mainloop()
