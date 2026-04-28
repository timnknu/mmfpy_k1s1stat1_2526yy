import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("My Timer")
        #setting window size
        width=348
        height=192
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        #root.resizable(width=False, height=False)

        self.s = tk.StringVar()
        time_entry = tk.Entry(root, textvariable=self.s)
        time_entry.place(x=70,y=40,width=186)
        self.s.set("10")

        lbl1 = tk.Label(root, text = "Кількість секунд")
        lbl1.place(x=0,y=0)

        start_btn = tk.Button(root, text = "Пуск",
                              command = self.start_bnt_onclick)
        start_btn.place(x=30,y=110,width=70,height=25)

        stop_btn = tk.Button(root, text = "Стоп",
                             command = self.stop_btn_onclick)
        stop_btn.place(x=220,y=110,width=70,height=25)

        self.is_active = False

    def update_time(self):
        if not self.is_active:
            tk.messagebox.showwarning(title="відповідь",
                                      message="відлік часу зупинений")
            return
        #

        old_text = self.s.get()
        old_val = int(old_text)
        if old_val == 0:
            #tk.messagebox.askyesno(title="питання",
            #                       message="Час вийшов. Запустити знову?")
            ans = tk.messagebox.askquestion(title="питання",
                                            message="Час вийшов. Запустити знову?",
                                            type=tk.messagebox.YESNO)
            tk.messagebox.showwarning(title="відповідь",
                                      message=ans)

        else:
            self.s.set( str(old_val - 1) )
            root.after(500, self.update_time) # запланувати повторний виклик
    #

    def start_bnt_onclick(self):
        self.is_active = True
        root.after(500, self.update_time)


    def stop_btn_onclick(self):
        self.is_active = False



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
#        ft = tkFont.Font(family='Times',size=10)
