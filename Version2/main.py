# -*- coding: utf-8 -*-
"""
Projet Informatique
Gestion de trafic routier
Programme principal
A. Gonnaud et MMM <3
Mai 2017
alice.gonnaud@ensg.eu
"""

import data as d

import create_lane

create_lane.creer_voies(d.nb_voies)

liste_voitures_circul = []
compteur_vehicules = 0

while len(liste_voitures_circul) != 0 and compteur_vehicules != d.nb_vehicules_voulu:
    cree = creer_voiture(compteur_vehicules)
    liste_voitures_circul.append(cree)
    compteur_vehicules += 1
    
    
    for vehi in liste_voitures_circul:
        vehi = liste_voitures_circul[i]
        vehi.serrer_droite()
        trop_proche = vehi.tester_environnement()
        if trop_proche:
            depassement_reussi = vehi.depasser()
            if not depassement_reussi:
                vehi.ralentir()
        else:
            vehi.accelerer()
        vehi.maj_position()
        if vehi.position > 1200:
            liste_voitures_circul.remove(vehi)
            del vehi
                  
    
    enregistrer_graphe()
        
        