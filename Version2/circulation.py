# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 09:07:01 2017

@author: Alice
"""
import create_car as cc
import vehicule as v
import parametre as p
import data as d


#CREATION VOITURE

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
conducteur = p.PART_CONDUCT[ville][i-1][0]

#vitesse
vitesse = d.vitesse_limite * conducteur.coef_vitesse

#prend_la_sortie
prend_la_sortie = randint(0,1)

#voie
ind_voie = randint(0, d.nb_voies)
voie_vehi = voie.Voie(ind_voie)

#type_vehicule
alea = random()
proba_cumul = 0
i = 0
while alea > proba_cumul:
    proba_cumul += p.PART_VEHICULE[ville][i][1]
    i +=1


#On cree le vehicule
vehi = p.PART_VEHICULE[ville][i-1][0](nom, conducteur, vitesse, prend_la_sortie, voie_vehi)

list_voie = [vehi.voie]
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
    
    vehi.maj-position()
    
    list_voie.append(vehi.voie)
    list_position.append(vehi.position)