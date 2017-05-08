# -*- coding: utf-8 -*-
"""
Projet Informatique
Gestion du trafic routier au niveau d'une sortie d'autoroute
Classe Conducteur et classes en heritant
Michael Gaudin et Alice Gonnaud
Mai 2017
"""

class Conducteur(object):
    def __init__(self):
        """
        Constructeur de la classe Conducteur, classe abstraite.
        
        Un objet heritant de Conducteur a deux attributs : un coefficient de 
        distance et un coefficient de vitesse.
        Le coefficient de distance pondere l'estimation de la distance de 
        securite (un conducteur plus prudent restera a une plus grande distance
        et aura un plus grand coefficient).
        Le coefficient de vitesse pondere la vitesse maximale a laquelle le 
        vehicule roule (un conduceur plus prudent ira moins vite et aura un 
        plus petit coefficient).
        """
        raise NotImplementedError
       
        
class Prudent(Conducteur):
    def __init__(self):
        self.coef_distance = 1.33
        self.coef_vitesse = 0.8
        
class Normal(Conducteur):
    def __init__(self):
        self.coef_distance = 1
        self.coef_vitesse = 1
        
class Chauffard(Conducteur):
    def __init__(self):
        self.coef_distance = 0.8
        self.coef_vitesse = 1.1