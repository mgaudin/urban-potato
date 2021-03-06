# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 09:07:01 2017

@author: Alice
"""

import vehicule as v
import parametre as p
import data as d
from random import *

ville = d.ville

#CREATION VOITURE

#On genere les parametres du véhicule
#nom
nom = 1

#type_conducteur
alea = random()
proba_cumul = 0
i = 0
while alea > proba_cumul:
    proba_cumul += p.PART_CONDUCT[ville][i][1]
    i +=1
conducteur = p.PART_CONDUCT[ville][i-1][0]

#vitesse
vitesse = d.vitesse_limite * conducteur.coef_vitesse

#prend_la_sortie
prend_la_sortie = randint(0,1)

#voie
#CREATE LANE
import voie

nb_voie = 3

sortie = voie.Sortie(-1, None, None, 90)

liste_voie = [voie.Voie(i, None, None) for i in range(nb_voie)]
liste_voie[0].voie_droite = sortie
liste_voie[0].voie_gauche = liste_voie[1]
liste_voie[nb_voie - 1].voie_droite = liste_voie[nb_voie - 2]
for i in range(1,nb_voie-1):
    liste_voie[i].voie_gauche = liste_voie[i+1]
    liste_voie[i].voie_droite = liste_voie[i-1]
#FIN CREATE LANE

ind_voie = randint(0, d.nb_voies)
voie_vehi = liste_voie[ind_voie]

#type_vehicule
alea = random()
proba_cumul = 0
i = 0
while alea > proba_cumul:
    proba_cumul += p.PART_VEHICULE[ville][i][1]
    i +=1


#On cree le vehicule
vehi = p.PART_VEHICULE[ville][i-1][0](nom, conducteur, vitesse, prend_la_sortie, voie_vehi)

list_voie = [vehi.voie.id]
list_position = [vehi.position]

while vehi.position < 1200:
    
    vehi.serrer_droite()
    
    trop_proche = vehi.tester_environnement()
    
    if trop_proche:
        depassement_reussi = vehi.depasser()
        
        if not depassement_reussi:
            vehi.ralentir()
    else:
        vehi.accelerer()
    
    vehi.maj_position()
    
    list_voie.append(vehi.voie.id)
    list_position.append(vehi.position)