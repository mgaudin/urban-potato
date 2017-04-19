# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 12:04:21 2017

@author: Michaël
"""

from tkinter import * 

fenetre = Tk()

titre = Label(fenetre, text="APPLICATION")
titre.pack()

espace = Label(fenetre, text=" ")
espace.pack()

label1 = Label(fenetre, text="Nombre de voitures")
label1.pack()
s1 = Spinbox(fenetre, from_=0, to=10)
s1.pack()

label2 = Label(fenetre, text="Nombre de voies")
label2.pack()
s2 = Spinbox(fenetre, from_=0, to=10)
s2.pack()

label3 = Label(fenetre, text="Vitesse limite")
liste = Listbox(fenetre)
liste.insert(1, "90")
liste.insert(2, "110")
liste.insert(3, "130")
label3.pack()
liste.pack()

label4 = Label(fenetre, text="Debit")
label4.pack()

label5 = Label(fenetre, text="Temps de modélisation")
label5.pack()
s5 = Spinbox(fenetre, from_=0, to=10)
s5.pack()

label6 = Label(fenetre, text="Part de chauffard")
value6 = DoubleVar()
scale6 = Scale(fenetre, variable=value6)
scale6.pack()
label6.pack()

label7 = Label(fenetre, text="Part de conducteurs prudent")
value7 = DoubleVar()
scale7 = Scale(fenetre, variable=value7)
scale7.pack()
label7.pack()

bouton=Button(fenetre, text="Lancer", command=fenetre.quit)
bouton.pack()

fenetre.mainloop()