# -*- coding: utf-8 -*-
"""
Created on December 5, 2018

@author: navi_
"""
from Tkinter import *
import tkMessageBox

import datetime
from secuencias import *

def btnAction():
	index = tkvar.get()
	seq1 = build_dict(txtLocalFile.get())
	seq2 = build_dict(txtRemFile.get())

	seq1a, seq2a = complete_seqs(seq1, seq2)

	factor = float(w.get())
	plotMode=0			#if plotMode==1, the plot only seq1 and seqRes
	if index =='Mutiplicacion':
		seqRes = basic_operation_seq(seq1a, seq2a, 'mult')

	if index =='Suma':
		seqRes = basic_operation_seq(seq1a, seq2a, 'add')
		print 'sumando'

	if index =='Resta':
		seqRes = basic_operation_seq(seq1a, seq2a, 'sub')

	if index =='Amplificacion/Atenuacion':
		seqRes = ampl_seq(seq1, factor)
		plotMode=1

	if index =='Desplazamiento':
		seqRes = shift_seq(seq1, factor)
		plotMode=1

	if index =='Reflejo':
		seqRes = reflection_seq(seq1)
		plotMode=1

	if index =='Diezmacion':
		seqRes = decim_seq(seq1, factor)
		plotMode=1

	if index =='Interpolacion':
		seqRes = interp_seq(seq1, int(factor))
		plotMode=1

	if index =='Convolucion ordinaria':
		seqRes = convolve(seq1, seq2)

	if index =='Convolucion periodica':
		seqRes = periodic_convolve(seq1, seq2)	

	if index =='Convolucion circular':
		seqRes = circular_convolve(seq1, seq2)	

	lblRes.config(text=build_seq(seqRes))	

	if plotMode==1:
		plot_two_sequences(seq1, seqRes)

	else:
		plot_two_sequences(seq1, seq2)
		plot_sequence(seqRes)

		

window = Tk()
window.title("Operaciones con secuencias")
window.geometry('550x400')

lbl = Label(window, text="Ingrese las secuencias y elija una operación del menú:")
lbl.grid(column=1, row=0, padx=10, pady=10)

lbl = Label(window, text="f[n] = ")
lbl.grid(column=0, row=2)

txtLocalFile = Entry(window,width=30)
txtLocalFile.grid(column=1, row=2, pady=7, sticky=W)

lbl2 = Label(window, text="g[n] = ")
lbl2.grid(column=0, row=3, pady=7)

defaultText = StringVar()
defaultText.set('3, 7, 3*, 6, 2')

txtRemFile = Entry(window, width = 30, textvariable = defaultText)
txtRemFile.grid(column=1, row=3, sticky=W)


lbl3 = Label(window, text="Factor = ")
lbl3.grid(column=0, row=4)

w = Spinbox(window, from_=-1000, to=1000)
w.grid(column=1, row=4, pady=7, sticky=W)

lbl = Label(window, text="Operación:")
lbl.grid(column=0, row=5, pady=7)

choices = { 'Mutiplicacion','Suma','Resta','Amplificacion/Atenuacion','Desplazamiento',
	'Reflejo', 'Diezmacion', 'Interpolacion', 'Convolucion ordinaria', 'Convolucion periodica', 'Convolucion circular'}
 
tkvar = StringVar()
popupMenu = OptionMenu(window, tkvar, *choices)

popupMenu.grid(row = 5, column =1, sticky=W, pady=7)
popupMenu.config(bg = "navajowhite")


btn = Button(window, text="Mostrar", bg="light slate blue", command=btnAction)
btn.grid(column=1, row=6)

lbl = Label(window, text="Resultado = ")
lbl.grid(column=0, row=7)

lblRes = Label(window, text="")
lblRes.grid(column=1, row=7, sticky=W)


def change_dropdown(*args):
    print( tkvar.get() )
    optionSelected = tkvar.get()
    if (tkvar.get() == 'Amplificacion/Atenuacion' or tkvar.get() == 'Diezmacion' or tkvar.get() == 'Desplazamiento' \
    	or tkvar.get() == 'Reflejo' or tkvar.get() == 'Interpolacion'):
    	lbl2.config(state='disabled') 
    	txtRemFile.config(state='disabled')
    	lbl3.config(state='normal')
    	w.config(state='normal')
    else:
    	lbl2.config(state='normal') 
    	txtRemFile.config(state='normal')
    	lbl3.config(state='disabled')
    	w.config(state='disabled')


 
# link function to change dropdown
tkvar.trace('w', change_dropdown)
window.mainloop()