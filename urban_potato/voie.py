# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 16:30:47 2017

@author: Alice
"""

class Voie(object):
    def __init__(self, id_voie, voie_gauche, voie_droite, limite):
        self.id = id_voie
        self.voie_gauche = voie_gauche
        self.voie_droite = voie_droite
        self.liste_voiture = []
        self.limite = limite
        self.libre = True
        
    def __str__(self):
        return "id = {}\nliste_voiture = {}\nlimite = {}".format(self.id, self.liste_voiture, self.limite)
    
class Sortie(Voie):
    def __init__(self, id_voie, voie_gauche, voie_droite, limite):
        Voie.__init__(self, id_voie, voie_gauche, voie_droite, limite)
        self.id = -1
        self.limite = 90
    
