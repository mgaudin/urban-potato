# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 16:30:47 2017

@author: Alice
"""

class Voie(object):
    def __init__(self, id_voie, voie_gauche, voie_droite, limite):
        self._id_voie = id_voie
        self._voie_gauche = voie_gauche
        self._voie_droite = voie_droite
        self._liste_vehicules = []
        self._limite = limite
        self._libre = True
        
    @property
    def id_voie(self):
        return self._id_voie
    
    @property
    def voie_gauche(self):
        return self._voie_gauche
    
    @property
    def voie_droite(self):
        return self._voie_droite
    
    @property
    def liste_vehicules(self):
        return self._liste_vehicules
    
    @property
    def limite(self):
        return self._limite
    
    @property
    def libre(self):
        return self._libre
    
    @voie_gauche.setter
    def voie_gauche(self, valeur):
        self._voie_gauche = valeur
        
    @voie_droite.setter
    def voie_droite(self, valeur):
        self._voie_droite = valeur
        
    @liste_vehicules.setter
    def liste_vehicules(self, valeur):
        self._liste_vehicules = valeur
        
    @libre.setter
    def libre(self, valeur):
        self._libre = valeur
        
    
    
        
    def __str__(self):
        return "id = {}\nliste_voiture = {}\nlimite = {}".format(self.id, self.liste_voiture, self.limite)
    
class Sortie(Voie):
    def __init__(self, id_voie, voie_gauche, voie_droite, limite):
        Voie.__init__(self, id_voie, voie_gauche, voie_droite, limite)
        self._id = -1
        self._limite = 90
    
