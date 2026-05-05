import tkinter

root = tkinter.Tk()

rates = {
    'USD': {'UAH': 36.57, 'EUR': 0.92,  'USD': 1},
    'EUR': {'UAH': 39.78, 'EUR': 1,     'USD': 1.09},
    'UAH': {'UAH': 1,     'EUR': 0.025, 'USD': 0.027}
}

# cFrom = 'UAH'
# cTo = 'USD'
# k = rates[cFrom][cTo]
# print(k)

def btn_onlick():
    print("Button was clicked!", usrval.get())

    s = usrval.get()
    d = s.split()
    v = float(d[0])
    cFrom = d[1]
    k = rates[cFrom]['UAH']
    res = v * k

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

