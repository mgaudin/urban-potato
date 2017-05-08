# -*- coding: utf-8 -*-
"""
Projet Informatique
Gestion du trafic routier au niveau d'une sortie d'autoroute
Classe Voie et sa classe fille Sortie
Michael Gaudin et Alice Gonnaud
Mai 2017
"""

class Voie(object):
    def __init__(self, id_voie, voie_gauche, voie_droite, limite):
        #entier unique, de 0 (voie de droite) à nb_voies - 1 (voie de gauche)
        self._id_voie = id_voie
        #instances de la classe Voie (ou None pour les voies exterieures)
        self._voie_gauche = voie_gauche
        self._voie_droite = voie_droite
        #liste d'objets de la classe Vehicule
        self._liste_vehicules = []
        #entier
        self._limite = limite
        #booleen
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
        
    
#ERROR 'liste_vehicules' is not defined
    def __str__(self):
        """
        Affiche le numero, la liste des numeros des vehicules et la limitation
        de vitesse de la voie.
        """
        liste_nom_vehicules = [vehi.nom for vehi in self._liste_vehicules]
        return "id = {}\nliste_vehicules = {}\nlimite = {}".format(self.id_voie, liste_nom_vehicules, self.limite)
  
    
class Sortie(Voie):
    def __init__(self, id_voie, voie_gauche, voie_droite, limite):
        Voie.__init__(self, id_voie, voie_gauche, voie_droite, limite)
        #Sortie : voie particulière, dont l'id vaut toujours -1
        self._id_voie = -1
        self._limite = 90
    
