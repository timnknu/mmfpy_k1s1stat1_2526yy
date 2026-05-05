import tkinter

root = tkinter.Tk()

def btn_onlick():
    print("Button was clicked!")
    usrval.set('HELLO')

usrval = tkinter.StringVar(value="початкове значення")
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

