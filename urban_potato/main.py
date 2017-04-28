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
import create_car

import sortie_graphique as graph

(liste_voie, sortie) = create_lane.creer_voies(d.nb_voies)

liste_voitures_circul = []
compteur_vehicules = 0
instant = 0

while not(len(liste_voitures_circul) == 0 and compteur_vehicules == d.nb_vehicules_voulu):
    if compteur_vehicules != d.nb_vehicules_voulu:
        (liste_vehicules_crees, compteur_vehicules) = create_car.generer_les_vehicules(compteur_vehicules, liste_voie)
        liste_voitures_circul = liste_voitures_circul + liste_vehicules_crees
    
    
    for vehi in liste_voitures_circul:
#Quand prendre la sortie ?
        if vehi._voie.id == 0:
            vehi.prendre_la_sortie(sortie)
            
        vehi.serrer_droite()
        trop_proche = vehi.tester_environnement()
        if trop_proche:
            depassement_reussi = vehi.depasser()
            if not depassement_reussi:
                vehi.ralentir()
        else:
            vehi.accelerer()
        vehi.maj_position()
#POSITION NEGATIVE : VEHICULES RECULANT
        if vehi.position > 1200 or vehi.position < 0:
            #On eleve le vehicule des voitures circulant sur la route
            liste_voitures_circul.remove(vehi)
            #On supprime le vehicule
            del(vehi)
                  
    instant += d.pas
    print(instant)
    print(compteur_vehicules)
    graph.plot(liste_voitures_circul, instant)
    #print(liste_voitures_circul)
        
print('hors')