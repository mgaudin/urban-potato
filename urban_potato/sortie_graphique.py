# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 15:37:28 2017

@author: Michaël
"""

import numpy as np
import matplotlib.pyplot as plt
import data as d
import matplotlib.animation as animation
import os


def plot_voitures(liste_voitures):
    """
    Methode permettant de tracer des voitures
    """
    liste_positions = []
    liste_voies = []
    for voiture in liste_voitures:
        liste_positions.append(voiture.position)
        liste_voies.append(voiture.voie)
    plt.plot(liste_positions,[10 * elem.id_voie + 5 for elem in liste_voies],'r>', markersize = 20)



def plot(liste_voitures, instant):
    """
    """

    # Voie standard
    x = np.linspace(0,1200,1200)
    
    # Voie de droite
    # Avant la sortie
    x_gauche_avant_sortie = np.linspace(0,600,600)
    y_gauche_avant_sortie = [0 for i in range(600)]
    
    # Après la sortie
    x_gauche_apres_sortie = np.linspace(730,1200,470)
    y_droite_apres_sortie = [0 for i in range(470)]
    
    # Voie de sortie
    # Bordure gauche
    xsortie_gauche = np.linspace(600,1200,600)
    ysortie_gauche = [(-0.1*i) for i in range(600)]
    
    # Bordure droite
    xsortie_droite = np.linspace(730,1200,470)
    ysortie_droite = [(-0.1*i) for i in range(470)]
    
    # Configuration du plot
    fig, ax = plt.subplots()
    
    # Suppression de l'axe des ordonnées
    ax.yaxis.set_visible(False)
    
    # Réglage de la couleur de fond
    fig.patch.set_facecolor('#E0E0E0')
    fig.patch.set_alpha(0.7)
    ax.patch.set_facecolor('#ababab')
    
    #Trace de la bordure droite de la voie de droite avant la sortie
    plt.plot(x_gauche_avant_sortie, y_gauche_avant_sortie, color='white', linestyle='-', linewidth=2)
    
    #Trace de la bordure droite de la voie de droite après la sortie
    plt.plot(x_gauche_apres_sortie, y_droite_apres_sortie, color='white', linestyle='-', linewidth=2)
    
    #Trace de la bordure gauche de la sortie
    plt.plot(xsortie_gauche, ysortie_gauche, color='white', linestyle='-', linewidth=2)
    
    #Trace de la bordure droite de la sortie
    plt.plot(xsortie_droite, ysortie_droite, color='white', linestyle='-', linewidth=2)
    
    # Trace des voies
    for i in range(1,d.nb_voies):
        y = [10*i for j in range(1200)]
        plt.plot(x,y, color='white', linestyle='--', linewidth=2)
    
    # Trace de la bordure droite de la voie de droite
    y = [10*d.nb_voies for i in range(1200)]
    plt.plot(x, y, color='white', linestyle='-', linewidth=2)

    
    # Trace des voitures
    plot_voitures(liste_voitures)
    
    
    # Configuration de la fenêtre
    plt.axis([0, 1200, -15, 10*(d.nb_voies + 1)])
    
    # Création d'un répertoire
    try:
        os.mkdir('Graphes')
    except OSError:
        pass
    
    # Enregistrement des graphes
    plt.savefig('Graphes/' + 'graphe' + str(instant) + '.png')
    
    # Affichage
    plt.show()

#ani = animation.FuncAnimation(fig, plot_voitures, init_func = plot_route)

if __name__ == '__main__':
#    liste_voitures = []
#    plot(liste_voitures, 0)
    pass