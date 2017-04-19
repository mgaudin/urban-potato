# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 16:03:53 2017

@author: Alice
"""

class Vehicule(object):
    def __init__(self, nom, type_conducteur, vitesse, prend_la_sortie, voie,\
                 type_vehicule):
        #entier unique
        self._nom = nom
        #appel a la BDD
        self._type_conducteur = type_conducteur 
        #en km/h
        self._vitesse = vitesse
        #booleen
        self._prend_la_sortie = prend_la_sortie
        #en m
        self._position = 0
        self._voie = voie
        #appel a la BDD
        self._type_vehicule = type_vehicule
    
    @property
    def nom(self):
        return self._nom
    
    @property
    def position(self):
        return self._position
        
    def maj_position(self, pas = 0.5):
        #vitesse en m/s
        vitesse = self._vitesse/3.6
        #unite de temps = 0.5 s
        avance = vitesse * pas
        self._position += int(avance)

#COMPORTEMENT SELON TYPE VEHICULE ?        
    def ralentir(self, vitesse_cible, position_cible, pas = 0.5):
        """
        /!\ ALERT /!\ : LA VOITURE ET LA CIBLE DOIVENT ETRE SUR LE MEME TRONCON
        """
        #differentiel de vitesse
        dvitesse = self._vitesse - vitesse_cible
        
        #s'il faut ralentir
        if dvitesse > 0:
            distance = position_cible - self._position
            temps = distance / dvitesse
            nouvelle_vitesse = ((vitesse_cible - self._vitesse) / temps) * pas\
                               + self._vitesse
            
            self._vitesse = nouvelle_vitesse

#COMPORTEMENT SELON TYPE CONDUCTEUR ?          
    def accelerer(self, limite, pas = 0.5):
        """
        :param limite: limite conducteur
        """
        dvitesse = self._vitesse - limite
        
        #HYP : accélération de 2km/h par seconde
        if dvitesse < 0:
            nouvelle_vitesse = self._vitesse + (2/3.6)*pas
            self._vitesse = nouvelle_vitesse
                                               
    
    def depasser(self, dict_voie):
        """
        Methode permettant de tester si le depassement est possible, et si oui,
        change la voiture de voie.
        Elle modifie la voie de la voiture, et la liste de voitures des voies
        concernees par le depassement.
        Le methode renvoie un booleen indiquant si le depassement s'est fait.
        
        :param dict_voie: dictionnaire des voies du modele
        :return: True si le depassement s'est fait, False sinon
        :rtype: booleen
        """
        depasse = False
        #s'il n'est ni sur la sortie, ni sur la voie de gauche
        if self._voie.id != -1 and self._voie.id != nb_voies - 1:
            
            #s'il n'y a pas de voiture
            #HYP : 60m libre derrière sur la voie de gauche
            position_limite = self._position - 60
            if position_limite <0:
                position_limite = 0
            
            voie_voulue = self._voie + 1
            
            libre = True
            liste_voitures_voie_voulue = dict_voie[voie_voulue].liste_voiture
            for vehicule in liste_voitures_voie_voulue:
                occupe = vehicule.position > position_limite and \
                vehicule.position < self._position
                if occupe :
                    libre = not(occupe)
            
            if libre:
                liste_voitures_voie_initiale = dict_voie[self._voie].liste_voiture
                self._voie += 1
                for i in range(liste_voitures_voie_initiale):
                    if liste_voitures_voie_initiale[i].nom == self._nom:
                        liste_voitures_voie_initiale.pop(i)
                liste_voiture_voie_voulue.append(self)
                depasse = True
                
        return depasse
    
              
    
    def serrer_droite(self, dict_voie):
        """
        Methode testant si la voiture a la place de se rabattre a droite, et si
        oui, la change de voie.
        La methode modifie la voie de la voiture, et la liste de voitures des 
        voies concernees, et ne renvoie rien.
        
        :param dict_voie: dictionnaire des voies du modele
        """
        #s'il n'est ni sur la sortie, ni sur la voie de droite
        if self._voie.id != -1 and self._voie.id != 0:
            
            #s'il n'y a pas de voiture
            #HYP : 60m libre derrière sur la voie de droite
            position_limite = self._position - 60
            if position_limite <0:
                position_limite = 0
            
            voie_voulue = self._voie - 1
            
            libre = True
            liste_voitures_voie_voulue = dict_voie[voie_voulue].liste_voiture:
            for vehicule in liste_voitures_voie_voulue:
                occupe = vehicule.position > position_limite and \
                vehicule.position < self._position
                if occupe :
                    libre = not(occupe)
                    
            if libre:
                liste_voitures_voie_initiale = dict_voie[self._voie].liste_voiture
                self._voie -= 1
                for i in range(liste_voitures_voie_initiale):
                    if liste_voitures_voie_initiale[i].nom = self._nom:
                        liste_voitures_voie_initiale.pop(i)
                liste_voiture_voie_voulue.append(self)

                
    def regarder_limitation(self):
        """
        methode calculant la limite a laquelle la voiture est prete a rouler,
        en fonction de la limitation de vitesse de l'autoroute du modele 
        vitesse_max et du type de conducteur (cf BDD)
        renvoie limite (utile dans methode accelerer)
        """
        pass
            