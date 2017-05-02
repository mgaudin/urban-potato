# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 14:30:18 2017

@author: Alice
"""

import create_car as cc
import create_lane as cl
import sortie_graphique as graph

(voie, sortie) = cl.creer_voies(3)
voiture1 = cc.creer_un_vehicule(0, voie)
voiture2 = cc.creer_un_vehicule(1, voie)
voiture1._position = 102
voiture1._vitesse = 100
voiture2._vitesse = voiture1.vitesse + 50
voiture1._voie = voie[0]
voiture2._voie = voie[0]
voie[0].liste_voiture = [voiture1, voiture2]

i = 0
while voiture1.position < 1200:
    voiture2.ralentir()
    voiture1.maj_position()
    voiture2.maj_position()
    
    graph.plot([voiture1, voiture2], i)
    
    i += 1
    
    