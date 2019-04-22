'''
22apr2019

massimo pasteris
https://www.python-course.eu/tkinter_entry_widgets.php

'''

from tkinter import *

def show_entry_fields():
   myNum=int(e3.get())
   myNumT=myNum +10
   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
   print('Somma=',myNumT)
   Label(master, text='Risultato='+str(myNumT)).grid(row=3)

master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)
Label(master, text="Numero").grid(row=2)


e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

Button(master, text='Quit', command=master.quit).grid(row=10, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=10, column=1, sticky=W, pady=4)

mainloop( )
