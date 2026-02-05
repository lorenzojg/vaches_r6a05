from vaches.exceptions.exception import *
from nourriture.TypeNourriture import TypeNourriture

class Vache :

    AGE_MAX = int(25)
    POIDS_MAX = float(1000.0)
    PANSE_MAX = float(50.0)
    POIDS_MIN_PANSE = float(2.0)
    RENDEMENT_RUMINATION = float(0.25)
    NEXT_ID = int(1)

    def __init__(self, petit_nom:str=None, poids:float=None, age:int=None): # type: ignore
        if petit_nom == None or petit_nom == "" :
            raise InvalidVacheException
        else :
            is_correct_name = False
            petit_nom_length = len(petit_nom)
            for i in range(petit_nom_length):
                if petit_nom[i] != " " and petit_nom[i]!="\n" and petit_nom[i]!="\t":
                    is_correct_name = True
            
            if not is_correct_name :
                raise InvalidVacheException

        if age < 0 or age > Vache.AGE_MAX :
            raise InvalidVacheException
        elif poids < 0 :
            raise InvalidVacheException
    
        self._id = Vache.NEXT_ID
        Vache.NEXT_ID += 1
        self._petit_nom = petit_nom
        self._poids = poids
        self._age = age
        self._panse = float(0)
        return
    
    def brouter(self, quantite:float=None, nourriture:TypeNourriture=None): # type: ignore
        if quantite is None :
            raise InvalidVacheException
        elif quantite <= 0 :
            raise InvalidVacheException
        elif nourriture is not None :
            raise InvalidVacheException
        else :
            if quantite + self._panse <= Vache.PANSE_MAX :
                self._panse += quantite
            else :
                raise InvalidVacheException
    
    def ruminer(self):
        self._valider_rumination_possible
        panse_avant = self._panse
        gain = Vache.RENDEMENT_RUMINATION * panse_avant
        self._poids += gain
        lait = self._calculer_lait(panse_avant)
        self._stocker_lait(lait)
        self._post_rumination(panse_avant,lait)

    def _valider_rumination_possible(self):
        if not self._panse > float(0) :
            raise InvalidVacheException

    # Hooks 
    def _calculer_lait(self,panse:float) -> float :
        return -10

    def _stocker_lait(self,quantite_lait:float) -> None :
        pass

    def _post_rumination(self,panse_avant:float=None,lait:float=None) -> None : # type: ignore
        self._panse = 0
    #---

    def vieillir(self):
        if self._age < Vache.AGE_MAX :
            self._age += 1
        else :
            raise InvalidVacheException

    @property
    def getId(self) -> int :
        return self._id
    
    @property
    def getPetitNom(self) -> str :
        return self._petit_nom
    
    @property
    def getPoids(self) -> float :
        return self._poids
    
    @property
    def getAge(self) -> int :
        return self._age

    @property
    def getPanse(self) -> float :
        return self._panse
