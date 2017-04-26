# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 16:03:53 2017

@author: Alice
"""

import data as d

class Vehicule(object):
    def __init__(self, nom, conducteur, vitesse, prend_la_sortie, voie):
        #entier unique
        self._nom = nom
        #objet conducteur (script conducteur)
        self._conducteur = conducteur
        #en km/h
        self._vitesse = vitesse
        #booleen
        self._prend_la_sortie = prend_la_sortie
        #en m
        self._position = 0
        #objet voie
        self._voie = voie
    
    @property
    def nom(self):
        return self._nom
    
    @property
    def conducteur(self):
        return self._conducteur
    
    @property
    def position(self):
        return self._position
    
    @property
    def vitesse(self):
        return self._vitesse
    
    @property
    def voie(self):
        return self._voie
        
    def maj_position(self):
        #vitesse en m/s
        vitesse = self._vitesse/3.6
        #unite de temps = 0.5 s par defaut
        avance = vitesse * d.pas
        self._position += avance

#COMPORTEMENT SELON TYPE VEHICULE ?        
    def ralentir(self):
        """
        /!\ ALERT /!\ : LA VOITURE ET LA CIBLE DOIVENT ETRE SUR LE MEME TRONCON
        """
        #on considère tous les vehicules sur la même voie
        liste_voitures = self._voie.liste_voiture
        
        i=0                           
        dist_min = liste_voitures[0].position - self._position
        while dist_min < 0:
            i = i+1
            dist_min = liste_voitures[i].position - self._position
        for vehicule in liste_voitures:
            distance = vehicule.position - self._position
            if distance < dist_min and distance > 0:
                dist_min = distance
                vehicule_devant = vehicule
            
            
        vitesse_cible = vehicule_devant.vitesse
        
        #differentiel de vitesse
        dvitesse = self._vitesse - vitesse_cible
        
        #s'il faut ralentir
        if dvitesse > 0:
            #temps = dist_min / dvitesse
            temps = dist_min / self._vitesse
            nouvelle_vitesse = ((vitesse_cible - self._vitesse) / temps) * d.pas\
                               + self._vitesse
            
            self._vitesse = nouvelle_vitesse

         
    def accelerer(self):
        """
        """
        #limite a laquelle la voiture est prete a rouler, en fonction de la 
        #limitation de vitesse de l'autoroute du modele vitesse_limite et du 
        #type de conducteur
        limite = self._conducteur.coef_vitesse * d.vitesse_limite
        
        dvitesse = limite - self._vitesse
        
        #HYP : accélération de 2km/h par seconde
        if dvitesse >= (2/3.6)*d.pas:
            nouvelle_vitesse  = self._vitesse + (2/3.6)*d.pas
        if dvitesse < (2/3.6)*d.pas:  #and dvitesse > 0
            nouvelle_vitesse  = limite
                
        self._vitesse = nouvelle_vitesse                               
    
    def depasser(self):
        """
        Methode permettant de tester si le depassement est possible, et si oui,
        change la voiture de voie.
        Elle modifie la voie de la voiture, et la liste de voitures des voies
        concernees par le depassement.
        Le methode renvoie un booleen indiquant si le depassement s'est fait.
        

        :return: True si le depassement s'est fait, False sinon
        :rtype: booleen
        """
        depasse = False
        #s'il n'est ni sur la sortie, ni sur la voie de gauche
        if self._voie.id != -1 and self._voie.id != d.nb_voies - 1:
            
            #s'il n'y a pas de voiture
            #HYP 0.6*vitesse_limite*coef
            distance_securite = 0.6 * d.vitesse_limite \
                                * self._conducteur.coef_distance 
                                
            position_limite_arriere = self._position - distance_securite
            position_limite_avant = self._position + distance_securite
            
            libre = True
            liste_voitures_voie_voulue = self._voie.voie_gauche.liste_voiture
            for vehicule in liste_voitures_voie_voulue:
                occupe = (vehicule.position > position_limite_arriere and \
                          vehicule.position < self._position) or \
                          (vehicule.position < position_limite_avant and \
                          vehicule.position > self._position)
                if occupe :
                    libre = not(occupe)
            
            if libre:
                liste_voitures_voie_initiale = self._voie.liste_voiture
                self._voie = self._voie.voie_gauche
                for i in range(liste_voitures_voie_initiale):
                    if liste_voitures_voie_initiale[i].nom == self._nom:
                        liste_voitures_voie_initiale.pop(i)
                liste_voitures_voie_voulue.append(self)
                depasse = True
                
        return depasse
    
              

    def serrer_droite(self):
        """
        Methode testant si la voiture a la place de se rabattre a droite, et si
        oui, la change de voie.
        La methode modifie la voie de la voiture, et la liste de voitures des 
        voies concernees, et ne renvoie rien.
        """
        #s'il n'est ni sur la sortie, ni sur la voie de droite
        if self._voie.id != -1 and self._voie.id != 0:
            
            #s'il n'y a pas de voiture
            #HYP 0.6*vitesse_limite*coef
            distance_securite = 0.6 * d.vitesse_limite \
                                * self._conducteur.coef_distance 
                                
            position_limite_arriere = self._position - distance_securite
            position_limite_avant = self._position + distance_securite
            
            libre = True
            liste_voitures_voie_voulue = self._voie.voie_droite.liste_voiture
            for vehicule in liste_voitures_voie_voulue:
                occupe = (vehicule.position > position_limite_arriere and \
                          vehicule.position < self._position) or \
                          (vehicule.position < position_limite_avant and \
                          vehicule.position > self._position)
                if occupe :
                    libre = not(occupe)
                    
            if libre:
                liste_voitures_voie_initiale = self._voie.liste_voiture
                self._voie = self._voie.voie_droite
                for i in range(liste_voitures_voie_initiale):
                    if liste_voitures_voie_initiale[i].nom == self._nom:
                        liste_voitures_voie_initiale.pop(i)
                liste_voitures_voie_voulue.append(self)

    def tester_environnement(self):
        """
        Methode permettant de tester si le vehicule est trop proche du vehicule
        qu'il suit (et qu'un depassement ou un ralentissement est necessaire).
        
        :return: True si le vehicule est trop proche du vehicule qu'il suit, 
                 False sinon.
        :rtype: booleen
        """
        #HYP dict
        
        voiture_proche = False
        
        #on considère tous les vehicules sur la même voie
        liste_voitures = self._voie.liste_voiture
                         
        #pour chaque vehicule                        
        for vehicule in liste_voitures :
            #si la distance au vehicule est inferieure a 70
            if vehicule.position - self._position < (0.6 * d.vitesse_limite \
                * self._conducteur.coef_distance) \
                and vehicule.position - self._position > 0:
                #le vehicule est (strictement) devant lui  
                voiture_proche = True
                
        return voiture_proche
                                                  

class Camion(Vehicule):
    def __init__(self, nom, conducteur, vitesse, prend_la_sortie, voie):
        Vehicule.__init__(self, nom, conducteur, vitesse, prend_la_sortie, voie)
        self.coef_vehicule = 1.2

class Voiture(Vehicule):
    def __init__(self, nom, conducteur, vitesse, prend_la_sortie, voie):
        Vehicule.__init__(self, nom, conducteur, vitesse, prend_la_sortie, voie)
        self.coef_vehicule = 1
        
class Moto(Vehicule):
    def __init__(self, nom, conducteur, vitesse, prend_la_sortie, voie):
        Vehicule.__init__(self, nom, conducteur, vitesse, prend_la_sortie, voie)
        self.coef_vehicule = 0.9
        
class Poney(Vehicule):
    def __init__(self, nom, conducteur, vitesse, prend_la_sortie, voie):
        Vehicule.__init__(self, nom, conducteur, vitesse, prend_la_sortie, voie)
        self.coef_vehicule = 0.4