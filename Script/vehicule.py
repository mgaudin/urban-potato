# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 16:03:53 2017

@author: Alice
"""

class Vehicule(object):
    def __init__(self, nom, type_conducteur, vitesse, prend_la_sortie, voie, type_vehicule):
        self._nom = nom
        self._type_conducteur = type_conducteur 
        self._vitesse = vitesse
        self._prend_la_sortie = prend_la_sortie
        self._position = 0
        self._voie = voie
        self._type_vehicule
        
    
        
    def maj_position(self):
        #vitesse en m/s
        vitesse = self._vitesse/3.6
        #unite de temps = 0.5 s
        avance = vitesse/2
        self._position += int(avance)
        
    def ralentir(self, vitesse_cible, position_cible):
        """
        /!\ ALERT /!\ : LA VOITURE ET LA CIBLE DOIVENT ETRE SUR LE MEME TRONCON
        """
        #differentiel de vitesse
        dvitesse = self._vitesse - vitesse_cible
        
        #s'il faut ralentir
        if dvitesse > 0:
            distance = position_cible - self._position
            temps = distance / dvitesse
            pas = temps / 0.5
            nouvelle_vitesse = ((vitesse_cible - self._vitesse) / temps) * pas + self._vitesse
            
            self._vitesse = nouvelle_vitesse
    
    def accelerer(self):
        pass
    
    def depasser(self):
        pass
    
    def serrer_droite(self):
        pass
    
    def regarder_limitation(self):
        pass
            