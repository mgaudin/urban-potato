# -*- coding: utf-8 -*-
"""
Projet Informatique
Gestion du trafic routier au niveau d'une sortie d'autoroute
Methodes pour initialiser les voies
Michael Gaudin et Alice Gonnaud
Mai 2017
"""

import classes.voie as voie
import ihm.data as d

def creer_voies(nb_voie, vitesse_limite):
    """
    Methode permettant de creer les voies de la modelisation (dont la sortie), 
    en fonction du nombre de voies demandees.
    
    La methode retourne les voies creees.
    
    :param nb_voie: nombre de voies a creer
    :return: (liste des voies, sortie)
    :rtype : couple (liste d'objets voie, objet sortie)
    """
    #Creation de la sortie, initiee sans voie voisine
    sortie = voie.Sortie(-1, None, None, 90)
    
    #Creation des autres voies, initiees sans voie voisine
    liste_voie = [voie.Voie(i, None, None, vitesse_limite) for i in range(nb_voie)]
    #La voie a droite de la voie la plus a droite est la sortie
    liste_voie[0].voie_droite = sortie
              
    #S'il y a strictement plus d'une voie (sinon, il n'y a rien de plus a traiter)
    if nb_voie > 1:
        #On complete les voies voisines des voies exterieures
        liste_voie[0].voie_gauche = liste_voie[1]
        liste_voie[nb_voie - 1].voie_droite = liste_voie[nb_voie - 2]
        #On complete les voies a gauche et a droite des autres voies
        for i in range(1,nb_voie-1):
            liste_voie[i].voie_gauche = liste_voie[i+1]
            liste_voie[i].voie_droite = liste_voie[i-1]
        
    #On retourne la liste des voies creees et la sortie
    return (liste_voie, sortie)
