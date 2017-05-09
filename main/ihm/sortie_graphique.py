# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 15:37:28 2017

@author: Michaël
"""

import numpy as np
import matplotlib.pyplot as plt
import ihm.data as d
import os

VEHICULES = (('Camion', 'k'), ('Voiture','r'), ('Moto','y'), ('Poney','g'))

def plot_route(nb_voies):
    """
    Methode permettant de tracer un fond de route
    
    Une sortie est tracee en plus d'un nombre de voies entre en parametre
    
    :param nb_voies: le nombre de voies souhaitee pour la route
    :type: integer
    :return: graphe matplotlib de la voie
    """
    # Voie standard
    x = np.linspace(0,1200,1200)
    
    # Voie de droite
    # Avant la sortie
    x_voie0_avant_sortie = np.linspace(0,500,500)
    y_voie0_avant_sortie = [0 for i in range(500)]
    
    # Après la sortie
    x_voie0_apres_sortie = np.linspace(730,1200,470)
    y_voie0_apres_sortie = [0 for i in range(470)]
    
    # Voie de sortie
    # Bordure gauche
    xsortie_gauche = np.linspace(500,600,100)
    ysortie_gauche = np.linspace(0,-10,100)
    
    # Bordure droite
    xsortie_droite = np.linspace(600,1200,600)
    ysortie_droite = [-10 for i in range(600)]
    
    #Couleur de fond
    plt.subplot(1,1,1)
    plt.subplot(1,1,1).axes.get_yaxis().set_visible(False)
    plt.subplot(1,1,1).axes.patch.set_facecolor('#ABABAB')
    
    #Trace de la bordure droite de la voie de droite avant la sortie
    plt.plot(x_voie0_avant_sortie, y_voie0_avant_sortie, color='white', linestyle='-', linewidth=2)
    
    #Trace de la bordure droite de la voie de droite après la sortie
    plt.plot(x_voie0_apres_sortie, y_voie0_apres_sortie, color='white', linestyle='-', linewidth=6)
    
    #Trace de la bordure gauche de la sortie
    plt.plot(xsortie_gauche, ysortie_gauche, color='white', linestyle='-', linewidth=2)
    
    #Trace de la bordure droite de la sortie
    plt.plot(xsortie_droite, ysortie_droite, color='white', linestyle='-', linewidth=2)
    
    # Trace des voies
    #On traite le cas ou il n'y a qu'une voie
    if nb_voies == 1 :
        pass
    #On traite le cas ou il y a plus d'une voie
    else:
        #Voie de droite avant la ligne de disuasion
        x_voie1_avant_disuation = np.linspace(0,400,400)
        y_voie1_avant_disuation = [10 for j in range(400)]
        
        #Voie de droite pendant la ligne de disuasion
        x_voie1_pendant_disuation = np.linspace(400,800,400)
        y_voie1_pendant_disuation = [10 for j in range(400)]
        
        #Voie de droite apres la ligne de disuasion
        x_voie1_apres_disuation = np.linspace(800,1200,400)
        y_voie1_apres_disuation = [10 for j in range(400)]
        
        #Trace de la bordure gauche de la voie de droite
        plt.plot(x_voie1_avant_disuation, y_voie1_avant_disuation, color='white', linestyle=(0, (5,10)), linewidth=2)
        plt.plot(x_voie1_pendant_disuation, y_voie1_pendant_disuation, color='white', linestyle=(0, (5,2)), linewidth=2)
        plt.plot(x_voie1_apres_disuation, y_voie1_apres_disuation, color='white', linestyle=(0, (5,10)), linewidth=2)
        
        #Trace des bordures des autres voies
        for i in range(2,nb_voies):
            y = [10*i for j in range(1200)]
            plt.plot(x,y, color='white', linestyle=(0, (5, 10)), linewidth=2)
    
    # Trace de la bordure droite de la voie de droite
    y = [10*nb_voies for i in range(1200)]
    plt.plot(x, y, color='white', linestyle='-', linewidth=2)

def plot_vehicules(liste_vehicules):
    """
    Methode permettant de tracer la position de vehicules
    
    :param liste_vehicules: liste des vehicules qu'il faut tracer
    :type: objets de la classe Vehicule
    :return: graphe matplotlib des vehicules
    """
    #On parcourt les vehicules
    for vehicule in liste_vehicules:
        #On recherche le type de vehicule afin de lui attribuer une couleur particuliere
        for i in range(len(VEHICULES)):
            if vehicule.__class__.__name__ == VEHICULES[i][0]:
                #On trace le vehicule dans une fenetre
                plt.plot(vehicule.position, 10 * vehicule.voie.id_voie + 5, VEHICULES[i][1]+'>', markersize = 20)
            #On affiche l'identifiant du vehicule s'il est dans la fenetre d'etude
            if vehicule.position < 1150:
                 plt.text(vehicule.position, 10 * vehicule.voie.id_voie + 5, vehicule.nom)

def plot(nb_voies, liste_vehicules, instant):
    """
    Methode permettant de tracer la voie et les vehicules
    
    La methode enregistre les sorties graphiques dans le dossier 'Graphe'
    
    :param nb_voies: nombre de voies de la modelisation
    :type: integer
    :param liste_vehicules: liste des vehicules de la modelisation
    :type: liste d'objets de la classe Vehicule
    :param instant:
    :type: float

    :return: graphe matplotlib affichant la voie et les vehicules
    """
    
    #Trace de la route
    plot_route(nb_voies)
    
    #Trace des voitures
    plot_vehicules(liste_vehicules)
    
    #Affichage
    plt.axis([0, 1200, -15, 10*(nb_voies + 1)])
    plt.grid()
    
    # Création d'un répertoire, eventuellement (s'il n'existe pas)
    try:
        os.mkdir('../../Graphes')
    except OSError:
        pass
    
    # Enregistrement des graphes
    plt.tight_layout()
    plt.savefig('../../Graphes/' + 'graphe' + str(instant) + '.png', figsize = (70,10), dpi = 300)
    plt.show()