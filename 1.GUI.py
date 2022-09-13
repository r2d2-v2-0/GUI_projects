import tkinter as tk

count = 0

def counter():
    global count
    count += 1
    btn3['text'] = f'кликов: {count}'

def switch_on():
    global count
    count += 1
    btn3['state'] = tk.NORMAL

def switch_off():
    global count
    count += 1
    btn3['state'] = tk.DISABLED
    



#                                      WINDOW
# _____________________________________________________________________________________
root = tk.Tk()
h = 400
w = 500
photo = tk.PhotoImage(file='python_syntax_2\hw.GUI\icon.png') #upload icon's file

root.iconphoto(False, photo) #turn on the icon

root.config(bg='#1CAC78') #set color of background

root.title('Калькулятор') #window's name

root.geometry(f"{h}x{w}+700+200") #set window size
root.minsize(300,400)
root.maxsize(500,600)
# --------------------------------------------------------------------------------------


btn1 = tk.Button(root, text='ВКЛ',
    command=switch_on,
    activebackground='grey',
    bg='green',
    )

btn2 = tk.Button(root, text='ВЫКЛ',
    command=switch_off,
    activebackground='grey',
    bg='red',
    )

btn3 = tk.Button(root, text=f'нажми: {count}',
    command=counter,
    activebackground='grey',
    state=tk.NORMAL
    )



btn1.pack()
btn2.pack()
btn3.pack()


root.mainloop()