import tkinter
import curr_conv_logic

root = tkinter.Tk()


def btn_onlick():
    print("Button was clicked!", usrval.get())

    s = usrval.get()
    try:
        res = curr_conv_logic.convert_currencies(s)
    except curr_conv_logic.InvalidFormatError:
        res = "Невірний формат"
    except curr_conv_logic.UnknownCurrencyError:
        res = "Невідома валюта"
    except curr_conv_logic.NegativeAmountError:
        res = "Невірна сума"

    usrval.set(str(res))

usrval = tkinter.StringVar(value="81.8 USD")
inpvalfield = tkinter.Entry(root)#, textvariable=usrval)
inpvalfield['textvariable'] = usrval
inpvalfield.pack()


btn = tkinter.Button(root, text="Конвертувати", pady=20, padx=50)
btn['command'] = btn_onlick
btn.pack()

reslbl = tkinter.Label(root)#, text="Результат буде тут")
reslbl['text'] = "Результат буде тут"
reslbl.pack()

root.mainloop()

