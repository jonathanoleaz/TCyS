# -*- coding: utf-8 -*-
"""
Created on December 5, 2018

@author: navi_
"""
from Tkinter import *
import tkMessageBox

import datetime
from secuencias import *

window = Tk()
window.title("Operaciones con secuencias")
window.geometry('550x400')

lbl = Label(window, text="Ingrese las secs. y elija una operación del menú:")
lbl.grid(column=1, row=0, padx=10, pady=10)

lbl = Label(window, text="f[n] = ")
lbl.grid(column=0, row=2)

txtLocalFile = Entry(window,width=30)
txtLocalFile.grid(column=1, row=2, pady=7, sticky=W)

lbl = Label(window, text="g[n] = ")
lbl.grid(column=0, row=3, pady=7)

defaultText = StringVar()
defaultText.set('3, 7, 3*, 6, 2')

txtRemFile = Entry(window, width = 30, textvariable = defaultText)
txtRemFile.grid(column=1, row=3, sticky=W)


lbl = Label(window, text="Factor = ")
lbl.grid(column=0, row=4)


w = Spinbox(window, from_=0, to=10)
w.grid(column=1, row=4, pady=7, sticky=W)

lbl = Label(window, text="Operación:")
lbl.grid(column=0, row=5, pady=7)

choices = { 'Mutiplicación','Suma','Resta','Amplificación/Atenuación','Desplazamiento',
	'Reflejo', 'Diezmación', 'Interpolación', 'Convolución ordinaria', 'Convolución periodica', 'Convolución circular'}
 
tkvar = StringVar()
popupMenu = OptionMenu(window, tkvar, *choices)

popupMenu.grid(row = 5, column =1, sticky=W)
popupMenu.config(bg = "navajowhite")




def change_dropdown(*args):
    print( tkvar.get() )
 
# link function to change dropdown
tkvar.trace('w', change_dropdown)
window.mainloop()