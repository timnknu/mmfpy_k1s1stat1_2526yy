import tkinter
from tkinter import messagebox
import curr_conv_logic
from tkinter import ttk

root = tkinter.Tk()


def btn_onlick():
    print("Button was clicked!", usrval.get())

    s = usrval.get()
    try:
        res = curr_conv_logic.convert_currencies(s)
        usrval.set(str(res))
    except curr_conv_logic.InvalidFormatError:
        messagebox.showerror("Помилка",
                             "Невірний формат",
                             parent=root)
    except curr_conv_logic.UnknownCurrencyError:
        messagebox.showerror("Помилка",
                             "Невідома валюта",
                             parent=root)
    except curr_conv_logic.NegativeAmountError:
        messagebox.showerror("Помилка",
                             "Від'ємне значення",
                             parent=root)


usrval = tkinter.StringVar(value="81.8 USD")
inpvalfield = tkinter.Entry(root)#, textvariable=usrval)
inpvalfield['textvariable'] = usrval
inpvalfield.pack()

cto = tkinter.ttk.Combobox(root, values=["USD", "EUR", "UAH"])
cto.pack()

btn = tkinter.Button(root, text="Конвертувати", pady=20, padx=50)
btn['command'] = btn_onlick
btn.pack()

reslbl = tkinter.Label(root)#, text="Результат буде тут")
reslbl['text'] = "Результат буде тут"
reslbl.pack()

root.mainloop()

