# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 15:37:28 2017

@author: Michaël
"""

import numpy as np
import matplotlib.pyplot as plt

def plot_route():
    #Route
    x = np.linspace(0,1200,1200)
    x_gauche_avant_sortie = np.linspace(0,700,700)
    x_gauche_apres_sortie = np.linspace(800,1200,400)
    xsortie_gauche = np.linspace(700,1200,500)
    xsortie_droite = np.linspace(800,1200,400)
    
    y1_avant_sortie = [0 for i in range(700)]
    y1_apres_sortie = [0 for i in range(400)]
    y2 = [10 for i in range(1200)]
    y3 = [20 for i in range(1200)]
    y4 = [30 for i in range(1200)]
    
    ysortie_gauche = [(-0.1*i) for i in range(500)]
    ysortie_droite = [(-0.1*i) for i in range(400)]
                      
    plt.plot(x_gauche_avant_sortie, y1_avant_sortie, color='blue', linestyle='-', linewidth=2)
    plt.plot(x_gauche_apres_sortie, y1_apres_sortie, color='blue', linestyle='-', linewidth=2)
    plt.plot(x,y2, color='blue', linestyle='--', linewidth=2)
    plt.plot(x,y3, color='blue', linestyle='--', linewidth=2)
    plt.plot(x,y4, color='blue', linestyle='--', linewidth=2)
    plt.plot(xsortie_gauche, ysortie_gauche, color='blue', linestyle='-', linewidth=2)
    plt.plot(xsortie_droite, ysortie_droite, color='blue', linestyle='-', linewidth=2)
    
    #Voitures
    #Voitures essais
    #plt.plot(50,25,'r>', markersize = 50)
    #plt.plot(350,15,'b>', markersize = 50)
    
    #Affichage
    plt.axis([0, 1200, -20, 50])
    plt.show()

def plot_voitures(liste_voitures):
    """
    Methode permettant de tracer des voitures
    """
    liste_positions = []
    liste_voies = []
    for voiture in liste_voitures:
        liste_positions.append(voiture.position)
        liste_voies.append(voiture.voie)
    plt.plot(liste_positions,[10 * elem.id + 5 for elem in liste_voies],'r>', markersize = 50)
    plt.axis([0, 1200, -20, 50])