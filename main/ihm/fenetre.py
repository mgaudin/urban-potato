# -*- coding: utf-8 -*-
"""
Projet Informatique
Gestion de trafic routier
Interface - Packet ihm
A. Gonnaud - M.Gaudin
Mai 2017
alice.gonnaud@ensg.eu - michael.gaudin@ensg.eu
"""
#Ce script permet de construire une fenetre d'interface pour l'utilisateur de
#l'application, afin qu'il puisse selectionner les parametres de la modelisation

#Importations
from tkinter import * 
from tkinter.messagebox import *
import os
import modele.modelisation as m
#import initialisation as init
    
#Creation d'un fenetre d'interface
fenetre = Tk()
#Titre pour l'interface
fenetre.title('Application')

# Choix de la taille de la fenetre
largeur_fenetre = 700
hauteur_fenetre = 700

# Calcul du placement de la fenetre sur l'ecran
# Au milieu
largeur = str(int(fenetre.winfo_screenwidth()/2 - largeur_fenetre/2))
hauteur = str(int(fenetre.winfo_screenheight()/2 - hauteur_fenetre/2))

# Definition de la taille de la fenetre
fenetre.geometry(str(largeur_fenetre)+"x"+str(hauteur_fenetre)+'+'+largeur+'+'+hauteur)

# Titre
titre = Label(fenetre, text="Urban Potato")
titre.grid(row=0, column=0, columnspan=2)

espace = Label(fenetre, text=" ")
espace.grid(row=1, column=0)

# Selection du nombre de vehicules
txt_nb_vehicules = Label(fenetre, text="Nombre de voitures", justify='center')
#txt_nb_vehicules.grid(row=1, column=0)
txt_nb_vehicules.grid(row=2, column=0, padx=10, pady=10)
var_nb_vehicules = Spinbox(fenetre, from_=0, to=50, justify='center')
#var_nb_voiture.set(20)
#var_nb_vehicules.grid(row=1, column=1)
var_nb_vehicules.grid(row=2, column=1, padx=10, pady=10)

# Selection du nombre de voies
txt_nb_voies = Label(fenetre, text="Nombre de voies")
txt_nb_voies.grid(row=3, column=0, padx=10, pady=10)
var_nb_voies = Spinbox(fenetre, from_=0, to=8, justify='center')
var_nb_voies.grid(row=3, column=1, padx=10, pady=10)

# Selection de la vitesse limite
txt_vitesse_limite = Label(fenetre, text="Vitesse limite (en km/h)")
txt_vitesse_limite.grid(row=4, column=0, padx=10, pady=10)
liste_vitesses = (90, 110, 130)
var_vitesse_limite = StringVar()
var_vitesse_limite.set(liste_vitesses[0])
var_vitesses_limite = OptionMenu(fenetre, var_vitesse_limite, *liste_vitesses)
var_vitesses_limite.grid(row=4, column=1, padx=10, pady=10)
#
#label4 = Label(fenetre, text="Debit d'entree")
#label4.pack()
#
#label6 = Label(fenetre, text="Part de chauffards")
#value6 = DoubleVar()
#scale6 = Scale(fenetre, variable=value6,orient=HORIZONTAL)
#scale6.pack()
#label6.pack()
#
#label7 = Label(fenetre, text="Part de conducteurs prudent")
#value7 = DoubleVar()
#scale7 = Scale(fenetre, variable=value7,orient=HORIZONTAL)
#scale7.pack()
#label7.pack()

#Selection du scenario
txt_scenario = Label(fenetre, text="Scenario")
txt_scenario.grid(row=5, column=0, padx=10, pady=10)
liste_scenarii = ('Sortie A7 direction Marseille', 'Sortie A4 direction Paris', 'Sortie A56 direction Dreux')
var_scenario = StringVar()
var_scenario.set(liste_scenarii[0])
var_scenarii = OptionMenu(fenetre, var_scenario, *liste_scenarii)
var_scenarii.grid(row=5, column=1, padx=10, pady=10)

#Debit
txt_debit = Label(fenetre, text="Debit")
txt_debit.grid(row=6, column=0, padx=10, pady=10)
var_debit = Spinbox(fenetre, from_=0, to=8, justify='center')
var_debit.grid(row=6, column=1, padx=10, pady=10)

#Pas
txt_pas = Label(fenetre, text="Pas")
txt_pas.grid(row=7, column=0, padx=10, pady=10)
var_pas = Spinbox(fenetre, from_=0, to=8, justify='center')
var_pas.grid(row=7, column=1, padx=10, pady=10)

#Barre d'echelle
echelle = Scale(fenetre,from_=0,to=100,resolution=1,orient=HORIZONTAL,\
length=100, width=20, label="Echelle", tickinterval=50)
echelle.grid(row=8, column=0, columnspan=2)
    
def enregistre_parametres():
    """
    Methode permettant de recuperer les parametres depuis l'interface utilisateur
    et d'executer la modelisation
    """
    #On recupere le nombre de vehicules desires par l'utilisateur dans la
    #modelisation
    nb_vehicules_voulu = int(var_nb_vehicules.get())
    #On recupere le nombre de voies desirees par l'utilisateur dans la
    #modelisation
    nb_voies = int(var_nb_voies.get())
    #On recupere la vitesse limite theorique de la portion d'autoroute desiree
    #par l'utilisateur dans la modelisation
    vitesse_limite = int(var_vitesse_limite.get())
    #On recupere le descriptif du scenario desire par l'utilisateur
    scenario_txt = var_scenario.get()
    #On recupere l'indice dans la liste des scenarii du scenario choisi
    scenario = liste_scenarii.index(scenario_txt)
    #On recupere le debit
    debit = int(var_debit.get())
    #On recupere le pas
    pas = float(var_pas.get())
    print('Nombre de vehicules = {}\nNombre de voies = {}\nVitesse limite = {}\nScenario = {}\nDebit = {}\nPas = {}\n'.format(nb_vehicules_voulu, nb_voies, vitesse_limite, scenario, debit, pas))
    if int(nb_vehicules_voulu) < 0 or int(nb_voies) < 0:
        showwarning('Attention','Il y a une erreur dans les valeurs entrees (valeur negative, etc.)')
        raise ValueError('Erreur dans les valeurs entrees en argument')
    fenetre.destroy()
    #Execution du script principal d'execution
    m.modelisation(vitesse_limite, nb_voies, scenario, pas, nb_vehicules_voulu, debit)

##On recupere le nombre de vehicules desires par l'utilisateur dans la
##modelisation
#nb_vehicules_voulu = int(var_nb_vehicules.get())
##On recupere le nombre de voies desirees par l'utilisateur dans la
##modelisation
#nb_voies = int(var_nb_voies.get())
##On recupere la vitesse limite theorique de la portion d'autoroute desiree
##par l'utilisateur dans la modelisation
#vitesse_limite = int(var_vitesse_limite.get())
##On recupere le descriptif du scenario desire par l'utilisateur
#scenario_txt = var_scenario.get()
##On recupere l'indice dans la liste des scenarii du scenario choisi
#scenario = liste_scenarii.index(scenario_txt)
##On recupere le debit
#debit = int(var_debit.get())
##On recupere le pas
#pas = float(var_pas.get())
    
#Bouton Lancer
lancer = Button(fenetre, text="Lancer", command=enregistre_parametres)
lancer.grid(row=9, column=0)

# Bouton Quitter
quitter = Button(fenetre, text="Quitter", command=fenetre.destroy)
quitter.grid(row=9, column=1)

fenetre.mainloop()