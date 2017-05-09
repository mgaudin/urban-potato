# -*- coding: utf-8 -*-
"""
Projet Informatique
Gestion du trafic routier au niveau d'une sortie d'autoroute
Programme principal
Michael Gaudin et Alice Gonnaud
Mai 2017
"""
#Importations
import os
import matplotlib.pyplot as plt

import initialisation.creer_voie as cvoie
import initialisation.creer_vehicule as cvehi

import ihm.sortie_graphique as graph


#Creation du repertoire images (suppression des images precedentes s'il y en a)
try:
    os.mkdir('../Graphes')
except OSError:
    for fichier in os.listdir('../Graphes'):
        os.remove('../Graphes/' + fichier)


def modelisation(vitesse_limite = 110, nb_voies = 3, scenario = 0, pas = 0.5, nb_vehicules_voulu = 20, debit = 0.5):
    """
    Methode permettant de modeliser la circulation de vehicules sur le troncon 
    d'autoroute.
    Elle prend en argument des parametres generaux du modele, ayant un impact 
    sur le trafic.
    
    La methode affiche des statistiques sur les vehicules.
    Elle permet de visualiser graphiquement l'evolution de la position des 
    vehicules.
    Elle ne renvoie rien.
    
    :param vitesse_limite: limitation de vitesse sur l'autoroute
    :param nb_voies: nombre de voies de l'autoroute (en plus de la sortie)
    :param scenario: definit les proportions de types de vehicules et de 
                     conducteurs du modele
    :param pas: duree separant deux instants modelises (en seconde)
    :param nb_vehicules_voulu: nombre de vehicules circulant a modeliser
    :param debit: debit de vehicules en entree du troncon modelise (en nombre 
                  de vehicules par seconde)
    """
    #Initialisation
    
    #On cree les voies
    (liste_voie, sortie) = cvoie.creer_voies(nb_voies, vitesse_limite)
    
    #Initialisation de la liste de tous les vehicules crees
    liste_vehicules_modelises = []
    
    #Initialisation de la liste des vehicules en circulation sur le troncon
    #modelise
    liste_voitures_circul = []
    
    #Initialisation du nombre de vehicules crees
    compteur_vehicules = 0
    
    #Initialisation du repere temporel
    instant = 0
    
    #Initialisation de la liste de vehicules ayant rate la sortie a cause du 
    #trafic
    liste_sortie_manquee = []
    
    #Initialisation de la liste de vehicules ayant entierement traverse le 
    #troncon d'autoroute modelise
    vehicule_hors = []
    
    #Initialisation de la liste de chaque vehicule associe aux instants 
    #auxquels il atteint 0m et 1200m (sert au calcul du temps de parcours)
    liste_temps = []
      
    #Debut de la modelisation graphique      
    plt.ion()
    
    
    #Modelisation de la circulation
    
    #Tant que tous les vehicules a creer n'ont pas traverse entierement le 
    #troncon d'autoroute, pour chaque instant
    while len(vehicule_hors) != nb_vehicules_voulu:
        
        #Initialisation de la liste de vehicules sortis du modele a l'instant 
        #donne (ayant traverse le troncon), vehicules a supprimer 
        a_supprimer = []
        
        #On ajoute progressivement les vehicules sur les voies
        
        #Si le nombre de vehicules deja crees n'est pas egal au nombre de 
        #vehicules a modeliser
        if compteur_vehicules != nb_vehicules_voulu:
            #On cree des vehicules
            (liste_vehicules_crees, compteur_vehicules) = cvehi.generer_les_vehicules(compteur_vehicules, liste_voie, pas, debit, nb_vehicules_voulu, scenario, nb_voies, vitesse_limite)
            
            #On associe les vehicules crees a l'instant auquel ils ont ete 
            #crees (utile au calcul du temps de parcours)
            liste_temps += [[vehi.nom, instant] for vehi in liste_vehicules_crees]
            
            #On ajoute les vehicules crees a la liste des vehicules en 
            #circulation
            liste_voitures_circul += liste_vehicules_crees

            #On ajoute les vehicules crees a la liste totale des vehicules 
            #crees (utile aux statistiques sur les vehicules)
            liste_vehicules_modelises += liste_vehicules_crees
        
        
        #On gere la circulation des vehicules sur le troncon modelise
        
        #Pour chacun des vehicules en circulation sur le troncon d'autoroute
        for vehi in liste_voitures_circul:
            
            #Gestion de la ligne de dissuasion : un vehicule ne peut pas se 
            #rabattre sur la voie la plus a droite au niveau de la ligne de 
            #dissuasion s'il cherche a prendre la sortie
            if (vehi.prend_la_sortie and vehi.position < 400 and vehi.position > 800) or (vehi.prend_la_sortie and vehi.voie.id_voie != 1) or not(vehi.prend_la_sortie):
                #Le vehicule cherche a se rabattre a droite s'il le peut
                vehi.serrer_droite()
            
            #Le vehicule prend la sortie s'il le veut et s'il le peut
            vehi.prendre_la_sortie(pas)
            
            #Si le vehicule suit de trop pres le vehicule devant lui
            trop_proche = vehi.tester_environnement()
            if trop_proche:
                #Le vehicule cherche a depasser si possible (un vehicule 
                #voulant prendre la sortie ne cherche pas a depasser, il reste
                #a droite)
                depassement_reussi = False
                if not(vehi.prend_la_sortie):
                    depassement_reussi = vehi.depasser(nb_voies)
                #Si le vehicule n'a pas pu depasser, il ralentit
                if not depassement_reussi:
                    vehi.ralentir(pas)
            
            #Si le vehicule n'a pas de vehicule proche devant lui
            else:
                #Le vehicule accelere (sans depasser sa limite)
                vehi.accelerer(vitesse_limite, pas)
                
            #La position du vehicule est mise a jour
            vehi.maj_position(pas)
    
            #Si le vehicule a franchi le troncon modelise
            if vehi.position > 1200 and vehi not in vehicule_hors:
                #On ajoute le vehicule a la liste des vehicules ayant franchi
                #le troncon (s'il n'y est pas deja)
                vehicule_hors.append(vehi)
                
                #On releve l'instant auquel le vehicule franchit le metre 1200 
                #(utile au calcul du temps de parcours)
                for couple in liste_temps:
                    if couple[0] == vehi.nom:
                        couple.append(instant)
                    
            #Si le vehicule est plus de 300m apres le troncon modelise 
            #(distance permettant de s'affranchir des effets de bords, 
            #l'existence des vehicules immediatement apres le metre 1200 ayant
            #un impact sur la circulation des vehicules encore sur le troncon)
            if vehi.position > 1500:
   
                #On ajoute le vehicule a la liste des vehicules ayant rate la 
                #sortie s'il est concerne
                if vehi.prend_la_sortie and vehi.voie.id_voie != -1:           
                    liste_sortie_manquee.append(vehi.nom)
                
                #On ajoute le vehicule a la liste des vehicules a supprimer
                a_supprimer.append(vehi)

        #Fin de la gestion de la circulation des vehicules pour l'instant donne
        
        #On supprime les vehicules hors du modele
        for vehi in a_supprimer:
            #On enleve le vehicule de la liste de vehicules de sa voie
            vehi.voie.liste_vehicules.remove(vehi)
            #On enleve le vehicule des voitures circulant sur la route
            liste_voitures_circul.remove(vehi)
            #On supprime le vehicule
            del(vehi)
        
        #On incremente le temps
        instant += pas
        
        #Affichages possibles (pour chaque instant)
#        print(instant) #echelle temporelle
#        print(compteur_vehicules) #nombre de vehicules deja crees

        #On genere le graphique des positions des vehicules pour l'instant 
        #donne
        graph.plot(nb_voies, liste_voitures_circul, instant)
        plt.pause(0.2)
        plt.clf()
        plt.draw()
        
        #Fin de l'instant donne
        
        
    #Fin de la modelisation graphique
    plt.ioff()
    
    
    #Calcul du temps de parcours de chaque vehicule (temps mis par le vehicule 
    #pour franchir le troncon de 1200m, instant auquel il a franchi le 
    #metre 1200 - instant de creation au metre 0)    
    temps_parcours = [triplet[2] - triplet[1] for triplet in liste_temps]
    #Calcul du temps de parcours moyen
    temps_parcours_moyen = sum(temps_parcours) / float(len(temps_parcours))
    
    #Affichage de statistiques sur les vehicules
    print("Temps de parcours minimal : {} s\nTemps de parcours moyen : {} s\nTemps de parcours maximal : {} s\n".format(min(temps_parcours), temps_parcours_moyen, max(temps_parcours)))
    print("Nombre de vehicules ayant rate la sortie : {}".format(len(liste_sortie_manquee)))
    print("Vehicules ayant rate la sortie : {}".format(liste_sortie_manquee))
    

if __name__ == '__main__':
    modelisation()



