# -*- coding: utf-8 -*-
"""
Projet Informatique
Gestion de trafic routier
Programme principal
A. Gonnaud et MMM <3
Mai 2017
alice.gonnaud@ensg.eu
"""
import os

import ihm.data as d

import initialisation.creer_voie as cvoie
import initialisation.creer_vehicule as cvehi

import sortie_graphique_enregitre_graph as graph

#Repertoire images
try:
    os.mkdir('Graphes')
except OSError:
    for fichier in os.listdir('Graphes'):
        os.remove('Graphes/' + fichier)

(liste_voie, sortie) = cvoie.creer_voies(d.nb_voies)
liste_vehicules_modelises = []
liste_voitures_circul = []
compteur_vehicules = 0
instant = 0
liste_sortie_manquee = []

while not(len(liste_voitures_circul) == 0 and compteur_vehicules == d.nb_vehicules_voulu):
    if compteur_vehicules != d.nb_vehicules_voulu:
        (liste_vehicules_crees, compteur_vehicules) = cvehi.generer_les_vehicules(compteur_vehicules, liste_voie)
        liste_voitures_circul = liste_voitures_circul + liste_vehicules_crees
        liste_vehicules_modelises = liste_vehicules_modelises  + liste_vehicules_crees
    
    for vehi in liste_voitures_circul:
#        if vehi._nom == 10:
#            print("vitesse",vehi.vitesse)
        
        #gestion ligne de dissuastion
        if (vehi.prend_la_sortie and vehi.position < 400 and vehi.position > 800) or (vehi.prend_la_sortie and vehi.voie.id_voie != 1) or not(vehi.prend_la_sortie):
            vehi.serrer_droite()
        
        vehi.prendre_la_sortie()
        
        trop_proche = vehi.tester_environnement()
        if trop_proche:
            depassement_reussi = False
            if not(vehi.prend_la_sortie):
                depassement_reussi = vehi.depasser()
            if not depassement_reussi:
                vehi.ralentir()
                
        else:
            vehi.accelerer()
        vehi.maj_position()
#POSITION NEGATIVE : VEHICULES RECULANT
        if vehi.position > 1200 or vehi.position < 0:
            if vehi.prend_la_sortie and vehi.voie.id_voie != -1:
                liste_sortie_manquee.append(vehi.nom)
            vehi.voie.liste_vehicules.remove(vehi)
            #On eleve le vehicule des voitures circulant sur la route
            liste_voitures_circul.remove(vehi)
            #On supprime le vehicule
            del(vehi)
                  
    instant += d.pas
    #print(instant)
    #print(compteur_vehicules)
    #graph.plot(liste_voitures_circul, instant)
    #print(liste_voitures_circul)
        
print('hors')
print(liste_sortie_manquee)

if __name__ == '__main__':
    pass