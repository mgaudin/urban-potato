# -*- coding: utf-8 -*-
"""
Projet Informatique
Gestion du trafic routier au niveau d'une sortie d'autoroute
Classe Vehicule et classes en heritant
Michael Gaudin et Alice Gonnaud
Mai 2017
"""

import ihm.data as d

class Vehicule(object):
    def __init__(self, nom, conducteur, vitesse, prend_la_sortie, voie):
        #Entier unique
        self._nom = nom
        #Objet de la classe conducteur
        self._type_conducteur = conducteur
        #Vitesse instantanee en km/h
        self._vitesse = vitesse
        #Booleen
        self._prend_la_sortie = prend_la_sortie
        #Flottant, en metre
        self._position = 0
        #Objet de la classe voie
        self._voie = voie
        #Coefficient defini dans les classes filles
        self._coef_vehicule = None
    
    @property
    def nom(self):
        return self._nom
    
    @property
    def type_conducteur(self):
        return self._type_conducteur
    
    @property
    def position(self):
        return self._position
    
    @property
    def vitesse(self):
        return self._vitesse
    
    @property
    def voie(self):
        return self._voie
    @property
    def prend_la_sortie(self):
        return self._prend_la_sortie
        
    @property
    def coef_vehicule(self):
        return self._coef_vehicule
    
    
    
    
    
        
    def maj_position(self):
        """
        Methode permettant de mettre a jour l'attribut position du vehicule, en 
        ajoutant a sa position la distance parcourue par le vehicule depuis 
        l'instant precedant, en fonction de sa vitesse instantanee.
        
        Cette methode modifie l'attribut position et ne retourne rien.
        """
        #On convertit la vitesse du vehicule (km/h) en m/s
        vitesse = self._vitesse/3.6
        
        #Le pas, temps s'ecoulant entre deux instants, est exprime en s
        #L'avance (en m) est la distance parcourue entre deux instants a la 
        #vitesse du vehicule
        avance = vitesse * d.pas
        
        #Mise a jour de l'attribut position
        self._position += avance
        

#COMPORTEMENT SELON TYPE VEHICULE ?        
    def ralentir(self):
        """
        /!\ ALERT /!\ : LA VOITURE ET LA CIBLE DOIVENT ETRE SUR LE MEME TRONCON
        
        Methode permettant au vehicule de ralentir.
        
        On adopte un modele de ralentissement lineaire, defini a chaque instant
        par la distance separant le vehicule de celui qu'il suit et leur 
        differentiel de vitesse.
        Tant que le vehicule est distant du vehicule qu'il suit de plus de la 
        distance de securite, il relentit lineairement, visant atteindre la 
        vitesse du vehicule qu'il suit au moment ou il sera distant de lui de 
        la distance de securite.
        S'il est plus proche du vehicule de devant que la distance de securite,
        on effectue un ralentissement d'urgence : le vehicule prend la vitesse 
        de celui devant lui.
        
        Cette methode modifie l'attribut vitesse et ne retourne rien.
        """
        #On cherche le vehicule de devant, pour calculer la distance separant
        #de lui et determiner sa vitesse.
        
        #On s'interesse aux vehicules de la meme voie
        liste_vehicules = self._voie.liste_vehicules
        
        #On cherche le vehicule immediatement devant, ie a la distance positive
        #minimale

        #On initialise en prenant un vehicule devant et en calculant sa distance
        #On considere le premier vehicule de la liste de la voie
        i=0                           
        dist_min = liste_vehicules[0].position - self._position
        vehicule_devant = liste_vehicules[0]
        #Si ce vehicule n'est pas devant, on parcourt tous les vehicules de la 
        #voie et on cherche le premier vehicule qui l'est
        while dist_min < 0:
            i = i+1
            dist_min = liste_vehicules[i].position - self._position
        
        #On parcourt tous les vehicules sur la même voie
        for vehicule in liste_vehicules:
            #On calcule la distance a laquelle ils sont
            distance = vehicule.position - self._position
            #On retient la distance minimale positive, et le vehicule concerne
            if distance < dist_min and distance > 0:
                dist_min = distance
                vehicule_devant = vehicule
            
        #On memorise la vitesse du vehicule de devant
        vitesse_cible = vehicule_devant.vitesse
        
        #On calcule le differentiel de vitesse avec ce vehicule
        dvitesse = self._vitesse - vitesse_cible
        
        #S'il est plus lent, on ralentit
        if dvitesse > 0:
            #Si on suit le vehicule de moins de la distance de securite, on 
            #opère un freinage d'urgence
            if dist_min < 0.6 * self._vitesse:
#                vit = self._vitesse
                #Le vehicule prend la vitesse du vehicule de devant
                self._vitesse = vitesse_cible
#                if self._nom == 10:
#                    print('urgence\n')
#                print("urgence vehi {}\ndistmin= {}\nvit_init= {}\nnouv_vit= {}\n".format(self._nom, dist_min, vit, self._vitesse))
            #Si le vehicule de devant est distant d'au moins la distance de 
            #securite
            else:
                #On calcule le temps (en secondes) qu'il faudrait pour suivre
                #la voiture de devant a exactement la distance de securite, 
                #si on maintenait la meme allure (pondere par le coefficient du 
                #vehicule, en facteur, qui accentue ou aplanit la pente du 
                #modele lineaire de ralentissement : un vehicule moins agile
                #ralentira moins vivement)
                temps = (dist_min - 0.6 * self._vitesse) / (self._vitesse/3.6) * self._coef_vehicule
                #La nouvelle vitesse suit la pente du differentiel de vitesse
                #en fonction du temps (ponderee par le coefficient du vehicule),
                #calculee pour l'instant suivant (en m/s)
                nouvelle_vitesse = ((vitesse_cible - self._vitesse) / (3.6*temps)) * d.pas + self._vitesse/3.6
                
                #On renvoie la nouvelle vitesse en km/h
                self._vitesse = nouvelle_vitesse*3.6
#            if self._nom == 10:
#                print("ralentit")
#            print(dist_min)
#            if nouvelle_vitesse < 0:
#                print("vehi {}: vit {};\ntps {};\ndist_min {};\ndiff_vit {};\nvit_init {};\n".format(self._nom, nouvelle_vitesse, temps, dist_min, diff_vit, vit))
        
        
         
    def accelerer(self):
        """
        Methode permettant au vehicule d'accelerer.
        On considere qu'il gagne 2km/h par seconde.
        
        Cette methode modifie l'attribut vitesse et ne retourne rien.
        """
        #Le vehicule ne depasse pas sa vitesse limite qui est la limitation de 
        #vitesse de l'autoroute ponderee par le coefficient vitesse propre au 
        #type de conducteur (un conducteur plus imprudent depassera la 
        #limitation de vitesse de l'autoroute)
        limite = self._type_conducteur.coef_vitesse * d.vitesse_limite
        
        #Calcul de l'ecart de la vitesse a la limite
        dvitesse = limite - self._vitesse
        
        #Si le vehicule ne depasse pas la limite en accelerant
        if dvitesse >= (2*d.pas):
            #Hypothese du modele : acceleration de 2km/h par seconde 
            nouvelle_vitesse = self._vitesse + 2*d.pas
        else:  
            #S'il risque de depasser en accelerant de 2km/h, il accelere a la 
            #limite
            nouvelle_vitesse = limite
                
        #L'attribut vitesse est mis a jour
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
        #On initialise le booleen indiquant si le depassement s'est fait
        depasse = False
        
        #Si le vehicule n'est ni sur la sortie, ni sur la voie la plus a gauche
        if self._voie.id_voie != -1 and self._voie.id_voie != d.nb_voies - 1:
            
            #On regarde s'il y a des voitures voie de gauche, devant ou 
            #arrivant derriere a moins de deux fois la distance de securite 
            #(laisse le temps au vehicule de derriere de ralenir s'il est plus
            #rapide)
            #La distance de securite est 0.6*vitesse (code de la route) 
            #ponderee par le coefficient distance du type de conducteur 
            #(distance plus courte pour les conducteurs moins prudents)
#self.vitesse ?
            distance_securite = 0.6 * 2 * d.vitesse_limite \
                                * self._type_conducteur.coef_distance 
            
            #On definit l'intervalle des positions qui ne doit pas comprendre
            #de vehicules pour autoriser le depassement
            #Position maximale du vehicule derriere soi
            position_limite_arriere = self._position - distance_securite
            #Position minimale du vehicule devant soi
            position_limite_avant = self._position + distance_securite
            
            #On teste si la voie de gauche est libre
            #Initialisation du booleen
            libre = True
            #On parcourt les vehicules de la voie de gauche
            for vehicule in self._voie.voie_gauche.liste_vehicules:
                #La voie est occupee si un vehicule se trouve sur cette voie, 
                #dans l'intervalle des positions defini plus haut
                occupe = (vehicule.position > position_limite_arriere and \
                          vehicule.position < self._position) or \
                          (vehicule.position < position_limite_avant and \
                          vehicule.position > self._position)
                #Mise a jour du booleen
                if occupe :
                    libre = not(occupe)
            
            #Si la voie est libre, on depasse
            if libre:
                #On supprime le vehicule de la voie quittee
                self._voie.liste_vehicules.remove(self)
                #On change de voie (mise a jour de l'attribut voie du vehicule)
                self._voie = self._voie.voie_gauche
                #On ajoute le vehicule a la voie de gauche
                self._voie.liste_vehicules.append(self)
                
                #On indique que le depassement s'est effectue
                depasse = True
        
        #On retourne si le depassement s'est fait ou non
        return depasse
    
              

    def serrer_droite(self):
        """
        Methode testant si le vehicule a la place de se rabattre a droite, et 
        si oui, le change de voie.
        
        La methode modifie la voie de la voiture, et la liste de voitures des 
        voies concernees, et ne renvoie rien.
        """
#NB: Methode similaire a depasser()
        
        #Si le vehicule n'est ni sur la sortie, ni sur la voie la plus a droite
        if self._voie.id_voie != -1 and self._voie.id_voie != 0:
            
            
            #On definit l'intervalle de position dans lequel aucun vehicule ne
            #doit se trouver pour pouvoir se rabattre a droite
#self.vitesse ?
            distance_securite = 0.6 * 2 * d.vitesse_limite
#coef conducteur ?
            #distance_securite = distance_securite* self._type_conducteur.coef_distance 
                                
            position_limite_arriere = self._position - distance_securite
            position_limite_avant = self._position + distance_securite
            
            #On teste si la voie de droite est disponible
            libre = True
            
            for vehicule in self._voie.voie_droite.liste_vehicules:
                occupe = (vehicule.position > position_limite_arriere and \
                          vehicule.position < self._position) or \
                          (vehicule.position < position_limite_avant and \
                          vehicule.position > self._position)
                if occupe :
                    libre = not(occupe)
                    
            #Si la voie de droite est disponible, on change le vehicule de voie      
            if libre:
                #On met a jour la liste de vehicules de la voie quittee
                self._voie.liste_vehicules.remove(self)
                #On met a jour l'attribut voie du véhicule
                self._voie = self._voie.voie_droite
                #On met a jour la liste de vehicules de la voie prise
                self._voie.liste_vehicules.append(self)

    def tester_environnement(self):
        """
        Methode permettant de tester si le vehicule est trop proche du vehicule
        qu'il suit (et qu'un depassement ou un ralentissement est necessaire).
        
        :return: True si le vehicule est trop proche du vehicule qu'il suit, 
                 False sinon.
        :rtype: booleen
        """
        #Initialisation du booleen
        vehicule_proche = False
                         
        #Pour chaque vehicule de la même voie                      
        for vehicule in self._voie.liste_vehicules :
            #Si la distance au vehicule est inferieure a deux fois la distance
            #de securite (laisse le temps de depasser ou ralentir) et que le 
            #vehicule est devant (strictement, exclut soi)
            if vehicule.position - self._position < (0.6 * 2 * d.vitesse_limite \
                * self._type_conducteur.coef_distance) \
                and vehicule.position - self._position > 0:
                #Le vehicule est trop proche
                vehicule_proche = True
                
        return vehicule_proche
    
    def prendre_la_sortie(self):
        """
        Methode permettant au vehicule de prendre la sortie, a condition qu'il
        veuille la prendre, et qu'il soit sur la bonne voie (la plus a droite) 
        et a la bonne position (en face de la sortie).
        
        Si le vehicule prend la sortie, cette methode met a jour la voie du 
        vehicule sortant (attribut voie), et la liste de vehicules de la voie 
        qu'il quitte (de droite) et qu'il joint (sortie). Sinon, elle ne 
        modifie rien.
        La methode ne renvoie rien.
        """
        #Si le vehicule est sur la voie la plus a droite, qu'il est avant la 
        #sortie et qu'il veut la prendre
        if self._voie.id_voie == 0 and self._position < 730 and \
        self.prendre_la_sortie:
            
            #On verifie que la sortie est disponible
            #On initialise la position du vehicule de devant a la position 
            #maximale possible (traite le cas ou aucun vehicule n'est devant)
            position_devant = 1200
            #Pour chaque vehicule de la sortie
            for vehi in self._voie.voie_droite.liste_vehicules:
                #Si le vehicule est le premier de la voie (position minimale)
                if vehi.position < position_devant:
                    #Alors il est le vehicule de devant
                    position_devant = vehi.position
                    vehicule_devant = vehi
            #On memorise la distance au vehicule de devant
            distance_devant = position_devant - self.position
                
            #Si le vehicule est en face de la sortie mais trop pres du vehicule
            #de devant (qui deja dans la voie de la sortie)
            if self._position < 600 and distance_devant < 2 * 0.6 * self._vitesse:
                    #Le vehicule ralentit pour ne pas manquer la sortie
                    vitesse_cible = vehicule_devant.vitesse
                    temps = (distance_devant - 0.6 * self._vitesse) / (self._vitesse/3.6)
                    nouvelle_vitesse = ((vitesse_cible - self._vitesse) / (3.6*temps)) * d.pas + self._vitesse/3.6
                    
                    self._vitesse = nouvelle_vitesse*3.6
            
            #Si le vehicule est en face de la sortie et suffisamment loin du 
            #vehicule de devant
            #(NB : si le vehicule est en fait devant le premier vehicule de la
            #sortie, distance_devant est negative, inferieure a la distance de 
            #securite, et le vehicule ne peut pas sortir et se rabattre devant
            #celui deja engage dans la sortie)
            if self._position >= 600 and distance_devant > 0.6 * self._vitesse:
                #Le vehicule prend la sortie
                #Mise a jour de la liste de vehicules de la voie quittee
                self._voie.liste_vehicules.remove(self)
                #Mise a jour de la voie du vehicule
                self._voie = self._voie.voie_droite
                #Mise a jur de liste de vehicules de la sortie
                self._voie.liste_vehicules.append(self)
            
                                                  

class Camion(Vehicule):
    def __init__(self, nom, conducteur, vitesse, prend_la_sortie, voie):
        Vehicule.__init__(self, nom, conducteur, vitesse, prend_la_sortie, voie)
        self._coef_vehicule = 1.1

class Voiture(Vehicule):
    def __init__(self, nom, conducteur, vitesse, prend_la_sortie, voie):
        Vehicule.__init__(self, nom, conducteur, vitesse, prend_la_sortie, voie)
        self._coef_vehicule = 1
        
class Moto(Vehicule):
    def __init__(self, nom, conducteur, vitesse, prend_la_sortie, voie):
        Vehicule.__init__(self, nom, conducteur, vitesse, prend_la_sortie, voie)
        self._coef_vehicule = 0.9
        
class Poney(Vehicule):
    def __init__(self, nom, conducteur, vitesse, prend_la_sortie, voie):
        Vehicule.__init__(self, nom, conducteur, vitesse, prend_la_sortie, voie)
        self._coef_vehicule = 0.6