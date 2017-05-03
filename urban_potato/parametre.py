# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 11:51:25 2017

@author: Alice
"""
import conducteur as c
import vehicule as v

prudent = c.Prudent()
normal = c.Normal()
chauffard = c.Chauffard()


PART_VEHICULE = (((v.Camion, 0.16), (v.Voiture, 0.68), (v.Moto, 0.15), (v.Poney, 0.01)),
                 ((v.Camion, 0.2), (v.Voiture, 0.7), (v.Moto, 0.09), (v.Poney, 0.01)),
                 ((v.Camion, 0.25), (v.Voiture, 0.25), (v.Moto, 0.25), (v.Poney, 0.25)))


PART_CONDUCT = (((prudent, 0.08), (normal, 0.87), (chauffard, 0.05)),
                ((prudent, 0.1), (normal, 0.8), (chauffard, 0.1)),
                ((prudent, 0.33), (normal, 0.34), (chauffard, 0.33)))


if __name__ == '__main__':
    pass