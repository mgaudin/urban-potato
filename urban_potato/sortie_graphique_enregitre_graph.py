# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 15:37:28 2017

@author: Michaël
"""

import numpy as np
import matplotlib.pyplot as plt
import data as d
import os

VEHICULES = [['Camion', 'k'], ['Voiture','r'], ['Moto','y'], ['Poney','g']]

def plot_route():
    """
    """
    # Voie standard
    x = np.linspace(0,1200,1200)
    
    # Voie de droite
    # Avant la sortie
    x_voie0_avant_sortie = np.linspace(0,600,600)
    y_voie0_avant_sortie = [0 for i in range(600)]
                             
    # Sortie
    x_voie0_pendant_sortie = np.linspace(600,730,130)
    y_voie0_pendant_sortie = [10 for i in range(130)]
    
    # Après la sortie
    x_voie0_apres_sortie = np.linspace(730,1200,470)
    y_voie0_apres_sortie = [0 for i in range(470)]
    
    # Voie de sortie
    # Bordure gauche
    xsortie_gauche = np.linspace(600,1200,600)
    ysortie_gauche = [(-0.1*i) for i in range(600)]
    
    # Bordure droite
    xsortie_droite = np.linspace(730,1200,470)
    ysortie_droite = [(-0.1*i) for i in range(470)]
    
    #Trace de la bordure droite de la voie de droite avant la sortie
    plt.plot(x_voie0_avant_sortie, y_voie0_avant_sortie, color='white', linestyle='-', linewidth=2)
    
    #Trace de la bordure droite de la voie de droite pendant la sortie
    #plt.plot(x_voie0_pendant_sortie, y_voie0_pendant_sortie, color='white', linestyle=(0, (5,1)), linewidth=2)
    
    #Trace de la bordure droite de la voie de droite après la sortie
    plt.plot(x_voie0_apres_sortie, y_voie0_apres_sortie, color='white', linestyle='-', linewidth=2)
    
    #Trace de la bordure gauche de la sortie
    plt.plot(xsortie_gauche, ysortie_gauche, color='white', linestyle='-', linewidth=2)
    
    #Trace de la bordure droite de la sortie
    plt.plot(xsortie_droite, ysortie_droite, color='white', linestyle='-', linewidth=2)
    
    # Trace des voies
    if d.nb_voies == 1 :
        pass
    else:
        x_voie1_avant_disuation = np.linspace(0,400,400)
        y_voie1_avant_disuation = [10 for j in range(400)]
        
        x_voie1_pendant_disuation = np.linspace(400,800,400)
        y_voie1_pendant_disuation = [10 for j in range(400)]
        
        x_voie1_apres_disuation = np.linspace(800,1200,400)
        y_voie1_apres_disuation = [10 for j in range(400)]
        
        plt.plot(x_voie1_avant_disuation, y_voie1_avant_disuation, color='white', linestyle=(0, (5,10)), linewidth=2)
        plt.plot(x_voie1_pendant_disuation, y_voie1_pendant_disuation, color='white', linestyle=(0, (5,2)), linewidth=2)
        plt.plot(x_voie1_apres_disuation, y_voie1_apres_disuation, color='white', linestyle=(0, (5,10)), linewidth=2)
        
        for i in range(2,d.nb_voies):
            y = [10*i for j in range(1200)]
            plt.plot(x,y, color='white', linestyle=(0, (5, 10)), linewidth=2)
    
    # Trace de la bordure droite de la voie de droite
    y = [10*d.nb_voies for i in range(1200)]
    plt.plot(x, y, color='white', linestyle='-', linewidth=2)

def plot_voitures(liste_voitures):
    """
    Methode permettant de tracer des voitures
    
    #Si la voiture est sur la sortie (voie d'id -1), elle prend un angle
    """
    liste_positions = []
    liste_voies = []
    liste_noms = []
    liste_couleurs = []
    for vehicule in liste_voitures:
        liste_positions.append(vehicule.position)
        liste_voies.append(vehicule.voie)
        liste_noms.append(vehicule.nom)
        for i in range(len(VEHICULES)):
            if vehicule.__class__.__name__ == VEHICULES[i][0]:
                liste_couleurs.append(VEHICULES[i][1])
        for i in range(len(liste_noms)):
            plt.plot(liste_positions[i], 10 * liste_voies[i].id_voie + 5, liste_couleurs[i]+'>', markersize = 20)
            plt.text(liste_positions[i], 10 * liste_voies[i].id_voie + 5, liste_noms[i])

"""                
    plt.plot(liste_positions[i],[10 * elem.id_voie + 5 for elem in liste_voies],liste_couleurs[:]+'>', markersize = 20)
    for i in range(len(liste_noms)):
        plt.text(liste_positions[i], 10 * liste_voies[i].id_voie + 5, liste_noms[i])
"""

def plot(liste_voitures, instant):
    """
    """
    
    # Configuration du plot
    fig, ax = plt.subplots()
    
    # Suppression de l'axe des ordonnées
    ax.yaxis.set_visible(False)
    
    # Réglage de la couleur de fond
    fig.patch.set_facecolor('#E0E0E0')
    fig.patch.set_alpha(0.7)
    ax.patch.set_facecolor('#ABABAB')
    
    #Trace de la route
    plot_route()
    
    #Trace des voitures
    plot_voitures(liste_voitures)
    
    #Affichage
    plt.axis([0, 1200, -(5 + d.nb_voies*3), 10*(d.nb_voies + 1)])
    plt.grid()
    
    # Création d'un répertoire
    try:
        os.mkdir('Graphes')
    except OSError:
        pass
    
    # Enregistrement des graphes
    plt.tight_layout()
    plt.savefig('Graphes/' + 'graphe' + str(instant) + '.png', figsize = (30,10), dpi = 300)
    plt.show()

if __name__ == '__main__':
    liste_voitures = []
    plot(liste_voitures,0)
#    plt.plot(900,5,'r>', markersize = 10)
#    plt.show()
    pass