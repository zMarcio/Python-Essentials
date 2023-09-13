import datetime
from datetime import date
from tkinter import *

def interfaceRelogio():
    dateNow = date.today()
    hourNow = datetime.datetime.now().time()
    
    hora = hourNow.hour
    minutos = hourNow.minute
    segundos = hourNow.second

    dia = dateNow.day
    mes = dateNow.month
    ano = dateNow.year

    relogio_label.config(text=f'{dia}/{mes}/{ano}\n{hora:02}:{minutos:02}:{segundos:02}')

    root.after(999,interfaceRelogio)
    




root = Tk()
root.title("Relógio")
relogio_label = Label(root, font=("Arial", 20))
relogio_label.pack()

interfaceRelogio()

root.mainloop()