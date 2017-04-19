# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 16:30:47 2017

@author: Alice
"""

class Voie(object):
    def __init__(self, id_voie):
        self.id = id_voie
        self.liste_voiture = []
        self.limite = 110
        
    def __str__(self):
        return "id = {}\nliste_voiture = {}\nlimite = {}".format(self.id, self.liste_voiture, self.limite)
    
class Sortie(Voie):
    def __init__(self, id_voie, limite):
        Voie.__init__(self, id_voie)
        self.id = -1
        self.limite = limite
    
