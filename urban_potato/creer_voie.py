# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 14:53:42 2017

@author: Michaël
"""



import classes.voie as voie
import ihm.data as d

def creer_voies(nb_voie):

    sortie = voie.Sortie(-1, None, None, 90)
    
    liste_voie = [voie.Voie(i, None, None, d.vitesse_limite) for i in range(nb_voie)]
    liste_voie[0].voie_droite = sortie
    if nb_voie > 1:
        liste_voie[0].voie_gauche = liste_voie[1]
        liste_voie[nb_voie - 1].voie_droite = liste_voie[nb_voie - 2]
        for i in range(1,nb_voie-1):
            liste_voie[i].voie_gauche = liste_voie[i+1]
            liste_voie[i].voie_droite = liste_voie[i-1]
        
    return (liste_voie, sortie)
