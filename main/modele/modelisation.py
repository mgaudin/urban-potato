# -*- coding: utf-8 -*-
"""
Projet Informatique
Gestion du trafic routier au niveau d'une sortie d'autoroute
Programme principal
Michael Gaudin et Alice Gonnaud
Mai 2017
"""
import os
import matplotlib.pyplot as plt

import initialisation.creer_voie as cvoie
import initialisation.creer_vehicule as cvehi

import ihm.sortie_graphique as graph


#Repertoire images
try:
    os.mkdir('../Graphes')
except OSError:
    for fichier in os.listdir('../Graphes'):
        os.remove('../Graphes/' + fichier)


def modelisation(vitesse_limite = 110, nb_voies = 3, scenario = 0, pas = 0.5, nb_vehicules_voulu = 20, debit = 0.5):
    
    (liste_voie, sortie) = cvoie.creer_voies(nb_voies, vitesse_limite)
    liste_vehicules_modelises = []
    liste_voitures_circul = []
    compteur_vehicules = 0
    instant = 0
    liste_sortie_manquee = []
    vehicule_hors = []
#temps parcours
    liste_temps = []
            
    plt.ion()
    
    while not(len(vehicule_hors) == nb_vehicules_voulu):
        a_supprimer = []
        if compteur_vehicules != nb_vehicules_voulu:
            (liste_vehicules_crees, compteur_vehicules) = cvehi.generer_les_vehicules(compteur_vehicules, liste_voie, pas, debit, nb_vehicules_voulu, scenario, nb_voies, vitesse_limite)
            
#temps parcours
            liste_temps += [[vehi.nom, instant] for vehi in liste_vehicules_crees]

            liste_voitures_circul = liste_voitures_circul + liste_vehicules_crees
#a passer en commentaire
            liste_vehicules_modelises = liste_vehicules_modelises  + liste_vehicules_crees
        
        for vehi in liste_voitures_circul:
            
            #gestion ligne de dissuasion
            if (vehi.prend_la_sortie and vehi.position < 400 and vehi.position > 800) or (vehi.prend_la_sortie and vehi.voie.id_voie != 1) or not(vehi.prend_la_sortie):
                vehi.serrer_droite()
            
            vehi.prendre_la_sortie(pas)
            
            trop_proche = vehi.tester_environnement()
            if trop_proche:
                depassement_reussi = False
                if not(vehi.prend_la_sortie):
                    depassement_reussi = vehi.depasser(nb_voies)
                if not depassement_reussi:
                    vehi.ralentir(pas)
                    
            else:
                vehi.accelerer(vitesse_limite, pas)
            vehi.maj_position(pas)
    
            if vehi.position > 1200 and vehi not in vehicule_hors:
                vehicule_hors.append(vehi)
                #temps parcours
                for couple in liste_temps:
                    if couple[0] == vehi.nom:
                        couple.append(instant)
                    
    
            if vehi.position > 1500:
    #a passer en commentaire     
                if vehi.prend_la_sortie and vehi.voie.id_voie != -1:           
                    liste_sortie_manquee.append(vehi.nom)
                
                a_supprimer.append(vehi)

                
                      
        for vehi in a_supprimer:

            #On enleve le vehicule de la liste de vehicules de sa voie
            vehi.voie.liste_vehicules.remove(vehi)
            #On enleve le vehicule des voitures circulant sur la route
            liste_voitures_circul.remove(vehi)
            #On supprime le vehicule
            del(vehi)
        
        instant += pas
#        print(instant)
#        print(compteur_vehicules)
        graph.plot(nb_voies, liste_voitures_circul, instant)
        plt.pause(0.2)
        plt.clf()
        plt.draw()
#        print(liste_voitures_circul)
        
    plt.ioff()
#a passer en commentaire      
    temps_parcours = [triplet[2] - triplet[1] for triplet in liste_temps]
    print("Temps de parcours minimal : {} s\nTemps de parcours maximal : {} s\n".format(min(temps_parcours), max(temps_parcours)))
#    print('hors')
    print("Nombre de vehicules ayant rate la sortie : {}".format(len(liste_sortie_manquee)))
    print("Vehicules ayant rate la sortie : {}".format(liste_sortie_manquee))
    

if __name__ == '__main__':
    modelisation()
