# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 15:51:03 2017

@author: Alice
"""

class Conducteur(object):
    def __init__(self):
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