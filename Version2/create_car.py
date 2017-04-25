# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 14:09:28 2017

@author: Michaël
"""

from random import *
import vehicule as v
import data as d
import parametre as p

compteur_vehicules = 0
ville = d.ville

#On tire a pile ou face si on cree une voiture à un instant t
create = randint(0,1)

#Si le hasard a decide de creer un véhicule
if create == True:
    #On genere les parametres du véhicule
    #nom
    nom = compteur_vehicules
    
    #type_conducteur
    alea = random()
    proba_cumul = 0
    i = 0
    while alea > proba_cumul:
        proba_cumul += p.PART_CONDUCT[ville][i][1]
        i +=1
    type_conducteur = p.PART_CONDUCT[ville][i][0]
    
    #vitesse
    vitesse = d.vitesse_limite * p.COEF_VITESSE_CONDUCTEUR[type_conducteur]
    
    #prend_la_sortie
    prend_la_sortie = randint(0,1)
    
    #voie
    voie = randint(0, d.nb_voies)
    
    #type_vehicule
    alea = random()
    proba_cumul = 0
    i = 0
    while alea > proba_cumul:
        proba_cumul += p.PART_VEHICULE[ville][i][1]
        i +=1
    type_vehicule = p.PART_VEHICULE[ville][i][0] 
    
    #On cree le vehicule
    vehicule = v.Vehicule(nom, type_conducteur, vitesse, prend_la_sortie, voie, type_vehicule)
    
    #On incremente le compteur de vehicule
    compteur_vehicules += 1