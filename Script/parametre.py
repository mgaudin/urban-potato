# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 11:51:25 2017

@author: Alice
"""

COEF_DIST_VEHICULE = {'Camion': 1.2, 'Voiture': 1, 'Moto': 0.9,'Poney': 0.4}

COEF_DIST_CONDUCTEUR = {'Prudent': 1.33, 'Normal': 1, 'Chauffard': 0.4}

COEF_VITESSE_CONDUCTEUR = {'Prudent': 0.8, 'Normal': 1, 'Chauffard': 1.1}


PART_VEHICULE = ((('Camion', 0.16), ('Voiture', 0.68), ('Moto', 0.05), ('Poney', 0.01))
                 (('Camion', 0.2), ('Voiture', 0.7),('Moto', 0.09), ('Poney', 0.01))

PART_CONDUCT = ((('Prudent', 0.08), ('Normal', 0.87), ('Chauffard', 0.05))
                (('Prudent', 0.1), ('Normal', 0.8), ('Chauffard', 0.1)))