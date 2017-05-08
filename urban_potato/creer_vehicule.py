# -*- coding: utf-8 -*-
"""
Projet Informatique
Gestion du trafic routier au niveau d'une sortie d'autoroute
Methodes pour inialiser les vehicules
Michael Gaudin et Alice Gonnaud
Mai 2017
"""

from random import *
import classes.vehicule as v
import ihm.data as d
import initialisation.parametre as p
import classes.conducteur as c
import classes.voie as vo

    
def creer_un_vehicule(compteur_vehicules, voie):
    """
    Methode creant une instance de Vehicule (en generant les attributs initiaux
    necessaires).
    Elle met egalement a jour la liste de vehicules de la voie sur laquelle le
    vehicule est cree.
    
    La methode renvoie le vehicule cree.
    
    :param compteur_vehicules: nombre de vehicules deja crees, sert a definir
                               l'id du vehicule
    :param voie: instance de la classe Voie, sur laquelle le vehicule est cree
   
    :return: instance creee de la classe Vehicule
    :rtype: objet vehicule
    """
    #On initialise les differents attributs necessaires pour creer un objet
    #vehicule
    
    #Le nom du vehicule est un entier unique (on choisit l'ordre dans lequel le 
    #vehicule a ete cree)
    nom = compteur_vehicules

#PROBA CUMULEE : ORDONNER ?    
    #On associe un type de conducteur au vehicule aleatoirement, avec la 
    #probabilite definie par le scenario choisi
    alea = random()
    proba_cumul = 0
    i = 0
    while alea > proba_cumul:
        proba_cumul += p.PART_CONDUCT[d.scenario][i][1]
        i +=1
    conducteur = p.PART_CONDUCT[d.scenario][i-1][0]
    
    #La vitesse est initialisee a la limitation de vitesse ponderee par le 
    #coefficient de vitesse associee au type de conducteur (un conducteur plus 
    #prudent ira moins vite)
    vitesse = d.vitesse_limite * conducteur.coef_vitesse

    #La voie du vehicule est celle entree en argument
    voie_vehi = voie
      
    #L'attribut prend_la_sortie vaut True ou False aléatoirement, avec une 
    #probabilite de valoir True d'autant plus elevee que le vehicule est proche
    #de la voie la plus a droite
    if d.nb_voies != 1:
        proba_sortie = (d.nb_voies - voie.id_voie) / ((d.nb_voies*(d.nb_voies + 1))/2)
    else:
        proba_sortie = 1/5
    alea = random()
    prend_la_sortie = (alea <= proba_sortie)
    
    #On associe un type de vehicule au vehicule aleatoirement, avec la 
    #probabilite definie par le scenario choisi
    alea = random()
    proba_cumul = 0
    i = 0
    while alea > proba_cumul:
        proba_cumul += p.PART_VEHICULE[d.scenario][i][1]
        i +=1
    
    
    #On cree le vehicule
    vehi = p.PART_VEHICULE[d.scenario][i-1][0](nom, conducteur, vitesse, prend_la_sortie, voie_vehi)
    
    #On met a jour la liste de vehicules de la voie sur laquelle le vehicule est cree
    voie.liste_vehicules.append(vehi)
              
    return vehi

#    #On incremente le compteur de vehicule
#    compteur_vehicules += 1

def generer_les_vehicules(compteur_vehicules, liste_voie):
    """
    Methode permettant de creer aleatoirement des vehicules, en tenant compte
    du debit demande, et selon l'occupation des voies, pour un instant donne.
    
    Cette methode fait appel a la methode creer_un_vehicule.
    Elle cree des objets vehicules, et renvoie la liste des vehicules crees et 
    le nombre total de vehicules crees mis a jour.
    
    :param compteur_vehicules: nombre de vehicules deja crees au cours de la
                               modelisation
    :param liste_voie: liste des objets voie de la modelisation
    
    :return: (liste des vehicules crees, compteur_vehicules mis a jour)
    :rtype: couple (liste d'objets Vehicule, entier)
    """
    #On initialise le nombre de voies occupees a zero
    voie_occupee = 0
    #On initialise la disponibilite de toute les voies a libre.
    for voie in liste_voie:
        voie.libre = True
        
        #Pour chaque voie, pour chacun des vehicules
        for vehi in voie.liste_vehicules:
#COEF VEHI ?
            #S'il existe un vehicule dont la position est inferieure a la 
            #distance de securite (ie proche du metre 0, ou le vehicule serait
            #cree)
            if vehi.position < 0.6*d.vitesse_limite:
                #Alors la voie n'est pas libre
                voie.libre = False
                #Mise a jour du nombre de voies occupees
                voie_occupee += 1
    
    #On compte le nombre de voies disponibles
    nb_voies_dispo = d.nb_voies - voie_occupee
    
    #S'il existe au moins une voie libre
    if nb_voies_dispo != 0:
        #On definit la probabilite de creation du vehicule sur les voies libres
        #en fonction de leur nombre, et du debit en entree demande
        probabilite = d.debit * d.pas / nb_voies_dispo
        #On traite le cas ou le debit demande est trop eleve en ramenant la 
        #somme des probabilites a 1
        if d.debit * d.pas > 1:
            probabilite = 1 / nb_voies_dispo
    #S'il n'y a pas de voie libre, la probabilite de creer des vehicules est 
    #nulle
    if nb_voies_dispo == 0:
        probabilite = 0
        
        
    #On initalise la liste des vehicules crees a l'instant donne    
    liste_vehicules_crees = []
    #Si la probabilite est non nulle, on cree des vehicules (avec une certaine
    #probabilite)
    if probabilite != 0:
        #On parcourt toutes les voies
        for voie in liste_voie:
            #Si la voie est libre
            if voie.libre:
                #On cree (ou pas) un vehicule, aleatoirement, selon la 
                #probabilite definie, et a condition que le nombre de vehicules
                #deja cree soit inferieur au nombre total de vehicules voulus
                alea = random()
                if alea <= probabilite and compteur_vehicules != d.nb_vehicules_voulu:
                    nouveau_vehicule = creer_un_vehicule(compteur_vehicules, voie)
#DISTANCE A CREATION                    
#                    id_min = -1
#                    min_pos = 1200
#                    for vehi in nouveau_vehicule.voie.liste_vehicules:
#                        if vehi.nom != nouveau_vehicule.nom and min_pos > vehi.position:
#                            min_pos = vehi.position
#                            id_min = vehi.nom
#                    print("cree id {} : pos_min= {}\ndevant id {}\nvoie libre: {}".format(nouveau_vehicule.nom, min_pos, id_min, nouveau_vehicule.voie.libre))
                    
                    #On met a jour le nombre de vehicules crees
                    compteur_vehicules += 1
                    #On stocke l'objet cree dans une liste
                    liste_vehicules_crees.append(nouveau_vehicule)
    
    #On renvoie la liste et le nombre total de vehicules crees
    return (liste_vehicules_crees, compteur_vehicules)