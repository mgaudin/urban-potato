# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 14:09:28 2017

@author: Michaël
"""

from random import *
import vehicule as v
import data as d
import parametre as p
import conducteur as c
import voie as vo

#compteur_vehicules = 0
#ville = d.ville
#
##On tire a pile ou face si on cree une voiture à un instant t
#create = randint(0,1)
#
##Si le hasard a decide de creer un véhicule
#if create == True:
#    pass
#    #On genere les parametres du véhicule
    
def creer_un_vehicule(compteur_vehicules, voie):
    """
    Methode creant une instance de vehicule (en generant les attributs initiaux
    necessaires).
    Elle met egalement a jour la liste de vehicules de la voie sur laquelle le
    vehicule est cree.
    La methode renvoie le vehicule cree.
    """
    #nom
    nom = compteur_vehicules
    
    #type_conducteur
    alea = random()
    proba_cumul = 0
    i = 0
    while alea > proba_cumul:
        proba_cumul += p.PART_CONDUCT[d.ville][i][1]
        i +=1
    conducteur = p.PART_CONDUCT[d.ville][i-1][0]
    
    #vitesse
    vitesse = d.vitesse_limite * conducteur.coef_vitesse

    
    #voie
    voie_vehi = voie
      
    #prend_la_sortie
    proba_sortie = (d.nb_voies - voie.id_voie) / ((d.nb_voies*(d.nb_voies + 1))/2)
    alea = random()
    prend_la_sortie = (alea <= proba_sortie)
    
    #type_vehicule
    alea = random()
    proba_cumul = 0
    i = 0
    while alea > proba_cumul:
        proba_cumul += p.PART_VEHICULE[d.ville][i][1]
        i +=1
    
    
    #On cree le vehicule
    vehi = p.PART_VEHICULE[d.ville][i-1][0](nom, conducteur, vitesse, prend_la_sortie, voie_vehi)
    
    #on met a jour la liste de voitures de la voie sur laquelle la voiture est creee
    voie.liste_vehicules.append(vehi)
              
    return vehi

#    #On incremente le compteur de vehicule
#    compteur_vehicules += 1

def generer_les_vehicules(compteur_vehicules, liste_voie):
    """
    Methode permettant de creer aleatoirement des vehicules, en tenant compte
    du debit demande, pour un instant donne.
    """
    voie_occupee = 0
    for voie in liste_voie:
        voie.libre = True
        
        for vehi in voie.liste_vehicules:
#COEF VEHI ?
            if vehi.position < 0.6*d.vitesse_limite:
                voie.libre = False
                voie_occupee += 1
    
    nb_voies_dispo = d.nb_voies - voie_occupee
    if nb_voies_dispo != 0:
        probabilite = d.debit * d.pas / nb_voies_dispo
        if d.debit * d.pas > 1:
            probabilite = 1 / nb_voies_dispo
    if nb_voies_dispo == 0:
        probabilite = 0
        
    liste_vehicules_crees = []
    if probabilite != 0:
        for voie in liste_voie:
            if voie.libre:
                alea = random()
                if alea <= probabilite and compteur_vehicules != d.nb_vehicules_voulu:
                    nouveau_vehicule = creer_un_vehicule(compteur_vehicules, voie)
#DISTANCE A CREATION                    
                    id_min = -1
                    min_pos = 1200
                    for vehi in nouveau_vehicule.voie.liste_vehicules:
                        if vehi.nom != nouveau_vehicule.nom and min_pos > vehi.position:
                            min_pos = vehi.position
                            id_min = vehi.nom
                    print("cree id {} : pos_min= {}\ndevant id {}\nvoie libre: {}".format(nouveau_vehicule.nom, min_pos, id_min, nouveau_vehicule.voie.libre))
                    
                    
                    compteur_vehicules += 1
                    liste_vehicules_crees.append(nouveau_vehicule)
    
    return (liste_vehicules_crees, compteur_vehicules)