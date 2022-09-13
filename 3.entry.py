import tkinter as tk

def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print('Empty Entry')

def delete_entry():
    name.delete(1, 5)

win = tk.Tk()
win.geometry(f"400x500+100+200")
win.title('Моё первое графическое приложение')

tk.Label(win,text='Name:').grid(row=0,column=0,stick='w')
name = tk.Entry(win)
name.grid(row=0,column=1)

tk.Button(win,text='get',command=get_entry).grid(row=1,column=0,stick='we')
tk.Button(win,text='delete',command=delete_entry).grid(row=1,column=1,stick='we')

win.grid_columnconfigure(0,minsize=100)
win.grid_columnconfigure(1,minsize=100)

win.mainloop()